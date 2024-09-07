from typing import Optional

from PyQt6.QtWidgets import QVBoxLayout, QLabel, QWidget, QDialog, QPushButton
from pytestqt.qtbot import QtBot


def test_get_nested_element(qtbot: QtBot):
    window: QWidget = __create_window()
    qtbot.addWidget(window)

    label: QLabel = get_nested_child(window, QLabel)
    assert label.text() == "Hello, World!"

    dialog_label: QLabel = get_nested_child(window, QDialog, QLabel)
    assert dialog_label.text() == "This is a dialog"

    ok_button: QPushButton = get_nested_child(window, QDialog, QPushButton, 0)
    assert ok_button.text() == "Ok"

    close_button: QPushButton = get_nested_child(window, QDialog, QPushButton, 1)
    assert close_button.text() == "Close"


def get_nested_child(widget: QWidget, *path: type[QWidget] | int) -> Optional:
    path_list: list[type[QWidget] | int] = list(path)
    normalized_path: list[(type[QWidget], int)] = __normalize_path(path_list)
    return __nested_child(widget, normalized_path)


def __nested_child(widget: QWidget, path: list[(type[QWidget], int)]) -> Optional:
    current_widget: QWidget = widget
    for part in path:
        clazz: type[QWidget] = part[0]
        index: int = part[1]
        children: list[QWidget] = current_widget.findChildren(clazz)
        if len(children) == 0:
            return None
        current_widget = children[index]
    return current_widget


def __normalize_path(path: list[type[QWidget] | int]) -> list[(type[QWidget], int)]:
    if path is None or len(path) == 0:
        return []
    if isinstance(path[0], int):
        raise RuntimeError("The 1st element cannot be an index")
    for i, part in enumerate(path):
        if isinstance(part, int):
            continue
        next_part: type[QWidget] | int = path[i + 1] if i < len(path) - 1 else None
        if next_part is not None and isinstance(next_part, int):
            yield part, next_part
        else:
            yield part, 0


def __create_window():
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
