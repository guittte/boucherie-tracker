
class MeatProduct:
    def __init__(self, name: str, type: str, price_per_kg: float):
        self.name = name
        self.type = type
        self.price_per_kg = price_per_kg

    def get_price(self, weight_kg: float) -> float:
        return self.price_per_kg * weight_kg

    def __str__(self):
        return f"{self.name} ({self.type}) - {self.price_per_kg:.2f}€/kg"

if __name__ == "__main__":
    # Example Usage
    beef_steak = MeatProduct("Steak de boeuf", "Boeuf", 25.50)
    pork_chop = MeatProduct("Côte de porc", "Porc", 12.90)

    print(beef_steak)
    print(f"Price for 0.5kg of {beef_steak.name}: {beef_steak.get_price(0.5):.2f}€")

    print(pork_chop)
    print(f"Price for 0.3kg of {pork_chop.name}: {pork_chop.get_price(0.3):.2f}€")
