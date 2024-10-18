from types import ModuleType
from typing import Optional
import importlib

from PyQt6.QtCore import QObject


def child(top_object: QObject, path: str) -> Optional:
    if top_object is None or path is None or len(path) == 0:
        return None
    normalized_path: list[(type[QObject], int)] = __normalize_path(path)
    return __nested_child(top_object, normalized_path)


def __nested_child(top_object: QObject, path: list[(type[QObject], int)]) -> Optional:
    current_object: QObject = top_object
    for part in path:
        clazz: type[QObject] = part[0]
        index: int = part[1]
        children: list[QObject] = current_object.findChildren(clazz)
        if len(children) == 0:
            return None
        current_object = children[index]
    return current_object


def __normalize_path(path: str) -> list[(type[QObject], int)]:
    if path is None or len(path) == 0:
        return []
    parts: list[str] = path.split("/")
    for i, part in enumerate(parts):
        if part.isdigit():
            continue
        next_part: str = parts[i + 1] if i < len(parts) - 1 else None
        module: ModuleType = importlib.import_module("PyQt6.QtWidgets")
        clazz: type[QObject] = getattr(module, part)
        if next_part is not None and next_part.isdigit():
            yield clazz, int(next_part)
        else:
            yield clazz, 0
