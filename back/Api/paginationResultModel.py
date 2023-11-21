from typing import Generic, TypeVar
from pydantic.generics import GenericModel

T = TypeVar('T')


class PaginationResultModel(GenericModel, Generic[T]):
    page: int
    totalCount: int
    rows: list[T]
