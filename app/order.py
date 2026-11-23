"""order 모듈"""


def create_order(seq):
    """주문 번호를 "ORD-" 뒤에 숫자 6자리로 만들어 반환한다."""
    return "ORD-" + str(seq).zfill(6)
