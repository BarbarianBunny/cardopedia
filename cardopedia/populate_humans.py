from cardopedia.card_name import CardName
from cardopedia.cardpedia import Cardpedia
from cardopedia.category_name import CategoryName
from cardopedia.group_name import GroupName
from cardopedia.populate import Populate

populate = Populate()


def populate_humans(cardpedia: Cardpedia):
    baby = cardpedia.category(CategoryName.humans).card(CardName.baby)
    baby.group(
        GroupName.recipe_plus_2_cards,
        [CardName.explorer, CardName.fisher, CardName.friendly_pirate, CardName.militia,
         CardName.swordsman, CardName.villager])
    baby.group(
        GroupName.recipe_ingredients,
        [CardName.house])   

    dog = cardpedia.category(CategoryName.humans).card(CardName.dog) 
    dog.group(
        GroupName.recipe_ingredients,
        [CardName.wolf, CardName.bone])
    dog.group(
        GroupName.alt_recipe,
        [CardName.house, CardName.dog, CardName.dog]) 
    dog.group(
        GroupName.drops,
        [CardName.corpse]) 

    explorer = cardpedia.category(CategoryName.humans).card(CardName.explorer)
    explorer.group(
        GroupName.recipe_plus_1_card,
        [CardName.fisher, CardName.militia, CardName.swordsman, CardName.villager])
    explorer.group(
        GroupName.recipe_ingredients,
        [CardName.map]) 
    explorer.group(
        GroupName.drops,
        [CardName.corpse])
    explorer.group(
        GroupName.misc,
        [CardName.catacombs, CardName.cave, CardName.forest, CardName.graveyard, CardName.jungle, CardName.mountain,
         CardName.old_village, CardName.plains])

    fisher = cardpedia.category(CategoryName.humans).card(CardName.fisher)
    fisher.group(
        GroupName.recipe_plus_1_card,
        [CardName.explorer, CardName.militia, CardName.swordsman, CardName.villager])
    fisher.group(
        GroupName.recipe_ingredients,
        [CardName.fishing_rod]) 
    fisher.group(
        GroupName.drops,
        [CardName.corpse])
    fisher.group(
        GroupName.misc,
        [CardName.fishing_spot])

    friendly_pirate = cardpedia.category(CategoryName.humans).card(CardName.friendly_pirate) 
    friendly_pirate.group(
        GroupName.recipe_ingredients,
        [CardName.pirate, CardName.parrot]) 
    friendly_pirate.group(
        GroupName.drops,
        [CardName.corpse]) 

    militia = cardpedia.category(CategoryName.humans).card(CardName.militia)
    militia.group(
        GroupName.recipe_plus_1_card,
        [CardName.explorer, CardName.fisher, CardName.swordsman, CardName.villager])
    militia.group(
        GroupName.recipe_ingredients,
        [CardName.spear]) 
    militia.group(
        GroupName.drops,
        [CardName.corpse]) 

    swordsman = cardpedia.category(CategoryName.humans).card(CardName.swordsman)
    swordsman.group(
        GroupName.recipe_plus_1_card,
        [CardName.explorer, CardName.fisher, CardName.militia, CardName.villager])
    swordsman.group(
        GroupName.recipe_ingredients,
        [CardName.sword]) 
    swordsman.group(
        GroupName.drops,
        [CardName.corpse]) 

    trained_monkey = cardpedia.category(CategoryName.humans).card(CardName.trained_monkey) 
    trained_monkey.group(
        GroupName.recipe_ingredients,
        [CardName.monkey, CardName.banana])   

    villager = cardpedia.category(CategoryName.humans).card(CardName.villager) 
    villager.group(
        GroupName.recipe_ingredients,
        [CardName.house, CardName.baby]) 
    villager.group(
        GroupName.drops,
        [CardName.corpse])
    villager.group(
        GroupName.misc,
        [CardName.humble_beginnings, CardName.seeking_wisdom, CardName.reap_sow, CardName.curious_cuisine,
         CardName.logic_and_reason, CardName.explorers, CardName.order_and_structure])
