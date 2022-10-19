from cardopedia.cardpedia import Cardpedia
from cardopedia.enums.group_name import GroupName


def generate_makes(cardpedia: Cardpedia):
    # dict[CardName: set[CardName made]]
    cards_with_makes = {}

    for category in cardpedia.categories:
        for card in category.cards:
            # For each card base add to cards_with_makes and append to list of makes
            if recipe_base := card.group(GroupName.recipe_plus_1_card):
                for card_name in recipe_base.card_names:
                    if makes := cards_with_makes.get(card_name):
                        makes.add(card.name)
                    else:
                        cards_with_makes.update({card_name: {card.name}})
            # For each card ingredient add to cards_with_makes and append to list of makes
            if recipe_ingredients := card.group(GroupName.recipe_ingredients):
                for card_name in recipe_ingredients.card_names:
                    if makes := cards_with_makes.get(card_name):
                        makes.add(card.name)
                    else:
                        cards_with_makes.update({card_name: {card.name}})
            # For each card ingredient add to cards_with_makes and append to list of makes
            if alt_recipe := card.group(GroupName.alt_recipe):
                for card_name in alt_recipe.card_names:
                    if makes := cards_with_makes.get(card_name):
                        makes.add(card.name)
                    else:
                        cards_with_makes.update({card_name: {card.name}})
    # For each card with a makes found add makes group with list of makes
    for category in cardpedia.categories:
        for card in category.cards:
            if card.name in cards_with_makes:
                card.group(GroupName.makes, sorted(list(cards_with_makes[card.name])))
