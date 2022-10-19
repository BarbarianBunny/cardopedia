import json

import pytest

from cardopedia.enums.category_name import CategoryName


class Enum:
    def class_exists(self):
        assert CategoryName

    def key_exists(self):
        assert CategoryName.packs

    def value_exists(self):
        assert CategoryName("Packs")

    def invalid_value(self):
        with pytest.raises(ValueError):
            CategoryName("Invalid")

    def jsonable(self):
        test_location = "test.json"
        test_data = {"test": [CategoryName.packs]}
        with open(test_location, "w") as f:
            json.dump(test_data, f)
        with open(test_location) as f:
            assert json.load(f) == test_data


class Ordered:

    def less_then_comparison(self):
        assert CategoryName.structures < CategoryName.humans


class Kebab:

    def one_words(self):
        assert CategoryName.packs.kebab() == "packs"


class HtmlButton:

    def given_name(self):
        assert CategoryName.packs.html_button() == \
               '<button id="packs" class="category"><span class="category__name">Packs</span></button>'
