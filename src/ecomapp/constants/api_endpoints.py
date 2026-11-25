class ApiEndpoints:
    class Auth:
        LOGIN = "/api/auth/login"
        REGISTER = "/api/auth/register"
        LOGOUT = "/api/auth/logout"
        REFRESH = "/api/auth/refresh"
        ME = "/api/auth/me"
        GOOGLE = "/api/auth/google"

    class Products:
        LIST = "/api/products"
        SEARCH = "/api/products/search"

        @staticmethod
        def by_id(product_id: str) -> str:
            return f"/api/products/{product_id}"

    class Cart:
        GET = "/api/cart"
        ADD_ITEM = "/api/cart/items"
        CLEAR = "/api/cart/clear"

        @staticmethod
        def update_item(item_id: str) -> str:
            return f"/api/cart/items/{item_id}"

        @staticmethod
        def remove_item(item_id: str) -> str:
            return f"/api/cart/items/{item_id}"

    class Wishlist:
        GET = "/api/wishlist"
        ADD_ITEM = "/api/wishlist/items"

        @staticmethod
        def remove_item(item_id: str) -> str:
            return f"/api/wishlist/items/{item_id}"

    class Orders:
        LIST = "/api/orders"
        CREATE = "/api/orders"

        @staticmethod
        def by_id(order_id: str) -> str:
            return f"/api/orders/{order_id}"

        @staticmethod
        def cancel(order_id: str) -> str:
            return f"/api/orders/{order_id}/cancel"

    class AdminProducts:
        LIST = "/api/admin/products"
        CREATE = "/api/admin/products"
        BULK_DELETE = "/api/admin/products/bulk-delete"

        @staticmethod
        def by_id(product_id: str) -> str:
            return f"/api/admin/products/{product_id}"

        @staticmethod
        def update(product_id: str) -> str:
            return f"/api/admin/products/{product_id}"

        @staticmethod
        def delete(product_id: str) -> str:
            return f"/api/admin/products/{product_id}"
