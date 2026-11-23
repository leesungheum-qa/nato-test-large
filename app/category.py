"""category 모듈"""


def is_valid_category(name):
    """카테고리가 "food", "book", "toy" 중 하나인지 확인한다."""
    return name in ("food", "book", "toy")
