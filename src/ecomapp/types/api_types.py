from dataclasses import dataclass, field
from typing import Any, Literal

HttpMethod = Literal["GET", "POST", "PUT", "PATCH", "DELETE"]


@dataclass(frozen=True)
class ApiResponse[T]:
    status: int
    body: T
    headers: dict[str, str]
    ok: bool


@dataclass(frozen=True)
class PaginatedResponse[T]:
    items: list[T]
    total: int
    page: int
    page_size: int


@dataclass(frozen=True)
class ApiError:
    status: int
    message: str
    detail: Any = None


@dataclass(frozen=True)
class RequestOptions:
    data: Any = None
    headers: dict[str, str] = field(default_factory=dict)
    params: dict[str, str] = field(default_factory=dict)
