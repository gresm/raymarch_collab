from typing import Generic, TypeVar


_K1 = TypeVar("_K1")
_K2 = TypeVar("_K2")


class _FuncRequestType(Generic[_K1, _K2]):
    def __call__(self, pos: tuple[_K1, _K2], *args, **kwargs) -> float: ...


_FuncType = _FuncRequestType[int, int]


class _ShapeCreator:
    def __init__(self, func: _FuncType):
        self.func = func

    def __call__(self, *args, **kwargs):
        return _ShapeExecutor(self, args, kwargs)


class _ShapeExecutor:
    def __init__(self, creator: _ShapeCreator, args: tuple, kwargs: dict):
        self.creator = creator
        self.args = args
        self.kwargs = kwargs

    def __call__(self, x: int, y: int):
        return self.creator.func((x, y), *self.args, *self.kwargs)


def shape(func: _FuncType):
    return _ShapeCreator(func)
