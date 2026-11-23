"""validate 모듈"""


def is_valid_qty(qty):
    """주문 수량이 1 이상 99 이하이면 True를 반환한다."""
    return 1 <= qty <= 99
