from cardopedia.support_modules.kebab_case import kebab_case
from cardopedia.enums.ordered_str_enum import OrderedStrEnum


class CategoryName(OrderedStrEnum):
    packs = "Packs"
    structures = "Structures"
    humans = "Humans"
    resources = "Resources"
    ideas = "Ideas"
    food = "Food"
    mobs = "Mobs"
    locations = "Locations"
    fish = "Fish"
    rumors = "Rumors"

    def kebab(self):
        return kebab_case(self.value)

    def html_button(self):
        return f'<button id="{self.kebab()}" class="category"><span class="category__name">{self.value}</span></button>'
