

from playwright.sync_api import Playwright,Page,expect, sync_playwright
import time
import re

def test_webTable1(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    table = page.locator("//table[@name='BookTable']/tbody")
    rows = table.locator("//tr")
    row_count = rows.count()
    cols=table.locator("//th")
    cols_count=cols.count()
    print("This is row count:",row_count)
    print(f"This is column count :{cols_count}")
    # value=page.locator("//table[@name='BookTable']/tbody/tr[2]/td[1]")
    # expect(value).to_contain_text("Learn Selenium")
    price_count = 0
    for r in range(2,row_count+1):
        #for c in range(1,cols_count+1):
        #value= page.locator("//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[" + str(c) + "]").text_content()
        Price_val= page.locator("//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[4]").text_content()
        if int(Price_val) >=1000:
            price_count=price_count+1
            print(Price_val)

    print(f"number of books greater than 1000 is :{price_count}")


#  i need a selenium count in a table
def test_count(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    table=page.locator("//table[@name='BookTable']/tbody")
    row_count=page.locator("//table[@name='BookTable']/tbody/tr").count()
    print("row count", {row_count})
    subject_count=0
    for r in range(2,row_count+1):
        subject_val=page.locator("//table[@name='BookTable']/tbody/tr["+ str(r) +"]/td[3]").text_content()
        if str(subject_val)=="Selenium":
            print(subject_val)
            subject_count=subject_count+1
    print("selenium subject count is " ,subject_count)















