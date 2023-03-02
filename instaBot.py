from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
# from secrets import pw
from selenium.webdriver.common.keys import Keys
from random import randint

class Bot():

    links = []
    valid_link = []

    comments = [
        'Great post!', 'Awesome!'
    ]

    def __init__(self):
        self.login('','')
        self.like_comment_by_hashtag('programming')

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

    def like_comment_by_hashtag(self, hashtag):
        self.driver.get('https://www.instagram.com/explore/tags/{}/'.format(hashtag))
        # links = self.driver.find_element(By.TAG_NAME, 'a')
        links = self.driver.find_elements(By.XPATH, "//a[@href]")

        def condition(link):
            return 'https://www.instagram.com/p/' in link.get_attribute('href')

        valid_links = list(filter(condition, links))
        # valid_links = ["https://www.instagram.com/p/CpQihxhv5Be/"]
        print(valid_links)

        print(links)

        for i in range(5):
            link = valid_links[i].get_attribute('href')
            if link not in self.links:
                self.links.append(link)

        for link in valid_links:
            print(link)
            self.driver.get(link)
            # follow
            sleep(5)
            self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div[1]/div[1]/article/div/div[2]/div/div[1]/div/header/div[2]/div[1]/div[2]/button/div/div").click()
            sleep(5)

            # comment
            self.driver.find_element(By.XPATH, 'RxpZH').click()
            sleep(1)
            self.driver.find_element(By.XPATH, "//textarea[@placeholder='Add a comment…']").send_keys(self.comments[randint(0,1)])
            sleep(1)
            self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

def main():
    while True:
        my_bot = Bot()
        sleep(20) # one hour

if __name__ == '__main__':
    main()
