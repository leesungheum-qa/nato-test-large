"""delivery 모듈"""


def estimate_days(remote):
    """도서산간 지역이면 5일, 아니면 2일을 반환한다."""
    return 5 if remote else 2
