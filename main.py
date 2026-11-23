"""진입 파일"""
from app.utils.calc import calc_total
from app.utils.shipping import calc_shipping_fee


def run():
    total = calc_total([10000, 20000])
    fee = calc_shipping_fee(total)
    print("합계:", total, "배송비:", fee)


if __name__ == "__main__":
    run()
