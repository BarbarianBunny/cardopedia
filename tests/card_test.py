from cardopedia.card import Card
from cardopedia.group import Group
from cardopedia.enums.card_name import CardName
from cardopedia.enums.group_name import GroupName


class InitClass:

    def given_name_str(self):
        assert Card("Villager")

    def given_name_str_card_name_list_strs(self):
        assert Card("Villager", {"Drops": ["Villager"]})

    def given_name_enum(self):
        assert Card(CardName.villager)

    def given_name_enum_card_name_list_enums(self):
        assert Card(CardName.villager, {GroupName.drops: [CardName.villager]})


class InitName:

    def given_str_only(self):
        assert Card("Villager").name

    def given_str(self):
        assert Card("Villager", {"Drops": ["Villager"]}).name

    def as_enum_given_str(self):
        assert isinstance(Card("Villager", {"Drops": ["Villager"]}).name, CardName)

    def given_enum(self):
        assert Card(CardName.villager, {"Drops": ["Villager"]}).name

    def as_enum_given_enum(self):
        assert isinstance(Card(CardName.villager, {"Drops": ["Villager"]}).name, CardName)


class InitGroups:

    def is_empty_list_given_name_only(self):
        assert Card("Villager").groups == []

    def given_dict(self):
        assert Card("Villager", {"Drops": ["Villager"]}).groups

    def as_group_given_str(self):
        assert isinstance(Card("Villager", {"Drops": ["Villager"]}).groups[0], Group)

    def given_dict_of_enums(self):
        assert Card("Villager", {GroupName.drops: [CardName.villager]}).groups

    def as_group_given_dict_of_enums(self):
        assert isinstance(Card("Villager", {GroupName.drops: [CardName.villager]}).groups[0], Group)

    def has_len_3_given_3_dicts(self):
        assert len(Card(CardName.villager, {GroupName.drops: [CardName.villager],
                                            GroupName.sources: [CardName.villager],
                                            GroupName.misc: [CardName.villager]}).groups) == 3

    def given_list_of_groups(self):
        assert Card(CardName.villager,
                    [Group(GroupName.drops, [CardName.villager]), Group(GroupName.sources, [CardName.animal_pen])])

    def contains_group_in_groups_given_list_with_group(self):
        assert Card(CardName.villager, [Group(GroupName.drops, [CardName.villager])]).groups[0].name == GroupName.drops


class Iter:

    def dict_given_name_only(self):
        assert dict(Card(CardName.villager)) == {}

    def dict_given_one_group(self):
        test_dict = {GroupName.drops: []}
        assert dict(Card(CardName.villager, test_dict)) == test_dict

    def dict_given_two_group(self):
        test_dict = {GroupName.drops: [], GroupName.misc: []}
        assert dict(Card(CardName.villager, test_dict)) == test_dict

    def dict_given_one_group_with_card_names(self):
        test_dict = {GroupName.drops: [CardName.warehouse, CardName.animal_pen]}
        assert dict(Card(CardName.villager, test_dict)) == test_dict


class Lt:

    def less_then(self):
        assert Card(CardName.warehouse) < Card(CardName.baby)

    def greater_then(self):
        assert Card(CardName.baby) > Card(CardName.warehouse)

    def list_of_cards_is_sortable(self):
        cards = [Card(CardName.baby), Card(CardName.warehouse)]
        cards.sort()
        assert cards[0].name == CardName.warehouse


class Le:

    def less_then_or_equal_given_equal(self):
        assert Card(CardName.warehouse) <= Card(CardName.warehouse)

    def less_then_or_equal_given_less(self):
        assert Card(CardName.warehouse) <= Card(CardName.baby)

    def greater_then_or_equal_given_equal(self):
        assert Card(CardName.baby) >= Card(CardName.baby)

    def greater_then_or_equal_given_greater(self):
        assert Card(CardName.baby) >= Card(CardName.warehouse)


class Sort:

    def given_name_only(self):
        card = Card(CardName.animal_pen)
        card.sort()
        assert card

    def given_reversed_order(self):
        card = Card(CardName.animal_pen, {GroupName.drops: [],
                                          GroupName.sources: [],
                                          GroupName.misc: []})
        card.sort()
        assert card.groups[0].name == GroupName.sources


class GroupMethod:

    def given_name_only(self):
        card = Card(CardName.animal_pen)
        assert card.group(GroupName.drops, [CardName.villager])

    def isinstance_group_given_name_only(self):
        card = Card(CardName.animal_pen)
        assert isinstance(card.group(GroupName.drops, [CardName.villager]), Group)

    def returns_group_with_name_given_name_only(self):
        card = Card(CardName.animal_pen)
        assert card.group(GroupName.drops, [CardName.villager]).name == GroupName.drops

    def isinstance_group_given_name_and_card_names(self):
        card = Card(CardName.animal_pen)
        assert isinstance(card.group(GroupName.drops, [CardName.villager]), Group)

    def returns_group_with_name_given_name_and_card_names(self):
        card = Card(CardName.animal_pen)
        assert card.group(GroupName.drops, [CardName.villager]).name == GroupName.drops

    def returns_group_with_card_name_given_name_and_card_names(self):
        card = Card(CardName.animal_pen)
        assert card.group(GroupName.drops, [CardName.villager]).card_names == [CardName.villager]

    def groups_len_of_1_given_duplicate_group(self):
        card = Card(CardName.animal_pen)
        card.group(GroupName.drops, [CardName.villager])
        card.group(GroupName.drops, [CardName.militia])
        assert len(card.groups) == 1

    def does_not_remove_card_names_when_getting_existing_group(self):
        card = Card(CardName.animal_pen)
        card.group(GroupName.drops, [CardName.villager])
        assert card.group(GroupName.drops).card_names == [CardName.villager]

    def overrides_card_names_given_card_names(self):
        card = Card(CardName.animal_pen)
        card.group(GroupName.drops, [CardName.villager])
        group = card.group(GroupName.drops, [CardName.militia])
        assert group.card_names[0] == CardName.militia


class Html:

    def is_str_given_name_only(self):
        assert isinstance(Card(CardName.animal_pen).html(), str)

    def is_str_given_name_and_one_group_in_groups(self):
        assert isinstance(Card(CardName.animal_pen, {GroupName.drops: []}).html(), str)

    def given_name_and_two_group_in_groups(self):
        assert isinstance(Card(CardName.animal_pen, {GroupName.drops: [], GroupName.misc: []}).html(), str)
