from PyQt6.QtWidgets import QLabel, QWidget, QPushButton, QGroupBox, QCheckBox
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


def test_group_box(window: QWidget, qtbot: QtBot):
    qtbot.addWidget(window)

    group_box: QGroupBox = child(window, "QGroupBox")
    assert group_box.title() == "Options"

    check_box_1: QCheckBox = child(window, "QGroupBox/QCheckBox")
    assert check_box_1.text() == "Option 1"

    check_box_2: QCheckBox = child(window, "QGroupBox/QCheckBox/1")
    assert check_box_2.text() == "Option 2"
