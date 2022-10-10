import pytest

from cardopedia.card_name import CardName
from cardopedia.group_name import GroupName


class NotImplementedBeyondClass:

    def less_then(self):
        with pytest.raises(TypeError):
            CardName.villager < GroupName.sources

    def less_then_or_equal(self):
        with pytest.raises(TypeError):
            CardName.villager <= GroupName.sources

    def greater_then(self):
        with pytest.raises(TypeError):
            CardName.villager > GroupName.sources

    def greater_then_or_equal(self):
        with pytest.raises(TypeError):
            CardName.villager >= GroupName.sources


class ImplementedWithinClass:

    def less_then(self):
        CardName.villager < CardName.rumor_the_island

    def less_then_or_equal(self):
        CardName.villager <= CardName.villager

    def greater_then(self):
        CardName.villager > CardName.warehouse

    def greater_then_or_equal(self):
        CardName.villager >= CardName.villager
