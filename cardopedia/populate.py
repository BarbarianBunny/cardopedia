from cardopedia.card_name import CardName


class Populate:

    def __init__(self):
        self.adults = sorted(
            [CardName.dog, CardName.explorer, CardName.fisher, CardName.friendly_pirate, CardName.militia,
             CardName.swordsman, CardName.trained_monkey, CardName.villager])
        self.trainable_adults = sorted([CardName.explorer, CardName.fisher, CardName.militia, CardName.swordsman,
                                        CardName.villager])
        self.growers = [CardName.greenhouse, CardName.farm, CardName.garden, CardName.soil, CardName.poop]
        self.ideas = sorted([CardName.idea_animal_pen,
                             CardName.idea_aquarium,
                             CardName.idea_bottle_of_rum,
                             CardName.idea_brick,
                             CardName.idea_brickyard,
                             CardName.idea_campfire,
                             CardName.idea_cathedral,
                             CardName.idea_ceviche,
                             CardName.idea_charcoal,
                             CardName.idea_chicken,
                             CardName.idea_coin,
                             CardName.idea_coin_chest,
                             CardName.idea_composter,
                             CardName.idea_cooked_meat,
                             CardName.idea_distillery,
                             CardName.idea_empty_bottle,
                             CardName.idea_fabric,
                             CardName.idea_farm,
                             CardName.idea_fish_trap,
                             CardName.idea_fishing_rod,
                             CardName.idea_frigate,
                             CardName.idea_frittata,
                             CardName.idea_fruit_salad,
                             CardName.idea_garden,
                             CardName.idea_glass,
                             CardName.idea_gold_bar,
                             CardName.idea_gold_mine,
                             CardName.idea_greenhouse,
                             CardName.idea_growth,
                             CardName.idea_house,
                             CardName.idea_iron_bar,
                             CardName.idea_iron_mine,
                             CardName.idea_lumber_camp,
                             CardName.idea_market,
                             CardName.idea_mess_hall,
                             CardName.idea_milkshake,
                             CardName.idea_offspring,
                             CardName.idea_omelette,
                             CardName.idea_plank,
                             CardName.idea_quarry,
                             CardName.idea_rope,
                             CardName.idea_rowboat,
                             CardName.idea_sacred_key,
                             CardName.idea_sail,
                             CardName.idea_sand_quarry,
                             CardName.idea_sandstone,
                             CardName.idea_sawmill,
                             CardName.idea_seafood_stew,
                             CardName.idea_shed,
                             CardName.idea_shell_chest,
                             CardName.idea_sloop,
                             CardName.idea_smelter,
                             CardName.idea_spear,
                             CardName.idea_stew,
                             CardName.idea_stick,
                             CardName.idea_stove,
                             CardName.idea_sushi,
                             CardName.idea_sword,
                             CardName.idea_tamago_sushi,
                             CardName.idea_temple,
                             CardName.idea_warehouse])
        self.boats = [CardName.frigate, CardName.rowboat, CardName.sloop]
        self.cookers = [CardName.campfire, CardName.stove]
        self.creature_holders = [CardName.animal_pen, CardName.aquarium]
        self.currency_holders = [CardName.coin_chest, CardName.shell_chest]
        self.labor_replacers = [CardName.brickyard, CardName.sawmill]
        self.infinite_resource_sources = [CardName.gold_mine, CardName.iron_mine, CardName.lumber_camp, CardName.quarry,
                                          CardName.sand_quarry]
        self.finite_resource_sources = [CardName.driftwood, CardName.cotton_plant, CardName.gold_deposit,
                                        CardName.iron_deposit, CardName.rock, CardName.tree]
        self.finite_food_sources = [CardName.apple_tree, CardName.banana_tree, CardName.berry_bush,
                                    CardName.fishing_spot, CardName.sugar_cane]
        self.food = sorted([CardName.apple,
                            CardName.banana,
                            CardName.berry,
                            CardName.bottle_of_rum,
                            CardName.cane_sugar,
                            CardName.carrot,
                            CardName.ceviche,
                            CardName.chili_pepper,
                            CardName.cooked_crab,
                            CardName.cooked_meat,
                            CardName.egg,
                            CardName.frittata,
                            CardName.fruit_salad,
                            CardName.grilled_fish,
                            CardName.lime,
                            CardName.milk,
                            CardName.milkshake,
                            CardName.mushroom,
                            CardName.omelette,
                            CardName.onion,
                            CardName.potato,
                            CardName.raw_crab_meat,
                            CardName.raw_fish,
                            CardName.raw_meat,
                            CardName.seafood_stew,
                            CardName.seaweed,
                            CardName.stew,
                            CardName.sushi,
                            CardName.tamago_sushi])
        self.spoilable_food = sorted([CardName.apple,
                                      CardName.banana,
                                      CardName.berry,
                                      CardName.cane_sugar,
                                      CardName.carrot,
                                      CardName.ceviche,
                                      CardName.chili_pepper,
                                      CardName.cooked_crab,
                                      CardName.cooked_meat,
                                      CardName.egg,
                                      CardName.frittata,
                                      CardName.fruit_salad,
                                      CardName.grilled_fish,
                                      CardName.lime,
                                      CardName.milk,
                                      CardName.milkshake,
                                      CardName.mushroom,
                                      CardName.omelette,
                                      CardName.onion,
                                      CardName.potato,
                                      CardName.raw_crab_meat,
                                      CardName.raw_fish,
                                      CardName.raw_meat,
                                      CardName.seafood_stew,
                                      CardName.seaweed,
                                      CardName.stew,
                                      CardName.sushi,
                                      CardName.tamago_sushi])

    @property
    def adults(self):
        return list(self._adults)

    @adults.setter
    def adults(self, card_names):
        self._adults = []
        if card_names:
            for card_name in card_names:
                self._adults.append(CardName(card_name))

    @property
    def trainable_adults(self):
        return list(self._trainable_adults)

    @trainable_adults.setter
    def trainable_adults(self, card_names):
        self._trainable_adults = []
        if card_names:
            for card_name in card_names:
                self._trainable_adults.append(CardName(card_name))

    @property
    def growers(self):
        return list(self._growers)

    @growers.setter
    def growers(self, card_names):
        self._growers = []
        if card_names:
            for card_name in card_names:
                self._growers.append(CardName(card_name))

    @property
    def ideas(self):
        return list(self._ideas)

    @ideas.setter
    def ideas(self, card_names):
        self._ideas = []
        if card_names:
            for card_name in card_names:
                self._ideas.append(CardName(card_name))

    @property
    def boats(self):
        return list(self._boats)

    @boats.setter
    def boats(self, card_names):
        self._boats = []
        if card_names:
            for card_name in card_names:
                self._boats.append(CardName(card_name))

    @property
    def cookers(self):
        return list(self._cookers)

    @cookers.setter
    def cookers(self, card_names):
        self._cookers = []
        if card_names:
            for card_name in card_names:
                self._cookers.append(CardName(card_name))

    @property
    def creature_holders(self):
        return list(self._creature_holders)

    @creature_holders.setter
    def creature_holders(self, card_names):
        self._creature_holders = []
        if card_names:
            for card_name in card_names:
                self._creature_holders.append(CardName(card_name))

    @property
    def currency_holders(self):
        return list(self._currency_holders)

    @currency_holders.setter
    def currency_holders(self, card_names):
        self._currency_holders = []
        if card_names:
            for card_name in card_names:
                self._currency_holders.append(CardName(card_name))

    @property
    def labor_replacers(self):
        return list(self._labor_replacers)

    @labor_replacers.setter
    def labor_replacers(self, card_names):
        self._labor_replacers = []
        if card_names:
            for card_name in card_names:
                self._labor_replacers.append(CardName(card_name))

    @property
    def infinite_resource_sources(self):
        return list(self._infinite_resource_sources)

    @infinite_resource_sources.setter
    def infinite_resource_sources(self, card_names):
        self._infinite_resource_sources = []
        if card_names:
            for card_name in card_names:
                self._infinite_resource_sources.append(CardName(card_name))

    @property
    def finite_resource_sources(self):
        return list(self._temporary_resource_sources)

    @finite_resource_sources.setter
    def finite_resource_sources(self, card_names):
        self._temporary_resource_sources = []
        if card_names:
            for card_name in card_names:
                self._temporary_resource_sources.append(CardName(card_name))

    @property
    def finite_food_sources(self):
        return list(self._temporary_food_sources)

    @finite_food_sources.setter
    def finite_food_sources(self, card_names):
        self._temporary_food_sources = []
        if card_names:
            for card_name in card_names:
                self._temporary_food_sources.append(CardName(card_name))

    @property
    def food(self):
        return list(self._food)

    @food.setter
    def food(self, card_names):
        self._food = []
        if card_names:
            for card_name in card_names:
                self._food.append(CardName(card_name))

    @property
    def spoilable_food(self):
        return list(self._spoilable_food)

    @spoilable_food.setter
    def spoilable_food(self, card_names):
        self._spoilable_food = []
        if card_names:
            for card_name in card_names:
                self._spoilable_food.append(CardName(card_name))
