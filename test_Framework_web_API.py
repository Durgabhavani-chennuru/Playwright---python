import json
import time
from venv import create

import pytest
from playwright.sync_api import Playwright, expect, Page
from pytest_playwright.pytest_playwright import browser

from pageObject import dashboard
from pageObject.dashboard import DashboardPage
from pageObject.login import LoginPage
from utils.apiBase import APIUtils
from utils.apiBaseFrameWork import APIUtils

#JSON file  -> util ->access into test.

with open('data/credentials.json') as f:
    test_data = json.load(f)
    print(test_data)
    user_credentials_list = test_data['user_credentials']

@pytest.mark.parametrize("user_credentials",user_credentials_list) #-->annotation we have different login detais here we are taking one by one user credentials
def test_placeOrder(playwright:Playwright,browserInstance, user_credentials):
    userName=user_credentials["userEmail"]
    password = user_credentials["userPassword"]


    #create order->order_id
    # we call the class in apibase
    api_utils=APIUtils()  # api_utils is object
    order_id=api_utils.createOrder(playwright,user_credentials)

    #login page
    loginPage=LoginPage(browserInstance)  #object for loginPage class
    loginPage.navigate()
    dashboardPage=loginPage.login(userName,password)

    #Dashboard page
    orderHistoryPage=dashboardPage.selectOrdersNavLink()
    orderDetailsPage=orderHistoryPage.selectOrder(order_id)
    orderDetailsPage.verifyOrderMessage()


    #order history page -> order is present

#page.wait_for_timeout(5000)# observe next page

#html report generation  ->  pip install pytest-html-> pytest -n 3 --html=report.html