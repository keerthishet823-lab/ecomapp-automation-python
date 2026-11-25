from dataclasses import dataclass


@dataclass(frozen=True)
class CategoryDefinition:
    name: str
    slug: str


# Shop-by-category slugs as they exist on muvake.com (header nav, home page
# "Shop by Category" tiles, and footer "Shop" links all point at these).
# Inventory varies per category — some legitimately render an empty state —
# so tests should not assume every category has products in stock.
CATEGORIES: tuple[CategoryDefinition, ...] = (
    CategoryDefinition("Sarees", "sarees"),
    CategoryDefinition("Kurtis", "kurtis"),
    CategoryDefinition("Kurti Sets", "kurti-sets"),
    CategoryDefinition("Coord Sets", "coord-sets"),
    CategoryDefinition("Short Tops", "short-tops"),
)
