# Authors: Rahmatulloh and Bahodir
# 1.2 items=[] in the class and coupons=[] as default are made once, so all carts share them. Root cause: one mutable list shared by all objects.
# 1.3 Create lists in __init__. In dataclass "coupons: list = []" gives ValueError, so use field(default_factory=list).
# 1.4 append changes the shared list. self.count += 1 is an assignment, it makes a new attribute only on this object.
from dataclasses import dataclass, field

class OldCart:
    items = []
    def __init__(self, user_id, coupons=[]):
        self.user_id = user_id
        self.coupons = coupons
    def add(self, sku, qty=1):
        self.items.append((sku, qty))
    def apply_coupon(self, code):
        self.coupons.append(code)

@dataclass
class Cart:
    user_id: str
    items: list = field(default_factory=list)
    coupons: list = field(default_factory=list)
    def add(self, sku, qty=1):
        self.items.append((sku, qty))
    def apply_coupon(self, code):
        self.coupons.append(code)

def check(cls):
    a = cls("Rahmatulloh")
    b = cls("Bahodir")
    a.add("A1", 2)
    a.apply_coupon("SALE")
    return b.items == [] and b.coupons == []

def test_cart():
    assert check(Cart)       # with OldCart this fails

def test_old_cart():
    assert not check(OldCart)


