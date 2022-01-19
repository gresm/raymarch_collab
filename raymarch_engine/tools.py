from __future__ import annotations

from typing import Protocol, TypeVar

import numpy as np


_K1 = TypeVar("_K1")


class _FuncRequestType(Protocol[_K1]):
    def __call__(self, ray: _K1, *args, **kwargs) -> float: ...


_DistanceFunc = _FuncRequestType[np.ndarray]


class _ShapeCreator:
    def __init__(self, func: _DistanceFunc):
        self.func = func

    def __call__(self, *args, **kwargs):
        return ShapeExecutor(self, args, kwargs)


class ShapeExecutor:
    def __init__(self, creator: _ShapeCreator, args: tuple, kwargs: dict):
        self.creator = creator
        self.args = args
        self.kwargs = kwargs

    def __call__(self, pos: tuple[float, float] | np.ndarray):
        return self.creator.func(np.array(pos), *self.args, *self.kwargs)


def shape(func: _DistanceFunc):
    return _ShapeCreator(func)
