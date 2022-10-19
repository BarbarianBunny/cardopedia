from cardopedia.support_modules.kebab_case import kebab_case
from cardopedia.enums.ordered_str_enum import OrderedStrEnum


class GroupName(OrderedStrEnum):
    sources = "Sources"  # Generated list of cards containing self in "Produces" or "
    recipe_ingredients = "Crafting Ingredients"  # List of cards that are all required in the recipe
    recipe_plus_1_card = "+1 Card"  # List of cards where one of the cards must be used in the recipe
    recipe_plus_2_cards = "+2 Cards"  # List of cards where two of the cards must be used in the recipe
    recipe_plus_3_cards = "+3 Cards"  # List of cards where three of the cards must be used in the recipe
    recipe_plus_5_cards = "+5 Cards"  # List of cards where five of the cards must be used in the recipe
    alt_recipe = "Alt Recipe"  # List of cards for an alternate recipe
    produces = "Produces"  # List of cards that are passively produced
    drops = "Drops"  # List of cards that are potentially dropped when interacted with. ie: click, kill, harvested
    makes = "Used to Make"  # Generated list of cards containing self in "Recipe Base" or "Recipe Ingredients"
    stores = "Stores"  # List of cards it's specifically designed to store
    misc = "Misc"  # Catch all but mostly for cards like animal_pen or aquarium which hold animals

    def kebab(self):
        return kebab_case(self.value)

    def html_button(self):
        return f'<button class="group"><span class="group__name">{self.value}</span></button>'
