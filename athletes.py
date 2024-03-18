class Athlete:
    def __init__(self, name, sport, country, age):
        self.name = name
        self.sport = sport
        self.country = country
        self.age = age

    def get_details(self):
        return f"Name: {self.name}, Sport: {self.sport}, Country: {self.country}, Age: {self.age}"

    def update_details(self, name=None, sport=None, country=None, age=None):
        if name:
            self.name = name
        if sport:
            self.sport = sport
        if country:
            self.country = country
        if age:
            self.age = age

# Example usage:
# athlete1 = Athlete("John Doe", "Swimming", "USA", 25)
# print(athlete1.get_details())
# athlete1.update_details(age=26)
# print(athlete1.get_details())