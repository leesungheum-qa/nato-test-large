"""cart 모듈"""


def add_to_cart(cart, item):
    """장바구니 목록에 상품을 추가하고 목록을 반환한다."""
    cart.append(item)
    return cart
