"""rank 모듈"""


def top_n(scores, n):
    """점수가 높은 순으로 n개를 반환한다."""
    return sorted(scores, reverse=True)[:n]
