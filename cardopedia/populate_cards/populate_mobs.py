from cardopedia.enums.card_name import CardName
from cardopedia.cardpedia import Cardpedia
from cardopedia.enums.category_name import CategoryName
from cardopedia.enums.group_name import GroupName


def populate_mobs(cardpedia: Cardpedia):
    bear = cardpedia.category(CategoryName.mobs).card(CardName.bear)
    bear.group(
        GroupName.drops,
        [CardName.poop, CardName.bone, CardName.raw_meat])

    chicken = cardpedia.category(CategoryName.mobs).card(CardName.chicken)
    chicken.group(
        GroupName.recipe_ingredients,
        [CardName.chicken, CardName.egg])
    chicken.group(
        GroupName.produces,
        [CardName.egg])
    chicken.group(
        GroupName.drops,
        [CardName.egg, CardName.poop, CardName.raw_meat, CardName.bone])
    chicken.group(
        GroupName.misc,
        [CardName.animal_pen])

    cow = cardpedia.category(CategoryName.mobs).card(CardName.cow)
    cow.group(
        GroupName.produces,
        [CardName.milk])
    cow.group(
        GroupName.drops,
        [CardName.milk, CardName.raw_meat, CardName.poop, CardName.bone])
    cow.group(
        GroupName.misc,
        [CardName.animal_pen])

    crab = cardpedia.category(CategoryName.mobs).card(CardName.crab)
    crab.group(
        GroupName.drops,
        [CardName.raw_crab_meat, CardName.momma_crab])

    demon = cardpedia.category(CategoryName.mobs).card(CardName.demon)
    demon.group(
        GroupName.recipe_ingredients,
        [CardName.temple, CardName.golden_goblet])
    demon.group(
        GroupName.drops,
        [CardName.the_island])

    demon_lord = cardpedia.category(CategoryName.mobs).card(CardName.demon_lord)
    demon_lord.group(
        GroupName.recipe_ingredients,
        [CardName.cathedral, CardName.island_relic])
    demon_lord.group(
        GroupName.drops,
        [CardName.the_island])

    giant_rat = cardpedia.category(CategoryName.mobs).card(CardName.giant_rat)
    giant_rat.group(
        GroupName.drops,
        [CardName.poop, CardName.bone, CardName.raw_meat])

    goblin = cardpedia.category(CategoryName.mobs).card(CardName.goblin)
    goblin.group(
        GroupName.drops,
        [CardName.coin, CardName.raw_meat, CardName.spear, CardName.map, CardName.key, CardName.poop])

    kraken = cardpedia.category(CategoryName.mobs).card(CardName.kraken)
    kraken.group(
        GroupName.drops,
        [CardName.raw_meat])

    momma_crab = cardpedia.category(CategoryName.mobs).card(CardName.momma_crab)
    momma_crab.group(
        GroupName.drops,
        [CardName.raw_crab_meat, CardName.poop])

    monkey = cardpedia.category(CategoryName.mobs).card(CardName.monkey)
    monkey.group(
        GroupName.drops,
        [CardName.raw_meat, CardName.banana, CardName.poop])
    monkey.group(
        GroupName.misc,
        [CardName.animal_pen])

    parrot = cardpedia.category(CategoryName.mobs).card(CardName.parrot)
    parrot.group(
        GroupName.produces,
        [CardName.berry])
    parrot.group(
        GroupName.drops,
        [CardName.raw_meat, CardName.poop])
    parrot.group(
        GroupName.misc,
        [CardName.animal_pen])

    pirate = cardpedia.category(CategoryName.mobs).card(CardName.pirate)
    pirate.group(
        GroupName.drops,
        [CardName.coin, CardName.map, CardName.poop])

    rabbit = cardpedia.category(CategoryName.mobs).card(CardName.rabbit)
    rabbit.group(
        GroupName.produces,
        [CardName.poop])
    rabbit.group(
        GroupName.drops,
        [CardName.raw_meat, CardName.carrot, CardName.bone, CardName.poop])
    rabbit.group(
        GroupName.misc,
        [CardName.animal_pen])

    rat = cardpedia.category(CategoryName.mobs).card(CardName.rat)
    rat.group(
        GroupName.drops,
        [CardName.coin, CardName.poop, CardName.bone, CardName.raw_meat])

    seagull = cardpedia.category(CategoryName.mobs).card(CardName.seagull)
    seagull.group(
        GroupName.drops,
        [CardName.raw_meat])

    skeleton = cardpedia.category(CategoryName.mobs).card(CardName.skeleton)
    skeleton.group(
        GroupName.drops,
        [CardName.coin, CardName.bone, CardName.spear, CardName.key])

    slime = cardpedia.category(CategoryName.mobs).card(CardName.slime)
    slime.group(
        GroupName.drops,
        [CardName.small_slime, CardName.small_slime, CardName.small_slime])

    small_slime = cardpedia.category(CategoryName.mobs).card(CardName.small_slime)
    small_slime.group(
        GroupName.drops,
        [CardName.onion, CardName.egg, CardName.coin, CardName.key])

    snake = cardpedia.category(CategoryName.mobs).card(CardName.snake)
    snake.group(
        GroupName.drops,
        [CardName.raw_meat])

    tentacle = cardpedia.category(CategoryName.mobs).card(CardName.tentacle)
    tentacle.group(
        GroupName.recipe_ingredients,
        [CardName.sacred_chest, CardName.sacred_key])
    tentacle.group(
        GroupName.drops,
        [CardName.raw_meat, CardName.kraken])

    tiger = cardpedia.category(CategoryName.mobs).card(CardName.tiger)
    tiger.group(
        GroupName.drops,
        [CardName.raw_meat, CardName.poop])

    wolf = cardpedia.category(CategoryName.mobs).card(CardName.wolf)
    wolf.group(
        GroupName.drops,
        [CardName.poop, CardName.bone, CardName.raw_meat])
