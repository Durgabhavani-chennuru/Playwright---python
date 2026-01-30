
import pytest_playwright
from playwright.sync_api import Page, expect, Expect

import time

from pytest_playwright.pytest_playwright import browser


def test_Locators(page:Page):
    page.goto("https://rahulshettyacademy.com/client/#/auth/login")
    page.get_by_placeholder("email@example.com").fill("durgabhavanichennuru3@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Bhavani@123")
    page.get_by_role("button", name="login").click()

    Zara_product=page.locator("//div[4]//div[1]").filter(has_text="ZARA COAT 3") # tag css
    Zara_product.get_by_role("button",name=" Add To Cart").click()

    iphone_product=page.locator("(//div[@class='card'])[5]").filter(has_text="iphone 13 pro")
    iphone_product.get_by_role("button",name="Add To Cart").click()


    page.locator("//button[@routerlink='/dashboard/cart']").click() # CART LOCATOR IN SELECTOR HUB

    expect(page.locator(".cartWrap")).to_have_count(2)