from typing import List
import logging

class Ogrenci:
    def __init__(self, ogrno, sube, adi, ogretim, kitapcik, cevaplar) -> None:
        self.ogrno = ogrno
        self.adi = adi.strip()
        self.sube = sube
        self.ogretim = ogretim
        self.kitapcik = kitapcik
        self.cevaplar = cevaplar
        self.dogru = 0
        self.yanlis = 0
        self.bos = 0
        self.puan = 0

class Answers:
    def __init__(self, group, answers) -> None:
        self.group = group
        self.question_count = 0
        self.student_count = 0
        self.mapping = []
        self.answers = answers
        self.statistics = []
        self.process_answers()

    def process_answers(self):
        self.question_count = len(self.answers.replace(" ", ""))
        self.statistics = [{"correct":0, "incorrect":0, "empty":0} for i in range(self.question_count)]
        m = 0
        for i in range(self.question_count):
            while(self.answers[m] == " "):
                m += 1
            self.mapping.append(m)
            m += 1

    def check_question(self, i, student_answers):
        return self.answers[self.mapping[i]] == student_answers[self.mapping[i]]

    def is_empty(self, i, student_answers):
        return " " == student_answers[self.mapping[i]]

    def get_student_answer(self, i, student_answers):
        return student_answers[self.mapping[i]]

class Exam:
    def __init__(self, filename, total_points=100) -> None:
        self.students = []
        self.answers = {}
        self.total_student_count = 0
        self.group_count = 0
        self.total_points = total_points
        self.outcome_mapping = None
        self.group_outcome_means = None
        self.outcomes = None
        self.open_file(filename)

    def open_file(self, filename):
        with open(filename, encoding="ISO-8859-9") as f:
            logging.info(f"{filename} dosyası açılıyor.")
            lines = f.readlines()
            logging.info(f"{len(lines)} satır okundu.")
        for line in lines:
            ogr, liste = self.process_line(line)
            if ogr:
                self.students.append(Ogrenci(*liste))
            else:
                logging.info(f"Cevap okunuyor. Cevap grubu: {liste[0]}")
                if liste[0] == " ":
                    grup = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                    grup = grup[self.group_count]
                    logging.warning(f"Cevap grubu boş girilmiş. Yeni grup {grup} olarak seçiliyor")
                    self.answers[grup] = Answers(grup, liste[1])
                else:
                    logging.info(f"Cevap grubu {liste[0]} eklendi.")
                    self.answers[liste[0]] = Answers(liste[0], liste[1])
                self.group_count += 1
        logging.info(f"Cevaplar ve öğrenciler okundu. Toplam {len(self.students)} öğrenci, {len(self.answers)} cevap grubu.")
        self.calculate_grades()

    def process_line(self, line):
        if line[11:16] == "CEVAP":
            return False, [line[36], line[37:137]]
        else:
            return True, [line[:8], line[8:11], line[11:35], line[35], line[36], line[37:137]]

    def calculate_grades(self):
        for student in self.students:
            student_group = student.kitapcik
            # if student forget to mark the group
            # choose the first one as his/her group
            if student_group not in self.answers:
                student_group = next(iter(self.answers))
                logging.warning(f"{student.ogrno} - {student.adi} grubu bulunamadı. Grup {student_group} olarak seçiliyor.")

            answer:Answers = self.answers[student_group]
            answer.student_count += 1
            self.total_student_count += 1

            for q in range(answer.question_count):
                if answer.is_empty(q, student.cevaplar):
                    student.bos += 1
                    answer.statistics[q]["empty"] += 1
                elif answer.check_question(q, student.cevaplar):
                    student.dogru += 1
                    answer.statistics[q]["correct"] += 1
                else:
                    student.yanlis += 1
                    answer.statistics[q]["incorrect"] += 1
            student.puan = round(student.dogru/answer.question_count*self.total_points)
            logging.info(f"{student.ogrno} - {student.adi} cevapları okundu. Doğru: {student.dogru} Yanlış: {student.yanlis} Boş: {student.bos} Puan: {student.puan}")

    def calculate_learnig_outcome_contributions(self, mapping, outcome_count):
        self.outcome_mapping = mapping
        group_outcomes = {}
        for answer in self.answers:
            group_outcomes[answer] = {}
            for i,q in enumerate(self.answers[answer].statistics):
                q["correct percentage"] = q["correct"] / self.answers[answer].student_count * 100
                if mapping[answer][i] not in group_outcomes[answer]:
                    group_outcomes[answer][mapping[answer][i]] = []
                group_outcomes[answer][mapping[answer][i]].append(q["correct percentage"])
        # print(group_outcomes)

        group_outcome_means = {}
        for answer in self.answers:
            group_outcome_means[answer] = {}
            for i in range(outcome_count):
                if i not in group_outcomes[answer]:
                    group_outcome_means[answer][i] = 0
                else:
                    group_outcome_means[answer][i] = self.mean(group_outcomes[answer][i])
        # print(group_outcome_means)
        self.group_outcome_means = group_outcome_means

        self.outcomes = [0 for i in range(outcome_count)]
        for o in range(outcome_count):
            for a in self.answers:
                self.outcomes[o] += group_outcome_means[a][o]*self.answers[a].student_count

            self.outcomes[o] /= self.total_student_count
        # print(self.outcomes)

    def mean(self, alist):
        return sum(alist) / len(alist)




if __name__ == "__main__":
    filename = "../muhtestpy/prog.dil.txt"
    exam = Exam(filename)
    print(exam)
