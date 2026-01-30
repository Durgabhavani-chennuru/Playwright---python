import pytest_playwright
from playwright.sync_api import Page, expect, Expect

import time

from pytest_playwright.pytest_playwright import browser
def test_UIValidationDynamicScript(page:Page):
    #iphone X, Nokia Edge ->verify 2 items are showing in cart
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()
    iphoneProduct= page.locator("app-card").filter(has_text="iphone X")
    iphoneProduct.get_by_role("button").click()
    nokiaProduct = page.locator("app-card").filter(has_text="Nokia Edge")
    nokiaProduct.get_by_role("button").click()
    page.get_by_text("checkout").click()
    expect(page.locator(".media-body")).to_have_count(2)
    time.sleep(5)



def test_childwindow(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    # by using locator
    #page.locator("//a[contains(text(),'Free Access to')]").click()
    # page.locator(".blinkingText").click()

    with page.expect_popup() as newPage_Info:
        # by using link
        page.get_by_role("link", name="Free Access to InterviewQues/ResumeAssistance/Material").click()  # new page
        child_page=newPage_Info.value
        text = child_page.locator(".im-para.red").inner_text()
        email = text.split("at ")[1].split(" ")[0]
        print(email)

        assert email == 'mentor@rahulshettyacademy.com'

        '''text=child_page.locator(".im-para.red").text_content()
        print(text) # Please email us at mentor@rahulshettyacademy.com with below template to receive response
        words = text.split("at")
        # 0-> Please email us  1-> mentor@rahulshettyacademy.com with below template to receive response
        email = words[1].split(" ")[0] # 0-> mentor@rahulshettyacademy.com 1-> with below template to receive response
        print(email)'''











#page.wait_for_timeout(5000)  # observe next page













