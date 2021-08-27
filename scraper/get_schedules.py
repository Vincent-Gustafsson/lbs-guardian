import os

from selenium.webdriver.chrome.webdriver import WebDriver

from utils import schedule_utils


def login(driver: WebDriver, username, password):
    username_input = driver.find_element_by_id("username")
    password_input = driver.find_element_by_id("password")

    login_btn_xpath = "/html/body/article/form/div[3]/button"
    login_btn = driver.find_element_by_xpath(login_btn_xpath)

    username_input.send_keys(username)
    password_input.send_keys(password)
    login_btn.click()


def navigate_to_schedule_page(driver: WebDriver):
    schedule_btn = driver.find_element_by_xpath('//*[@id="menu_left"]/a[5]')
    schedule_btn.click()


def get_schedule_links(driver: WebDriver, schedule_type):
    schedule_utils.set_schedule_display_options(driver, schedule_type)

    dropdown_element = driver.find_element_by_class_name("dropdown-menu")
    links = schedule_utils.extract_links(dropdown_element.get_attribute('innerHTML'))  # noqa: E501

    return links


def screenshot_schedules_from_links(driver: WebDriver, links, schedule_type):
    for link in links:
        full_link = "https://sms.schoolsoft.se/lbs/jsp/student/" + link
        driver.get(full_link)

        person_name_xpath = '//*[@id="schedule_cont"]/div[1]/div[4]/div[2]/a'
        person_name = driver.find_element_by_xpath(person_name_xpath).text

        schedule_xpath = '//*[@id="schedule_cont_content"]'
        schedule = driver.find_element_by_xpath(schedule_xpath)

        SCHEDULES_FOLDER = os.getenv('SCHEDULES_FOLDER')
        uid = schedule_utils.generate_uid(person_name, schedule_type)
        schedule.screenshot(f"{SCHEDULES_FOLDER}/{uid}.png")


def get_schedules(schedule_type):
    USERNAME = os.environ["SCHOOLSOFT_USERNAME"]
    PASSWORD = os.environ["SCHOOLSOFT_PASSWORD"]

    driver = schedule_utils.setup_selenium()

    login(driver, USERNAME, PASSWORD)

    navigate_to_schedule_page(driver)

    links = get_schedule_links(driver, schedule_type)

    screenshot_schedules_from_links(driver, links, schedule_type)
