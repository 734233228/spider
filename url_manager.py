# 制作url存储器
class UrlManager:
    def __init__(self):
        self.new_url = set()
        self.old_url = set()
    def add_new_url(self,url):
        if url is None:
            return
        if url not in self.new_url and url not in self.old_url:
            self.new_url.add(url)

    def add_new_urls(self,urls):
        if len(urls) != 0 and urls:
            for url in urls:
                self.new_url.add(url)
        else:
            return None

    def has_new_url(self):
        return len(self.new_url) != 0

    def get_new_url(self):
        url = self.new_url.pop()
        self.old_url.add(url)
        return url
