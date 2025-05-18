from abc import ABC, abstractmethod

class AbstractItem(ABC):
    @abstractmethod
    def calculate_total_price(self):
        pass

class Item(AbstractItem):
    def __init__(self, name, quantity, priceperunit, taxrate):
        self.__name = name
        self.__quantity = quantity
        self.__price_per_unit = priceperunit
        self.__tax_rate = taxrate

    @property
    def name(self):
        return self.__name

    @name.setter                          # encapsulation using getter and setter method
    def name(self, new_name):
        self.__name = new_name

    def __str__(self):
        return f"{self.__name}:Quantity={self.__quantity},Unit Price={self.__price_per_unit}, Tax Rate={self.__tax_rate}%"

    def calculate_total_price(self):
        total_price = self.__quantity * self.__price_per_unit
        tax = total_price * (self.__tax_rate / 100)
        return total_price + tax

class Bill:
    def __init__(self):
        self.items = []

    def add_item(self, name, quantity, priceperunit, taxrate):
        if quantity <= 0 or priceperunit <= 0:
            print(f"Invalid quantity or price for item '{name}'. Item not added.")
            return
        item = Item(name, quantity, priceperunit, taxrate)
        self.items.append(item)
        print(f"Added item: {item}")

    def remove_item(self, name):
        for item in self.items:
            if item.name == name:
                self.items.remove(item)
                print(f"Removed item: {name}")
                return
        print(f"Item {name} not in the bill")

    def generate_bill(self):
        if not self.items:
            print("No items to display in the bill.")
            return
        print("\n--- Billing details ---")
        total_amount = 0
        for item in self.items:
            item_price = item.calculate_total_price()
            total_amount += item_price
            print(f"{item.name} - Total Price: ₹{item_price:.2f}")
        print(f"\nTotal Amount: ₹{total_amount:.2f}")
        return total_amount

    def __add__(self, other):
        combined_bill = Bill()
        combined_bill.items = self.items + other.items
        return combined_bill

class discountBill(Bill):
    def __init__(self, discount_rate):
        super().__init__()
        self.discount_rate = discount_rate

    def generate_bill(self):
        total_amount = super().generate_bill()
        if total_amount is None:
            return
        discount = total_amount * (self.discount_rate / 100)
        final_amount = total_amount - discount
        print(f"Discount ({self.discount_rate}%): -₹{discount:.2f}")
        print(f"Final Payable Amount: ₹{final_amount}")

if __name__ == "__main__":
    bill1 = Bill()
    bill1.add_item("Milk", 2, 50, 5)
    bill1.add_item("Bread", 1, 30, 0)
    bill1.add_item("Eggs", 12, 5, 2)
    bill1.generate_bill()

    bill2 = Bill()
    bill2.add_item("Juice", 1, 100, 10)
    bill2.add_item("Butter", 1, 80, 5)

    combined_bill = bill1 + bill2
    print("\n--- Combined Bill ---")
    combined_bill.generate_bill()

    print("\n--- discount Bill ---")
    discounted_bill = discountBill(discount_rate=10)
    discounted_bill.items = combined_bill.items
    discounted_bill.generate_bill()
