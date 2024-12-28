from rules.basic_rule import BasicRule

class NijigenDaiaruComRule(BasicRule):
    def __init__(self) -> None:
        super().__init__(
            "nijigen-daiaru.com",
            [
                "#container > div > div.main-column-inner > div.autopagerize_page_element > article:nth-child(8) > div > div.article-body > div > div.main_contents > p > a:nth-child(xxxx) > img"
            ],
            start_nth_child_index = 1
        )