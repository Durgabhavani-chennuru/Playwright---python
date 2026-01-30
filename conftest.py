import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser selection"
    )

    parser.addoption(
        "--url_name", action="store", default="https://rahulshettyacademy.com/client", help="server selection"
    )


@pytest.fixture(scope="session")
def user_credentials(request):
    return request.param


@pytest.fixture(scope="session")
def browserInstance(playwright,request):
    # if we execute through the terminal
    browser_name=request.config.getoption("browser_name")
    url_name = request.config.getoption("url_name")
    if browser_name=="chrome":
        playwright.chromium.launch(headless=False)
    elif browser_name=="firefox":
        playwright.firefox.launch(headless=False)

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    #page.goto(url_name)
    yield page
    context.close()
    browser.close()

#pytest --browser_name chrome -m smoke -n 3 --tracing on/off --html=report.html


##html report generation  ->  pip install pytest-html-> pytest -n 3 --html=report.html
#ls-> cd .\Playwright\ -> ls ->pytest file name --headed
# recording a trace(test results)->  pytest -n 3 --tracing on/off --html=report.html

# to see the test results and screenshorts goto trace viwer in google-> search link(trace.playwright.dev)->click ->clearadd files


