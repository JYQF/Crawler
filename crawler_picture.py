import urllib3
from bs4 import BeautifulSoup
from urllib.request import urlretrieve

# 下载网页，返回网页内容
def download_web(url):
	http = urllib3.PoolManager()
	response = http.request("GET", url)
	response_data = response.data
	html_content = response_data.decode()
	return html_content

#将字符串内容保存到文件中
def saveContent(filename, content):
	#filename要保存的文件名，content要保存的字符串内容的变量
	fo = open(filename, "w", encoding="utf-8")
	fo.write(content)
	fo.close()

#得到BeautifulSoup对象 用于下一步解析
def get_beautifulsoup(filename):
	#输入要分析的html文件名，返回值为对应的BeautifulSoup对象
	fo = open(filename, "r", encoding='utf-8')
	html_content = fo.read()
	fo.close()
	doc = BeautifulSoup(html_content, "lxml")
	return doc

def parse_html(doc):
	images = doc.find_all("img")
	for i in images:
		src = i["src"]
		filename = src.split("/")[-1]
		# print(i["src"])
		urlretrieve(src, "images/" + filename)
#类似于爬取数据
def main():
	filename = "test_picture.html.html"
	url = "https://www.duitang.com/blogs/tag/?name=%E5%BE%AE%E5%8D%9A%E7%94%B5%E8%84%91%E7%89%88%E5%A3%81%E7%BA%B8"
	#url = "https://www.sohu.com/a/451545597_669338"
	result = download_web(url)
	saveContent(filename, result)
	doc = get_beautifulsoup(filename)
	parse_html(doc)

if __name__ == '__main__':
	main()