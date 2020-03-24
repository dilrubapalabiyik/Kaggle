# -*- coding: utf-8 -*-
import scrapy
import re

season_regex = re.compile('.*([0-9]{4}-[0-9]{2})') 


class RankCollectoSpider(scrapy.Spider):
	name = 'rank_collecto'

	def __init__(self):
		self.years = ['2010','2011','2012','2013','2014','2015','2016','2017','2018','2019']
		self.league_sub_dir = '/group/league/'
		self.domain = 'http://www.espn.com/nba/standings/_/season/'

	def start_requests(self):
	        for y in self.years:
	            yield scrapy.Request(url=self.domain+y+self.league_sub_dir,callback = self.parse)

	def parse(self, response):
		season_string = response.xpath('//h1[@class="headline headline__h1 dib"]/text()').extract()[0]
		team_names = response.xpath('//div[@class="flex"]/table/tbody/tr')
		teams_stats = response.xpath('//div[@class = "Table__Scroller"]/table/tbody/tr')

		season_name = season_regex.search(season_string).group(1)

		for n in range(0,30):
			team_tag = team_names[n].xpath('.//span[@class = "dn show-mobile"]')
			team_abbr = team_tag.xpath('.//abbr/text()').extract()
			team_stat = teams_stats[n]
			win = team_stat.xpath('.//td[1]/span/text()').extract()
			loss = team_stat.xpath('.//td[2]/span/text()').extract()
			pct = team_stat.xpath('.//td[3]/span/text()').extract()
			home = team_stat.xpath('.//td[5]/span/text()').extract()
			away  = team_stat.xpath('.//td[6]/span/text()').extract()
			div = team_stat.xpath('.//td[7]/span/text()').extract()
			conf = team_stat.xpath('.//td[8]/span/text()').extract()
			ppg = team_stat.xpath('.//td[9]/span/text()').extract()
			opp_ppg = team_stat.xpath('.//td[10]/span/text()').extract()
			diff = team_stat.xpath('.//td[11]/span/text()').extract()

			yield{'season_name': season_name,
			'team_name': team_abbr,
			 'win':win,
			 'loss':loss,
			 'pct':pct,
			 'home':home,
			 'away':away,
			 'div':div,
			 'conf': conf, 
			 'ppg': ppg,
			 'opp_ppg':opp_ppg,
			 'diff':diff
			}