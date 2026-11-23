"""phone 모듈"""


def mask_phone(phone):
    """전화번호 가운데 네 자리를 ****로 가린다."""
    return phone[:3] + "-****-" + phone[-4:]
