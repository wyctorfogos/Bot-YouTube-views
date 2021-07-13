import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Assistir_video_YouTube:
    def Video(url,num_visualizacoes,tempo_visualizacao):
        path="C:\Program Files (x86)\chromedriver.exe"

        driver=webdriver.Chrome(path)
        #url="https://www.youtube.com/watch?v=xxNNZt9aNz0"
        driver.get(url)
        #print(By.XPATH('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[3]/div/ytd-player/div/div/div[33]/div[2]/div[1]/button'))
        ##button_play= driver.find_element_by_xpath("//button[@class='ytp-large-play-button ytp-button']")
        for i in range(num_visualizacoes):
            try:
                button_play= driver.find_element_by_xpath("//button[@class='ytp-large-play-button ytp-button']")
                button_play.click()
            except:
                WebDriverWait(driver, 5).until_not(EC.url_to_be(
                    (By.XPATH, "//button[@class='ytp-large-play-button ytp-button']")))
                driver.refresh()
        #button_play.click()
        #button_play.send_keys(Keys.ENTER)
        #print(button_play)
            time.sleep(tempo_visualizacao)
        driver.quit()
