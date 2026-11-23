"""wishlist 모듈"""


def toggle_wish(wish, item):
    """찜 목록에 상품이 있으면 빼고, 없으면 넣는다."""
    wish.remove(item) if item in wish else wish.append(item)
    return wish
