"""배송비 계산 모듈"""

FREE_SHIPPING_LIMIT = 50000
BASE_FEE = 3000


def calc_shipping_fee(order_amount):
    """주문 금액이 50,000원 이상이면 0원, 아니면 3,000원을 반환한다."""
    if order_amount >= FREE_SHIPPING_LIMIT:
        return 0
    return BASE_FEE
