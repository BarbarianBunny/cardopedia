from cardopedia.card_name import CardName
from cardopedia.populate import Populate


class Adults:

    def contains_cardname(self):
        assert isinstance(Populate().adults[0], CardName)


class TrainableAdults:

    def contains_cardname(self):
        assert isinstance(Populate().trainable_adults[0], CardName)


class Growers:

    def contains_cardname(self):
        assert isinstance(Populate().growers[0], CardName)


class Ideas:

    def contains_cardname(self):
        assert isinstance(Populate().ideas[0], CardName)


class Boats:

    def contains_cardname(self):
        assert isinstance(Populate().boats[0], CardName)


class Cookers:

    def contains_cardname(self):
        assert isinstance(Populate().cookers[0], CardName)


class CreatureHolders:

    def contains_cardname(self):
        assert isinstance(Populate().creature_holders[0], CardName)


class CurrencyHolders:

    def contains_cardname(self):
        assert isinstance(Populate().currency_holders[0], CardName)


class LaborReplacers:

    def contains_cardname(self):
        assert isinstance(Populate().labor_replacers[0], CardName)


class InfiniteResourceSources:

    def contains_cardname(self):
        assert isinstance(Populate().infinite_resource_sources[0], CardName)


class FiniteResourceSources:

    def contains_cardname(self):
        assert isinstance(Populate().finite_resource_sources[0], CardName)


class FiniteFoodSources:

    def contains_cardname(self):
        assert isinstance(Populate().finite_food_sources[0], CardName)


class Food:

    def contains_cardname(self):
        assert isinstance(Populate().food[0], CardName)


class SpoilableFood:

    def contains_cardname(self):
        assert isinstance(Populate().spoilable_food[0], CardName)
