from rules.basic_rule import BasicRule

class NyahentaiReRule(BasicRule):
    def __init__(self) -> None:
        super().__init__(
            "nyahentai.re",
            [
                "#post-comic > img:nth-child(xxxx)"
            ],
            start_nth_child_index = 1
        )