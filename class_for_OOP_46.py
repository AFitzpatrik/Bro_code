class Car: #toto je objekt
    def __init__(self, model, year, color, for_sale): #constructor, totu metodu potřebujeme vždy když vytváříme objekt.
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"You drive the {self.color} {self.model}!")


    def stop(self):
        print(f"You stop the {self.color} {self.model}!")


    def describe(self):
        print(f"{self.year} {self.color} {self.model}")
