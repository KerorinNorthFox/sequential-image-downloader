from bs4 import BeautifulSoup
from uri import Uri
from rules.rule import Rule
import requests
from logger import logger

"""
基本的な処理が実装されたルール
"""
class BasicRule(Rule):
    def __init__(self, domain:str, selectors:list[str], start_nth_child_index:int):
        self._domain = domain
        self._selectors = selectors
        self._start_nth_child_index = start_nth_child_index
    
    def __call__(self) -> str:
        return self._domain
        
    @property
    def selectors(self):
        return self._selectors
    
    @property
    def start_nth_child_index(self):
        return self._start_nth_child_index
        
    # uri先のサイトの縦に並べられた画像のurlをリストとして取得
    def collect_image_urls(self, uri: Uri) -> list[str]:
        image_urls: list[str] = []
        
        html = self.getHtml(uri)
        body = self.parseHtml(html)
        
        i = 0
        selector_number = 0
        try_again_limit = 2
        while(True):
            selectors: str = self.get_complete_selectors(i, uri)
            img = body.select(selectors[selector_number])
            
            if img == []:
                if try_again_limit <= 0:
                    logger.warn(f"img is not exist. Try again same selector. (try count :{try_again_limit})")
                    try_again_limit -= 1
                    i += 1
                    continue
                if selector_number+1 >= len(selectors):
                    logger.error("img is not exist.")
                    break
                logger.warn("img is not exist. Try another selector.")
                selector_number += 1
                continue
            
            src = self.get_image_src(img)
            if src == "" or src is None:
                logger.error("src is not exist.")
                continue
            logger.info(f"src :{src}")
            image_urls.append(src)
            i += 1
        
        return image_urls
    
    def request(self, url:str):
        headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15"}
        res = requests.get(url, headers=headers)
        return res
    
    # uri先のhtmlを取得
    def getHtml(self, uri:Uri) -> str:
        res = self.request(uri.url)
        if res.status_code != 200 and res.status_code != 201:
            raise Exception(f"Cannot connect -> status code:{res.status_code}")
        html = res.text
        return html
    
    # htmlをbeautifulsoupでパース
    def parseHtml(self, html:str):
        body = BeautifulSoup(html, "html.parser")
        return body
        
    def get_complete_selectors(self, i:int, uri) -> list[str]:
        return [selector.replace("xxxx", str(i+self._start_nth_child_index)) for selector in self._selectors]
    
    def get_image_src(self, img):
        for attr in img[0].__dict__["attrs"]:
            if "src" in attr:
                key = attr
        src = img[0][key]
        src = src.split(" ")[0]
        return src