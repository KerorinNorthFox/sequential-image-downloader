from rules.id_required_rule import IdRequiredRule

class HimebonBlogRule(IdRequiredRule):
    def __init__(self) -> None:
        super().__init__(
            "himebon.blog",
            [
                "#post-yyyy > div.entry-content.cf.iwe-border-bold > p:nth-child(xxxx) > a > img"
            ],
            start_nth_child_index = 2
        )