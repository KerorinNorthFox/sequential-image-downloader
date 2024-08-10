import re
import os
import time
import json
import requests
from logger import Logger
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

from uri import URI

class ImageDownloader(object):
  def __init__(self) -> None:
    self.urls: list[URI] = []
    self.selector_json = {}
    self.logger = Logger()
  
  # txtファイルからURLを読み込む
  def load_urls(self, urls_list_path) -> None:
    with open(urls_list_path, mode="r", encoding="utf-8") as f:
      urls: list[str] = f.readlines()
      for url in urls:
        uri = URI(url)
        self.urls.append(uri)
  
  # jsonを読み込む
  def load_json(self, json_path) -> None:
    with open(json_path, mode="r", encoding="utf-8") as f:
      self.selector_json = json.load(f)
  
  def download(self):
    self.logger.info(f"The URL :{self.urls}")
    
    if self._check_urls(self.urls): quit(1)
    
    for uri in self.urls:
      time.sleep(0.5)
      print("\n================================")
      self.logger.info(f"url_structure:{uri.url_structure}\nprotocol     :{uri.protocol}\ndomain       :{uri.domain}\ndirectories  :{uri.directories}\nfile         :{uri.file}\n")
    
      res = self._request(uri.url)
      
      if res.status_code != 200 and res.status_code != 201:
        self.logger.error(f"Cannot connect -> status code:{res.status_code}")
        continue
      
      body = self._parse_html(res.text)
      
      i = 0
      json_obj = self.selector_json[uri.domain]
      selectors: list[str] = json_obj["selectors"]
      offset: int = json_obj["offset"]
      isNecessaryFileNumber: bool = json_obj["isNecessaryFileNumber"]
      
      space_directories_path = ""
      if uri.directories != []: # urlの間のディレクトリをパスにする
        for directory in uri.directories:
          space_directories_path += "/" + directory
          
      save_directory = f"./save/{uri.domain}{space_directories_path}/{uri.file if len(uri.file) < 30 else uri.file[0:29] }"
      dir_ban_words = ["?", "？", ":"]
      for dir_ban_word in dir_ban_words:
        save_directory = save_directory.replace(dir_ban_word, "")
      self.logger.info(f"save directory :{save_directory}")
      
      if not os.path.isdir(save_directory):
        self.logger.info(f"Try to create a directory : {save_directory}")
        os.makedirs(save_directory)
        self.logger.info(f"Created a directory {save_directory}")
      
      selector_number = 0
      while(True):
        time.sleep(0.1)
        self.logger.info(f"i={i}")
        
        selector = selectors[selector_number].replace("xxxx", str(i+offset))
        selector = selector.replace("yyyy", re.sub("\\D", "", uri.file)) if isNecessaryFileNumber else selector
        img = body.select(selector)
        
        if img == []:
          if selector_number+1 >= len(selectors):
            self.logger.error("img is not exist.")
            break
          selector_number += 1
          self.logger.warn("imt is not exist. Try another selector.")
          continue
        
        for attr in img[0].__dict__["attrs"]:
          if "src" in attr:
            key = attr
        src = img[0][key]
        src = src.split(" ")[0]
        if src == "" or src is None:
          self.logger.error(f"src is not exist.")
          continue
        self.logger.info(f"src={src}")
        
        file = f"{save_directory}/{i+1}.jpg"
        i += 1
        if os.path.exists(file):
          self.logger.warn(f"The file {file} is already exists. Skip it.")
          continue
        with open(file, mode="wb") as f:
          img_res = self._request(src)
          f.write(img_res.content)
        
  def _check_urls(self, urls: list[URI]):
    if urls == []:
      self.logger.error(f"The 'urls_list' is empty.")
      return True
    if [url for url in urls if not "http" in url.protocol] != []:
      self.logger.error("The 'urls_list' contains what is not url.")
      return True
    return False
  
  def _request(self, url: str):
    ua = UserAgent()
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15"}
    res = requests.get(url, headers=headers)
    return res
    
  def _parse_html(self, html_text: str):
    body = BeautifulSoup(html_text, "html.parser")
    return body