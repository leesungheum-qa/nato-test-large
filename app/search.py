"""search 모듈"""


def filter_by_price(products, min_price, max_price):
    """가격이 min_price 이상 max_price 이하인 상품만 골라 반환한다."""
    return [p for p in products if min_price <= p["price"] <= max_price]
