from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from bs4 import BeautifulSoup


BLACKLISTED_SCHEDULES = frozenset((
    "- Adamsson Lucas",
    "- Rajala William",
    "- Svensson Vilgot",
    "None",
))


def setup_selenium():
    options = webdriver.ChromeOptions()

    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument("--start-maximized")
    options.add_argument("--window-size=1920x1080")

    driver = webdriver.Chrome(
        "C:/Program Files (x86)/chromedriver",
        options=options
    )

    driver.implicitly_wait(30)
    driver.get("https://sms.schoolsoft.se/lbs/jsp/student/right_student_schedule.jsp?menu=schedule")  # noqa: E501

    return driver


def set_schedule_display_options(driver: WebDriver, schedule_type):
    if schedule_type == "teacher":
        # Open "visningsalternativ"
        driver.find_element_by_id("opencloseview").click()

        # Choose teacher option
        driver.find_element_by_id("type1").click()

        # Show teacher schedule
        driver.find_element_by_xpath('//*[@id="select"]/input').click()

    elif schedule_type == "student":
        # Open "visningsalternativ"
        driver.find_element_by_id("opencloseview").click()

        # Choose teacher option
        driver.find_element_by_id("type2").click()

        # Show teacher schedule
        driver.find_element_by_xpath('//*[@id="select"]/input').click()


def extract_links(html):
    soup = BeautifulSoup(html, features="html.parser")
    student_tags = soup.find_all("a")

    return [link['href'] for link in student_tags]


def generate_uid(name, person_type):
    if name not in BLACKLISTED_SCHEDULES:
        if person_type == "student":
            # Get fullname and ignore class
            name_components = name.split()[::-1][:-1]
            # Make all names lower (firstnames and lastnames)
            name_components = [name.lower() for name in name_components]

            student_class = name.split()[::-1][-1]

            name = "".join([proper[:2] for proper in name_components])

            uid = name + student_class

            return uid

        if person_type == "teacher":
            name_components = name.split()[::-1]
            # Make all names lower (firstnames and lastnames)
            name_components = [name.lower() for name in name_components]

            uid = "".join([n[:2] for n in name_components])

            return uid
