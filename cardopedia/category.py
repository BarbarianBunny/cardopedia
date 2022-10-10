from cardopedia.card import Card
from cardopedia.card_name import CardName
from cardopedia.category_name import CategoryName
from cardopedia.group_name import GroupName


class Category:

    def __init__(self, name: str or CategoryName,
                 cards: dict[str: dict[str: list[str]]] or dict[CardName: dict[GroupName: list[CardName]]] = None):
        self.name = name
        self.cards = cards

    def __iter__(self):
        if self.cards:
            for card in self.cards:
                yield card.name, dict(card)

    def __lt__(self, other):
        return self.name < other.name

    def __le__(self, other):
        return self.name <= other.name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = CategoryName(name)

    @property
    def cards(self):
        return self._cards

    @cards.setter
    def cards(self, cards: list[Card] or dict[CardName: dict[GroupName: list[CardName]]]):
        self._cards = []
        if isinstance(cards, dict):
            for card_name, groups in cards.items():
                self._cards.append(Card(card_name, groups))
        elif isinstance(cards, list):
            for card in cards:
                self._cards.append(card)

    def sort(self):
        self.cards.sort()
        if self.cards:
            for card in self.cards:
                card.sort()

    def card(self, card_name, groups=None):
        if any((card := check_card).name == card_name for check_card in self.cards):
            if groups:
                card.groups = groups
            return card
        else:
            self.cards.append(Card(card_name, groups))
            return self.cards[-1]

    def html(self):
        card_html = []
        if self.cards:
            for card in self.cards:
                card_html.append(card.html())
        if self.name != CategoryName.ideas:
            return f'{self.name.html_button()}<div class="category-content">{"".join(card_html)}</div>'
        else:
            return f'{self.name.html_button()}<div class="category-content--hidden">{"".join(card_html)}</div>'
