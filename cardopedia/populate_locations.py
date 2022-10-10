from cardopedia.card_name import CardName
from cardopedia.cardpedia import Cardpedia
from cardopedia.category_name import CategoryName
from cardopedia.group_name import GroupName
from cardopedia.populate import Populate

populate = Populate()


def populate_locations(cardpedia: Cardpedia):
    catacombs = cardpedia.category(CategoryName.locations).card(CardName.catacombs)
    catacombs.group(
        GroupName.drops,
        sorted([CardName.skeleton, CardName.goblin, CardName.wolf, CardName.slime, CardName.treasure_chest,
                CardName.giant_rat, CardName.golden_goblet]))

    cave = cardpedia.category(CategoryName.locations).card(CardName.cave)
    cave.group(
        GroupName.drops,
        sorted([CardName.goblin, CardName.giant_rat, CardName.rat, CardName.pirate, CardName.snake, CardName.bear,
                CardName.crab, CardName.treasure_map]))

    forest = cardpedia.category(CategoryName.locations).card(CardName.forest)
    forest.group(
        GroupName.drops,
        sorted(
            [CardName.berry_bush, CardName.apple, CardName.apple_tree, CardName.tree, CardName.stick, CardName.rabbit,
             CardName.goblin, CardName.bear, CardName.mushroom, CardName.catacombs, CardName.treasure_chest,
             CardName.wolf]))

    graveyard = cardpedia.category(CategoryName.locations).card(CardName.graveyard)
    graveyard.group(
        GroupName.recipe_ingredients,
        [CardName.corpse, CardName.corpse])
    graveyard.group(
        GroupName.drops,
        sorted([CardName.bone, CardName.soil, CardName.skeleton, CardName.treasure_chest, CardName.corpse,
                CardName.catacombs]))

    jungle = cardpedia.category(CategoryName.locations).card(CardName.jungle)
    jungle.group(
        GroupName.drops,
        sorted([CardName.tiger, CardName.cotton_plant, CardName.banana, CardName.monkey, CardName.lime,
                CardName.sugar_cane, CardName.parrot, CardName.baby, CardName.old_tome, CardName.wolf]))

    mountain = cardpedia.category(CategoryName.locations).card(CardName.mountain)
    mountain.group(
        GroupName.drops,
        [*sorted([CardName.rock, CardName.iron_deposit, CardName.bear, CardName.giant_rat, CardName.treasure_chest,
                  CardName.catacombs]),
         *sorted([CardName.idea_smelter])])

    old_village = cardpedia.category(CategoryName.locations).card(CardName.old_village)
    old_village.group(
        GroupName.drops,
        sorted([CardName.coin, CardName.villager, CardName.wood, CardName.corpse, CardName.iron_bar, CardName.catacombs,
                CardName.slime, CardName.treasure_chest, CardName.old_tome, CardName.goblin, CardName.milk]))

    plains = cardpedia.category(CategoryName.locations).card(CardName.plains)
    plains.group(
        GroupName.drops,
        sorted([CardName.chicken, CardName.mushroom, CardName.wolf, CardName.soil, CardName.rat, CardName.cow,
                CardName.onion, CardName.carrot, CardName.milk]))
