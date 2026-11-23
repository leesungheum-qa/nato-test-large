"""금액 계산 모듈"""

TAX_RATE = 0.1


def calc_total(prices):
    """가격 목록의 합계에 부가세 10%를 더한 값을 반환한다."""
    subtotal = sum(prices)
    return round(subtotal * (1 + TAX_RATE))


def calc_discount(price, rate):
    """가격에서 할인율(rate, 0~1)만큼 뺀 값을 반환한다."""
    return round(price * (1 - rate))
