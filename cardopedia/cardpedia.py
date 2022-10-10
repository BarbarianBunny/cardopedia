from cardopedia.card_name import CardName
from cardopedia.category import Category
from cardopedia.category_name import CategoryName
from cardopedia.group_name import GroupName


class Cardpedia:

    def __init__(self, categories: dict[str: dict[str: dict[str: list[str]]]] or
                                   dict[CategoryName: dict[CardName: dict[GroupName: list[CardName]]]] = None):
        self.categories = categories

    def __iter__(self):
        if self.categories:
            for category in self.categories:
                yield category.name, dict(category)

    @property
    def categories(self):
        return self._categories

    @categories.setter
    def categories(self,
                   categories: list[Category] or dict[CategoryName: dict[CardName: dict[GroupName: list[CardName]]]]):
        self._categories = []
        if isinstance(categories, dict):
            for category_name, cards in categories.items():
                self._categories.append(Category(category_name, cards))
        elif isinstance(categories, list):
            for category in categories:
                self._categories.append(category)

    def sort(self):
        self.categories.sort()
        if self.categories:
            for category in self.categories:
                category.sort()

    def category(self, category_name, cards=None):
        if any((category := check_category).name == category_name for check_category in self.categories):
            if cards:
                category.cards = cards
            return category
        else:
            self.categories.append(Category(category_name, cards))
            return self.categories[-1]

    def html(self):
        category_html = []
        if self.categories:
            for category in self.categories:
                category_html.append(category.html())
        return f'{self.html_pre_body()}{"".join(category_html)}{self.html_post_body()}'

    @staticmethod
    def html_pre_body():
        return f'<!DOCTYPE html>' \
               '<html lang="en">' \
               '<head>' \
               '<meta charset="utf-8" />' \
               '<meta name="viewport" content="width=device-width, initial-scale=1" />' \
               '<link rel="stylesheet" href="styles/cardopedia.css" />' \
               '<title>Cardopedia</title>' \
               '<script src="scripts/jquery.js"></script>' \
               '<script src="scripts/toggle.js"></script>' \
               '<!-- ****** faviconit.com favicons ****** -->' \
               '<link rel="shortcut icon" href="icons/cardopedia.ico">' \
               '<link rel="icon" sizes="16x16 32x32 64x64" href="icons/cardopedia.ico">' \
               '<link rel="icon" type="image/png" sizes="196x196" href="icons/cardopedia-192.png">' \
               '<link rel="icon" type="image/png" sizes="160x160" href="icons/cardopedia-160.png">' \
               '<link rel="icon" type="image/png" sizes="96x96" href="icons/cardopedia-96.png">' \
               '<link rel="icon" type="image/png" sizes="64x64" href="icons/cardopedia-64.png">' \
               '<link rel="icon" type="image/png" sizes="32x32" href="icons/cardopedia-32.png">' \
               '<link rel="icon" type="image/png" sizes="16x16" href="icons/cardopedia-16.png">' \
               '<link rel="apple-touch-icon" href="icons/cardopedia-57.png">' \
               '<link rel="apple-touch-icon" sizes="114x114" href="icons/cardopedia-114.png">' \
               '<link rel="apple-touch-icon" sizes="72x72" href="icons/cardopedia-72.png">' \
               '<link rel="apple-touch-icon" sizes="144x144" href="icons/cardopedia-144.png">' \
               '<link rel="apple-touch-icon" sizes="60x60" href="icons/cardopedia-60.png">' \
               '<link rel="apple-touch-icon" sizes="120x120" href="icons/cardopedia-120.png">' \
               '<link rel="apple-touch-icon" sizes="76x76" href="icons/cardopedia-76.png">' \
               '<link rel="apple-touch-icon" sizes="152x152" href="icons/cardopedia-152.png">' \
               '<link rel="apple-touch-icon" sizes="180x180" href="icons/cardopedia-180.png">' \
               '<meta name="msapplication-TileColor" content="#FFFFFF">' \
               '<meta name="msapplication-TileImage" content="icons/cardopedia-144.png">' \
               '<meta name="msapplication-config" content="icons/browserconfig.xml">' \
               '<!-- ****** faviconit.com favicons ****** -->' \
               '</head>' \
               '<body>'

    @staticmethod
    def html_post_body():
        return f'</body></html>'
