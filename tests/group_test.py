import pytest

from cardopedia.card import Card
from cardopedia.enums.card_name import CardName
from cardopedia.group import Group
from cardopedia.enums.group_name import GroupName


class InitClass:

    def raises_type_error_given_name_only(self):
        with pytest.raises(TypeError):
           Group("Drops")

    def given_name_str_card_name_list_strs(self):
        assert Group("Drops", ["Villager"])

    def given_name_enum_card_name_list_enums(self):
        assert Group(GroupName.drops, [CardName.villager])


class InitName:


    def given_str(self):
        assert Group("Drops", ["Villager"]).name

    def as_enum_given_str(self):
        assert isinstance(Group("Drops", ["Villager"]).name, GroupName)

    def given_enum(self):
        assert Group(GroupName.drops, ["Villager"]).name

    def as_enum_given_enum(self):
        assert isinstance(Group(GroupName.drops, ["Villager"]).name, GroupName)


class InitCardNames:


    def given_str(self):
        assert Group("Drops", ["Villager"]).card_names

    def as_enum_given_str(self):
        assert isinstance(Group("Drops", ["Villager"]).card_names[0], CardName)

    def given_enum(self):
        assert Group("Drops", [CardName.villager]).card_names

    def as_enum_given_enum(self):
        assert isinstance(Group("Drops", [CardName.villager]).card_names[0], CardName)

    def has_len_3_given_3_enum(self):
        assert len(Group(GroupName.drops, [CardName.villager, CardName.villager, CardName.villager]).card_names) == 3


class SortNotImplementedOutsideClass:

    def card_group_sort(self):
        with pytest.raises(TypeError):
            [Card(CardName.villager), Group(GroupName.drops, [CardName.villager])].sort()


class Lt:

    def less_then(self):
        assert Group(GroupName.sources, [CardName.villager]) < Group(GroupName.drops, [CardName.villager])

    def greater_then(self):
        assert Group(GroupName.drops, [CardName.villager]) > Group(GroupName.sources, [CardName.villager])

    def list_of_groups_is_sortable(self):
        groups = [Group(GroupName.drops, [CardName.villager]), Group(GroupName.sources, [CardName.villager])]
        groups.sort()
        assert groups[0].name == GroupName.sources


class Le:

    def less_then_or_equal_given_equal(self):
        assert Group(GroupName.drops, [CardName.villager]) <= Group(GroupName.drops, [CardName.villager])

    def less_then_or_equal_given_less(self):
        assert Group(GroupName.sources, [CardName.villager]) <= Group(GroupName.drops, [CardName.villager])

    def greater_then_or_equal_given_equal(self):
        assert Group(GroupName.drops, [CardName.villager]) >= Group(GroupName.drops, [CardName.villager])

    def greater_then_or_equal_given_greater(self):
        assert Group(GroupName.drops, [CardName.villager]) >= Group(GroupName.sources, [CardName.villager])


class Html:

    def given_name_and_one_card_in_cards(self):
        assert Group(GroupName.drops, [CardName.animal_pen]).html() == \
               '<button class="group"><span class="group__name">Drops</span></button>' \
               '<div class="group-content">' \
               '<a href="#animal-pen" class="card-link">' \
               '<img class="card-image" src="images/animal-pen.png" alt="Animal Pen card" />' \
               '</a>' \
               '</div>'

    def given_name_and_two_card_in_cards(self):
        assert Group(GroupName.drops, [CardName.animal_pen, CardName.aquarium]).html() == \
               '<button class="group"><span class="group__name">Drops</span></button>' \
               '<div class="group-content">' \
               '<a href="#animal-pen" class="card-link">' \
               '<img class="card-image" src="images/animal-pen.png" alt="Animal Pen card" />' \
               '</a>' \
               '<a href="#aquarium" class="card-link">' \
               '<img class="card-image" src="images/aquarium.png" alt="Aquarium card" />' \
               '</a>' \
               '</div>'
