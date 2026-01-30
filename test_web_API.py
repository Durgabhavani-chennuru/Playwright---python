import time
from venv import create

from playwright.sync_api import Playwright, expect
from pytest_playwright.pytest_playwright import browser

from utils.apiBase import APIUtils
from utils.apiBase import APIUtils

#placing an order by using api in 1 sec . yeah we can also place an order through ui but its taking 4 or 5 sec
# like login-> add to cart,check out,place order

def test_placeOrder(playwright:Playwright):
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()

    #create order->order_id
    # we call the class in apibase

    api_utils=APIUtils()  # api_utils is object
    order_id=api_utils.createOrder(playwright)

    #login
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_placeholder("email@example.com").fill("durgabhavanichennuru3@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Bhavani@123")
    page.get_by_role("button",name="login").click()

    page.get_by_role("button",name="ORDERS").click()

    #order history page -> order is present
    row=page.locator("tr").filter(has_text=order_id)
    row.get_by_role("button",name="View").click()
    expect(page.locator(".tagline")).to_contain_text("Thank you for Shopping With Us")
    context.close()


    #page.wait_for_timeout(5000)# observe next page


