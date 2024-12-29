from image_downloader import ImageDownloader, load_uris
import os

parent_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
save_dir = os.path.join(parent_dir, "save")

def main():
    p = ImageDownloader()

    uris = load_uris(os.path.join(parent_dir, "urls.txt"))

    for uri in uris:
        p.download(uri, save_dir)
        # TODO: ダウンロード終了したらurls.txtから完了したurlを削除する処理

if __name__ == '__main__':
    main()