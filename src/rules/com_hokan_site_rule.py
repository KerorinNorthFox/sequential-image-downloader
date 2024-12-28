from rules.id_required_rule import IdRequiredRule

class ComHokanSiteRule(IdRequiredRule):
    def __init__(self) -> None:
        super().__init__(
            "com-hokan.site",
            [
                "#post-yyyy > div.entry-content.cf > figure > ul > li:nth-child(xxxx) > figure > a > img"
            ],
            start_nth_child_index = 1
        )