# -*-coding:utf-8 -*-
import requests

"""
下载图片

:return: 
"""
def download_image():
    url = "http://gb.cri.cn/mmsource/images/2013/08/27/17/16941621138191493501.jpg"
    respons = requests.get(url)
    print respons.status_code, respons.reason
    with open('tesp.png', 'wb') as fd:
        for chunk in respons.iter_content(128):
            fd.write(chunk)


if __name__ == '__main__':
    download_image()