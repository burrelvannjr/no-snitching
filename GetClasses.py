import requests
from bs4 import BeautifulSoup
import re

def fetch_courses(url, output_file, coursePrefix):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    pattern = re.compile(rf'{coursePrefix} \d{{3}}')
    courses = soup.find_all('a', title=pattern)
    with open(output_file, 'a') as file:
    	for course in courses:
            print(course)
    		title = course['title']
    		title = title.replace("opens a new window", "")
    		file.write(title + '\n')


# Path to the output file
output_file = 'courses.txt'

# URL of the page you want to scrape (SDSU links)
for pagenumber in range(1,52):
	url_page = "https://catalog.sdsu.edu/content.php?catoid=9&catoid=9&navoid=776&filter%5Bitem_type%5D=3&filter%5Bonly_active%5D=1&filter%5B3%5D=1&filter%5Bcpage%5D=" + str(pagenumber) + "#acalog_template_course_filter"
	#course_prefix = pattern.split(" ", 1)[0]
	fetch_courses(url_page, output_file, "NA")



