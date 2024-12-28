from rules.basic_rule import BasicRule

class NukibooksComRule(BasicRule):
    def __init__(self) -> None:
        super().__init__(
            "nukibooks.com",
            [
                "body > main > div.container > div.container.article-page-list > img:nth-child(xxxx)"
            ],
            start_nth_child_index = 1
        )