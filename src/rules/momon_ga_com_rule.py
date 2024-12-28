from rules.basic_rule import BasicRule

# momon-ga.com
class MomonGaComRule(BasicRule):
    def __init__(self) -> None:
        super().__init__(
            "momon-ga.com",
            [
                "#post-hentai > img:nth-child(xxxx)"
            ],
            start_nth_child_index = 2
        )
