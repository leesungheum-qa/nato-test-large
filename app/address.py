"""address 모듈"""


def format_address(city, district, detail):
    """시, 구, 상세 주소를 공백으로 이어 한 줄 주소로 반환한다."""
    return f"{city} {district} {detail}"
