from rules.basic_rule import BasicRule

class WWWSexloveeroNetRule(BasicRule):
    def __init__(self) -> None:
        super().__init__(
            "www.sexloveero.net",
            [
                "#content > div > main > article > div > p:nth-child(xxxx) > a > img"
            ],
            start_nth_child_index = 1
        )