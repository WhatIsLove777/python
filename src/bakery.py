class Pastry:
    """Pastry class."""

    def __init__(self, name: str, complexity_level: int):
        """Class constructor."""
        self.name = name
        self.complexity_level = complexity_level

    def __repr__(self):
        """Represent object in string format."""
        return self.name

class Baker:
    """Class baker."""

    def __init__(self, name: str, experience_level: int, money: int):
        """Class constructor."""
        self.name = name
        self.experience_level = experience_level
        self.money = money

    def __str__(self):
        """Represent object in string format."""
        return "Baker: {}({})".format(self.name, self.experience_level)

    def __repr__(self):
        """Represent object in string format."""
        return "Baker: {}({})".format(self.name, self.experience_level)

class Bakery:
    """Class bakery."""

    def __init__(self, name: str, min_experience_level: int, budget: int):
        """Class constructor."""
        self.name = name
        self.min_experience_level = min_experience_level
        self.budget = budget
        self.recipes = {}
        self.bakers = []
        self.pastries = []

    def add_baker(self, baker: Baker) -> Baker:
        """Add baker."""
        # Для удобства можно вывести имя и уровень опыта каждого работника
        print(baker.name)
        print(baker.experience_level)
        # print(self.min_experience_level)

        if baker.experience_level >= self.min_experience_level:
            i = -1
            while i < len(self.bakers):
                # if baker.name not in self.bakers:
                #     return self.bakers.append(baker.name)
                # else:
                #     print("Baker exists")
                # i+=1
                if baker.name not in self.bakers:
                    return self.bakers.append(baker.name)
                    for key in bakers:
                        print(key, bakers)
                else:
                    print("Baker exists")
                i+=1
        else:
            print(f"Not enough experience, sorry {baker.name}")

    def remove_baker(self, baker: Baker):
        """Remove baker."""
        i = -1
        while i < len(self.bakers):
            if self.name not in self.bakers:
                return "No such baker"
            else:
                return self.bakers.remove(baker.name)
            i+=1

    def add_recipe(self, name: str):
        """Add recipe."""
        i = -1
        while i < len(self.recipes):
            if self.name not in self.recipes:
                # return self.recipes = self.recipes[self.name] = baker.name
                self.budget -= len(name)
                return self.recipes.update({name : self.bakers[i]})
            else:
                return "Recipe exists already"
            i+=1

    def make_order(self, name: str) -> Pastry:
        """Make order."""
        i = -1
        while i < len(self.recipes):
            if name not in self.recipes:
                return "No such recipe in the list"
            else:
                self.budget += len(name) * 2
                # Baker.money+= len(name) * 2
                return self.recipes, 
            i+=1


    def get_recipes(self) -> dict:
        """Get recipes."""
        return self.recipes

    def get_pastries(self) -> list:
        """Get pastries."""
        return self.pastries

    def get_bakers(self) -> list:
        """Get baker."""
        return self.bakers
        # Baker.__repr__(self)

    def __str__(self):
        """Represent object in string format."""
        return "Bakery {}: {} baker(s)".format(self.name, len(self.bakers))