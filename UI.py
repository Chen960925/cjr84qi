from selenium import webdriver
import time
import requests
# driver=webdriver.Chrome()#选择Chorme浏览器 -- 跟浏览器建立会话==赋值给drive
# driver.implicitly_wait(10)#隐式等待==10s,如果元素提前出现，提前结束等待：10s后还没有出线，报错！==整个会话生效
# #1、打开具体的网址
# driver.get("http://baidu.com")
# #2、窗口最大化
# driver.maximize_window()
# #3、前进 后退 刷新
# driver.get("http://taobao.com")
# time.sleep(2) #等待=2s
# driver.forward()
# time.sleep(2)
# driver.back()
# time.sleep(2)
# driver.refresh()
# #4、关闭浏览器
# driver.close()#关闭当前的窗口
# driver.quit()#关闭整个浏览器
''''''
#页面的标题
# driver.get("http://erp.lemfix.com/login.html")
# title = driver.title #获取页面标题
# print(title)
# username=driver.find_element_by_id("username")#id 唯一
# username.send_keys("test123")#输入内容-用户名
# driver.find_element_by_id("password").send_keys("123456")#输入内容-密码
# driver.find_element_by_id("btnSubmit").click()#点击操作
# #判断是否登陆成功
# # time.sleep(2)
# username=driver.find_element_by_xpath("//p").text#获取元素的文本
# if username == "测试用户":
#     print("登陆用户是{}".format(username))
# else:
#     print("用例执行失败！")
# driver.find_element_by_xpath('//span[text()="零售出库"]').click()
# #寻找到了子页面，进行iframe的切换
# id = driver.find_element_by_xpath('//div[text()="零售出库"]/..').get_attribute("id")#获取元素的属性值
# frameid = id + "-frame"
# # driver.switch_to.frame(frameid)#通过id切换iframe子页面
# driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@id='{}']".format(frameid)))#通过元素定位来进行切换iframe
# #下面的代码都在子页面的
# driver.find_element_by_id("searchNumber").send_keys('448')
# driver.find_element_by_id("searchBtn").click()
# time.sleep(2)
# num=driver.find_element_by_xpath('//tr[@id="datagrid-row-r1-2-0"]//td[@field="number"]/div').text #获取它的文本
# if "448" in num:
#     print("搜索正确！")
# else:
#     print("搜索失败！")

url_baidu = "https://www.baidu.com/s"
head = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0"}
data_baidu={"wd":"柠檬班"}
resp = requests.get(url=url_baidu,headers=head,params=data_baidu)
# print(resp.text) #文本结果 -- 自动解码 -- 80%
print(resp.content.decode("utf8"))#手动指定解码方式
