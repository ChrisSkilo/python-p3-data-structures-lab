spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    pass
    names = [food['name'] for food in spicy_foods]
    return names
#print(get_names(spicy_foods))



def get_spiciest_foods(spicy_foods):
    pass
    spiciest = [dict(foods) for foods in spicy_foods if foods["heat_level"]>5]
    return spiciest
#print(get_spiciest_foods(spicy_foods))




def print_spicy_foods(spicy_foods):
    pass
    for food in spicy_foods:
          print( food["name"] + " " + "("+ (food["cuisine"])+ ")" + " | " + "Heat Level: "+ "🌶"*(food["heat_level"]))
#print_spicy_foods(spicy_foods)



def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    pass
    filtered_foods= [food for food in spicy_foods if food["cuisine"]== cuisine]
    for food in filtered_foods:
        return food
#print(get_spicy_food_by_cuisine(spicy_foods, "American"))


def print_spiciest_foods(spicy_foods):
    pass
    filter_food= [food for food in spicy_foods if food["heat_level"]>5]
    for food in filter_food:
        print(food["name"] +" "+ "("+ food["cuisine"] + ")" + " | "+ "Heat Level:"+ "🌶"* food["heat_level"] )
#print(print_spiciest_foods(spicy_foods))


def get_average_heat_level(spicy_foods):
    pass
    total_heat = sum(foods["heat_level"] for foods in spicy_foods)
    average = total_heat / len(spicy_foods)
    return average
print(get_average_heat_level(spicy_foods))


def create_spicy_food(spicy_foods, spicy_food):
    pass
    spicy_foods.append(spicy_food)
    return spicy_foods