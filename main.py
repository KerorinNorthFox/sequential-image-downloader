from image_dl import ImageDownloader


def main():
  p = ImageDownloader()
  
  p.load_urls("./urls.txt")
  p.load_json("./selector.json")

  p.download()


if __name__ == '__main__':
  main()