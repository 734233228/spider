class HtmlOutputer:

    def __init__(self):
        self.datas = []

    # 把传进来的字典 放进list中
    def collect_data(self,data):
        if data is None:
            return
        self.datas.append(data)

    # 创建一个html并且把抓取到的数据显示出来
    def output_html(self):
        with open("spider.html", "w", encoding="utf-8") as f:
            f.write("<html>")
            f.write("<body>")
            f.write("<table>")
            # 列出 url、title、summary、
            for data in self.datas:
                f.write("<tr>")
                f.write("<td>%s</td>" % data['url'])
                f.write("<td>%s</td>" % data['title'])
                f.write("<td>%s</td>" % data['summary'])
                f.write("</tr>")
            f.write("</table>")
            f.write("</body>")
            f.write("</html>")


