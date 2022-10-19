from cardopedia.enums.card_name import CardName
from cardopedia.cardpedia import Cardpedia
from cardopedia.enums.category_name import CategoryName
from cardopedia.enums.group_name import GroupName


def populate_fish(cardpedia: Cardpedia):
    cod = cardpedia.category(CategoryName.fish).card(CardName.cod)
    cod.group(
        GroupName.drops,
        [CardName.raw_fish])

    eel = cardpedia.category(CategoryName.fish).card(CardName.eel)
    eel.group(
        GroupName.recipe_ingredients,
        [CardName.fish_trap, CardName.banana])
    eel.group(
        GroupName.drops,
        [CardName.raw_fish, CardName.raw_fish])

    mackerel = cardpedia.category(CategoryName.fish).card(CardName.mackerel)
    # all food that isn't banana, lime, or raw_meat
    mackerel.group(
        GroupName.recipe_plus_1_card,
        [CardName.apple, CardName.berry, CardName.bottle_of_rum, CardName.cane_sugar, CardName.carrot, CardName.ceviche,
         CardName.chili_pepper, CardName.cooked_crab, CardName.cooked_meat, CardName.egg, CardName.frittata,
         CardName.fruit_salad, CardName.grilled_fish, CardName.milk, CardName.milkshake, CardName.mushroom,
         CardName.omelette, CardName.onion, CardName.potato, CardName.raw_crab_meat, CardName.raw_fish,
         CardName.seafood_stew, CardName.seaweed, CardName.stew, CardName.sushi, CardName.tamago_sushi])
    mackerel.group(
        GroupName.recipe_ingredients,
        [CardName.fish_trap])
    mackerel.group(
        GroupName.drops,
        [CardName.raw_fish, CardName.raw_fish])

    shark = cardpedia.category(CategoryName.fish).card(CardName.shark)
    shark.group(
        GroupName.recipe_ingredients,
        [CardName.fish_trap, CardName.raw_meat])
    shark.group(
        GroupName.drops,
        [CardName.raw_fish, CardName.raw_fish, CardName.raw_fish])

    tuna = cardpedia.category(CategoryName.fish).card(CardName.tuna)
    tuna.group(
        GroupName.recipe_ingredients,
        [CardName.fish_trap, CardName.lime])
    tuna.group(
        GroupName.drops,
        [CardName.raw_fish, CardName.raw_fish, CardName.raw_fish])
