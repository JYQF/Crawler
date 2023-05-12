import requests
import pandas as pd
from requests.exceptions import RequestException
#爬取表格时新安装了pandas、html5lib、openpyxl库
#pandas可以将各种类型的数据（CSV、Excel、SQL数据库等）加载到Python中

def download_web(url):
    try:
        response = requests.get(url)
        # 判断HTTP响应状态码是否等于200 如果响应状态码为200说明请求成功，服务器已经返回了响应内容
        if response.status_code == 200:
            return response.text
        else:
            return "None"
    #如果在发送HTTP请求时出现异常，捕获并处理RequestException异常
    except RequestException as e:
        #异常对象 e 作为返回值返回，以提示调用者发生了异常，并且无法正常地获取响应内容
        return e

def get_excel(filename):
    html = download_web("http://fx.cmbchina.com/Hq/")
    #下载指定 URL 的 HTML 内容，并将其保存在 html 变量中
    cmb_table_list = pd.read_html(html)
    #解析 HTML 内容，并将结果存储在 cmb_table_list 变量中
    cmb_table_list[1].to_excel(filename)
    #确认需要的是第二个元素（下标为 1），并将其转换为 Excel 格式

def main():
    filename="test.xlsx"
    get_excel(filename)

if __name__ == '__main__':
    main()

