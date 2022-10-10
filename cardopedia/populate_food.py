from cardopedia.card_name import CardName
from cardopedia.cardpedia import Cardpedia
from cardopedia.category_name import CategoryName
from cardopedia.group_name import GroupName
from cardopedia.populate import Populate

populate = Populate()


def populate_food(cardpedia: Cardpedia):
    apple = cardpedia.category(CategoryName.food).card(CardName.apple)
    apple.group(
        GroupName.drops,
        [CardName.goop])

    banana = cardpedia.category(CategoryName.food).card(CardName.banana)
    banana.group(
        GroupName.drops,
        [CardName.goop])

    berry = cardpedia.category(CategoryName.food).card(CardName.berry)
    berry.group(
        GroupName.drops,
        [CardName.goop])

    bottle_of_rum = cardpedia.category(CategoryName.food).card(CardName.bottle_of_rum)
    bottle_of_rum.group(
        GroupName.recipe_ingredients,
        sorted([CardName.distillery, CardName.bottle_of_water, CardName.cane_sugar]))

    cane_sugar = cardpedia.category(CategoryName.food).card(CardName.cane_sugar)
    cane_sugar.group(
        GroupName.drops,
        [CardName.goop])

    carrot = cardpedia.category(CategoryName.food).card(CardName.carrot)
    carrot.group(
        GroupName.recipe_plus_1_card,
        populate.growers)
    carrot.group(
        GroupName.recipe_ingredients,
        [CardName.carrot])
    carrot.group(
        GroupName.drops,
        [CardName.goop])

    ceviche = cardpedia.category(CategoryName.food).card(CardName.ceviche)
    ceviche.group(
        GroupName.recipe_ingredients,
        [CardName.lime, CardName.raw_fish])
    ceviche.group(
        GroupName.drops,
        [CardName.goop])

    chili_pepper = cardpedia.category(CategoryName.food).card(CardName.chili_pepper)
    chili_pepper.group(
        GroupName.recipe_plus_1_card,
        populate.growers)
    chili_pepper.group(
        GroupName.recipe_ingredients,
        [CardName.chili_pepper])
    chili_pepper.group(
        GroupName.drops,
        [CardName.goop])

    cooked_crab = cardpedia.category(CategoryName.food).card(CardName.cooked_crab)
    cooked_crab.group(
        GroupName.recipe_plus_1_card,
        populate.cookers)
    cooked_crab.group(
        GroupName.recipe_ingredients,
        [CardName.raw_crab_meat])
    cooked_crab.group(
        GroupName.drops,
        [CardName.goop])

    cooked_meat = cardpedia.category(CategoryName.food).card(CardName.cooked_meat)
    cooked_meat.group(
        GroupName.recipe_plus_1_card,
        populate.cookers)
    cooked_meat.group(
        GroupName.recipe_ingredients,
        [CardName.raw_meat])
    cooked_meat.group(
        GroupName.drops,
        [CardName.goop])

    egg = cardpedia.category(CategoryName.food).card(CardName.egg)
    egg.group(
        GroupName.drops,
        [CardName.goop])

    frittata = cardpedia.category(CategoryName.food).card(CardName.frittata)
    frittata.group(
        GroupName.recipe_plus_1_card,
        populate.cookers)
    frittata.group(
        GroupName.recipe_ingredients,
        [CardName.egg, CardName.potato])
    frittata.group(
        GroupName.drops,
        [CardName.goop])

    fruit_salad = cardpedia.category(CategoryName.food).card(CardName.fruit_salad)
    fruit_salad.group(
        GroupName.recipe_ingredients,
        [CardName.apple, CardName.berry])
    fruit_salad.group(
        GroupName.drops,
        [CardName.goop])

    grilled_fish = cardpedia.category(CategoryName.food).card(CardName.grilled_fish)
    grilled_fish.group(
        GroupName.recipe_plus_1_card,
        populate.cookers)
    grilled_fish.group(
        GroupName.recipe_ingredients,
        [CardName.raw_fish])
    grilled_fish.group(
        GroupName.drops,
        [CardName.goop])

    lime = cardpedia.category(CategoryName.food).card(CardName.lime)
    lime.group(
        GroupName.recipe_plus_1_card,
        populate.growers)
    lime.group(
        GroupName.recipe_ingredients,
        [CardName.lime])
    lime.group(
        GroupName.drops,
        [CardName.goop])

    milk = cardpedia.category(CategoryName.food).card(CardName.milk)
    milk.group(
        GroupName.drops,
        [CardName.goop])

    milkshake = cardpedia.category(CategoryName.food).card(CardName.milkshake)
    milkshake.group(
        GroupName.recipe_ingredients,
        sorted([CardName.milk, CardName.berry]))
    milkshake.group(
        GroupName.drops,
        [CardName.goop])

    mushroom = cardpedia.category(CategoryName.food).card(CardName.mushroom)
    mushroom.group(
        GroupName.recipe_plus_1_card,
        populate.growers)
    mushroom.group(
        GroupName.recipe_ingredients,
        [CardName.mushroom])
    mushroom.group(
        GroupName.drops,
        [CardName.goop])

    omelette = cardpedia.category(CategoryName.food).card(CardName.omelette)
    omelette.group(
        GroupName.recipe_plus_1_card,
        populate.cookers)
    omelette.group(
        GroupName.recipe_ingredients,
        [CardName.egg, CardName.egg])
    omelette.group(
        GroupName.drops,
        [CardName.goop])

    onion = cardpedia.category(CategoryName.food).card(CardName.onion)
    onion.group(
        GroupName.recipe_plus_1_card,
        populate.growers)
    onion.group(
        GroupName.recipe_ingredients,
        [CardName.onion])
    onion.group(
        GroupName.drops,
        [CardName.goop])

    potato = cardpedia.category(CategoryName.food).card(CardName.potato)
    potato.group(
        GroupName.recipe_plus_1_card,
        populate.growers)
    potato.group(
        GroupName.recipe_ingredients,
        [CardName.potato])
    potato.group(
        GroupName.drops,
        [CardName.goop])

    raw_crab_meat = cardpedia.category(CategoryName.food).card(CardName.raw_crab_meat)
    raw_crab_meat.group(
        GroupName.drops,
        [CardName.goop])

    raw_fish = cardpedia.category(CategoryName.food).card(CardName.raw_fish)
    raw_fish.group(
        GroupName.drops,
        [CardName.goop])

    raw_meat = cardpedia.category(CategoryName.food).card(CardName.raw_meat)
    raw_meat.group(
        GroupName.drops,
        [CardName.goop])

    seafood_stew = cardpedia.category(CategoryName.food).card(CardName.seafood_stew)
    seafood_stew.group(
        GroupName.recipe_plus_1_card,
        populate.cookers)
    seafood_stew.group(
        GroupName.recipe_ingredients,
        sorted([CardName.raw_crab_meat, CardName.raw_fish, CardName.chili_pepper]))
    seafood_stew.group(
        GroupName.drops,
        [CardName.goop])

    seaweed = cardpedia.category(CategoryName.food).card(CardName.seaweed)
    seaweed.group(
        GroupName.recipe_plus_1_card,
        populate.growers)
    seaweed.group(
        GroupName.recipe_ingredients,
        [CardName.seaweed])
    seaweed.group(
        GroupName.drops,
        [CardName.goop])

    stew = cardpedia.category(CategoryName.food).card(CardName.stew)
    stew.group(
        GroupName.recipe_plus_1_card,
        populate.cookers)
    stew.group(
        GroupName.recipe_ingredients,
        sorted([CardName.raw_meat, CardName.carrot, CardName.onion, CardName.potato]))
    stew.group(
        GroupName.drops,
        [CardName.goop])

    sushi = cardpedia.category(CategoryName.food).card(CardName.sushi)
    sushi.group(
        GroupName.recipe_ingredients,
        [CardName.raw_fish, CardName.seaweed])
    sushi.group(
        GroupName.drops,
        [CardName.goop])

    tamago_sushi = cardpedia.category(CategoryName.food).card(CardName.tamago_sushi)
    tamago_sushi.group(
        GroupName.recipe_ingredients,
        [CardName.omelette, CardName.seaweed])
    tamago_sushi.group(
        GroupName.drops,
        [CardName.goop])
