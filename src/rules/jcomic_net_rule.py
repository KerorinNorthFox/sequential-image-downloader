from rules.basic_rule import BasicRule

class JcomicNetRule(BasicRule):
    def __init__(self) -> None:
        super().__init__(
            "jcomic.net",
            [
                "body > div.container > div.row.col-lg-12.col-md-12.col-xs-12 > img:nth-child(xxxx)"
            ],
            start_nth_child_index = 2
        )