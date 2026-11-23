"""point 모듈"""


def earn_point(paid):
    """결제 금액의 1%를 정수로 내려 적립 포인트로 반환한다."""
    return int(paid * 0.01)
