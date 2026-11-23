"""refund 모듈"""


def calc_refund(paid):
    """환불 금액은 결제 금액에서 반품 배송비 3,000원을 뺀 값이다."""
    return max(paid - 3000, 0)
