from cardopedia.enums.card_name import CardName
from cardopedia.cardpedia import Cardpedia
from cardopedia.enums.category_name import CategoryName
from cardopedia.enums.group_name import GroupName
from cardopedia.populate_cards.populate import Populate

populate = Populate()


def populate_resources(cardpedia: Cardpedia):
    bone = cardpedia.category(CategoryName.resources).card(CardName.bone)

    bottle_of_water = cardpedia.category(CategoryName.resources).card(CardName.bottle_of_water)
    bottle_of_water.group(
        GroupName.recipe_ingredients,
        [CardName.empty_bottle, CardName.spring])

    brick = cardpedia.category(CategoryName.resources).card(CardName.brick)
    brick.group(
        GroupName.recipe_plus_1_card,
        populate.adults)
    brick.group(
        GroupName.recipe_ingredients,
        [CardName.stone, CardName.stone, CardName.stone])
    brick.group(
        GroupName.alt_recipe,
        [CardName.brickyard, CardName.stone, CardName.stone])
    brick.group(
        GroupName.misc,
        [CardName.plank])

    charcoal = cardpedia.category(CategoryName.resources).card(CardName.charcoal)
    charcoal.group(
        GroupName.recipe_plus_1_card,
        populate.cookers)
    charcoal.group(
        GroupName.recipe_ingredients,
        [CardName.wood])
    charcoal.group(
        GroupName.misc,
        populate.adults)

    coin = cardpedia.category(CategoryName.resources).card(CardName.coin)
    coin.group(
        GroupName.recipe_ingredients,
        [CardName.smelter, CardName.gold_bar, CardName.wood])
    coin.group(
        GroupName.misc,
        [CardName.pirate_boat])

    corpse = cardpedia.category(CategoryName.resources).card(CardName.corpse)

    cotton = cardpedia.category(CategoryName.resources).card(CardName.cotton)

    empty_bottle = cardpedia.category(CategoryName.resources).card(CardName.empty_bottle)
    empty_bottle.group(
        GroupName.recipe_plus_1_card,
        populate.cookers)
    empty_bottle.group(
        GroupName.recipe_ingredients,
        [CardName.glass, CardName.glass])

    fabric = cardpedia.category(CategoryName.resources).card(CardName.fabric)
    fabric.group(
        GroupName.recipe_plus_1_card,
        populate.adults)
    fabric.group(
        GroupName.recipe_ingredients,
        [CardName.cotton, CardName.cotton, CardName.cotton, CardName.cotton])

    fishing_rod = cardpedia.category(CategoryName.resources).card(CardName.fishing_rod)
    fishing_rod.group(
        GroupName.recipe_ingredients,
        [CardName.stick, CardName.rope])

    flint = cardpedia.category(CategoryName.resources).card(CardName.flint)
    flint.group(
        GroupName.misc,
        [CardName.stick])

    glass = cardpedia.category(CategoryName.resources).card(CardName.glass)
    glass.group(
        GroupName.recipe_ingredients,
        [CardName.smelter, CardName.sand, CardName.wood])

    gold_bar = cardpedia.category(CategoryName.resources).card(CardName.gold_bar)
    gold_bar.group(
        GroupName.recipe_ingredients,
        [CardName.smelter, CardName.gold_ore, CardName.wood])

    gold_ore = cardpedia.category(CategoryName.resources).card(CardName.gold_ore)

    golden_goblet = cardpedia.category(CategoryName.resources).card(CardName.golden_goblet)

    goop = cardpedia.category(CategoryName.resources).card(CardName.goop)

    iron_bar = cardpedia.category(CategoryName.resources).card(CardName.iron_bar)
    iron_bar.group(
        GroupName.recipe_ingredients,
        [CardName.smelter, CardName.iron_ore, CardName.wood])

    iron_ore = cardpedia.category(CategoryName.resources).card(CardName.iron_ore)

    island_relic = cardpedia.category(CategoryName.resources).card(CardName.island_relic)
    island_relic.group(
        GroupName.recipe_ingredients,
        [CardName.sacred_chest, CardName.sacred_key])

    key = cardpedia.category(CategoryName.resources).card(CardName.key)
    key.group(
        GroupName.misc,
        [CardName.treasure_chest])

    map = cardpedia.category(CategoryName.resources).card(CardName.map)

    old_tome = cardpedia.category(CategoryName.resources).card(CardName.old_tome)
    old_tome.group(
        GroupName.drops,
        populate.ideas)

    plank = cardpedia.category(CategoryName.resources).card(CardName.plank)
    plank.group(
        GroupName.recipe_plus_1_card,
        populate.adults)
    plank.group(
        GroupName.recipe_ingredients,
        [CardName.wood, CardName.wood, CardName.wood])
    plank.group(
        GroupName.alt_recipe,
        [CardName.sawmill, CardName.wood, CardName.wood])
    plank.group(
        GroupName.misc,
        [CardName.brick])

    poop = cardpedia.category(CategoryName.resources).card(CardName.poop)
    poop.group(
        GroupName.misc,
        [CardName.greenhouse, CardName.farm, CardName.garden, CardName.soil])

    rope = cardpedia.category(CategoryName.resources).card(CardName.rope)
    rope.group(
        GroupName.recipe_plus_1_card,
        populate.adults)
    rope.group(
        GroupName.recipe_ingredients,
        [CardName.cotton, CardName.cotton])

    sacred_chest = cardpedia.category(CategoryName.resources).card(CardName.sacred_chest)

    sacred_key = cardpedia.category(CategoryName.resources).card(CardName.sacred_key)
    sacred_key.group(
        GroupName.recipe_ingredients,
        [CardName.smelter,
         CardName.gold_bar, CardName.gold_bar, CardName.gold_bar,
         CardName.glass, CardName.glass, CardName.glass])

    sail = cardpedia.category(CategoryName.resources).card(CardName.sail)
    sail.group(
        GroupName.recipe_plus_1_card,
        populate.adults)
    sail.group(
        GroupName.recipe_ingredients,
        [CardName.fabric, CardName.rope])

    sand = cardpedia.category(CategoryName.resources).card(CardName.sand)

    sandstone = cardpedia.category(CategoryName.resources).card(CardName.sandstone)
    sandstone.group(
        GroupName.recipe_plus_1_card,
        populate.adults)
    sandstone.group(
        GroupName.recipe_ingredients,
        [CardName.sand, CardName.sand])

    shell = cardpedia.category(CategoryName.resources).card(CardName.shell)

    spear = cardpedia.category(CategoryName.resources).card(CardName.spear)
    spear.group(
        GroupName.recipe_ingredients,
        [CardName.stick, CardName.stick, CardName.wood])

    stick = cardpedia.category(CategoryName.resources).card(CardName.stick)
    stick.group(
        GroupName.misc,
        [CardName.flint])

    stone = cardpedia.category(CategoryName.resources).card(CardName.stone)
    stone.group(
        GroupName.misc,
        [CardName.wood])

    sword = cardpedia.category(CategoryName.resources).card(CardName.sword)
    sword.group(
        GroupName.recipe_ingredients,
        [CardName.stick, CardName.stick, CardName.iron_bar])

    treasure_map = cardpedia.category(CategoryName.resources).card(CardName.treasure_map)
    treasure_map.group(
        GroupName.drops,
        [CardName.sacred_chest])

    wood = cardpedia.category(CategoryName.resources).card(CardName.wood)
    wood.group(
        GroupName.drops,
        [CardName.stick])
    wood.group(
        GroupName.misc,
        [CardName.stone])
