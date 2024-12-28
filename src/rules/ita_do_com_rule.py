from rules.basic_rule import BasicRule

class ItaDoComRule(BasicRule):
    def __init__(self) -> None:
        super().__init__(
            "ita-do.com",
            [
                "#ColumnL > article > div.box.singleBox > p:nth-child(xxxx) > img"
            ],
            start_nth_child_index = 1
        )