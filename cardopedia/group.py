from cardopedia.card_name import CardName
from cardopedia.group_name import GroupName


class Group:

    def __init__(self, name: str or GroupName, card_names: list[str] or list[CardName]):
        self.name = name
        self.card_names = card_names

    def __lt__(self, other):
        return self.name < other.name

    def __le__(self, other):
        return self.name <= other.name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = GroupName(name)

    @property
    def card_names(self):
        return self._card_names

    @card_names.setter
    def card_names(self, card_names):
        self._card_names = []
        if card_names:
            for card_name in card_names:
                self._card_names.append(CardName(card_name))

    def html(self):
        card_links = []
        if self.card_names:
            for card_name in self.card_names:
                card_links.append(card_name.html_link())
        return f'{self.name.html_button()}<div class="group-content">{"".join(card_links)}</div>'
