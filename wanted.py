import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import sqlite3


# ---headless 설정 -----
options = webdriver.ChromeOptions()

options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
# ----------------------

# ---sqlite3 설정 -----
# con = sqlite3.connect("programmers.db")
# cur = con.cursor()
# ---------------------


def iframe_checker(url):
    req = requests.get(url)

    driver = webdriver.Chrome("/home/jaewon/다운로드/chromedriver", chrome_options=options)
    driver.get(url)
    iframe = driver.find_elements_by_tag_name('iframe')
    print(iframe)
    if iframe != None:
        for i, iframe in enumerate(iframe):
            try:
                print(driver.page_source)
                print(f"{i}번쨰 iframe 입니다.")
                driver.switch_to_default_content()

            except:
                driver.switch_to_default_content()
                print(f"pass by except: iframes[{i}]")
                pass


class WantedHandler:
    def __init__(self, url):
        self.url = url

        self.driver = webdriver.Chrome("/home/jaewon/다운로드/chromedriver")

    def Parse(self):
        # req = requests.get(self.url)
        self.driver.get(self.url)
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        titles = soup.select("ul.clearfix > li > div > a  > div > dl > dt")
        companies = soup.select("ul.clearfix > li > div > a  > div > dl > dd")
        
        for title in titles:
            print(title.text)
        for company in companies:
            print(company.text)
        



class RocketPunchHandler:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome("/home/jaewon/다운로드/chromedriver")

    def Parse(self):
        req = requests.get(self.url)
        soup = BeautifulSoup(req.content, 'html.parser')
        li_tag = soup.select("#company-list > div")
        print(li_tag)


class ProgrammersHandler:
    def __init__(self, url):
        self.url = url
        # self.driver = webdriver.Chrome("/home/jaewon/다운로드/chromedriver")
        self.count = 1

        # ----sqlite3 설정--------
        self.con = sqlite3.connect("Programmers.db")
        self.cur = self.con.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS jobs(id integer PRIMARY KEY autoincrement, job CHAR(32),address text,experience CHAR(32))")
        # -----------------------

    def Parse(self):
        req = requests.get(self.url+str(self.count))
        print(url)
        while req.status_code == 200:
            soup = BeautifulSoup(req.content, 'html.parser')
            titles = soup.select("h4.position-title")
            companys = soup.select("h5.company-name")
            addresses = soup.select("li.location")
            experiences = soup.select("li.experience")

            idx = 0
            for i in soup.select("li.list-position-item"):
                idx += 1

            for num in range(0, idx):
                pass

            # print("---TITLE-----")
            # for title in titles:
            #     print(title.text)
            # print("-------------")
            # print("---company---")
            # for company in companys:
            #     print(company.text)
            # print("-------------")

            # print("---address---")
            # for address in addresses:
            #     print(address.text)
            # print("-------------")

            # print("---experience--")
            # for experiences in experiences:
            #     print(experiences.text)
            # print("---------------")

            # self.count +=1
            break


# iframe_checker("https://www.wanted.co.kr/wdlist/518/873?country=kr&job_sort=job.latest_order&years=-1&locations=all")
URL = "https://www.wanted.co.kr/wdlist/518/873?country=kr&job_sort=job.latest_order&years=-1&locations=all"
W = WantedHandler(URL)
W.Parse()
# url = "https://www.rocketpunch.com/jobs"
# R = RocketPunchHandler(url)
# R.Parse()
# url = "https://programmers.co.kr/job?page="
# P = ProgrammersHandler(url)
# P.Parse()
