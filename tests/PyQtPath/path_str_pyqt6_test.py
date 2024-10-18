from PyQt6.QtWidgets import QLabel, QWidget, QPushButton, QGroupBox, QCheckBox, QVBoxLayout, QComboBox
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


def test_get_current(window: QWidget, qtbot: QtBot):
    qtbot.addWidget(window)
    widget: QWidget = child(window, "")
    assert widget == window


def test_layout(window: QWidget, qtbot: QtBot):
    qtbot.addWidget(window)

    window_layout: QVBoxLayout = child(window, "QVBoxLayout")
    assert window_layout.objectName() == "window-layout"

    vbox_layout: QVBoxLayout = child(window, "QVBoxLayout/QVBoxLayout")
    assert vbox_layout.objectName() == "vbox-layout-1"

    label1: QLabel = child(window, "QVBoxLayout/QVBoxLayout/QLabel")
    assert label1.text() == "VBox Label 1"

    label2: QLabel = child(window, "QVBoxLayout/QVBoxLayout/QLabel/1")
    assert label2.text() == "VBox Label 2"


def test_combo_box(window: QWidget, qtbot: QtBot):
    qtbot.addWidget(window)
    combo_box: QComboBox = child(window, "QVBoxLayout/QComboBox")
    assert combo_box.objectName() == "combo-box-1"
