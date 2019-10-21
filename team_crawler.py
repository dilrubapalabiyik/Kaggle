import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import pandas as pd



# a bunch of functions 

def choose_per_game(driver,url,season):

	"""
	this is the prerequisite step for the other steps, since the other dropdowns will appear only after clicking "get stats"
	"""
	driver.get(url)
	if(season !='2018-19'):   # select season first since it is not equal to the default season
		get_stats = driver.find_element(By.XPATH,"//button[contains(text(),'Get Stats')]")
		get_stats.click()
		time.sleep(1)

		year_drop_down = driver.find_element(By.XPATH,"//div[@class='col-md-4']/div/div[@tabindex='0']/div[@class='multiselect__select']")
		year_drop_down.click()
		time.sleep(1)

		choose_season = driver.find_element(By.XPATH,"//div[@class='col-md-4']/div/div/div[@tabindex='-1']/ul/li[@class='multiselect__element']//*[text()='"+season+"']")
		choose_season.click()
		time.sleep(1)

		remove_previous_season = driver.find_element(By.XPATH,"//div[@class='col-md-4']/div/div[@tabindex='0']/div[@class='multiselect__tags']/div/span[1]/span[@class='custom__remove']")
		remove_previous_season.click()
		time.sleep(1)

		year_drop_down.click()
		time.sleep(1)

	get_stats = driver.find_element(By.XPATH,"//button[contains(text(),'Get Stats')]")  # after selecting season, generating data, then choose per game tab
	time.sleep(1)
	get_stats.click()
	time.sleep(1)
	stat_type_drop_down = driver.find_element(By.XPATH,"//main/div[4]/div[@class='row']/div[@class='col-md-2'][1]/div/div[@tabindex='0']/div[@class='multiselect__select']")
	stat_type_drop_down.click()
	time.sleep(1)
	per_game= driver.find_element(By.XPATH,"//main/div[4]/div[@class='row']/div[@class='col-md-2'][1]/div/div/div[@tabindex='-1']/ul/li[@class='multiselect__element']//*[text()='Per Game']")
	per_game.click()


def get_scoring(driver,url,season):

	"""
	this is for getting csv for "scoring" category
	"""

	choose_per_game(driver,team_url,season)
	download_link_scoring = driver.find_element(By.XPATH,"//a[@download='pbpstats_export.csv']")
	download_link_scoring.click()
	time.sleep(1)
	os.rename('pbpstats_export.csv', 'team_scoring_'+season+'.csv')


def get_assists(driver,url,season):

	"""
	this is for getting csv for "Assists" category
	"""

	choose_per_game(driver,url,season)
	table_data_dropdown = driver.find_element(By.XPATH,"//main/div[4]/div[@class='row']/div[@class='col-md-2'][2]/div/div[@tabindex='0']/div[@class='multiselect__select']")
	table_data_dropdown.click()
	time.sleep(1)
	assists_tab = driver.find_element(By.XPATH,"//main/div[4]/div[@class='row']/div[@class='col-md-2'][2]/div/div/div[@tabindex='-1']/ul/li[@class='multiselect__element']//*[text()='Assists']")
	assists_tab.click()
	time.sleep(1)
	download_link_assists = driver.find_element(By.XPATH,"//a[@download='pbpstats_export.csv']")
	download_link_assists.click()
	time.sleep(1)
	os.rename('pbpstats_export.csv', 'team_assists_'+season+'.csv')

def get_rebounds(driver,url,season):

	"""
	this is for getting csv for "Rebounds" category
	"""

	choose_per_game(driver,team_url,season)
	table_data_dropdown = driver.find_element(By.XPATH,"//main/div[4]/div[@class='row']/div[@class='col-md-2'][2]/div/div[@tabindex='0']/div[@class='multiselect__select']")
	table_data_dropdown.click()
	time.sleep(1)
	rebounds_tab = driver.find_element(By.XPATH,"//main/div[4]/div[@class='row']/div[@class='col-md-2'][2]/div/div/div[@tabindex='-1']/ul/li[@class='multiselect__element']//*[text()='Rebounds']")
	rebounds_tab.click()
	time.sleep(1)
	download_link_rebounds = driver.find_element(By.XPATH,"//a[@download='pbpstats_export.csv']")
	download_link_rebounds.click()
	time.sleep(1)
	os.rename('pbpstats_export.csv', 'team_rebounds_'+season+'.csv')

# `````````````````````````````````````````````````````````````````````````````````````````````````````````````````````


# main body

if __name__ == "main":

	chrome_options = webdriver.ChromeOptions()
	download_dir = '/home/chenjie/Desktop/WebScraping/Team_CSVs'
	prefs = {'download.default_directory' : download_dir} # setting download directory
	chrome_options.add_experimental_option('prefs', prefs)  

	driver = webdriver.Chrome('/home/chenjie/Desktop/WebScraping/NBA_PBP/chromedriver',chrome_options=chrome_options) # load Chrome driver here
	team_url = 'https://www.pbpstats.com/totals/nba/team' # initial page url

	year_list = ['2009-10','2010-11','2011-12','2012-13','2013-14','2014-15','2015-16','2016-17','2017-18','2018-19']

	for n in year_list: 

		get_scoring(driver,team_url,n)
		get_assists(driver,team_url,n)
		get_rebounds(driver,team_url,n)




