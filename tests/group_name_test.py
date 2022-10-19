import json

import pytest

from cardopedia.enums.group_name import GroupName


class Enum:
    def class_exists(self):
        assert GroupName

    def key_exists(self):
        assert GroupName.drops

    def value_exists(self):
        assert GroupName("Drops")

    def invalid_value(self):
        with pytest.raises(ValueError):
            GroupName("Invalid")

    def jsonable(self):
        test_location = "test.json"
        test_data = {"test": [GroupName.drops]}
        with open(test_location, "w") as f:
            json.dump(test_data, f)
        with open(test_location) as f:
            assert json.load(f) == test_data

class Ordered:

    def less_then_comparison(self):
        assert GroupName.drops > GroupName.sources

class Kebab:

    def two_words(self):
        assert GroupName.recipe_ingredients.kebab() == "crafting-ingredients"

class HtmlButton:

    def is_str_given_name(self):
        assert isinstance(GroupName.drops.html_button(), str)
