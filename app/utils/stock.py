"""재고 확인 모듈"""


def is_in_stock(stock_table, item_id):
    """재고 표에서 item_id의 수량이 1개 이상이면 True를 반환한다."""
    return stock_table.get(item_id, 0) > 0


def reduce_stock(stock_table, item_id, count):
    """재고를 count만큼 줄이고, 부족하면 ValueError를 발생시킨다."""
    if stock_table.get(item_id, 0) < count:
        raise ValueError("재고가 부족합니다")
    stock_table[item_id] -= count
    return stock_table[item_id]
