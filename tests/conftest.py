import pytest
from PyQt6.QtWidgets import QWidget, QLabel, QDialog, QVBoxLayout, QPushButton


@pytest.fixture
def window() -> QWidget:
    label: QLabel = QLabel("Hello, World!")
    dialog: QDialog = __create_dialog()
    layout: QVBoxLayout = QVBoxLayout()
    layout.addWidget(label)
    layout.addWidget(dialog)
    window: QWidget = QWidget()
    window.setLayout(layout)
    return window


def __create_dialog() -> QDialog:
    layout: QVBoxLayout = QVBoxLayout()
    layout.addWidget(QLabel("This is a dialog"))
    layout.addWidget(QPushButton("Ok"))
    layout.addWidget(QPushButton("Close"))

    dialog: QDialog = QDialog()
    dialog.setLayout(layout)
    return dialog
