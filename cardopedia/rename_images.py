import os

from cardopedia.card_name import CardName
from cardopedia.kebab_case import kebab_case

os.getcwd()
collection = "C:/Users/carur/IdeaProjects/cardopedia/webpage/images"

card_name = CardName
card_names = [card.name for card in card_name]
card_names = card_names[15:]


for i, filename in enumerate(os.listdir(collection)):
    os.rename(collection + "/" + filename, collection + "/" + kebab_case(filename) + ".png")
