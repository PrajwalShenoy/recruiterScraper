from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep


options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options)
driver.implicitly_wait(10) 
adp_url = "https://app.careerfairplus.com/abiwt_ca/fair/4982/employer/345051"
driver.get(adp_url)
sleep(5)
checkBox = driver.find_elements(By.CLASS_NAME, "css-1m9pwf3")[1].click()
selections = driver.find_element(By.CLASS_NAME, "employer-list")
comps = selections.find_elements(By.CLASS_NAME, "employer-list-item-container")
for comp in comps:
    comp.click()
    companyName = driver.find_element(By.CLASS_NAME, "desktop-employer-card-container") \
                .find_element(By.TAG_NAME, "section") \
                .find_element(By.TAG_NAME, "header") \
                .find_element(By.CLASS_NAME, "MuiCardHeader-content") \
                .find_element(By.CLASS_NAME, "MuiTypography-root") \
                .find_element(By.TAG_NAME, "div").text
    print("Company name: " + companyName)
    recSet = []
    recruiters = driver.find_elements(By.XPATH, "//section[@aria-roledescription='Schedule']")
    for recruiter in recruiters:
        rec = recruiter.find_elements(By.TAG_NAME, "section")[1].find_elements(By.TAG_NAME, "div")[1].find_element(By.TAG_NAME, "h6").text
        if rec not in recSet:
            recSet.append(rec)
    print(recSet)
    print()


# comps[0]

# companyName = driver.find_element(By.CLASS_NAME, "desktop-employer-card-container") \
#                 .find_element(By.TAG_NAME, "section") \
#                 .find_element(By.TAG_NAME, "header") \
#                 .find_element(By.CLASS_NAME, "MuiCardHeader-content") \
#                 .find_element(By.CLASS_NAME, "MuiTypography-root") \
#                 .find_element(By.TAG_NAME, "div").text

# recruiters = driver.find_elements(By.XPATH, "//section[@aria-roledescription='Schedule']")
# recruiter = recruiters[0]
# recruiter.find_elements(By.TAG_NAME, "section")[1].find_elements(By.TAG_NAME, "div")[1].find_element(By.TAG_NAME, "h6").text