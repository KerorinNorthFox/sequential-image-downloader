from rules.rules import RULES
from rules.rule import Rule
from uri import Uri
from logger import logger
import os

"""
テキストファイルからuriを読み込む
"""
def load_uris(url_txt_path:str) -> list[Uri]:
    with open(url_txt_path, mode="r", encoding="utf-8") as f:
        urls: list[str] = f.readlines()
        return [Uri(url) for url in urls]

class ImageDownloader(object):
    def download(self, uri:Uri, save_dir:str):
        logger.info(f"The Url :{uri()}")
        
        if self._check_uri(uri): quit(1)
        
        print("\n================================")
        logger.info(f"\nurl_structure:{uri.url_structure}\nprotocol     :{uri.protocol}\ndomain       :{uri.domain}\ndirectories  :{uri.directories}\nfile         :{uri.file}\n")
        
        rule: Rule = self._get_selector_rule(uri.domain)
        image_urls: list[str] = rule.collect_image_urls(uri)
        
        complete_save_dir = self._combine_save_dir(save_dir, uri)
        
        for i, image_url in enumerate(image_urls):
            save_path = os.path.join(complete_save_dir, f"{i+1}.jpg")
            if os.path.exists(save_path):
                logger.warn(f"The file is already exists. Skip it.")
                continue
            
            with open(save_path, mode="wb") as f:
                img_res = rule.request(image_url)
                f.write(img_res.content)
                logger.info(f"{image_url} Download completed.")
    
    """
    uriをチェックする
    1.uriにhttpが含まれているか
    """
    def _check_uri(self, uri: Uri):
        if not "http" in uri.protocol:
            logger.error("Given uri is not url")
            return True
        return False
    
    """
    ドメインに対応するパースルールを取得
    """
    def _get_selector_rule(self, domain:str) -> Rule:
        for rule in RULES:
            if domain == rule():
                return rule
    
    def _combine_save_dir(self, save_path, uri) -> str:
        space_directories_path = ""
        if uri.directories != []: # urlの間のディレクトリをパスにする
            for directory in uri.directories:
                space_directories_path += "/" + directory
                
        save_directory_leaf = f"{uri.domain}{space_directories_path}/{uri.file if len(uri.file) < 30 else uri.file[0:29] }"
        
        dir_ban_words = ["?", "？", ":"]
        for dir_ban_word in dir_ban_words:
            save_directory_leaf = save_directory_leaf.replace(dir_ban_word, "")
            
        save_directory = os.path.join(save_path, save_directory_leaf)
            
        logger.info(f"save directory :{save_directory}")
        
        if not os.path.isdir(save_directory):
            logger.info(f"Try to create a directory : {save_directory}")
            os.makedirs(save_directory)
            logger.info(f"Created a directory {save_directory}")
            
        return save_directory
            