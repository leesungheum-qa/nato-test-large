"""coupon 모듈"""


def apply_coupon(price, code):
    """쿠폰 코드가 "WELCOME10"이면 10% 할인된 금액을, 아니면 원래 금액을 반환한다."""
    return round(price * 0.9) if code == "WELCOME10" else price
