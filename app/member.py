"""member 모듈"""


def get_grade(total):
    """누적 구매액이 100만 원 이상이면 "GOLD", 50만 원 이상이면 "SILVER", 아니면 "BASIC"을 반환한다."""
    return "GOLD" if total >= 1000000 else "SILVER" if total >= 500000 else "BASIC"
