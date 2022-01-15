from typing import Protocol, TypeVar


_K1 = TypeVar("_K1")
_K2 = TypeVar("_K2")


class _FuncRequestType(Protocol[_K1, _K2]):
    def __call__(self, pos: tuple[_K1, _K2], *args, **kwargs) -> float: ...


_DistanceFunc = _FuncRequestType[int, int]


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

    def __call__(self, x: int, y: int):
        return self.creator.func((x, y), *self.args, *self.kwargs)


def shape(func: _DistanceFunc):
    return _ShapeCreator(func)
