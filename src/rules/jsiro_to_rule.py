from rules.cloudflare_rule import CloudflareRule

class JsiroToRule(CloudflareRule):
    def __init__(self) -> None:

        super().__init__(
            "jsiro.to",
            [
                "body > div:nth-child(2) > div > div > div.body.container.mb-3 > div.d-flex.flex-column.gap-2.mb-2 > div:nth-child(1) > div.bgg-dark.post-item > div > section > div > figure:nth-child(xxxx) > img.lazyload-preview"
            ],
            start_nth_child_index = 2
        )
