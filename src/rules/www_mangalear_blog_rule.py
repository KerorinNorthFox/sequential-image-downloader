from rules.basic_rule import BasicRule

class WWWMangalearBlogRule(BasicRule):
    def __init__(self) -> None:
        super().__init__(
            "www.mangalear.blog",
            [
                "#the-content > p:nth-child(xxxx) > a > img"
            ],
            start_nth_child_index = 1
        )