from cardopedia.enums.card_name import CardName
from cardopedia.cardpedia import Cardpedia
from cardopedia.enums.category_name import CategoryName
from cardopedia.generate_groups import generate_makes
from cardopedia.enums.group_name import GroupName


class GenerateMakes:

    def recipe_base(self):
        cardpedia = Cardpedia()
        cardpedia.category(CategoryName.food).card(CardName.carrot).group(GroupName.recipe_plus_1_card, [CardName.poop])
        poop = cardpedia.category(CategoryName.resources).card(CardName.poop)
        generate_makes.generate_makes(cardpedia)
        assert poop.group(GroupName.makes).card_names == [CardName.carrot]

    def recipe_ingredient(self):
        cardpedia = Cardpedia()
        cardpedia.category(CategoryName.food).card(CardName.carrot).group(GroupName.recipe_ingredients, [CardName.poop])
        poop = cardpedia.category(CategoryName.resources).card(CardName.poop)
        generate_makes.generate_makes(cardpedia)
        assert poop.group(GroupName.makes).card_names == [CardName.carrot]


    def recipe(self):
        cardpedia = Cardpedia()
        cardpedia.category(CategoryName.food).card(CardName.carrot).group(GroupName.recipe_plus_1_card, [CardName.poop])
        cardpedia.category(CategoryName.food).card(CardName.apple).group(GroupName.recipe_ingredients, [CardName.poop])
        poop = cardpedia.category(CategoryName.resources).card(CardName.poop)
        generate_makes.generate_makes(cardpedia)
        assert poop.group(GroupName.makes).card_names == [CardName.apple, CardName.carrot]


    def both_from_one(self):
        cardpedia = Cardpedia()
        cardpedia.category(CategoryName.food).card(CardName.carrot).group(GroupName.recipe_plus_1_card, [CardName.poop])
        cardpedia.category(CategoryName.food).card(CardName.carrot).group(GroupName.recipe_ingredients, [CardName.poop])
        poop = cardpedia.category(CategoryName.resources).card(CardName.poop)
        generate_makes.generate_makes(cardpedia)
        assert poop.group(GroupName.makes).card_names == [CardName.carrot]