import time
from selenium import webdriver
from pyautogui import write
import sys
import os

mins = 0
if len(sys.argv)>1:
    mins = int(sys.argv[1])
# from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
# binary = FirefoxBinary("C:\ProgramData\Microsoft\Windows\Start Menu\Programs")

gecko_path = os.getcwd()+'/geckodriver.exe'
url = "https://docs.google.com/forms/d/e/1FAIpQLSfINznF_zML420lxzJC5NE-gizeczXILsHvnaHqNe8rL9Fa3w/viewform"
success = "https://docs.google.com/forms/d/e/1FAIpQLSfINznF_zML420lxzJC5NE-gizeczXILsHvnaHqNe8rL9Fa3w/formResponse"
dmk_options = [10,20,30,40,50,60,70,80,90,100,110,120,180]

def selectOpt(driver,i_menu=0,i_opt=0):
    # driver = webdriver.Firefox(firefox_binary=binary)
    driver.find_elements_by_class_name("quantumWizMenuPaperselectOptionList")[i_menu].click()
    for _ in range(i_opt):
        write(['down'])
    write(['enter'])
    time.sleep(1)

def submitForm(driver):
    driver.find_element_by_class_name("appsMaterialWizButtonPaperbuttonContent").click()

def submitDmk(i_qnt):
    dmk_added = 0
    dmk_to_add = dmk_options[i_qnt-1]
    # driver = webdriver.Firefox(executable_path=r'C:\val_corner\pyScraping\geckodriver.exe')
    driver = webdriver.Firefox(executable_path = gecko_path)
    driver.get(url)
    time.sleep(1)
    selectOpt(driver,0,27) # 0 refers to the first dropdown and 27 to the UK option
    selectOpt(driver,1,i_qnt) # 1 refers to the second dropdown and i_qnt to the amount of daimoku
    submitForm(driver)
    if driver.current_url == success:
        dmk_added = dmk_to_add
        print("Added {} mins".format(dmk_added))
    else: 
        print("Failed to add {} mins".format(dmk_to_add))
    driver.close()
    return dmk_added

def how_many(mins=0,hrs=0):
    qnt = hrs*60 + mins
    res = {}
    i = 13
    for unit in reversed(dmk_options):
        units = int(qnt/unit)
        if units >= 1:
            res[i]=units
            qnt -= units*unit
            if qnt<=0:
                break
        i -= 1
    return res

def addDmk(mins):
    total_added = 0
    print("\nAdding {} mins to the SGI Europe Daimoku Counter...".format(mins))
    for i_qnt, units in how_many(mins).items():
        for iteration in range(units):
            total_added += submitDmk(i_qnt)
    print("\nSummary: {} new mins were added to the SGI Europe Daimoku Counter!".format(total_added))
    if mins > total_added:
        print("Warning: of the {} minutes requested, {} minutes were not added to the Counter.".format(mins,mins-total_added))
    print()

            
addDmk(mins)
