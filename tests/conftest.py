import pytest
from PyQt6.QtWidgets import QWidget, QLabel, QDialog, QVBoxLayout, QPushButton, QGroupBox, QCheckBox, QComboBox, \
    QHBoxLayout


@pytest.fixture
def window() -> QWidget:
    label: QLabel = QLabel("Hello, World!")
    dialog: QDialog = __create_dialog()
    layout: QVBoxLayout = QVBoxLayout()
    layout.setObjectName("window-layout")
    group_box: QGroupBox = __create_group_box()
    box_layout: QHBoxLayout = __create_box_layout()
    combo_box: QComboBox = __create_combo_box()

    layout.addWidget(label)
    layout.addWidget(dialog)
    layout.addWidget(group_box)
    layout.addLayout(box_layout)
    layout.addWidget(combo_box)

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


def __create_box_layout() -> QHBoxLayout:
    label1: QLabel = QLabel("VBox Label 1")
    label2: QLabel = QLabel("VBox Label 2")
    combo_box_3: QComboBox = QComboBox()
    combo_box_3.setObjectName("combo-box-3")
    layout1: QVBoxLayout = QVBoxLayout()
    layout1.setObjectName("vbox-layout-1")
    layout1.addWidget(label1)
    layout1.addWidget(label2)
    layout1.addWidget(combo_box_3)

    combo_box: QComboBox = QComboBox()
    combo_box.setObjectName("combo-box-2")
    layout2: QVBoxLayout = QVBoxLayout()
    layout2.setObjectName("vbox-layout-2")
    layout2.addWidget(combo_box)

    top_layout: QHBoxLayout = QHBoxLayout()
    top_layout.addLayout(layout1)
    top_layout.addLayout(layout2)
    return top_layout


def __create_combo_box() -> QComboBox:
    combo_box: QComboBox = QComboBox()
    combo_box.setObjectName("combo-box-1")
    return combo_box
