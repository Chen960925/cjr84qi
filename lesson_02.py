url_baidu = "https://www.baidu.com"
resp = requests.get(url=url_baidu)
print(resp.text) #文本结果 -- 自动解码
print(resp.content.decode("utf8"))