from rules.basic_rule import BasicRule

class DDDSmartNetRule(BasicRule):
    def __init__(self) -> None:
        super().__init__(
            "ddd-smart.net",
            [
                "#comic-area > img:nth-child(xxxx)"
            ],
            start_nth_child_index = 1
        )