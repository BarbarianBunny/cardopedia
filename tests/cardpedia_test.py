from cardopedia.card import Card
from cardopedia.cardpedia import Cardpedia
from cardopedia.category import Category
from cardopedia.category_name import CategoryName
from cardopedia.card_name import CardName
from cardopedia.group_name import GroupName


class InitClass:

    def empty_categories(self):
        assert Cardpedia()

    def given_category_str_without_cards(self):
        assert Cardpedia({"Packs": {}})

    def given_category_enum_without_cards(self):
        assert Cardpedia({CategoryName.packs: {}})

    def given_categories_strs(self):
        assert Cardpedia({"Packs": {"Villager": {"Drops": ["Villager"]}}})

    def given_categories_enum(self):
        assert Cardpedia({CategoryName.packs: {CardName.villager: {GroupName.drops: [CardName.villager]}}})


class InitCategories:

    def is_empty_list_given_nothing(self):
        assert Cardpedia().categories == []

    def given_dict(self):
        assert Cardpedia({"Packs": {"Villager": {"Drops": ["Villager"]}}}).categories

    def as_category_given_str(self):
        assert isinstance(Cardpedia({"Packs": {"Villager": {"Drops": ["Villager"]}}}).categories[0], Category)

    def given_dict_of_enums(self):
        assert Cardpedia({CategoryName.packs: {CardName.villager: {GroupName.drops: [CardName.villager]}}}).categories

    def as_group_given_dict_of_enums(self):
        assert isinstance(Cardpedia(
            {CategoryName.packs: {CardName.villager: {GroupName.drops: [CardName.villager]}}}).categories[0], Category)

    def has_len_3_given_3_dicts(self):
        assert len(Cardpedia(
            {CategoryName.packs: {CardName.villager: {GroupName.drops: [CardName.villager]}},
             CategoryName.structures: {CardName.villager: {GroupName.drops: [CardName.villager]}},
             CategoryName.humans: {CardName.villager: {GroupName.drops: [CardName.villager]}}}).categories) == 3


class Iter:

    def dict_given_name_only(self):
        assert dict(Cardpedia()) == {}

    def dict_given_one_category(self):
        test_dict = {CategoryName.packs: {}}
        assert dict(Cardpedia(test_dict)) == test_dict

    def dict_given_two_category(self):
        test_dict = {CategoryName.packs: {}, CategoryName.structures: {}}
        assert dict(Cardpedia(test_dict)) == test_dict

    def dict_given_one_category_with_card(self):
        test_dict = {CategoryName.packs: {CardName.villager: {}}}
        assert dict(Cardpedia(test_dict)) == test_dict

    def dict_given_one_category_with_card_with_group(self):
        test_dict = {CategoryName.packs: {CardName.villager: {GroupName.sources: []}}}
        assert dict(Cardpedia(test_dict)) == test_dict

    def dict_given_one_category_with_card_with_group_and_card_names(self):
        test_dict = {
            CategoryName.packs: {CardName.villager: {GroupName.sources: [CardName.warehouse, CardName.animal_pen]}}}
        assert dict(Cardpedia(test_dict)) == test_dict


class Sort:

    def given_nothing(self):
        cardpedia = Cardpedia()
        cardpedia.sort()
        assert cardpedia

    def given_reversed_order(self):
        cardpedia = Cardpedia({CategoryName.humans: [],
                               CategoryName.structures: []})
        cardpedia.sort()
        assert cardpedia.categories[0].name == CategoryName.structures

    def calls_category_sort(self):
        cardopedia = Cardpedia({CategoryName.structures: {CardName.baby: [], CardName.warehouse: []}})
        cardopedia.sort()
        assert cardopedia.categories[0].cards[0].name == CardName.warehouse


class CategoryMethod:

    def given_name_only(self):
        cardpedia = Cardpedia()
        assert cardpedia.category(CategoryName.packs)

    def isinstance_category_given_name_only(self):
        cardpedia = Cardpedia()
        assert isinstance(cardpedia.category(CategoryName.packs), Category)

    def returns_category_with_name_given_name_only(self):
        cardpedia = Cardpedia()
        assert cardpedia.category(CategoryName.packs).name == CategoryName.packs

    def isinstance_category_given_name_and_empty_cards(self):
        cardpedia = Cardpedia()
        assert isinstance(cardpedia.category(CategoryName.packs, []), Category)

    def isinstance_category_given_name_and_cards(self):
        cardpedia = Cardpedia()
        assert isinstance(cardpedia.category(CategoryName.packs, [Card(CardName.villager)]), Category)

    def returns_category_with_name_given_name_and_cards(self):
        cardpedia = Cardpedia()
        assert cardpedia.category(CategoryName.packs, [Card(CardName.villager)]).name == CategoryName.packs

    def returns_category_with_card_given_name_and_cards(self):
        cardpedia = Cardpedia()
        assert cardpedia.category(CategoryName.packs, [Card(CardName.villager)]).cards[0].name == CardName.villager

    def categories_len_of_1_given_duplicate_category(self):
        cardpedia = Cardpedia()
        cardpedia.category(CategoryName.packs)
        cardpedia.category(CategoryName.packs)
        assert len(cardpedia.categories) == 1

    def does_not_remove_cards_when_getting_existing_card(self):
        cardpedia = Cardpedia()
        cardpedia.category(CategoryName.packs, [Card(CardName.villager)])
        assert cardpedia.category(CategoryName.packs).cards[0].name == CardName.villager


class HtmlPreBody:

    def is_str_given_nothing(self):
        assert isinstance(Cardpedia().html_pre_body(), str)

class HtmlPostBody:

    def is_str_given_nothing(self):
        assert isinstance(Cardpedia().html_post_body(), str)


class Html:

    def is_str_given_nothing(self):
        assert isinstance(Cardpedia().html(), str)

    def is_str_given_one_category_in_categories(self):
        assert isinstance(Cardpedia({CategoryName.packs: {}}).html(), str)

    def is_str_given_two_category_in_categories(self):
        assert isinstance(Cardpedia({CategoryName.packs: {}, CategoryName.structures: {}}).html(), str)
