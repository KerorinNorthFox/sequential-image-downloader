from uri import Uri
from rules.basic_rule import BasicRule
from DrissionPage import ChromiumPage
import time

class JsiroToRule(BasicRule):
    def __init__(self) -> None:

        super().__init__(
            "jsiro.to",
            [
                "body > div:nth-child(2) > div > div > div.body.container.mb-3 > div.d-flex.flex-column.gap-2.mb-2 > div:nth-child(1) > div.bgg-dark.post-item > div > section > div > figure:nth-child(xxxx) > img.lazyload-preview"
            ],
            start_nth_child_index = 2
        )
        
    def getHtml(self, uri: Uri) -> str:
        page = ChromiumPage()
        page.get(uri.url)
        time.sleep(2.5) # 認証画面をgetしてしまうので2.5秒スリープ
        html = page.html
        page.quit()
        return html