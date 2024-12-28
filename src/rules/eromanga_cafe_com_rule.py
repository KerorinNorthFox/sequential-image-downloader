from rules.id_required_rule import IdRequiredRule

class EromangaCafeComRule(IdRequiredRule):
    def __init__(self) -> None:

        super().__init__(
            "eromanga-cafe.com",
            [
                "#post-yyyy > div.kijibox > p:nth-child(xxxx) > a > img",
                "#post-yyyy > div.kijibox > p:nth-child(xxxx) > a > picture > img",
                "#post-yyyy > p:nth-child(xxxx) > a > img"
            ],
            start_nth_child_index = 11
        )