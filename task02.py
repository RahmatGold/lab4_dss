# Authors: Rahmatulloh and Bahodir
# 2.1 right: 0 / 18000 / 15000. Checkout: 0 / 15000 / 12000. Receipt: 15000 / 15000 / 15000. Courier: 0 / 15600.0 / 13800.0.
#     Only Receipt is right in the 3rd case, nobody in the 2nd.
# 2.2 Order has the data, so the rule is in Order.delivery_fee().
# 2.3 math.ceil
import math

class Order:
    PRICE_PER_KM = 3000
    def __init__(self, food_total, distance_km):
        self.food_total = food_total
        self.distance_km = distance_km
    def delivery_fee(self):
        if self.food_total >= 150_000:
            return 0
        return 12_000 + math.ceil(max(0, self.distance_km - 3)) * self.PRICE_PER_KM

class CheckoutService:
    def delivery_fee(self, order):
        return order.delivery_fee()

class ReceiptService:
    def delivery_fee(self, order):
        return order.delivery_fee()

class CourierPayoutService:
    def delivery_fee(self, order):
        return order.delivery_fee()

def test_fee():
    assert Order(149_999, 3.0).delivery_fee() == 12_000
    assert Order(150_000, 3.0).delivery_fee() == 0
    assert Order(90_000, 3.01).delivery_fee() == 15_000
    assert Order(90_000, 4.0).delivery_fee() == 15_000


