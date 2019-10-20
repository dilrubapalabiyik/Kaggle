import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import pandas as pd


# class nba_crawler:
	
# 	def __init__(self):
# 		pass

# 	def craw_year(self,categories=category_list, years=year_list): 
# 	# craw year or a list of years, default categories are ['Scoring','Assists','Rebounds'], years are from 2009-10 to 2018-19 season (10 seasons)
# 	# custom categories and years should be imported as list
# 		for y in years:


chrome_options = webdriver.ChromeOptions() 
prefs = {'download.default_directory' : '/home/chenjie/Desktop/WebScraping/Team_CSVs'}
chrome_options.add_experimental_option('prefs', prefs)

os.chdir("/home/chenjie/Desktop/WebScraping/Team_CSVs")
driver = webdriver.Chrome('/home/chenjie/Desktop/WebScraping/NBA_PBP/chromedriver',chrome_options=chrome_options)
team_url = 'https://www.pbpstats.com/totals/nba/team'



year_list = ['2009-10','2010-11','2011-12','2012-13','2013-14','2014-15','2015-16','2016-17','2017-18','2018-19']
category_list = ['Scoring','Assists','Rebounds']





if '2018-19' in year_list:
	driver.get(team_url)
	get_stats = driver.find_element(By.XPATH,"//button[contains(text(),'Get Stats')]")
	time.sleep(1)
	get_stats.click()
	time.sleep(1)

	download_link = driver.find_element(By.XPATH,"//a[@download='pbpstats_export.csv']")
	download_link.click()
	time.sleep(2)
	os.rename('pbpstats_export.csv', 'team_2018-19.csv')


for n in year_list:

	if n == '2018-19':
		continue
	else:
		driver.get(team_url)
		get_stats = driver.find_element(By.XPATH,"//button[contains(text(),'Get Stats')]")
		time.sleep(1)
		get_stats.click()
		time.sleep(1)

		drop_down = driver.find_element(By.XPATH,"//div[@class='col-md-4']/div/div[@tabindex='0']/div[@class='multiselect__select']")
		drop_down.click()
		time.sleep(1)

		choose_season = driver.find_element(By.XPATH,"//div[@class='col-md-4']/div/div/div[@tabindex='-1']/ul/li[@class='multiselect__element']//*[text()='"+n+"']")
		choose_season.click()
		time.sleep(1)

		remove_previous_season = driver.find_element(By.XPATH,"//div[@class='col-md-4']/div/div[@tabindex='0']/div[@class='multiselect__tags']/div/span[1]/span[@class='custom__remove']")
		remove_previous_season.click()
		time.sleep(1)
		drop_down.click()
		time.sleep(1)
		get_stats.click()
		time.sleep(1)


		download_link = driver.find_element(By.XPATH,"//a[@download='pbpstats_export.csv']")
		download_link.click()
		time.sleep(2)
		os.rename('pbpstats_export.csv', 'team_'+n+'.csv')
		time.sleep(1)
