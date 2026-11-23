"""notify 모듈"""


def make_message(order_no):
    """주문 번호를 넣어 "주문 ORD-xxx가 접수되었습니다" 문구를 반환한다."""
    return f"주문 {order_no}가 접수되었습니다"
