from PyQt6.QtCore import QObject
from PyQt6.QtWidgets import QCheckBox, QLabel, QDialog, QPushButton, QTableWidget, QGroupBox, QLayout

from .types import QObjectSubClass


def path(objects: QObject) -> 'Path':
    return Path([objects])


class Path:
    def __init__(self, objects: list[QObject]) -> None:
        self.objects: list[QObject] = objects

    def get(self, index: int = 0) -> QObjectSubClass:
        return self.objects[index]

    def checkbox(self, index: int = 0) -> 'Path':
        return self.child(QCheckBox, index)

    def label(self, index: int = 0) -> 'Path':
        return self.child(QLabel, index)

    def dialog(self, index: int = 0) -> 'Path':
        return self.child(QDialog, index)

    def button(self, index: int = 0) -> 'Path':
        return self.child(QPushButton, index)

    def table(self, index: int = 0) -> 'Path':
        return self.child(QTableWidget, index)

    def group(self, index: int = 0) -> 'Path':
        return self.child(QGroupBox, index)

    def layout(self, index: int = 0) -> 'Path':
        obj: QObject = self.objects[0]
        children: list[QObject] = obj.children()
        layouts: list[QLayout] = [child for child in children if isinstance(child, QLayout)]
        lay: QLayout = layouts[index]
        return Path([lay])

    def child(self, clazz: type[QObject], index: int = 0) -> 'Path':
        obj: QObject = self.objects[0]
        if isinstance(obj, QLayout):
            return Path([obj.itemAt(index).widget()])
        else:
            return Path([obj.findChildren(clazz)[index]])
