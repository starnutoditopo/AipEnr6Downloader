#!/usr/bin/python

# Requirements
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import os
import sys
import getopt

default_download_dir = '/Data/AIP'

def print_usage():
    print(f'Usage:')
    print(f'   {sys.argv[0]} -u <user_name> -p <password> [-o <output directory>]')
    print(f'      -u <user_name>')
    print(f'      -p <password>')
    print(f'      -o <output directory> (default: {default_download_dir})')

def main(argv):
    # Configuration
    user_name = None
    password = None
    TIME_TIMEOUT = 120
    download_dir = default_download_dir

    try:
      opts, args = getopt.getopt(argv,"hu:p:o:",["username=","password=","outputdirectory="])
    except getopt.GetoptError:
      print_usage()
      sys.exit(2)
    for opt, arg in opts:
      if opt == '-h':
         print_usage()
         sys.exit()
      elif opt in ("-u", "--username"):
         user_name = arg
      elif opt in ("-p", "--password"):
         password = arg
      elif opt in ("-o", "--outputdirectory"):
         download_dir = arg
    print('User name is: ', user_name)
    #print('Password is: ', password)
    print('Output directory is: ', download_dir)



    # Code
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    # options.add_argument('window-size=1200x600')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("start-maximized");
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_experimental_option('prefs',  {
        "download.default_directory": download_dir,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "plugins.always_open_pdf_externally": True
        }
    )

    def wait_for_downloads():
        while any([filename.endswith(".crdownload") for filename in os.listdir(download_dir)]):
            time.sleep(2)

    with webdriver.Chrome(options=options) as driver:
        driver.maximize_window();    
        
        driver.get("https://www.enav.it/enavWebPortalStatic/AIP/AIP/enr/enr6/ENR6.htm")
        user_box = WebDriverWait(driver, TIME_TIMEOUT).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[2]/form/input[1]')))
        user_box.click()
        user_box.send_keys(user_name)

        password_box = WebDriverWait(driver, TIME_TIMEOUT).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[2]/form/input[2]')))
        password_box.click()
        password_box.send_keys(password)
        
        
        button = WebDriverWait(driver, TIME_TIMEOUT).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[2]/form/center/button')))
        button.click()
        
        # wait the ready state to be complete
        WebDriverWait(driver=driver, timeout=10).until(
            lambda x: x.execute_script("return document.readyState === 'complete'")
        )
        
        #print('Page source:')
        #print(driver.page_source)

        links = []
        page_links = driver.find_elements_by_tag_name('a')
        for link in page_links:
            href = link.get_attribute('href')
            if href is not None:
                #print(href)
                links.append(href)
                
        print('Downloading links:')
        for link in links:
            print(link)
            driver.get(link)

        print('... waiting for all download to finish...')
        wait_for_downloads()
        # print("output directory:")
        # print(os.listdir(download_dir))
        print('... done.')
        driver.quit()

if __name__ == "__main__":
   main(sys.argv[1:])