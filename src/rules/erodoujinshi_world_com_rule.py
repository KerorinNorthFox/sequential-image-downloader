from rules.id_required_rule import IdRequiredRule

class ErodoujinshiWorldComRule(IdRequiredRule):
    def __init__(self) -> None:
        super().__init__(
            "erodoujinshi-world.com",
            [
                "#post-yyyy > section > div.content > p:nth-child(xxxx) > a > img"
            ],
            start_nth_child_index = 3
        )