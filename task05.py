# Authors: Rahmatulloh and Bahodir
# 5.3 price * (100 - discount) // 100
# 5.4 p = Stored(100000, 10); p.price = 200000; p.final is still 90000.
class Product:
    def __init__(self, sku, price, discount_percent=0):
        self._sku = sku
        self.price = price
        self.discount_percent = discount_percent
    @property
    def sku(self):
        return self._sku
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, v):
        if type(v) is not int or v <= 0:
            raise ValueError("bad price")
        self._price = v
    @property
    def discount_percent(self):
        return self._d
    @discount_percent.setter
    def discount_percent(self, v):
        if type(v) is not int or v < 0 or v > 90:
            raise ValueError("bad discount")
        self._d = v
    def final_price(self):
        return self._price * (100 - self._d) // 100

def test_product():
    p = Product("A1", 99_990, 15)
    assert p.final_price() == 84_991
    p.price = 120_000
    for f in (lambda: setattr(p, "price", 0),
              lambda: setattr(p, "discount_percent", 150),
              lambda: Product("A1", -5)):
        try:
            f()
            assert False
        except ValueError:
            pass
    try:
        p.sku = "X"
        assert False
    except AttributeError:
        pass


