from bs4 import BeautifulSoup
import urllib,re,csv,os,requests,itertools,pdfkit
import requests.packages.urllib3
import requests
requests.packages.urllib3.disable_warnings()



def fetch_courses(url, output_file):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    for info in soup.find_all('td' ,attrs={'class':'width'}):
        full_course_name = info.find('a').text
        #print(full_course_name)
        course_prefix = full_course_name.split("-")[0]
        print(course_prefix)
        with open(output_file, 'a') as file:
            title = course_prefix
            #title = title.replace("opens a new window", "")
            file.write(title + '\n')



output_file = 'courses.txt'



for pagenumber in range(1,52):
	url = "https://catalog.sdsu.edu/content.php?catoid=9&catoid=9&navoid=776&filter%5Bitem_type%5D=3&filter%5Bonly_active%5D=1&filter%5B3%5D=1&filter%5Bcpage%5D=" + str(pagenumber) + "#acalog_template_course_filter"
	fetch_courses(url, output_file)



