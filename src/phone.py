from src.item import Item

class Phone:
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        super().__init__(name, price, quantity)
        self._number_of_sim = number_of_sim

    def __repr__(self):
        return f"Phone('{self.name}', {self.price}, {self.quantity}, {self._number_of_sim})"

    @property
    def number_of_sim(self):
        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, count):
        if isinstance(count, int) and count > 0:
            self._number_of_sim = count
        raise Exception