import time


from playwright.sync_api import Page, expect


def test_Tables(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    loc=page.locator("//table[@name='BookTable']/tbody/tr[3]/td[2]")  # ctrl +f enter
    expect(loc).to_contain_text("Mukesh")
    time.sleep(3)

    # another way using loop concept not hardcode
    rows=page.locator("//table[@name='BookTable']/tbody/tr").count()
    columns= page.locator("//table[@name='BookTable']/tbody/tr/th").count()
    for r in range(2,rows+1):
        for c in range(1,columns+1):
            value=page.locator("//table[@name='BookTable']/tbody/tr["+ str(r) +"]/td["+ str(c) +"]").text_content()
            if value=="Mukesh":
                value1 = page.locator("//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[" + str(c) + "]")
                expect(value1).to_contain_text("Mukesh")
                break





















