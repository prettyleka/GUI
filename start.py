import os
import subprocess
from builtins import super
from tkinter import *
from subprocess import *
from PyQt5 import QtWidgets, QtCore, QtGui, Qt
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QButtonGroup, QCheckBox



import design  # Это наш конвертированный файл дизайна


class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):  # Это здесь нужно для доступа к переменным, методам и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.treeWidget.setHeaderLabels(['Files'])
        self.treeWidget.setAlternatingRowColors(True)
        self.current_dir = ""
        self.selectBtn.clicked.connect(self.browse_folder)
        self.runBtn.clicked.connect(self.run_checked_tests)
        self.stopBtn.clicked.connect(self.stop_all_tests)
        self.clearBtn.clicked.connect(self.clear)
        self.refreshBtn.clicked.connect(self.print_logs)
        self.Check.clicked.connect(self.all_checked)
        self.Uncheck.clicked.connect(self.uncheck)
        self.file_types = {
            ".js": "node",
            ".py": "python"
        }
        self.processes = []

        self.runBtn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.stopBtn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.selectBtn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.clearBtn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.refreshBtn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.Uncheck.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.Check.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.stopBtn.setStyleSheet(
            "QPushButton:hover { background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #FAFBFE, stop: 1 #DCDEF1) }")
        self.runBtn.setStyleSheet(
            "QPushButton:hover { background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #FAFBFE, stop: 1 #DCDEF1) }")
        self.clearBtn.setStyleSheet(
            "QPushButton:hover { background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #FAFBFE, stop: 1 #DCDEF1) }")
        self.selectBtn.setStyleSheet(
            "QPushButton:hover { background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #FAFBFE, stop: 1 #DCDEF1) }")
        self.refreshBtn.setStyleSheet(
            "QPushButton:hover { background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #FAFBFE, stop: 1 #DCDEF1) }")
        self.Check.setStyleSheet(
            "QPushButton:hover { background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #FAFBFE, stop: 1 #DCDEF1) }")
        self.Uncheck.setStyleSheet(
            "QPushButton:hover { background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #FAFBFE, stop: 1 #DCDEF1) }")

        self.label_2.setOpenExternalLinks(True)
        self.label_3.setOpenExternalLinks(True)
        self.label_2.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.label_3.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.label_2.setStyleSheet(
            "QLabel:hover { background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #FAFBFE, stop: 1 #DCDEF1) }")
        self.label_3.setStyleSheet(
            "QLabel:hover { background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #FAFBFE, stop: 1 #DCDEF1) }")

        self.label_2.setText("<a href=\"https://www.linkedin.com/in/valeria-basova-58495318/\">Valeria Basov</a>")
        self.label_3.setText("<a href=\"https://www.linkedin.com/in/ilya-livshits-b12295108\">Iliya Livshits</a>")



    def browse_folder(self):
        self.current_dir = QtWidgets.QFileDialog.getExistingDirectory(self, "Select a folder")  # путь к файлам
        if self.current_dir:  # не продолжать, если нет доступа к файлам
            self.treeWidget.clear()  # на случай, если в дирректории были файлы
            for file_name in os.listdir(self.current_dir):  # для каждого файла в директории
                if file_name.endswith('js') or file_name.endswith('py'):
                    item = QtWidgets.QTreeWidgetItem(self.treeWidget, [file_name])
                    item.setCheckState(0, QtCore.Qt.Unchecked)  # квадратики
                    print(file_name)



    def clear(self):
        self.listWidget.clear()

    def run_file_with(self, file_name):
        if not self.file_types:
            return ""
        for eof in self.file_types:
            if file_name.endswith(eof):
                return self.file_types[eof]
        return ""

    def find_checked(self):  # найти отмеченные файлы
        checked_items = list()
        root = self.treeWidget.invisibleRootItem()  # создали корень
        child_count = root.childCount()  #
        for i in range(child_count):
            i_child = root.child(i)
            if i_child.checkState(0) == QtCore.Qt.Checked:
                checked_items.append(i_child.text(0))
        return checked_items

    def is_allowed_file(self, file_name):
        if not self.file_types:
            return True
        for eof in self.file_types:
            if file_name.endswith(eof):
                return True
        return False

    def generate_command_for_file_names(self, file_names):  # создаем лист с тестами
        command_list = list(map(lambda file_name: f"{self.run_file_with(file_name)} {file_name}", file_names))
        return " && ".join(command_list)

    def run_checked_tests(self):
        checked_files = self.find_checked()
        if not checked_files:
            return ""
        run_command = self.generate_command_for_file_names(checked_files)
        process = subprocess.Popen(run_command, shell=True, cwd=self.current_dir)
        self.processes.append({"id": process.pid})
        self.runBtn.setEnabled(False)
        self.treeWidget.setEnabled(False)

    def print_logs(self):
        logger_file_path = self.current_dir + "/log/"
        for file in os.listdir(logger_file_path):
            if file.endswith(".log"):
                logger_file_full_path = logger_file_path + file
                with open(logger_file_full_path, "r") as logger_file:
                    self.listWidget.append(logger_file.read())


    def kill(self, proc_pid):
        Popen("TASKKILL /F /PID {pid} /T".format(pid=proc_pid))

    def stop_all_tests(self, proc_pid):
        exit_msg = "Are you sure you want to stop?"
        resp = QtWidgets.QMessageBox.question(self, "save changes", exit_msg, QtWidgets.QMessageBox.Yes,
                                              QtWidgets.QMessageBox.No)
        if resp == QtWidgets.QMessageBox.Yes:
            for p in self.processes:
                self.kill(p["id"])
                self.runBtn.setEnabled(True)
                self.treeWidget.setEnabled(True)


    def all_checked(self):
        root = self.treeWidget.invisibleRootItem()  # создали корень
        child_count = root.childCount()  #
        for i in range(child_count):
            i_child = root.child(i)
            i_child.setCheckState(0, QtCore.Qt.Checked)

    def uncheck(self):
        root = self.treeWidget.invisibleRootItem()  # создали корень
        child_count = root.childCount()  #
        for i in range(child_count):
            i_child = root.child(i)
            i_child.setCheckState(0, QtCore.Qt.Unchecked)






def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
