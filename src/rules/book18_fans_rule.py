from rules.basic_rule import BasicRule

class Book18FansRule(BasicRule):
    def __init__(self) -> None:
        super().__init__(
            "book18.fans",
            [
                "#post-hentai > img:nth-child(xxxx)"
            ],
            start_nth_child_index = 1
        )