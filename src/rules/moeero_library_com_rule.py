from rules.id_required_rule import IdRequiredRule

class MoeeroLibraryComRule(IdRequiredRule):
    def __init__(self) -> None:

        super().__init__(
            "moeero-library.com",
            [
                "#post-yyyy > div.kijibox > p:nth-child(xxxx) > a > img",
                "#post-yyyy > div.kijibox > p:nth-child(xxxx) > a > picture > img",
                "#post-yyyy > div.kijibox > p:nth-child(xxxx) > img"
            ],
            start_nth_child_index = 4
        )