
from selenium import webdriver
import time
import json
import os
import datetime
# -*- coding: UTF-8 -*-
import numpy as np
import pandas as pd
import requests
from selenium.webdriver.common.keys import Keys
import time
import datetime
import re
import pymysql.cursors
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import configparser
conf = configparser.ConfigParser()
conf.read('conf.cfg')



def login():
    global browser
    url = 'http://apps.webofknowledge.com/WOS_AdvancedSearch_input.do?SID=E6BSTw6tqmrshja6omN&product=WOS&search_mode=AdvancedSearch'
    print("now access %s" % (url))
    a = browser.get(url)
    ###login in City U
    # browser.find_element_by_id("cred_userid_inputtext").send_keys("chaochehe2")
    # browser.find_element_by_id("cred_password_inputtext").send_keys("Welcoly0301")
    # browser.find_element_by_id('cred_sign_in_button').click()

def delete_history_information():
    global browser
    ###transition to wos  And Delete history information
    browser.find_element_by_name("selsets").click()
    browser.find_element_by_class_name("delete-button-style").click()
    ###clear history information
    browser.find_element_by_id("value(input1)").clear()

def search():
    global browser
    extraction = conf.items('Graph')[0][1]
    browser.find_element_by_id("value(input1)").send_keys(extraction)
    browser.find_element_by_id('searchButton').click()
    ###choose the latest result
    browser.find_element_by_id('set_1_div').click()

def adjust_format():
    global browser
    Action = ActionChains(browser)
    ######Record Content
    click_temp = browser.find_element_by_id('select2-bib_fields-container')
    Action.click(click_temp).perform()
    Action.move_by_offset(5, 40).perform()
    Action.move_by_offset(0, 40).perform()
    Action.move_by_offset(0, 40).perform()
    Action.click().perform()
    ####File Format
    # browser.find_element_by_id('select2-saveOptions-container').click()
    # click_temp1 = browser.find_element_by_id('select2-saveOptions-container')
    # Action.click(click_temp1).perform()
    # Action.move_by_offset(5, -30).perform()
    # Action.move_by_offset(0, -30).perform()
    # Action.move_by_offset(0, -30).perform()
    # Action.click().perform()



def iteration():
    global browser
    for i in range(4000, 100000, 500):
        ###transit to download window
        from random import randint
        from time import sleep

        time.sleep(8)

        try:
            browser.find_element_by_class_name('selectedExportOption').click()
            # click number of record range
            browser.find_element_by_id('numberOfRecordsRange').click()
            ###fill in mark from and mark to
        except:
            try:
                browser.find_element_by_class_name('selectedExportOption').click()
                # click number of record range
                browser.find_element_by_id('numberOfRecordsRange').click()
                ###fill in mark from and mark to
            except:
                try:
                    browser.find_element_by_class_name('selectedExportOption').click()
                    # click number of record range
                    browser.find_element_by_id('numberOfRecordsRange').click()
                    ###fill in mark from and mark to
                except:
                    pass
        browser.find_element_by_id("markFrom").send_keys(Keys.BACKSPACE)
        browser.find_element_by_id("markTo").send_keys(Keys.BACKSPACE)
        browser.find_element_by_id("markTo").send_keys(Keys.BACKSPACE)
        browser.find_element_by_id("markTo").send_keys(Keys.BACKSPACE)
        browser.find_element_by_id("markTo").send_keys(Keys.BACKSPACE)
        browser.find_element_by_id("markTo").send_keys(Keys.BACKSPACE)

        browser.find_element_by_id("markFrom").send_keys(i + 1)
        browser.find_element_by_id("markTo").send_keys(Keys.BACKSPACE)
        browser.find_element_by_id("markTo").send_keys(Keys.BACKSPACE)
        browser.find_element_by_id("markTo").send_keys(Keys.BACKSPACE)
        browser.find_element_by_id("markTo").send_keys(Keys.BACKSPACE)
        browser.find_element_by_id("markTo").send_keys(Keys.BACKSPACE)
        browser.find_element_by_id("markTo").send_keys(Keys.BACKSPACE)
        browser.find_element_by_id("markTo").send_keys(Keys.BACKSPACE)
        browser.find_element_by_id("markTo").send_keys(Keys.BACKSPACE)
        browser.find_element_by_id("markTo").send_keys(Keys.BACKSPACE)
        browser.find_element_by_id("markTo").send_keys(i + 500)

        adjust_format()
        # 转回去
        time.sleep(2)
        try:
            browser.find_element_by_class_name("quickoutput-overlay-buttonset").find_element_by_class_name(
                "quickoutput-action").click()
            browser.find_element_by_class_name("quickoutput-overlay-buttonset").find_element_by_class_name(
                "quickoutput-cancel-action").click()
        except:
            try:
                browser.find_element_by_class_name("quickoutput-overlay-buttonset").find_element_by_class_name(
                    "quickoutput-action").click()
                browser.find_element_by_class_name("quickoutput-overlay-buttonset").find_element_by_class_name(
                    "quickoutput-cancel-action").click()
            except:
                try:
                    browser.find_element_by_class_name("quickoutput-overlay-buttonset").find_element_by_class_name(
                        "quickoutput-action").click()
                    browser.find_element_by_class_name("quickoutput-overlay-buttonset").find_element_by_class_name(
                        "quickoutput-cancel-action").click()
                except:
                    pass

        print("%s is finished" % i)



def set_dir(year):
    global browser
    # browser = webdriver.Firefox()
    # browser.maximize_window()
    options = webdriver.ChromeOptions()
    prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': 'C:\\workspace\\pycharm workspace\\Third_paper_temp\\crawl_data\\pharmaceutical\\wos_data\\%s'%year}
    options.add_experimental_option('prefs', prefs)
    browser = webdriver.Chrome(chrome_options=options)



def main():
    year = input("year:")
    global browser
    set_dir(year)
    login()
    time.sleep(3)
    delete_history_information()
    time.sleep(3)
    search()
    time.sleep(4)
    input("year")
    input("document")
    input("language")
    iteration()


if __name__ == '__main__':
    main()



