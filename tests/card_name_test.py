import json

import pytest

from cardopedia.card_name import CardName


class Enum:

    def class_exists(self):
        assert CardName

    def key_exists(self):
        assert CardName.villager

    def value_exists(self):
        assert CardName("Villager")

    def invalid_value(self):
        with pytest.raises(ValueError):
            CardName("Invalid")

    def jsonable(self):
        test_location = "test.json"
        test_data = {"test": [CardName.villager]}
        with open(test_location, "w") as f:
            json.dump(test_data, f)
        with open(test_location) as f:
            assert json.load(f) == test_data

class Ordered:

    def less_then_comparison(self):
        assert CardName.warehouse < CardName.baby

class Kebab:

    def given_two_words(self):
        assert CardName.animal_pen.kebab() == "animal-pen"


class HtmlImg:

    def is_str_given_animal_pen(self):
        assert isinstance(CardName.animal_pen.html_img(), str)


class HtmlButton:

    def is_str_given_animal_pen(self):
        assert isinstance(CardName.animal_pen.html_button(), str)


class HtmlLink:

    def is_str_given_animal_pen(self):
        assert isinstance(CardName.animal_pen.html_link(), str)
