from basketball_reference_web_scraper import client
from basketball_reference_web_scraper.data import OutputType

# Get 2017-2018 season totals for all players
client.players_season_totals(season_end_year=2018,output_type=OutputType.CSV,output_file_path='/home/chenjie/Desktop/CSP571/test18.csv')

# The players_season_totals method also supports all output behavior previously described