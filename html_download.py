import urllib.request
from urllib.parse import quote
import  string

class HtmlDownload:

    # 下载html
    def download(self,url):
        if url is None:
            return
        url = quote(url, safe=string.printable) # url 中文转换
        resqonse = urllib.request.urlopen(url) # 打开 url
        if resqonse.getcode() != 200:  # 判断打开是否成功
            return None
        return resqonse.read() # 下载