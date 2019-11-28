import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import pandas as pd
import glob


# a bunch of functions 

class WebCrawler:

	def __init__(self,driver,data_level,url):
		"""
		driver: chrome driver object
		data_level: 'Team' or 'Player'
		"""
		self.driver = driver
		self.data_level = data_level
		self.url = url

	def choose_per_game(self,url,season,season_type):

		"""
		this is the prerequisite step for the other steps, since the other dropdowns will appear only after clicking "get stats"
		"""
		self.driver.get(self.url)
		if(season !='2019-20'):   # select season first since it is not equal to the default season
			get_stats = self.driver.find_element(By.XPATH,"//button[contains(text(),'Get Stats')]")
			get_stats.click()
			time.sleep(1)

			year_drop_down = self.driver.find_element(By.XPATH,"//div[@class='col-md-4']/div/div[@tabindex='0']/div[@class='multiselect__select']")
			year_drop_down.click()
			time.sleep(1)

			choose_season = self.driver.find_element(By.XPATH,"//div[@class='col-md-4']/div/div/div[@tabindex='-1']/ul/li[@class='multiselect__element']//*[text()='"+season+"']")
			choose_season.click()
			time.sleep(1)

			remove_previous_season = self.driver.find_element(By.XPATH,"//div[@class='col-md-4']/div/div[@tabindex='0']/div[@class='multiselect__tags']/div/span[1]/span[@class='custom__remove']")
			remove_previous_season.click()
			time.sleep(1)

			year_drop_down.click()
			time.sleep(1)

		get_stats = self.driver.find_element(By.XPATH,"//button[contains(text(),'Get Stats')]")  # after selecting season, generating data, then choose per game tab
		time.sleep(1)
		get_stats.click()
		time.sleep(3)
		stat_type_drop_down = self.driver.find_element(By.XPATH,"//main/div[4]/div[@class='row']/div[@class='col-md-2'][1]/div/div[@tabindex='0']/div[@class='multiselect__select']")
		stat_type_drop_down.click()
		time.sleep(1)
		per_game= self.driver.find_element(By.XPATH,"//main/div[4]/div[@class='row']/div[@class='col-md-2'][1]/div/div/div[@tabindex='-1']/ul/li[@class='multiselect__element']//*[text()='Per Game']")
		per_game.click()


	def get_scoring(self,season,season_type):

		"""
		this is for getting csv for "scoring" category
		"""

		self.choose_per_game(self.url,season,season_type)
		download_link_scoring = self.driver.find_element(By.XPATH,"//a[@download='pbpstats_export.csv']")
		download_link_scoring.click()
		time.sleep(1)
		os.rename('pbpstats_export.csv',self.data_level+'_scoring_'+season+'.csv')
		self.process_csv(self.data_level+'_scoring_'+season+'.csv',season,season_type)


	def get_assists(self,season,season_type):

		"""
		this is for getting csv for "Assists" category
		"""

		self.choose_per_game(self.url,season,season_type)
		table_data_dropdown = self.driver.find_element(By.XPATH,"//main/div[4]/div[@class='row']/div[@class='col-md-2'][2]/div/div[@tabindex='0']/div[@class='multiselect__select']")
		table_data_dropdown.click()
		time.sleep(3)
		assists_tab = self.driver.find_element(By.XPATH,"//main/div[4]/div[@class='row']/div[@class='col-md-2'][2]/div/div/div[@tabindex='-1']/ul/li[@class='multiselect__element']//*[text()='Assists']")
		assists_tab.click()
		time.sleep(3)
		download_link_assists = self.driver.find_element(By.XPATH,"//a[@download='pbpstats_export.csv']")
		download_link_assists.click()
		time.sleep(3)
		os.rename('pbpstats_export.csv', self.data_level+'_assists_'+season+'.csv')
		self.process_csv(self.data_level+'_assists_'+season+'.csv',season,season_type)


	def get_rebounds(self,season,season_type):

		"""
		this is for getting csv for "Rebounds" category
		"""

		self.choose_per_game(self.url,season,season_type)
		table_data_dropdown = self.driver.find_element(By.XPATH,"//main/div[4]/div[@class='row']/div[@class='col-md-2'][2]/div/div[@tabindex='0']/div[@class='multiselect__select']")
		table_data_dropdown.click()
		time.sleep(1)
		rebounds_tab = self.driver.find_element(By.XPATH,"//main/div[4]/div[@class='row']/div[@class='col-md-2'][2]/div/div/div[@tabindex='-1']/ul/li[@class='multiselect__element']//*[text()='Rebounds']")
		rebounds_tab.click()
		time.sleep(1)
		download_link_rebounds = self.driver.find_element(By.XPATH,"//a[@download='pbpstats_export.csv']")
		download_link_rebounds.click()
		time.sleep(1)
		os.rename('pbpstats_export.csv', self.data_level+'_rebounds_'+season+'.csv')
		self.process_csv(self.data_level+'_rebounds_'+season+'.csv',season,season_type)


	def get_stats(self,year,season_type):
		self.get_scoring(year,season_type)
		self.get_assists(year,season_type)
		self.get_rebounds(year,season_type)		


	def process_csv(self,file_name,season,season_type):
		"""
		using pandas open generated csv file and add 2 extra cols, 
		"season","season_type"(we potentially will need both regular season and playoffs)
		"""
		raw_file = pd.read_csv(file_name)
		raw_file['season'] = season
		raw_file['season_type'] = season_type
		raw_file.to_csv(file_name,index=False)


	def csv_concatenation(self):
		scoring_files = [s for s in glob.glob(self.data_level+'*scoring*.csv')]
		combined_scoring_csv = pd.concat([pd.read_csv(s) for s in scoring_files ])
		combined_scoring_csv.to_csv(self.data_level+"_Scoring.csv",index=False)

		assists_files = [s for s in glob.glob(self.data_level+'*assists*.csv')]
		combined_assists_csv = pd.concat([pd.read_csv(s) for s in assists_files ])
		combined_assists_csv.to_csv(self.data_level+"_Assists.csv",index=False)

		rebounds_files = [s for s in glob.glob(self.data_level+'*rebounds*.csv')]
		combined_rebounds_csv = pd.concat([pd.read_csv(s) for s in rebounds_files ])
		combined_rebounds_csv.to_csv(self.data_level+"_Rebounds.csv",index=False)



	
# `````````````````````````````````````````````````````````````````````````````````````````````````````````````````````


# main body

if __name__ == "__main__":

	year_list = ['2009-10']

	chrome_options = webdriver.ChromeOptions()
	download_dir = "/home/chenjie/Desktop/CSP571/Test" # change this to dir where you want to put your data
	os.chdir(download_dir) 
	prefs = {'download.default_directory' : download_dir} # setting download directory
	chrome_options.add_experimental_option('prefs', prefs)  
	chrome_driver = webdriver.Chrome('/home/chenjie/Desktop/CSP571/chromedriver',options=chrome_options) # load Chrome driver here
	
	team_crawler = WebCrawler(driver=chrome_driver,data_level='Team',url='https://www.pbpstats.com/totals/nba/team')
	player_crawler = WebCrawler(driver=chrome_driver,data_level='Player',url='https://www.pbpstats.com/totals/nba/player')
	for y in year_list:
		team_crawler.get_stats(y,'regular season')
		player_crawler.get_stats(y,'regular season')

	team_crawler.csv_concatenation()
	player_crawler.csv_concatenation()
