import requests
from playwright.sync_api import Playwright
from pytest_playwright.pytest_playwright import new_context
import re


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


#get data
def test_get_orders(playwright:Playwright):
    token = test_loginGetToken(playwright)
    api_get_request=playwright.request.new_context(base_url="https://rahulshettyacademy.com/client/")
    get_response=api_get_request.get("/api/ecom/order/get-orders-for-customer/688afe586f585eb60d51935f",
                                      headers={"Authorization":token,"Content-Type": "application/json"})
    #assert get_response.ok
    print(get_response)
    json_response=get_response.json()
    print(json_response)
    print(type(json_response))
    orders= json_response["data"]
    print(orders)
    for i in json_response["data"]:
        print(i['_id'])




































