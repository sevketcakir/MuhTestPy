from PySide6.QtCore import Qt, QAbstractTableModel, QModelIndex
from PySide6.QtWidgets import QApplication, QComboBox, QStyledItemDelegate, QTableView


class LearningOutcomeModel(QAbstractTableModel):
    def __init__(self, questions, learning_outcomes, groups, parent=None):
        """
        :param questions: List of question strings.
        :param learning_outcomes: List of learning outcomes available for selection.
        :param groups: List of group names (one column for each group).
        :param parent: Parent QObject.
        """
        super().__init__(parent)
        self.questions = questions
        self.learning_outcomes = learning_outcomes
        self.mapid = {name:id for id,name in enumerate(questions)}
        self.mapid.update({name:id for id,name in enumerate(learning_outcomes)})
        self.mapid[None] = 0
        self.groups = groups  # List of group names
        self.selected_outcomes = {group: [None] * len(questions) for group in groups}

    def rowCount(self, parent=QModelIndex()):
        return len(self.questions)

    def columnCount(self, parent=QModelIndex()):
        # One column for the question text and one column per group
        return 1 + len(self.groups)

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None

        row, column = index.row(), index.column()

        if role == Qt.DisplayRole:
            if column == 0:
                return self.questions[row]  # Question text
            else:
                group = self.groups[column - 1]
                return self.selected_outcomes[group][row] if self.selected_outcomes[group][row] else "Select..."

        return None

    def setData(self, index, value, role=Qt.EditRole):
        if not index.isValid():
            return False

        if role == Qt.EditRole and index.column() > 0:
            group = self.groups[index.column() - 1]
            self.selected_outcomes[group][index.row()] = value
            self.dataChanged.emit(index, index, [Qt.DisplayRole])
            return True

        return False

    def flags(self, index):
        if not index.isValid():
            return Qt.NoItemFlags

        if index.column() > 0:
            return Qt.ItemIsEditable | Qt.ItemIsEnabled | Qt.ItemIsSelectable
        return Qt.ItemIsEnabled | Qt.ItemIsSelectable

    def get_group_outcome_mapping(self):
        """
        Returns a dictionary mapping each group to a dictionary of question-to-selected-outcome mappings.
        Example:
        {
            "Group 1": {"Question 1": "Outcome A", "Question 2": "Outcome B"},
            "Group 2": {"Question 1": "Outcome C", "Question 2": "Outcome A"},
        }
        """
        mapping = {}
        for group in self.groups:
            mapping[group] = {
                self.mapid[question]: self.mapid[self.selected_outcomes[group][row]]
                for row, question in enumerate(self.questions)
            }
        return mapping, len(self.learning_outcomes)

class ComboBoxDelegate(QStyledItemDelegate):
    def __init__(self, items, parent=None):
        """
        :param items: List of items to display in the combobox.
        :param parent: Parent QObject.
        """
        super().__init__(parent)
        self.items = items

    def createEditor(self, parent, option, index):
        combo_box = QComboBox(parent)
        combo_box.addItems(self.items)
        return combo_box

    def setEditorData(self, editor, index):
        value = index.model().data(index, Qt.DisplayRole)
        if value in self.items:
            editor.setCurrentText(value)

    def setModelData(self, editor, model, index):
        model.setData(index, editor.currentText(), Qt.EditRole)


def main():
    import sys

    app = QApplication(sys.argv)

    # Example data
    questions = ["Question 1", "Question 2", "Question 3"]
    learning_outcomes = ["Outcome A", "Outcome B", "Outcome C"]
    groups = ["Group 1", "Group 2", "Group 3"]  # Dynamic number of groups

    model = LearningOutcomeModel(questions, learning_outcomes, groups)

    table_view = QTableView()
    table_view.setModel(model)

    # Set the delegate for all group columns
    delegate = ComboBoxDelegate(learning_outcomes)
    for column in range(1, len(groups) + 1):  # Delegate for group columns only
        table_view.setItemDelegateForColumn(column, delegate)

    table_view.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
