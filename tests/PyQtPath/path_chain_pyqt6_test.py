from PyQt5.QtWidgets import QCheckBox
from PyQt6.QtWidgets import QLabel, QWidget, QPushButton, QGroupBox
from pytestqt.qtbot import QtBot

from src.PyQtPath.path_chain_pyqt6 import path


def test_get_nested_element(window: QWidget, qtbot: QtBot):
    qtbot.addWidget(window)

    label: QLabel = path(window).label().get()
    assert label.text() == "Hello, World!"

    dialog_label: QLabel = path(window).dialog().label().get()
    assert dialog_label.text() == "This is a dialog"

    ok_button: QPushButton = path(window).dialog().button().get()
    assert ok_button.text() == "Ok"

    close_button: QPushButton = path(window).dialog().button(1).get()
    assert close_button.text() == "Close"


def test_group_box(window: QWidget, qtbot: QtBot):
    qtbot.addWidget(window)

    group_box: QGroupBox = path(window).group().get()
    assert group_box.title() == "Options"

    check_box_1: QCheckBox = path(window).group().checkbox().get()
    assert check_box_1.text() == "Option 1"

    check_box_2: QCheckBox = path(window).group().checkbox(1).get()
    assert check_box_2.text() == "Option 2"
