import requests

import pandas as pd


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver = webdriver.Chrome()
import re


class PageGetter:
    driver = False
    def __init__(self, defaultBrowser='firefox'):
        if defaultBrowser == 'firefox':
            self.driver = webdriver.Firefox()
            self.driver.add_cookie(cookie_dict)
        elif defaultBrowser == 'chrome':
            self.driver = webdriver.Chrome()
           
        else:
            raise Exception('Not a browser')

    def getPage(self, url):
        if not self.driver:
            raise Exception("You should start a browser connection")
        self.driver.get(url)
        # wait until there is an <article> tag in the DOM
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "section"))
        )
    
        html = self.driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        return soup
    


    def close(self):
        self.driver.quit()


def process_data(job):
    city_selector = '.loc.css-nq3w9f.pr-xxsm'
    city = job.select(city_selector)[0].text
    company = job.select('a.css-10l5u4p.e1n63ojh0.jobLink')[0].text
    title=job.select('.jobInfoItem.jobTitle.css-13w0lq6.eigr9kq1.jobLink')[0].text
    return { 
        "city":city,
        "company":company,
        "title":title
    }
def scrape_jobs(soup):
   
    ul ='.jl.react-job-listing.gdGrid'
    job_list =  soup.select(ul)
    return [process_data(job) for job in job_list]

def append_first_page_to_url(url):
    if '_IP1' not in url:
        return url.replace('.htm', '_IP1.htm')
    else:
        return url

def get_jobs(url,filename):
    url = append_first_page_to_url(url)
    pg = PageGetter('chrome')
    job_array =[]
    soup = pg.getPage(url)
    no_of_jobs = soup.select('div#ResultsFooter >div.cell.middle.hideMob.padVertSm')[0].text
    no_of_jobs = int(re.search(r'\d+$',no_of_jobs).group())
    for i in range(1,no_of_jobs + 1):
        if i > 1:
            soup = pg.getPage(url)
            prev = f"_IP{str(i-1)}"
            next_page = f"_IP{str(i)}"
            url = url.replace(prev,next_page)
        jobs = scrape_jobs(soup)
        job_array +=jobs
        print(url)
    pg.close()
    df = pd.DataFrame(job_array)
    df.to_csv(f'./input/{filename}.csv', encoding='utf-8')
    return job_array


