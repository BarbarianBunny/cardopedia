from cardopedia.card import Card
from cardopedia.category import Category
from cardopedia.enums.category_name import CategoryName
from cardopedia.group import Group
from cardopedia.enums.card_name import CardName
from cardopedia.enums.group_name import GroupName


class InitClass:

    def given_name_str(self):
        assert Category("Packs")

    def given_name_str_cards_strs(self):
        assert Category("Packs", {"Villager": {"Drops": ["Villager"]}})

    def given_name_enum(self):
        assert Category(CategoryName.packs)

    def given_name_enum_cards_enums(self):
        assert Category(CategoryName.packs, {CardName.villager: {GroupName.drops: [CardName.villager]}})


class InitName:

    def given_str_only(self):
        assert Category("Packs").name

    def given_str(self):
        assert Category("Packs", {"Villager": {"Drops": ["Villager"]}}).name

    def as_enum_given_str(self):
        assert isinstance(Category("Packs", {"Villager": {"Drops": ["Villager"]}}).name, CategoryName)

    def given_enum(self):
        assert Category(CategoryName.packs, {"Villager": {"Drops": ["Villager"]}}).name

    def as_enum_given_enum(self):
        assert isinstance(Category(CategoryName.packs, {"Villager": {"Drops": ["Villager"]}}).name, CategoryName)


class InitCards:

    def is_empty_list_given_name_only(self):
        assert Category("Packs").cards == []

    def given_dict(self):
        assert Category("Packs", {"Villager": {"Drops": ["Villager"]}}).cards

    def as_card_given_str(self):
        print(type(Category("Packs", {"Villager": {"Drops": ["Villager"]}}).cards[0]))
        assert isinstance(Category("Packs", {"Villager": {"Drops": ["Villager"]}}).cards[0], Card)

    def given_dict_of_enums(self):
        assert Category("Packs", {CardName.villager: {GroupName.drops: [CardName.villager]}}).cards

    def as_card_given_dict_of_enums(self):
        assert isinstance(Category("Packs", {CardName.villager: {GroupName.drops: [CardName.villager]}}).cards[0],
                          Card)

    def has_len_3_given_3_dicts(self):
        assert len(Category(CategoryName.packs, {CardName.villager: {GroupName.drops: [CardName.villager]},
                                                 CardName.militia: {GroupName.drops: [CardName.villager]},
                                                 CardName.swordsman: {
                                                     GroupName.drops: [CardName.villager]}}).cards) == 3

    def given_empty_cards(self):
        assert Category(CategoryName.structures, [])

    def given_list_of_cards(self):
        assert Category(CategoryName.structures, [Card(CardName.villager, []), Card(CardName.animal_pen, [])])

    def contains_card_in_cards_given_list_with_card(self):
        assert Category(CategoryName.structures, [Card(CardName.villager, [])]).cards[0].name == CardName.villager


class Iter:

    def dict_given_name_only(self):
        assert dict(Category(CategoryName.packs)) == {}

    def dict_given_one_card(self):
        test_dict = {CardName.villager: {}}
        assert dict(Category(CategoryName.packs, test_dict)) == test_dict

    def dict_given_two_card(self):
        test_dict = {CardName.villager: {}, CardName.aquarium: {}}
        assert dict(Category(CategoryName.packs, test_dict)) == test_dict

    def dict_given_one_card_with_group(self):
        test_dict = {CardName.villager: {GroupName.drops: [CardName.warehouse, CardName.animal_pen]}}
        assert dict(Category(CategoryName.packs, test_dict)) == test_dict

    def dict_given_one_card_with_group_and_card_names(self):
        test_dict = {CardName.villager: {GroupName.drops: [CardName.warehouse, CardName.animal_pen]}}
        assert dict(Category(CategoryName.packs, test_dict)) == test_dict


class Lt:

    def less_then(self):
        assert Category(CategoryName.structures) < Category(CategoryName.humans)

    def greater_then(self):
        assert Category(CategoryName.humans) > Category(CategoryName.structures)

    def list_of_cards_is_sortable(self):
        category = [Category(CategoryName.humans), Category(CategoryName.structures)]
        category.sort()
        assert category[0].name == CategoryName.structures


class Le:

    def less_then_or_equal_given_equal(self):
        assert Category(CategoryName.structures) <= Category(CategoryName.structures)

    def less_then_or_equal_given_less(self):
        assert Category(CategoryName.structures) <= Category(CategoryName.humans)

    def greater_then_or_equal_given_equal(self):
        assert Category(CategoryName.humans) >= Category(CategoryName.humans)

    def greater_then_or_equal_given_greater(self):
        assert Category(CategoryName.humans) >= Category(CategoryName.structures)


class Sort:

    def given_name_only(self):
        category = Category(CategoryName.packs)
        category.sort()
        assert category

    def given_reversed_order(self):
        category = Category(CategoryName.packs, {CardName.baby: [],
                                                 CardName.warehouse: []})
        category.sort()
        assert category.cards[0].name == CardName.warehouse

    def calls_group_sort(self):
        category = Category(CategoryName.structures, {CardName.baby: {GroupName.drops: [], GroupName.sources: []}})
        category.sort()
        assert category.cards[0].groups[0].name == GroupName.sources


class CardMethod:

    def given_name_only(self):
        category = Category(CategoryName.packs)
        assert category.card(CardName.villager)

    def isinstance_card_given_name_only(self):
        category = Category(CategoryName.packs)
        assert isinstance(category.card(CardName.villager), Card)

    def returns_card_with_name_given_name_only(self):
        category = Category(CategoryName.packs)
        assert category.card(CardName.villager).name == CardName.villager

    def isinstance_card_given_name_and_empty_groups(self):
        category = Category(CategoryName.packs)
        assert isinstance(category.card(CardName.villager, []), Card)

    def isinstance_card_given_name_and_groups(self):
        category = Category(CategoryName.packs)
        assert isinstance(category.card(CardName.villager, [Group(GroupName.drops, [CardName.villager])]), Card)

    def returns_card_with_name_given_name_and_groups(self):
        category = Category(CategoryName.packs)
        assert category.card(CardName.villager, [Group(GroupName.drops, [CardName.villager])]).name == CardName.villager

    def returns_card_with_group_given_name_and_groups(self):
        category = Category(CategoryName.packs)
        assert category.card(CardName.villager, [Group(GroupName.drops, [CardName.villager])]).groups[
                   0].name == GroupName.drops

    def cards_len_of_1_given_duplicate_card(self):
        category = Category(CategoryName.packs)
        category.card(CardName.villager)
        category.card(CardName.villager)
        assert len(category.cards) == 1

    def does_not_remove_groups_when_getting_existing_group(self):
        category = Category(CategoryName.packs)
        category.card(CardName.villager, [Group(GroupName.drops, [CardName.villager])])
        assert category.card(CardName.villager).groups[0].name == GroupName.drops


class Html:

    def is_str_given_name_only(self):
        assert isinstance(Category(CategoryName.packs).html(), str)

    def is_str_given_name_and_one_card_in_cards(self):
        assert isinstance(Category(CategoryName.packs, {CardName.animal_pen: {}}).html(), str)

    def is_str_given_name_and_two_card_in_cards(self):
        assert isinstance(Category(CategoryName.packs, {CardName.animal_pen: {}, CardName.aquarium: {}}).html(), str)
