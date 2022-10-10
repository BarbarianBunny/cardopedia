from cardopedia import kebab_case


class KebabCase:

    def title_case(self):
        assert kebab_case.kebab_case("Kebab Case") == "kebab-case"

    def snake_case(self):
        assert kebab_case.kebab_case("kebab_case") == "kebab-case"

    def idea(self):
        assert kebab_case.kebab_case("Idea: Kebab Case") == "idea-kebab-case"

    def idea_warped(self):
        assert kebab_case.kebab_case("idea_-_Kebab_Case") == "idea-kebab-case"
