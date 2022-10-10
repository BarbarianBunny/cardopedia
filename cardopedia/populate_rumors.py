from cardopedia.card_name import CardName
from cardopedia.cardpedia import Cardpedia
from cardopedia.category_name import CategoryName
from cardopedia.group_name import GroupName


def populate_rumors(cardpedia: Cardpedia):
    rumor_eel_bait = cardpedia.category(CategoryName.rumors).card(CardName.rumor_eel_bait)
    rumor_eel_bait.group(
        GroupName.misc,
        [CardName.eel])

    rumor_shark_bait = cardpedia.category(CategoryName.rumors).card(CardName.rumor_shark_bait)
    rumor_shark_bait.group(
        GroupName.misc,
        [CardName.shark])

    rumor_the_island = cardpedia.category(CategoryName.rumors).card(CardName.rumor_the_island)

    rumor_tuna_bait = cardpedia.category(CategoryName.rumors).card(CardName.rumor_tuna_bait)
    rumor_tuna_bait.group(
        GroupName.misc,
        [CardName.tuna])
