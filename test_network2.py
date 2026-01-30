import time

from playwright.sync_api import Page

from test_interceptNetwork1 import intercept_response

# search others order id in my account it gives-> you are not authorized to view
def intercept_request(route):
    #others url
    route.continue_(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=697891d7c941646b7abc8332")


def test_network1(page:Page):
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*",intercept_request)

    page.get_by_placeholder("email@example.com").fill("durgabhavanichennuru3@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Bhavani@123")
    page.get_by_role("button", name="login").click()
    page.get_by_role("button", name="ORDERS").click()
    page.get_by_role("button",name="View").first.click()

    message=page.locator(".blink_me").text_content()
    print(message)
    time.sleep(5)




