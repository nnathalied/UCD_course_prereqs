'''*** 
get_courses.py
get_courses(course_subject, course_number, search_subject, prereqs)
started: 2020-10-12

fetches and prints courses in the department <search_subject>
you gain access to by taking <course_subject course_number>

uses code from https://matix.io/extract-text-from-webpage-using-beautifulsoup-and-python/
to extract text from UC Davis General Catalog 

***'''

import requests
from bs4 import BeautifulSoup
import re
import string

def get_courses(course_subject, course_number, search_subject, prereqs):
    url = 'https://ucdavis.pubs.curricunet.com/Catalog/' + search_subject.lower() + '-courses-sc'
    res = requests.get(url)
    html_page = res.content
    soup = BeautifulSoup(html_page, 'html.parser')
    text = soup.get_text()
    output = text.split()

    i = 0
    while(i < (len(output) - 2)):
        find_course_number = False
        find_prereqs = False
        if(search_subject in output[i]) and (output[i + 1][0:3].isdigit()): #if at a new course listing

            output_course_num = output[i + 1]
            course = search_subject + " " + output_course_num + " "
            short_term_index = (i + 2)
    
            while(short_term_index < (len(output) - 1)):
                if("Prerequisite" in output[short_term_index]):
                    while("." not in output[short_term_index]):
                        if(course_number in output[short_term_index]):
                            find_course_number = True
                        course += (output[short_term_index] + " ")
                        short_term_index += 1
                elif("Effective" in output[short_term_index]):
                    while("." not in output[short_term_index]):
                        course += (output[short_term_index] + " ")
                        short_term_index += 1
                    if(("Quarter") in output[short_term_index]):
                        course += "Quarter."
                    break
                else:
                    course += (output[short_term_index] + " ")
                    short_term_index += 1
            # print("---course-----\n", course)
            i = (short_term_index - 1) #skip i to "Quarter" at end of course
            if(find_course_number): # if course is a pre req for current course
                prereqs.append(course)
        i += 1
            
