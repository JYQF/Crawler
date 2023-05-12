import requests
from bs4 import BeautifulSoup
#requests库 HTTP库 允许发送各种HTTP请求，处理响应
#beautifulsoup4库 解析操作HTML或XML文档 提取所需数据

#安装requests库和beautifulsoup4库
#使用BeautifulSoup解析HTML文档时，它依赖于一个底层的解析器库来解析文档
#需要安装一个支持更多功能的解析器库，lxml（在函数get_beautifulsoup中用到）

#下载网页 返回网页内容
def download_web(url):
    #url要下载的网页网址
    response = requests.get(url).text
    #通过使用.text 属性，我们可以获得响应内容的文本表示形式，一个字符串。
    return response


#将字符串内容保存到文件中
def saveContent(filename, content):
    #filename要保存的文件名，content要保存的字符串内容的变量
    with open(filename, mode="w", encoding="utf-8") as f:
        #write方法将content内容写入文件
        f.write(content)

#得到BeautifulSoup对象 用于下一步解析
def get_beautifulsoup(filename):
    #输入要分析的html文件名，返回值为对应的 BeautifulSoup 对象
    with open(filename, "r", encoding='utf-8') as f:
        content = f.read()
        #要安装解析器库lxml
        soup = BeautifulSoup(content, "lxml")
    return soup

#从HTML文档中解析信息
def parse(soup):
    #使用find_all方法 查找HTML文档中所有class属性为app的div元素
    post = soup.find_all("div", class_="app")
    #循环列表,对每个元素查找其中所有的a标签
    for i in post:
        link = i.find_all("a")[1]
        """
        此处使用 [1] 索引而不是 [0]，是因为在 HTML 中，
        每个 div 元素中都包含两个 a 标签元素，而我们只需要第二个标签中的信息。
        如果使用 [0] 索引，则会获得第一个 a 标签元素
        """
        #打印文本和超链接
        print(link.text.strip())
        print(link["href"])


def main():
    #输入想要爬取的网页地址
    url = "https://tianchi.aliyun.com/dataset/"
    #存储爬取数据的文件名
    filename = "aliyun.html"
    #调用第一个函数 下载网页 返回内容
    result = download_web(url)
    #将字符串内容保存到文件中
    saveContent("aliyun.html", result)
    soup = get_beautifulsoup(filename)
    #解析信息
    parse(soup)

if __name__ == '__main__':
    main()