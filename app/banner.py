"""banner 모듈"""


def pick_banner(on_event):
    """이벤트 중이면 "event", 아니면 "default" 배너 이름을 반환한다."""
    return "event" if on_event else "default"
