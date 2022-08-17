from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def do_the_job(choices_list):
    random.shuffle(choices_list)
    path = r"C:\Users\Marwen\Desktop\python\chromedriver.exe"
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    for choice in choices_list:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://pprdv.interieur.gouv.fr/booking/create/989")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        try:
            errorElement = driver.find_element(By.XPATH, "/html/body/h1")

            if errorElement.text == "Service surchargé":
                print("surcharged")
                driver.close()
                continue
            if errorElement.text == "403 Forbidden":
                print("forbidden")
                driver.close()
                break
            continue
        except NoSuchElementException:
            pass

        try:
            # search = driver.find_element(By.XPATH, "/html/body/h1")
            checkbox = driver.find_element(By.XPATH,
                                           "/html/body/div[1]/div[2]/div[3]/div/div/form/div[1]/input[@type='checkbox']")
            checkbox.send_keys(Keys.SPACE)
            # wait = WebDriverWait(driver, 10)
            # element = wait.until(EC.invisibility_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[3]/div/div/form/div[1]/input[@type='checkbox']")))
            # element_button = wait.until(EC.element_to_be_clickable((By.ID, 'condition'))).click()

            button = driver.find_element(By.NAME, "nextButton")
            button.click()

            try:
                errorElement = driver.find_element(By.XPATH, "/html/body/h1")

                if errorElement.text == "Service surchargé":
                    print("surcharged")
                    driver.close()
                    continue
                if errorElement.text == "403 Forbidden":
                    print("forbidden")
                    driver.close()
                    break
                continue
            except NoSuchElementException:
                pass

            radio = driver.find_element(By.XPATH, choice)
            radio.click()
            next_button = driver.find_element(By.XPATH,
                                              "/html/body/div[1]/div[2]/div[3]/div/div/form/div/input[@type='submit']")
            next_button.click()

            try:
                errorElement = driver.find_element(By.XPATH, "/html/body/h1")

                if errorElement.text == "Service surchargé":
                    print("surcharged")
                    driver.close()
                    continue
                if errorElement.text == "403 Forbidden":
                    print("forbidden")
                    driver.close()
                    break
                continue
            except NoSuchElementException:
                pass

            result = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/div/div/form")
            if result.text == "Il n'existe plus de plage horaire libre pour votre demande de rendez-vous. Veuillez recommencer ultérieurement.":
                print("not available")
                # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "FormBookingCreate")))
                driver.close()
                continue
            print("available")
            break;

        except Exception:
            pass


def get_choices_list():
    return [
        "/html/body/div[1]/div[2]/div[3]/div/div/form/fieldset/p[1]/input[@type='radio']",
        "/html/body/div[1]/div[2]/div[3]/div/div/form/fieldset/p[2]/input[@type='radio']",
        "/html/body/div[1]/div[2]/div[3]/div/div/form/fieldset/p[3]/input[@type='radio']",
        "/html/body/div[1]/div[2]/div[3]/div/div/form/fieldset/p[4]/input[@type='radio']",
        "/html/body/div[1]/div[2]/div[3]/div/div/form/fieldset/p[5]/input[@type='radio']",
        "/html/body/div[1]/div[2]/div[3]/div/div/form/fieldset/p[6]/input[@type='radio']",
        "/html/body/div[1]/div[2]/div[3]/div/div/form/fieldset/p[7]/input[@type='radio']",
        "/html/body/div[1]/div[2]/div[3]/div/div/form/fieldset/p[8]/input[@type='radio']",
        "/html/body/div[1]/div[2]/div[3]/div/div/form/fieldset/p[9]/input[@type='radio']"
    ]


if __name__ == '__main__':
    do_the_job(get_choices_list())
