#-*- coding: utf-8-*-
import sys
reload(sys)
sys.setdef aultencoding('utf-8')
import unittest
from POimportLoginPage
from seleniumimport webdriver
classCaselogin126mail(unittest.TestCase):
"""
登录case
 """
@classmethod
def setUpClass(cls):
 cls.driver = webdriver.Chrome()
 cls.driver.implicitly_wait(30)
 
 cls.url ="http://xxxx.xxx.com"
 cls.username ="xxxxx"
 cls.password ="xxxxx"
 
#用例执行体
def test_login_mail(self):
#声明LoginPage类对象
login_page=LoginPage.LoginPage(self.driver, self.url, u”xxxxx”)
 
#调用打开页面组件
login_page.open()
#调用用户名输入组件
login_page.input_username(self.username)
#调用密码输入组件
login_page.input_password(self.password)
#调用点击登录按钮组件
login_page.click_submit()
@classmethod
def tearDownClass(cls):
 cls.driver.quit()
 
if __name__=="__main__":
 unittest.main()
