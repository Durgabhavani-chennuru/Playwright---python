
'''test case ->the orders page have orders but you have to test the condition
""You have No Orders to show at this time.
Please Visit Back Us""  without deleting the orders then use intercept concept(mocking the response) '''
from playwright.sync_api import Playwright, Page

fakePayLoadOrderResponse={"data":[],"message":"No Orders"}

def intercept_response(route):
    route.fulfill(json=fakePayLoadOrderResponse)

def test_network1(page:Page):
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/688afe586f585eb60d51935f",intercept_response)

    page.get_by_placeholder("email@example.com").fill("durgabhavanichennuru3@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Bhavani@123")
    page.get_by_role("button", name="login").click()
    page.get_by_role("button", name="ORDERS").click()

    no_order_text=page.locator("//div[@class='mt-4 ng-star-inserted']").text_content()
    print(no_order_text)



# this is one type of testing without intercept using api without UI
def test_loginGetToken(playwright:Playwright):
    api_request=playwright.request.new_context(base_url="https://rahulshettyacademy.com/client/")
    response=api_request.post("https://rahulshettyacademy.com/api/ecom/auth/login",
                              data={"userEmail": "durgabhavanichennuru3@gmail.com",
                                    "userPassword": "Bhavani@123"})

    assert response.ok
    print(response.json())
    response_body=response.json()["token"]
    print(response_body)
    return response_body

def test_no_orders_message(playwright: Playwright):
    token=test_loginGetToken(playwright)
    # Create API request context
    api_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com/client/")

    # Send GET request to Orders API
    response = api_context.get("/api/ecom/order/get-orders-for-customer/688afe586f585eb60d51935f",headers={"Authorization":token,"Content-Type": "application/json"})

    # Status code validation
    assert response.status == 200

    response_body = response.json()
    print(response_body)

    if len(response_body["data"]) >0:
        print(response_body["data"])
    else:
        print("You have No Orders to show at this time. Please Visit Back Us")

    # Validate no orders message
    #expected_message = "You have No Orders to show at this time. Please Visit Back Us"
    #assert response_body["message"] == expected_message



