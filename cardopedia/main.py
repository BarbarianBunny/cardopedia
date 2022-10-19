import os
from cardopedia.cardpedia import Cardpedia
from cardopedia.generate_groups.generate_makes import generate_makes
from cardopedia.generate_groups.generate_sources import generate_sources
from cardopedia.populate_cards.populate_fish import populate_fish
from cardopedia.populate_cards.populate_food import populate_food
from cardopedia.populate_cards.populate_humans import populate_humans
from cardopedia.populate_cards.populate_ideas import populate_ideas
from cardopedia.populate_cards.populate_locations import populate_locations
from cardopedia.populate_cards.populate_mobs import populate_mobs
from cardopedia.populate_cards.populate_packs import populate_packs
from cardopedia.populate_cards.populate_resources import populate_resources
from cardopedia.populate_cards.populate_rumors import populate_rumors
from cardopedia.populate_cards.populate_structures import populate_structures

cardpedia = Cardpedia()

populate_packs(cardpedia)
populate_structures(cardpedia)
populate_humans(cardpedia)
populate_resources(cardpedia)
populate_ideas(cardpedia)
populate_food(cardpedia)
populate_mobs(cardpedia)
populate_locations(cardpedia)
populate_fish(cardpedia)
populate_rumors(cardpedia)

generate_sources(cardpedia)
generate_makes(cardpedia)

cardpedia.sort()

html = cardpedia.html()

dirname = os.path.dirname(__file__)

with open(os.path.join(dirname, "..", "webpage", "index.html"), "w") as f:
    f.write(html)