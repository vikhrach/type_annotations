"""
TODO:

Define a decorator that wraps a function and returns a function with the same signature.
"""
from typing import Callable, TypeVar


def decorator[T:Callable](func:T)->T:
    return func


