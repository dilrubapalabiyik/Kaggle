# CSP571
This is the repo for the project of CSP571

# Phase 1: Database Creation
* Schema are defined based on [Basketbal PBP site](https://www.pbpstats.com)
* Postgres database 
* get a copy!
    * use command below to "restore"  `.sql file` to get a copy for yourself!
~~~shell
psql -h <hostname> -p <port> -U <username> -d <your precreated db name> < <your .sql file dir>
~~~

FYI, pg_dump:

~~~shell
pg_dump -h <hostname> -p <port> -U <username> -t(optional if only dump certain table) <tablename> <dbname> > <filename>
~~~

# Phase 2: Webscraping
* We had 2 data sources to scrape from:
    * [Basketbal PBP site for average stats](https://www.pbpstats.com)
        * Selenium
    * [ESPN NBA site for team win ratios](https://www.espn.com/nba/standings/_/season/)
        * Scrapy