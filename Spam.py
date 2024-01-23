import random
import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium_stealth import stealth
from datetime import date

import time

firstTime = True

def read_random_line(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return random.choice(lines).strip()

while True:
    #url = "https://app.smartsheet.com/b/form/0425c7c578b54316a0a7d76b9e28dfb5"
    url = "https://app.smartsheet.com/b/form/2a7626b7413b4a16989f2ea0b8d86a47"
    

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
    random_time = read_random_line('times.txt')
    random_last_name = random_last_name.lower()
    random_first_name = random_first_name.lower()

    #email = random_first_name + "." + random_last_name + "@student.csulb.edu"

    rand_num = random.randint(1000,9999)

    email_pre = []
    email_join = []
    email_post = []

    pre1 = random_first_name
    pre2 = random_first_name[0]
    pre3 = random_first_name[0:2]
    join1 = "."
    join2 = "_"
    join3 = ""
    post1 = random_last_name
    if len(random_last_name)<=3:
        post2 = random_last_name[0:2] + str(rand_num)
    else:
        post2 = random_last_name + str(rand_num)

    if len(random_last_name)<=3:
        post3 = random_last_name
    else:
        post3 = random_last_name[0:2]


    email_pre.append(pre1)
    email_pre.append(pre2)
    email_pre.append(pre3)
    email_join.append(join1)
    email_join.append(join2)
    email_join.append(join3)
    email_post.append(post1)
    email_post.append(post2)
    email_post.append(post3)

    pick = random.randint(0,2)
    email_prefix = email_pre[pick]
    pick = random.randint(0,2)
    email_joiner = email_join[pick]
    pick = random.randint(0,2)
    email_suffix = email_post[pick]


    email = email_prefix + email_joiner + email_suffix + "@sdsu.edu"


    miss_dates = ["01/22/2024"]

    today = date.today()
    miss_date = today.strftime("%m/%d/%Y")
    miss_dates.append(miss_date)
    miss_dates = list(set(miss_dates))
    rand_pick = random.randint(0,(len(miss_dates)-1))
    missed_class_date = miss_dates[rand_pick]
    
    
    #get the first 4 characters of course title and save to variable
    department_title = random_course[:4]


    # Print the random selections (or process them as needed)
    print(f'First Name: {random_first_name}, Place: {random_last_name}, Course: {random_course}, Time: {random_time}, Professor: {random_professor}')

    # Find input boxes by guessed IDs or names
    driver.get(url)


    #before finding elements, need to verify if one exists and has been loaded
    #if it has been loaded, then find the element
    
    # Finding elements by id using Selenium
    class_student_service = driver.find_element(By.ID, 'text_box_Class/Student Service').send_keys(random_course)
    instructor_coach_counselor_librarian = driver.find_element(By.ID, 'text_box_Instructor/Coach/Counselor/Librarian').send_keys(random_professor)
    date_of_class_or_service = driver.find_element(By.ID, 'date_Date of Class or Service').send_keys(missed_class_date)
    time_of_class_or_service = driver.find_element(By.ID, "text_box_Time of Class or Service").send_keys(random_time)
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
