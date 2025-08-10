from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


class send_response:
    def fill_form(self, name, email, subject, message):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")  # Run without UI
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")

        form_link = "https://docs.google.com/forms/d/e/1FAIpQLSeF5QdXPA8h7_Sw11gHSY2d7XxDB3GaxSFOhxbBojUpSPTEng/viewform?usp=sharing&ouid=116599140460711299047"

        driver = webdriver.Chrome(options=chrome_options)
        driver.get(form_link)
        sleep(1)

        driver.find_element(By.XPATH,
                            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(
            name)
        sleep(0.1)

        driver.find_element(By.XPATH,
                            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(
            email)
        sleep(0.1)

        driver.find_element(By.XPATH,
                            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(
            subject)
        sleep(0.1)

        driver.find_element(By.XPATH,
                            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/textarea').send_keys(
            message)
        sleep(0.1)

        driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span').click()
        sleep(0.5)

        driver.quit()
