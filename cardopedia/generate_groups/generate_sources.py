from cardopedia.cardpedia import Cardpedia
from cardopedia.enums.group_name import GroupName


def generate_sources(cardpedia: Cardpedia):
    # dict[CardName: set[CardName sources]]
    cards_with_source = {}

    for category in cardpedia.categories:
        for card in category.cards:
            # For each card produced add to cards_with_source and append to list of sources
            if produces := card.group(GroupName.produces):
                for card_name in produces.card_names:
                    if sources := cards_with_source.get(card_name):
                        sources.add(card.name)
                    else:
                        cards_with_source.update({card_name: {card.name}})
            # For each card dropped add to cards_with_source and append to list of sources
            if drops := card.group(GroupName.drops):
                for card_name in drops.card_names:
                    if sources := cards_with_source.get(card_name):
                        sources.add(card.name)
                    else:
                        cards_with_source.update({card_name: {card.name}})
            # For each card stored add to cards_with_source and append to list of sources
            if stores := card.group(GroupName.stores):
                for card_name in stores.card_names:
                    if sources := cards_with_source.get(card_name):
                        sources.add(card.name)
                    else:
                        cards_with_source.update({card_name: {card.name}})
    # For each card with a source found add sources group with list of sources
    for category in cardpedia.categories:
        for card in category.cards:
            if card.name in cards_with_source:
                card.group(GroupName.sources, sorted(list(cards_with_source[card.name])))
