import pytest
from selenium import webdriver
import pytest
import os
from datetime import datetime

#command to pass the browser name => pytest filename.py --browser_name edge
# if no brswer name is passing in the comment - it will automatically take
#pytest test_E2EFlow.py --browser_name edge --url "https://yourapp.com"

def pytest_addoption(parser):
    parser.addoption(
            "--browser_name", action="store", default="chrome", help="broswer selection"
    )
    parser.addoption(
        "--url", action="store", default="https://rahulshettyacademy.com/loginpagePractise/", help="passing the url"
    )


@pytest.fixture(scope="function")
def setup(request):
    browser=request.config.getoption("browser_name") #to get the value of request fetch from command request

    if browser=="chrome":
        driver = webdriver.Chrome()
    elif browser=="edge":
        driver=webdriver.Edge()
    else:
        driver=webdriver.Firefox()
    driver.implicitly_wait(10)
    #driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    yield driver  #first these peice of code will return and later it will reteun the driver and it is passing to the methods
    driver.close() #after the post execution of test case

@pytest.fixture() #to pass the url at run
def pass_Url(request):
    return request.config.getoption("url")


# Hook to add extra content to the HTML report

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("setup")  # adjust to your fixture
        if driver:
            time_stamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            file_name = f"{item.name}_{time_stamp}.png"
            screenshots_dir = os.path.join("Reports", "Screenshots")
            os.makedirs(screenshots_dir, exist_ok=True)

            # Save screenshot
            screenshot_path = os.path.join(screenshots_dir, file_name)
            driver.save_screenshot(screenshot_path)

            # ✅ RELATIVE PATH is key
            rel_path = os.path.relpath(screenshot_path, os.path.dirname(item.config.option.htmlpath))

            extra.append(pytest_html.extras.image(rel_path))

    report.extra = extra
