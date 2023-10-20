from typing import Generic, TypeVar
from pydantic.generics import GenericModel

T = TypeVar('T')


class OperationResultModel(GenericModel, Generic[T]):
    error: str = ''
    data: T = ''
