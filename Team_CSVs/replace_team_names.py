import pandas as pd 

replace_rank_dict ={
'GS':'GSW',
'NJ':'BKN',
'NY':'NYK',
'SA':'SAS',
'UTAH':'UTA',
'WSH':'WAS'
}


ranks = pd.read_csv('/home/chenjie/Desktop/CSP571/Team_Ranks/rank_result_raw.csv')

ranks['team_name'] = ranks['team_name'].replace(replace_rank_dict)

ranks.to_csv('/home/chenjie/Desktop/CSP571/Team_Ranks/rank_result_cleaned.csv',index=False)