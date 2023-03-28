from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.common.exceptions import 
from time import sleep
import pw
from selenium.webdriver.common.keys import Keys
from random import randint

user = pw.user
password = pw.password

class Bot():

    links = []
    valid_link = []
    

    comments = [
        'lecker!', 'Das sieht gut aus. Muss ich unbedingt auch ausprobieren! :)'
    ]

    def __init__(self):
        hashtags = ['rezepte', 'veggie', 'kochen', 'leckerschmecker', 'backen', 'pasta', 'foodie']
        self.login(user,password)
        self.like_comment_by_hashtag(hashtags)

    def login(self, username, password):
        self.driver = webdriver.Chrome()
        self.driver.get('https://instagram.com/')
        sleep(5)
        insta_cookies = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]')
        insta_cookies.click()
        username_input = self.driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input')
        username_input.send_keys(username)
        sleep(1)
        password_input = self.driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_input.send_keys(password)
        sleep(1)
        password_input.send_keys(Keys.RETURN)
        sleep(5)
        self.driver.find_element(By.XPATH, "//button[contains(text(), 'Jetzt nicht')]").click() # clicking 'Jetzt nicht btn'
        sleep(2)
        self.driver.find_element(By.XPATH, "//button[contains(text(), 'Jetzt nicht')]").click() # clicking 'Jetzt nicht btn'

    def like_comment_by_hashtag(self, hashtags):
        for hashtag in hashtags:
            self.driver.get('https://www.instagram.com/explore/tags/{}/'.format(hashtag))
            sleep(5)
            links = self.driver.find_elements(By.TAG_NAME, 'a')
            # links = self.driver.find_elements(By.XPATH, "//a[@href]")

            def condition(link):
                return 'https://www.instagram.com/p/' in link.get_attribute('href')

            valid_links = list(filter(condition, links))
            # valid_links = ["https://www.instagram.com/p/CpQihxhv5Be/"]

            for i in range(10):
                link = valid_links[i].get_attribute('href')
                if link not in self.links:
                    self.links.append(link)

            for link in self.links:
                print(link)
                self.driver.get(link)
                # follow
                sleep(3)
                try:
                    # self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div[1]/div[1]/article/div/div[2]/div/div[1]/div/header/div[2]/div[1]/div[2]/button/div/div").click()
                    self.driver.find_element(By.XPATH, "//button/div/div[contains(text(), 'Folgen')]").click()
                except:
                    pass
                # comment
                sleep(3)
                # try:
                # try:
                #     post = self.driver.find_element(By.XPATH, "//textarea[@placeholder='Kommentieren …']")
                #     post.send_keys(self.comments[randint(0,1)])
                # except:
                #     post = self.driver.find_element(By.XPATH, "//textarea[@placeholder='Kommentieren …']")
                #     post.send_keys(self.comments[randint(0,1)])
                    
                # sleep(1)
                # try:
                #     self.driver.find_element(By.XPATH, "//div[contains(text(), 'Posten')]").click()
                # except:
                #     pass
                # sleep(2)

def main():
    while True:
        my_bot = Bot()
        sleep(20) # one hour

if __name__ == '__main__':
    main()
