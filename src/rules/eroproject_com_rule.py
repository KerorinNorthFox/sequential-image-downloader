from rules.id_required_rule import IdRequiredRule

class EroprojectComRule(IdRequiredRule):
    def __init__(self) -> None:
        super().__init__(
            "eroproject.com",
            [
                "#post-yyyy > div > section > a:nth-child(xxxx) > img"
            ],
            start_nth_child_index = 4
        )