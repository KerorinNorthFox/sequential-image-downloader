from rules.id_required_rule import IdRequiredRule

class HentaiBooksComRule(IdRequiredRule):
    def __init__(self) -> None:
        super().__init__(
            "hentai-books.com",
            [
                "#post-yyyy > section > a:nth-child(xxxx) > img"
            ],
            start_nth_child_index = 2
        )