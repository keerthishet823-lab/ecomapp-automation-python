from dataclasses import dataclass
from typing import Literal

SortOption = Literal[
    "Recommended",
    "Price: Low to High",
    "Price: High to Low",
    "Discount",
    "Newest First",
]


@dataclass(frozen=True)
class ProductCardSummary:
    name: str
    href: str | None
    price: str | None
    original_price: str | None
    discount_label: str | None
