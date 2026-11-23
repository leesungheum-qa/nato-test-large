"""date_util 모듈"""


def is_weekend(weekday):
    """요일 번호(월=0)가 5 이상이면 주말이므로 True를 반환한다."""
    return weekday >= 5
