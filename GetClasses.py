import requests
from bs4 import BeautifulSoup
import re

def fetch_courses(url, output_file, coursePrefix):
    # Send a GET request to the URL
    response = requests.get(url)
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Define a pattern to match course titles like "ACCT xxx"
    pattern = re.compile(rf'{coursePrefix} \d{{3}}')

    # Find all 'a' tags with a 'title' attribute
    courses = soup.find_all('a', title=pattern)

    # Open the output file in write mode
    with open(output_file, 'a') as file:
        # Extract and write the course titles to the file
        for course in courses:
            title = course['title']
            title = title.replace("opens a new window", "")
            file.write(title + '\n')

# URL of the page you want to scrape
url_page1 = 'http://catalog.csulb.edu/content.php?catoid=8&navoid=903'
url_page2 = 'http://catalog.csulb.edu/content.php?catoid=8&catoid=8&navoid=903&filter%5Bitem_type%5D=3&filter%5Bonly_active%5D=1&filter%5B3%5D=1&filter%5Bcpage%5D=2#acalog_template_course_filter'
# Path to the output file
output_file = 'courses.txt'

# Fetch the courses and save to the file
fetch_courses(url_page1, output_file, "ACCT")
fetch_courses(url_page2, output_file, "ANTH")
