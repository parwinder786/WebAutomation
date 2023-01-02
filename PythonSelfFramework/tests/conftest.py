import pytest
from selenium import webdriver
import time
driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )
# syntax for choose the browser at run= time
#https://docs.pytest.org/en/7.1.x/example/simple.html (copy in conftest file)
#setup fixture to open browser

@pytest.fixture(scope="class")
def setup(request): #request is instance, you can use it in child class
    global driver # to define call over class
    browser_name=request.config.getoption("browser_name") #it will pull the browser value at run time
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="C:\\Users\\XT23495\\Downloads\\chromedriver.exe")
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="C:\\Users\\XT23495\\Downloads\\chromedriver.exe")
    elif browser_name == "IE":
        print("IE driver")
    driver.get("C:\\Users\\XT23495\\Downloads\\chromedriver.exe")
    driver.maximize_window()

    request.cls.driver = driver # driver can be called in child class
    yield
    driver.close()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
        driver.get_screenshot_as_file(name) # will have access to global driver defined inside the setup

