from behave import *
from selenium.webdriver.common.by import By

import logging

logging.basicConfig(level=logging.INFO)  # Set the logging level
logger = logging.getLogger(__name__)


@given(u': User is on Registration page')
def step_impl(context):
    context.driver.get("https://www.thetestingworld.com/testings/")
    # print("$$$$$$$$$$$$$", context.my_context.shared_data['name'])
    # assert context.my_context.shared_data['name'] == "Vijay"
    # logger.info("#########", context.my_context.shared_data['name'])


@when(u': User entered username')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[@name='fld_username']").send_keys("Har")
    context.my_context.shared_data["page"] = "registration page"


@when(u': User entered email id')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[@name='fld_email']").send_keys("Har@gmail.com")
    current_page = context.my_context.shared_data.get("page")
    logger.info("User is on the:- {}".format(current_page))


@when(u': User entered password')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[@name='fld_password']").send_keys("har@1234")


@when(u': User click on signup button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[@type='submit']").click()


@then(u': User should be registered successfully')
def step_impl(context):
    print("Registered")
    assert False

