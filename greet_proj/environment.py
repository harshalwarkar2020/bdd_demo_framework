import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class MyContext:
    def __init__(self):
        self.shared_data = {}


def before_all(context):
    service = Service(executable_path=r"C:\Users\harshalashok_warkar\study_codes\bdd_demo\drivers\chromedriver.exe")
    options = webdriver.ChromeOptions()
    context.driver = webdriver.Chrome(service=service, options=options)
    context.my_context = MyContext()
    # time.sleep(8)
    # context.driver.maximize_window()


def after_All(context):
    context.driver.close()
    context.my_context.shared_data = {}


# def before_feature(context, feature):
#     service = Service(executable_path=r"C:\Users\harshalashok_warkar\study_codes\bdd_demo\drivers\chromedriver.exe")
#     options = webdriver.ChromeOptions()
#     context.driver = webdriver.Chrome(service=service, options=options)
#     context.driver.maximize_window()


# def after_feature(context, feature):
#     context.driver.close()

# def before_scenario(context, scenario):
#     service = Service(executable_path=r"C:\Users\harshalashok_warkar\study_codes\bdd_demo\drivers\chromedriver.exe")
#     options = webdriver.ChromeOptions()
#     context.driver = webdriver.Chrome(service=service, options=options)
#     context.driver.maximize_window()
#
#
# def after_scenario(context, scenario):
#     context.driver.close()



# def before_step(context, step):
#     service = Service(executable_path=r"C:\Users\harshalashok_warkar\study_codes\bdd_demo\drivers\chromedriver.exe")
#     options = webdriver.ChromeOptions()
#     context.driver = webdriver.Chrome(service=service, options=options)
#     context.driver.maximize_window()
#
#
# def after_step(context, step):
#     context.driver.close()
#
#
# def before_tag(context, tag):
#     service = Service(executable_path=r"C:\Users\harshalashok_warkar\study_codes\bdd_demo\drivers\chromedriver.exe")
#     options = webdriver.ChromeOptions()
#     context.driver = webdriver.Chrome(service=service, options=options)
#     context.driver.maximize_window()
#
#
# def after_tag(context, tag):
#     context.driver.close()




