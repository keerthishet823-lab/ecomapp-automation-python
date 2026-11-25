class Routes:
    HOME = "/"
    LOGIN = "/login"
    REGISTER = "/register"
    CATALOG = "/products"
    CART = "/cart"
    WISHLIST = "/wishlist"
    CHECKOUT = "/checkout"
    ORDER_HISTORY = "/orders"
    ACCOUNT = "/account"
    ACCOUNT_PROFILE = "/account/profile"
    ACCOUNT_ORDERS = "/account/orders"

    @staticmethod
    def product_details(product_id: str) -> str:
        return f"/products/{product_id}"

    @staticmethod
    def order_details(order_id: str) -> str:
        return f"/orders/{order_id}"

    @staticmethod
    def category(slug: str) -> str:
        return f"/categories/{slug}"

    class Admin:
        ROOT = "/admin"
        PRODUCTS = "/admin/products"
        PRODUCT_CREATE = "/admin/products/new"

        @staticmethod
        def product_edit(product_id: str) -> str:
            return f"/admin/products/{product_id}/edit"
