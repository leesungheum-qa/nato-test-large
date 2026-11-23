"""review 모듈"""


def average_rating(ratings):
    """별점 목록의 평균을 소수 첫째 자리까지 반환한다. 비어 있으면 0을 반환한다."""
    return round(sum(ratings) / len(ratings), 1) if ratings else 0
