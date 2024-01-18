import random
import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium_stealth import stealth

import time

firstTime = True

def read_random_line(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return random.choice(lines).strip()

while True:
    url = "https://app.smartsheet.com/b/form/0425c7c578b54316a0a7d76b9e28dfb5"
    

    chrome_options = Options()
    options = webdriver.ChromeOptions() 
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)

    
    # Set path to chromedriver as per your configuration
    webdriver_service = Service(ChromeDriverManager().install())

    # Initialize the driver
    driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)
    chrome_options.add_argument("--disable-blink-features")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    #print(driver.execute_script("return navigator.userAgent;"))

    stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )
    
    # Read a random line from each file
    random_first_name = read_random_line('first-names.txt')
    random_last_name = read_random_line('last-names.txt')
    random_course = read_random_line('courses.txt')
    random_professor = read_random_line('professors.txt')
    random_date = read_random_line('dates.txt')
    random_last_name = random_last_name.lower()

    email = random_first_name + "." + random_last_name + "@student.csulb.edu"

    #get the first 4 characters of course title and save to variable
    department_title = random_course[:4]


    # Print the random selections (or process them as needed)
    print(f'First Name: {random_first_name}, Place: {random_last_name}, Course: {random_course}, Date: {random_date}, Professor: {random_professor}')

    # Find input boxes by guessed IDs or names
    driver.get(url)


    #before finding elements, need to verify if one exists and has been loaded
    #if it has been loaded, then find the element
    
    # Finding elements by id using Selenium
    class_student_service = driver.find_element(By.ID, 'text_box_Class/Student Service').send_keys(random_course)
    instructor_coach_counselor_librarian = driver.find_element(By.ID, 'text_box_Instructor/Coach/Counselor/Librarian').send_keys(random_professor)
    date_of_class_or_service = driver.find_element(By.ID, 'date_Date of Class or Service').send_keys("1/22/2024")
    time_of_class_or_service = driver.find_element(By.ID, "text_box_Time of Class or Service").send_keys(random_date)
    department_or_college = driver.find_element(By.ID, 'text_box_Department or College').send_keys(department_title)
    submitter_name = driver.find_element(By.ID, 'text_box_Submitter\'s Name').send_keys(random_first_name + " " + random_last_name)
    submitter_email = driver.find_element(By.ID, 'text_box_Submitter\'s Email').send_keys(email)

    # Print to verify (optional)
    print(class_student_service, instructor_coach_counselor_librarian, date_of_class_or_service, time_of_class_or_service, department_or_college, submitter_name, submitter_email)

    # Click the submit button that has data client id submit
    submit_button = driver.find_element(By.XPATH, "//button[@data-client-id='form_submit_btn']").click()

    # Wait for the page to load (adjust the time as needed)
    time.sleep(4)

    #let the user fill out the captcha
    if firstTime:
        input("Press Enter to continue...")

    #close the browser and cleanup to restart the loop
    driver.close()
    driver.quit()

    firstTime = False
