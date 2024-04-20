import requests
from bs4 import BeautifulSoup
import os


def mkdir(path='data'):
    folder = os.path.exists(path)
    if not folder:
        print("--- 创建新的文件夹? ---")
        os.makedirs(path)
        print("--- OK ? ---")
    else:
        print("--- ⚠️ 文件夹已存在! ---")


def fetchHtml(url, headers):
    '''
    发起网络请求，获取网页源码
    '''

    r = requests.get(url, headers=headers)
    return r.text


def main(xhs_url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63"
    }

    page_text = fetchHtml(
        xhs_url, headers)
    soup = BeautifulSoup(page_text, 'html.parser')
    img_div = soup.select('meta')
    img_src_list = []
    for img in img_div:
        if "content" in img.attrs.keys() and img.attrs["content"][:5] == "http:":
            img_src_list.append(img.attrs["content"].split('/n')[0])

    index = 0
    mkdir()
    for url in img_src_list:
        index += 1
        fileurl = f"./data/tupian{index}.jpeg"
        print(url)
        r = requests.get(
            url, headers=headers)
        # print(r.content)
        with open(fileurl, 'wb') as f:
            f.write(r.content)


if __name__ == "__main__":
    main("https://www.xiaohongshu.com/explore/661b8366000000001a013bb5")
