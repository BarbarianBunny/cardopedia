from cardopedia.generate_groups import generate_sources
from cardopedia.enums.card_name import CardName
from cardopedia.cardpedia import Cardpedia
from cardopedia.enums.category_name import CategoryName
from cardopedia.enums.group_name import GroupName


class GenerateSources:

    def produces(self):
        cardpedia = Cardpedia()
        cardpedia.category(CategoryName.mobs).card(CardName.chicken).group(GroupName.produces, [CardName.poop])
        poop = cardpedia.category(CategoryName.resources).card(CardName.poop)
        generate_sources.generate_sources(cardpedia)
        assert poop.group(GroupName.sources).card_names == [CardName.chicken]

    def drops(self):
        cardpedia = Cardpedia()
        cardpedia.category(CategoryName.mobs).card(CardName.chicken).group(GroupName.drops, [CardName.poop])
        poop = cardpedia.category(CategoryName.resources).card(CardName.poop)
        generate_sources.generate_sources(cardpedia)
        assert poop.group(GroupName.sources).card_names == [CardName.chicken]


    def both_from_one(self):
        cardpedia = Cardpedia()
        cardpedia.category(CategoryName.mobs).card(CardName.chicken).group(GroupName.produces, [CardName.poop])
        cardpedia.category(CategoryName.mobs).card(CardName.chicken).group(GroupName.drops, [CardName.poop])
        poop = cardpedia.category(CategoryName.resources).card(CardName.poop)
        generate_sources.generate_sources(cardpedia)
        assert poop.group(GroupName.sources).card_names == [CardName.chicken]


    def drops_and_produces(self):
        cardpedia = Cardpedia()
        cardpedia.category(CategoryName.mobs).card(CardName.rabbit).group(GroupName.produces, [CardName.poop])
        cardpedia.category(CategoryName.mobs).card(CardName.chicken).group(GroupName.drops, [CardName.poop])
        poop = cardpedia.category(CategoryName.resources).card(CardName.poop)
        generate_sources.generate_sources(cardpedia)
        assert poop.group(GroupName.sources).card_names == [CardName.chicken, CardName.rabbit]