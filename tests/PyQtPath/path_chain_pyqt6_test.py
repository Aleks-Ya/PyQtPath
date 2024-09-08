from PyQt6.QtWidgets import QLabel, QWidget, QPushButton
from pytestqt.qtbot import QtBot

from src.PyQtPath.path_chain_pyqt6 import path


def test_get_nested_element(window: QWidget, qtbot: QtBot):
    qtbot.addWidget(window)

    label: QLabel = path(window).label().get()
    assert label.text() == "Hello, World!"

    dialog_label: QLabel = path(window).dialog().label().get()
    assert dialog_label.text() == "This is a dialog"

    ok_button: QPushButton = path(window).dialog().button(0).get()
    assert ok_button.text() == "Ok"

    close_button: QPushButton = path(window).dialog().button(1).get()
    assert close_button.text() == "Close"
