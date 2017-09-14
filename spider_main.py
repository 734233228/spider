from baike_spider import url_manager, html_download, html_parser, html_outputer


class SpiderMain:
    def __init__(self):
        self.url = url_manager.UrlManager()
        self.download = html_download.HtmlDownload()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()
    def craw(self,root_url):
        self.url.add_new_url(root_url)
        count = 1
        try:
            while self.url.has_new_url():
                new_url = self.url.get_new_url()
                print("%d:%s" % (count,new_url))
                html_cont = self.download.download(new_url)
                urls,data = self.parser.parse(new_url, html_cont)
                self.url.add_new_urls(urls)
                self.outputer.collect_data(data)
                if count == 10:
                    break
                count += 1
        except:
            print("craw failed")
        return self.outputer.output_html()

if __name__ == '__main__':
    root_url = 'https://baike.baidu.com/item/Python/407313?fr=aladdin'
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)