from PyQt6.QtWidgets import QLabel, QWidget, QPushButton, QGroupBox, QCheckBox, QVBoxLayout, QComboBox
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


def test_get_current(window: QWidget, qtbot: QtBot):
    qtbot.addWidget(window)
    widget: QWidget = path(window).get()
    assert widget == window


def test_layout(window: QWidget, qtbot: QtBot):
    qtbot.addWidget(window)

    window_layout: QVBoxLayout = path(window).layout().get()
    assert window_layout.objectName() == "window-layout"

    vbox_layout_1: QVBoxLayout = path(window).layout().layout().layout().get()
    assert vbox_layout_1.objectName() == "vbox-layout-1"

    label1: QLabel = path(window).layout().layout().layout().label().get()
    assert label1.text() == "VBox Label 1"

    label2: QLabel = path(window).layout().layout().layout().label(1).get()
    assert label2.text() == "VBox Label 2"

    vbox_layout_2: QVBoxLayout = path(window).layout().layout().layout(1).get()
    assert vbox_layout_2.objectName() == "vbox-layout-2"

    combo_box: QComboBox = path(window).layout().layout().layout(1).combobox().get()
    assert combo_box.objectName() == "combo-box-2"


def test_combo_box(window: QWidget, qtbot: QtBot):
    qtbot.addWidget(window)
    combo_box: QComboBox = path(window).combobox(1).get()  # finds all children among all Layouts
    assert combo_box.objectName() == "combo-box-1"
