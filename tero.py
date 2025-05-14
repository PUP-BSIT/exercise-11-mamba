import random

def get_emoji_menu():
    return """
🍕 Pizza
🍔 Burger
🍣 Sushi
🍜 Ramen
🌮 Taco
🍦 Ice Cream
"""

def get_random_food():
    food_items = get_emoji_menu().strip().split("\n")
    return random.choice(food_items)

random_food = get_random_food()