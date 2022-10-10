from cardopedia.card_name import CardName
from cardopedia.cardpedia import Cardpedia
from cardopedia.category_name import CategoryName
from cardopedia.group_name import GroupName
from cardopedia.populate import Populate

populate = Populate()


def populate_structures(cardpedia: Cardpedia):
    animal_pen = cardpedia.category(CategoryName.structures).card(CardName.animal_pen)
    animal_pen.group(
        GroupName.recipe_plus_1_card,
        populate.adults)
    animal_pen.group(
        GroupName.recipe_ingredients,
        [CardName.plank, CardName.plank, CardName.wood, CardName.wood, CardName.iron_bar])
    animal_pen.group(
        GroupName.stores,
        [CardName.chicken, CardName.cow, CardName.monkey, CardName.parrot, CardName.rabbit])
    animal_pen.group(
        GroupName.misc,
        [CardName.aquarium])

    apple_tree = cardpedia.category(CategoryName.structures).card(CardName.apple_tree)
    apple_tree.group(
        GroupName.recipe_plus_1_card,
        populate.growers)
    apple_tree.group(
        GroupName.recipe_ingredients,
        [CardName.apple])
    apple_tree.group(
        GroupName.drops,
        [CardName.apple, CardName.stick, CardName.wood])

    aquarium = cardpedia.category(CategoryName.structures).card(CardName.aquarium)
    aquarium.group(
        GroupName.recipe_plus_1_card,
        populate.adults)
    aquarium.group(
        GroupName.recipe_ingredients,
        [CardName.glass, CardName.glass, CardName.iron_bar])
    aquarium.group(
        GroupName.stores,
        [CardName.cod, CardName.mackerel, CardName.tuna])
    aquarium.group(
        GroupName.misc,
        [CardName.animal_pen])

    banana_tree = cardpedia.category(CategoryName.structures).card(CardName.banana_tree)
    banana_tree.group(
        GroupName.recipe_plus_1_card,
        populate.growers)
    banana_tree.group(
        GroupName.recipe_ingredients,
        [CardName.banana])
    banana_tree.group(
        GroupName.drops,
        [CardName.banana])

    berry_bush = cardpedia.category(CategoryName.structures).card(CardName.berry_bush)
    berry_bush.group(
        GroupName.recipe_plus_1_card,
        populate.growers)
    berry_bush.group(
        GroupName.recipe_ingredients,
        [CardName.berry])
    berry_bush.group(
        GroupName.drops,
        [CardName.berry, CardName.rabbit])

    brickyard = cardpedia.category(CategoryName.structures).card(CardName.brickyard)
    brickyard.group(
        GroupName.recipe_plus_1_card,
        populate.adults)
    brickyard.group(
        GroupName.recipe_ingredients,
        [CardName.brick, CardName.iron_bar, CardName.wood])
    brickyard.group(
        GroupName.misc,
        [CardName.sawmill])

    campfire = cardpedia.category(CategoryName.structures).card(CardName.campfire)
    campfire.group(
        GroupName.recipe_ingredients,
        [CardName.flint, CardName.stick])
    campfire.group(
        GroupName.misc,
        [CardName.stove])

    cathedral = cardpedia.category(CategoryName.structures).card(CardName.cathedral)
    cathedral.group(
        GroupName.recipe_plus_5_cards,
        populate.adults)
    cathedral.group(
        GroupName.recipe_ingredients,
        [CardName.gold_bar, CardName.gold_bar, CardName.gold_bar, CardName.gold_bar, CardName.gold_bar,
         CardName.glass, CardName.glass, CardName.glass, CardName.glass, CardName.glass,
         CardName.brick, CardName.brick, CardName.brick, CardName.brick, CardName.brick,
         CardName.plank, CardName.plank, CardName.plank, CardName.plank, CardName.plank])

    coin_chest = cardpedia.category(CategoryName.structures).card(CardName.coin_chest)
    coin_chest.group(
        GroupName.recipe_ingredients,
        [CardName.coin, CardName.wood, CardName.wood])
    coin_chest.group(
        GroupName.stores,
        [CardName.coin])
    coin_chest.group(
        GroupName.misc,
        [CardName.shell_chest])

    composter = cardpedia.category(CategoryName.structures).card(CardName.composter)
    composter.group(
        GroupName.recipe_plus_1_card,
        populate.adults)
    composter.group(
        GroupName.recipe_ingredients,
        [CardName.poop, CardName.poop, CardName.plank, CardName.brick])

    cotton_plant = cardpedia.category(CategoryName.structures).card(CardName.cotton_plant)
    cotton_plant.group(
        GroupName.recipe_plus_1_card,
        populate.growers)
    cotton_plant.group(
        GroupName.recipe_ingredients,
        [CardName.cotton])
    cotton_plant.group(
        GroupName.drops,
        [CardName.cotton])

    distillery = cardpedia.category(CategoryName.structures).card(CardName.distillery)
    distillery.group(
        GroupName.recipe_plus_1_card,
        populate.adults)
    distillery.group(
        GroupName.recipe_ingredients,
        [CardName.stove, CardName.iron_bar, CardName.plank])

    driftwood = cardpedia.category(CategoryName.structures).card(CardName.driftwood)
    driftwood.group(
        GroupName.drops,
        [CardName.wood, CardName.stick])

    farm = cardpedia.category(CategoryName.structures).card(CardName.farm)
    farm.group(
        GroupName.recipe_plus_1_card,
        populate.adults)
    farm.group(
        GroupName.recipe_ingredients,
        [CardName.soil, CardName.brick, CardName.brick, CardName.plank, CardName.plank])
    farm.group(
        GroupName.misc,
        [CardName.greenhouse, CardName.garden, CardName.soil, CardName.poop])

    fish_trap = cardpedia.category(CategoryName.structures).card(CardName.fish_trap)
    fish_trap.group(
        GroupName.recipe_ingredients,
        [CardName.fishing_spot, CardName.stone, CardName.rope])

    fishing_spot = cardpedia.category(CategoryName.structures).card(CardName.fishing_spot)
    fishing_spot.group(
        GroupName.drops,
        [CardName.cod, CardName.mackerel])

    frigate = cardpedia.category(CategoryName.structures).card(CardName.frigate)
    frigate.group(
        GroupName.recipe_plus_2_cards,
        populate.adults)
    frigate.group(
        GroupName.recipe_ingredients,
        [CardName.plank, CardName.plank, CardName.plank, CardName.plank, CardName.plank,
         CardName.plank, CardName.plank, CardName.plank, CardName.plank, CardName.plank,
         CardName.sail, CardName.sail, CardName.sail])
    frigate.group(
        GroupName.misc,
        [CardName.sloop, CardName.rowboat])

    garden = cardpedia.category(CategoryName.structures).card(CardName.garden)
    garden.group(
        GroupName.recipe_plus_1_card,
        populate.adults)
    garden.group(
        GroupName.recipe_ingredients,
        [CardName.soil, CardName.wood, CardName.wood, CardName.stone, CardName.stone])
    garden.group(
        GroupName.misc,
        [CardName.greenhouse, CardName.farm, CardName.soil, CardName.poop])

    gold_deposit = cardpedia.category(CategoryName.structures).card(CardName.gold_deposit)
    gold_deposit.group(
        GroupName.drops,
        [CardName.gold_ore, CardName.stone, CardName.coin])
    gold_deposit.group(
        GroupName.misc,
        [CardName.iron_deposit])

    gold_mine = cardpedia.category(CategoryName.structures).card(CardName.gold_mine)
    gold_mine.group(
        GroupName.recipe_plus_1_card,
        populate.adults)
    gold_mine.group(
        GroupName.recipe_ingredients,
        [CardName.flint, CardName.gold_ore, CardName.wood, CardName.stone])
    gold_mine.group(
        GroupName.drops,
        [CardName.gold_ore, CardName.stone, CardName.coin])
    gold_mine.group(
        GroupName.misc,
        [CardName.iron_mine, CardName.lumber_camp, CardName.quarry, CardName.sand_quarry])

    greenhouse = cardpedia.category(CategoryName.structures).card(CardName.greenhouse)
    greenhouse.group(
        GroupName.recipe_plus_1_card,
        populate.adults)
    greenhouse.group(
        GroupName.recipe_ingredients,
        [CardName.iron_bar, CardName.iron_bar, CardName.glass, CardName.glass, CardName.soil])
    greenhouse.group(
        GroupName.misc,
        [CardName.farm, CardName.garden, CardName.soil, CardName.poop])

    house = cardpedia.category(CategoryName.structures).card(CardName.house)
    house.group(
        GroupName.recipe_plus_1_card,
        populate.adults)
    house.group(
        GroupName.recipe_ingredients,
        [CardName.stone, CardName.wood, CardName.wood])

    iron_deposit = cardpedia.category(CategoryName.structures).card(CardName.iron_deposit)
    iron_deposit.group(
        GroupName.drops,
        [CardName.iron_ore, CardName.stone, CardName.coin])
    iron_deposit.group(
        GroupName.misc,
        [CardName.gold_deposit])

    iron_mine = cardpedia.category(CategoryName.structures).card(CardName.iron_mine)
    iron_mine.group(
        GroupName.recipe_plus_1_card,
        populate.adults)
    iron_mine.group(
        GroupName.recipe_ingredients,
        [CardName.flint, CardName.flint, CardName.wood, CardName.stone])
    iron_mine.group(
        GroupName.drops,
        [CardName.iron_ore, CardName.stone, CardName.coin])
    iron_mine.group(
        GroupName.misc,
        [CardName.gold_mine, CardName.lumber_camp, CardName.quarry, CardName.sand_quarry])

    lumber_camp = cardpedia.category(CategoryName.structures).card(CardName.lumber_camp)
    lumber_camp.group(
        GroupName.recipe_plus_1_card,
        populate.adults)
    lumber_camp.group(
        GroupName.recipe_ingredients,
        [CardName.wood, CardName.wood, CardName.wood, CardName.stone])
    lumber_camp.group(
        GroupName.drops,
        [CardName.wood])
    lumber_camp.group(
        GroupName.misc,
        [CardName.gold_mine, CardName.iron_mine, CardName.quarry, CardName.sand_quarry])

    market = cardpedia.category(CategoryName.structures).card(CardName.market)
    market.group(
        GroupName.recipe_plus_1_card,
        populate.adults)
    market.group(
        GroupName.recipe_ingredients,
        [CardName.coin, CardName.coin, CardName.coin, CardName.plank, CardName.brick])
    market.group(
        GroupName.alt_recipe,
        [CardName.shell, CardName.shell, CardName.shell, CardName.plank, CardName.brick])

    mess_hall = cardpedia.category(CategoryName.structures).card(CardName.mess_hall)
    mess_hall.group(
        GroupName.recipe_ingredients,
        [CardName.plank, CardName.iron_bar, CardName.campfire])

    pirate_boat = cardpedia.category(CategoryName.structures).card(CardName.pirate_boat)
    pirate_boat.group(
        GroupName.produces,
        [CardName.pirate, CardName.pirate, CardName.pirate])
    pirate_boat.group(
        GroupName.misc,
        [CardName.coin, CardName.coin, CardName.coin, CardName.coin, CardName.coin,
         CardName.coin, CardName.coin, CardName.coin, CardName.coin, CardName.coin])

    quarry = cardpedia.category(CategoryName.structures).card(CardName.quarry)
    quarry.group(
        GroupName.recipe_plus_1_card,
        populate.adults)
    quarry.group(
        GroupName.recipe_ingredients,
        [CardName.stone, CardName.stone, CardName.stone, CardName.wood])
    quarry.group(
        GroupName.drops,
        [CardName.stone, CardName.flint])
    quarry.group(
        GroupName.misc,
        [CardName.gold_mine, CardName.iron_mine, CardName.lumber_camp, CardName.sand_quarry])

    rock = cardpedia.category(CategoryName.structures).card(CardName.rock)
    rock.group(
        GroupName.drops,
        [CardName.stone, CardName.flint, CardName.coin])

    rowboat = cardpedia.category(CategoryName.structures).card(CardName.rowboat)
    rowboat.group(
        GroupName.recipe_ingredients,
        [CardName.iron_bar, CardName.plank])
    rowboat.group(
        GroupName.misc,
        [CardName.frigate, CardName.sloop])

    sand_quarry = cardpedia.category(CategoryName.structures).card(CardName.sand_quarry)
    sand_quarry.group(
        GroupName.recipe_plus_1_card,
        populate.adults)
    sand_quarry.group(
        GroupName.recipe_ingredients,
        [CardName.sand, CardName.flint, CardName.wood])
    sand_quarry.group(
        GroupName.drops,
        [CardName.sand])
    sand_quarry.group(
        GroupName.misc,
        [CardName.gold_mine, CardName.iron_mine, CardName.lumber_camp, CardName.quarry])

    sawmill = cardpedia.category(CategoryName.structures).card(CardName.sawmill)
    sawmill.group(
        GroupName.recipe_plus_1_card,
        populate.adults)
    sawmill.group(
        GroupName.recipe_ingredients,
        [CardName.plank, CardName.wood, CardName.stone, CardName.iron_bar])
    sawmill.group(
        GroupName.misc,
        [CardName.brickyard])

    shed = cardpedia.category(CategoryName.structures).card(CardName.shed)
    shed.group(
        GroupName.recipe_plus_1_card,
        populate.adults)
    shed.group(
        GroupName.recipe_ingredients,
        [CardName.stone, CardName.wood, CardName.stick])
    shed.group(
        GroupName.misc,
        [CardName.warehouse])

    shell_chest = cardpedia.category(CategoryName.structures).card(CardName.shell_chest)
    shell_chest.group(
        GroupName.recipe_ingredients,
        [CardName.shell, CardName.wood, CardName.wood])
    shell_chest.group(
        GroupName.stores,
        [CardName.shell])
    shell_chest.group(
        GroupName.misc,
        [CardName.coin_chest])

    sloop = cardpedia.category(CategoryName.structures).card(CardName.sloop)
    sloop.group(
        GroupName.recipe_ingredients,
        [CardName.plank, CardName.plank, CardName.sail])
    sloop.group(
        GroupName.misc,
        [CardName.frigate, CardName.rowboat])

    smelter = cardpedia.category(CategoryName.structures).card(CardName.smelter)
    smelter.group(
        GroupName.recipe_plus_1_card,
        populate.adults)
    smelter.group(
        GroupName.recipe_ingredients,
        [CardName.flint, CardName.flint, CardName.brick, CardName.brick, CardName.plank])

    soil = cardpedia.category(CategoryName.structures).card(CardName.soil)
    soil.group(GroupName.recipe_ingredients,
               [CardName.composter])
    soil.group(GroupName.recipe_plus_5_cards,
               populate.food)
    soil.group(
        GroupName.misc,
        [CardName.greenhouse, CardName.farm, CardName.garden, CardName.poop])

    spring = cardpedia.category(CategoryName.structures).card(CardName.spring)

    stove = cardpedia.category(CategoryName.structures).card(CardName.stove)
    stove.group(
        GroupName.recipe_plus_1_card,
        populate.adults)
    stove.group(
        GroupName.recipe_ingredients,
        [CardName.flint, CardName.brick, CardName.iron_bar])
    stove.group(
        GroupName.misc,
        [CardName.campfire])

    strange_portal = cardpedia.category(CategoryName.structures).card(CardName.strange_portal)
    strange_portal.group(
        GroupName.drops,
        [CardName.rat, CardName.goblin, CardName.giant_rat, CardName.slime, CardName.bear, CardName.wolf,
         CardName.skeleton])

    sugar_cane = cardpedia.category(CategoryName.structures).card(CardName.sugar_cane)
    sugar_cane.group(
        GroupName.drops,
        [CardName.cane_sugar])

    temple = cardpedia.category(CategoryName.structures).card(CardName.temple)
    temple.group(
        GroupName.recipe_plus_3_cards,
        populate.adults)
    temple.group(
        GroupName.recipe_ingredients,
        [CardName.plank, CardName.plank, CardName.plank, CardName.plank, CardName.plank,
         CardName.brick, CardName.brick, CardName.brick, CardName.brick, CardName.brick,
         CardName.iron_bar, CardName.iron_bar, CardName.iron_bar])

    travelling_cart = cardpedia.category(CategoryName.structures).card(CardName.travelling_cart)
    travelling_cart.group(
        GroupName.drops,
        sorted(list({CardName.soil, CardName.bone, CardName.plank, CardName.brick, CardName.iron_bar, CardName.iron_ore,
                     CardName.apple, CardName.frittata, CardName.spear, CardName.map, CardName.old_tome, CardName.key,
                     CardName.flint, CardName.treasure_chest, CardName.golden_goblet})))
    travelling_cart.group(
        GroupName.misc,
        [CardName.coin, CardName.coin, CardName.coin, CardName.coin, CardName.coin])

    treasure_chest = cardpedia.category(CategoryName.structures).card(CardName.treasure_chest)
    treasure_chest.group(
        GroupName.drops,
        sorted(list({CardName.apple, CardName.berry, CardName.bone, CardName.brick, CardName.carrot,
                     CardName.cooked_meat, CardName.corpse,
                     CardName.egg, CardName.flint, CardName.frittata, CardName.fruit_salad, CardName.iron_bar,
                     CardName.iron_ore, CardName.wood, CardName.key, CardName.map,
                     CardName.milk, CardName.milkshake, CardName.mushroom, CardName.old_tome, CardName.omelette,
                     CardName.onion, CardName.plank, CardName.potato, CardName.raw_meat,
                     CardName.poop, CardName.spear, CardName.stew, CardName.stick, CardName.stone, CardName.sword})))
    treasure_chest.group(
        GroupName.misc,
        [CardName.key])

    tree = cardpedia.category(CategoryName.structures).card(CardName.tree)
    tree.group(
        GroupName.drops,
        [CardName.wood, CardName.stick, CardName.apple])

    warehouse = cardpedia.category(CategoryName.structures).card(CardName.warehouse)
    warehouse.group(
        GroupName.recipe_plus_1_card,
        populate.adults)
    warehouse.group(
        GroupName.recipe_ingredients,
        [CardName.iron_bar, CardName.stone])
    warehouse.group(
        GroupName.misc,
        [CardName.shed])
