from rules.id_required_rule import IdRequiredRule

class EromangaLifeComRule(IdRequiredRule):
    def __init__(self) -> None:
        super().__init__(
            "eromanga-life.com",
            [
                "#post-yyyy > div > div.entry-content > p:nth-child(xxxx) > a > img",
                "#post-yyyy > div > div.entry-content > p:nth-child(xxxx) > a > picture > img"
            ],
            start_nth_child_index = 6
        )