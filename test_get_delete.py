from playwright.sync_api import Playwright, sync_playwright


def test_get_token(playwright: Playwright) -> str:
    api_request_context = playwright.request.new_context(
        base_url="https://rahulshettyacademy.com/client"
    )
    response = api_request_context.post(
        "/api/ecom/auth/login",
        data={
            "userEmail": "siva.pallikonda@gmail.com",
            "userPassword": "Test@123"
        }
    )
    assert response.ok, f"Login API failed: {response.status}"
    response_body = response.json()

    # Return only token
    return response_body["token"]


def test_getOrder(playwright: Playwright):
    token = test_get_token(playwright)
    customerid = "6973880bc941646b7ab2a190"
    api_get_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com/client")
    getResponse = api_get_request_context.get(url=f"/api/ecom/order/get-orders-for-customer/{customerid}",
                                              headers={"Authorization": token, "Content-Type": "application/json"})
    print(getResponse)
    print(getResponse.json())
    json_response = getResponse.json()
    order_ids = [item["_id"] for item in json_response["data"]]
    print("order_ids are:")
    for i in order_ids:
        print(i)


def test_deleteOrder(playwright: Playwright):
    token = test_get_token(playwright)
    # Test Data
    delorder_id = "69747413c941646b7ab3d2a7"
    customerid = "6973880bc941646b7ab2a190"

    # Verifying the count of orders before delete
    api_del_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com/client")
    # customerid = "6973880bc941646b7ab2a190"
    api_get_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com/client")
    getResponse = api_get_request_context.get(url=f"/api/ecom/order/get-orders-for-customer/{customerid}",
                                              headers={"Authorization": token, "Content-Type": "application/json"})

    json_response = getResponse.json()
    order_count = len(json_response["data"])
    print("Number of orders before delete:", order_count)
    # delete request

    delResponse = api_del_request_context.delete(url=f"/api/ecom/order/delete-order/{delorder_id}",
                                                 headers={"Authorization": token, "Content-Type": "application/json"})
    assert delResponse.status == 400
    #assert delResponse.status_text == 'OK'

    # Verifying the count of orders After delete

    api_get_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com/client")
    getResponse = api_get_request_context.get(url=f"/api/ecom/order/get-orders-for-customer/{customerid}",
                                              headers={"Authorization": token, "Content-Type": "application/json"})
    json_response = getResponse.json()
    order_count = len(json_response["data"])
    print("Number of orders before delete:", order_count)


