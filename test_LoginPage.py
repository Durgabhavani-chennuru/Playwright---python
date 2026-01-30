

import pytest_playwright
from playwright.sync_api import Page, expect

import time

from pytest_playwright.pytest_playwright import browser

def test_LoginPage(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("consult")
    page.locator("#terms").check()# css id
    page.get_by_role("link",name="terms and conditions")
    page.get_by_role("button",name="Sign In").click()
    #expect(page.get_by_text("Incorrect username/password.")).to_be_visible()
    time.sleep(3)




