import pytest
from PyQt6.QtWidgets import QWidget, QLabel, QDialog, QVBoxLayout, QPushButton, QGroupBox, QCheckBox


@pytest.fixture
def window() -> QWidget:
    label: QLabel = QLabel("Hello, World!")
    dialog: QDialog = __create_dialog()
    layout: QVBoxLayout = QVBoxLayout()
    group_box: QGroupBox = __create_group_box()
    layout.addWidget(label)
    layout.addWidget(dialog)
    layout.addWidget(group_box)
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


def __create_group_box() -> QGroupBox:
    checkbox1: QCheckBox = QCheckBox("Option 1")
    checkbox2: QCheckBox = QCheckBox("Option 2")
    group_layout: QVBoxLayout = QVBoxLayout()
    group_layout.addWidget(checkbox1)
    group_layout.addWidget(checkbox2)
    group_box: QGroupBox = QGroupBox("Options")
    group_box.setLayout(group_layout)
    return group_box
