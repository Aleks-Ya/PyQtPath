from PyQt6.QtWidgets import QLabel, QWidget, QPushButton, QGroupBox
from pytestqt.qtbot import QtBot

from src.PyQtPath.path_str_pyqt6 import child


def test_get_nested_element(window: QWidget, qtbot: QtBot):
    qtbot.addWidget(window)

    label: QLabel = child(window, "QLabel")
    assert label.text() == "Hello, World!"

    dialog_label: QLabel = child(window, "QDialog/QLabel")
    assert dialog_label.text() == "This is a dialog"

    ok_button: QPushButton = child(window, "QDialog/QPushButton/0")
    assert ok_button.text() == "Ok"

    close_button: QPushButton = child(window, "QDialog/QPushButton/1")
    assert close_button.text() == "Close"

    group_box: QGroupBox = child(window, "QGroupBox")
    assert group_box.title() == "Options"
