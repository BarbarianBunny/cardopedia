from cardopedia.card_name import CardName
from cardopedia.group import Group
from cardopedia.group_name import GroupName


class Card:

    def __init__(self, name: str or CardName, groups: dict[str: list[str]] or dict[GroupName: list[CardName]] = None):
        self.name = name
        self.groups = groups

    def __iter__(self):
        if self.groups:
            for group in self.groups:
                yield group.name, group.card_names

    def __lt__(self, other):
        return self.name < other.name

    def __le__(self, other):
        return self.name <= other.name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = CardName(name)

    @property
    def groups(self):
        return self._groups

    @groups.setter
    def groups(self, groups: list[Group] or dict[GroupName: list[CardName]]):
        self._groups = []
        if groups:
            if isinstance(groups, dict):
                for group_name, card_names in groups.items():
                    self._groups.append(Group(group_name, card_names))
            elif isinstance(groups, list):
                for group in groups:
                    self._groups.append(group)

    def sort(self):
        self.groups.sort()

    def group(self, group_name, card_names=None):
        if any((group := check_group).name == group_name for check_group in self.groups):
            if card_names:
                group.card_names = card_names
            return group
        else:
            if card_names:
                self.groups.append(Group(group_name, card_names))
                return self.groups[-1]

    def html(self):
        group_html = []
        if self.groups:
            for group in self.groups:
                group_html.append(group.html())
        return f'{self.name.html_button()}<div class="card-content--hidden">{"".join(group_html)}</div>'
