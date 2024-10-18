import pytest
from PyQt6.QtWidgets import QWidget, QLabel, QDialog, QVBoxLayout, QPushButton, QGroupBox, QCheckBox


@pytest.fixture
def window() -> QWidget:
    label: QLabel = QLabel("Hello, World!")
    dialog: QDialog = __create_dialog()
    layout: QVBoxLayout = QVBoxLayout()
    layout.setObjectName("window-layout")
    group_box: QGroupBox = __create_group_box()
    box_layout: QVBoxLayout = __create_box_layout()
    layout.addWidget(label)
    layout.addWidget(dialog)
    layout.addWidget(group_box)
    layout.addLayout(box_layout)
    window: QWidget = QWidget()
    window.setLayout(layout)
    return window


def __create_dialog() -> QDialog:
    layout: QVBoxLayout = QVBoxLayout()
    layout.setObjectName("dialog-layout")
    layout.addWidget(QLabel("This is a dialog"))
    layout.addWidget(QPushButton("Ok"))
    layout.addWidget(QPushButton("Close"))

    dialog: QDialog = QDialog()
    dialog.setLayout(layout)
    return dialog


def __create_group_box() -> QGroupBox:
    checkbox1: QCheckBox = QCheckBox("Option 1")
    checkbox2: QCheckBox = QCheckBox("Option 2")
    layout: QVBoxLayout = QVBoxLayout()
    layout.setObjectName("group-box-layout")
    layout.addWidget(checkbox1)
    layout.addWidget(checkbox2)
    group_box: QGroupBox = QGroupBox("Options")
    group_box.setLayout(layout)
    return group_box


def __create_box_layout() -> QVBoxLayout:
    label1: QLabel = QLabel("VBox Label 1")
    label2: QLabel = QLabel("VBox Label 2")
    layout: QVBoxLayout = QVBoxLayout()
    layout.setObjectName("vbox-layout")
    layout.addWidget(label1)
    layout.addWidget(label2)
    return layout
