from multiprocessing.managers import Token

from playwright.sync_api import Playwright
from pytest_playwright.pytest_playwright import browser


orderPayLoad= {"orders": [{"country": "india", "productOrderedId": "6964af52c941646b7a919472"}]}



class APIUtils:
    def getToken(self, playwright:Playwright,user_credentials):
        user_email=user_credentials['userEmail']
        user_Password = user_credentials['userPassword']
        api_request_context=playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response=api_request_context.post("api/ecom/auth/login",
                                 data={"userEmail": user_email , "userPassword":user_Password})
        assert response.ok
        print(response.json())
        response_body=response.json()
        return response_body["token"]


    #we place an order through api so use request instead of chromium
    def createOrder(self,playwright:Playwright,user_credentials):
        #call the above function to get token here
        token = self.getToken(playwright,user_credentials)
        api_request_context=playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response=api_request_context.post("api/ecom/order/create-order",
                                 data=orderPayLoad,
                                 headers={"Authorization":token,
                                          "content-type":"application/json"
                                          })
        print(response.json())  #  we just need order id
        response_body=response.json()
        order_id=response_body["orders"][0]  # i need only order id in json response
        return order_id


















