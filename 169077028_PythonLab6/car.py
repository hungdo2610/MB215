def __init__ (self, make, model, year): #activity1: Define car class
    self.make = make
    self.__model = model #activity3: Hiding data attributes
    self.year = year
    

def display_info(self): #activity2: Public method to display car info
    print("Make:", self.make)
    print("Model:", self.model)
    print("Year:", self.year)

def __update_model(self, new_model): #activity2: Private method to update model
    self.model = new_model

def __str__ (self): #activity4: The str method
    return f"{self.make} {self.model} ({self.year})"
    