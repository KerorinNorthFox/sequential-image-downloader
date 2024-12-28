from rules.id_required_rule import IdRequiredRule

class EromangaKiwamiComRule(IdRequiredRule):
    def __init__(self) -> None:
        super().__init__(
            "eromanga-kiwami.com",
            [
                "#post-yyyy > div > section > p:nth-child(xxxx) > img"
            ],
            start_nth_child_index = 1
        )