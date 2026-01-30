from time import process_time_ns

import pytest_playwright
from playwright.sync_api import Page, expect

import time

from pytest_playwright.pytest_playwright import browser
def test_MoreValidations(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")

    page.locator("input[value='radio2']").check()
    assert page.is_checked("input[value='radio2']")
    print("radio button is selected successfully")


    page.select_option("#dropdown-class-example", value="option2")
    selected=page.locator("#dropdown-class-example").input_value()
    assert selected=="option2"
    print("successfull")

    page.locator("#checkBoxOption2").check()
    assert page.is_checked("#checkBoxOption2")
    print("selected")

    page.get_by_role("button", name="Open Window").click()
    assert page.get_by_role("button",name="Open Window")
    print("window successfuly opened")

    #hide/display placeholder
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_role("button", name="Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()

    # AlertBoxes
    page.on("dialog", lambda dialog: dialog.accept())  # lambda is like a function in one line
    page.get_by_role("button", name="Confirm").click()
    time.sleep(4)
    page.on("dialog", lambda dialog: dialog.accept())
    page.get_by_role("button", name="Alert").click()

    # MouseHover
    page.locator("#mousehover").hover()
    page.get_by_role("link", name="Top").click()

    # Frame Handing -> frame inside a page
    pageFrame = page.frame_locator("#courses-iframe")
    pageFrame.get_by_role("link", name="All Access plan").click()
    expect(pageFrame.locator("body")).to_contain_text("Happy Subscibers!")
    time.sleep(3)
















