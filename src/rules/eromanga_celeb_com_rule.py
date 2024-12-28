from rules.basic_rule import BasicRule

class EromangaCelebComRule(BasicRule):
    def __init__(self) -> None:
        super().__init__(
            "eromanga-celeb.com",
            [
                "#article > div.article_inner > p > a:nth-child(xxxx) > img"
            ],
            start_nth_child_index = 1
        )