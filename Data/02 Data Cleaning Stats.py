import pandas as pd
import numpy as np
import re
# import Functions


st1 = 'C:/Users/gioek/Programming/MyAnimeList/MyAnimeList2/Data/01 Stats Rest.csv'
st2 = 'C:/Users/gioek/Programming/MyAnimeList/MyAnimeList2/Data/01 Stats Watching-Completed.csv'
Save_Path = 'C:/Users/gioek/Programming/MyAnimeList/Data/02 Anime Stats Cleaned.csv'





st1 = pd.read_csv(st1)
st2 = pd.read_csv(st2)
st2 = st2.drop(columns = ['Flag'], axis=1)

df = pd.merge(st1, st2, on='Title')

# colms = [1,7]





#  Delete DUBLICATES

df = df.drop_duplicates(subset=['Title'])


del st1, st2




df = df[df['Summary_Stats_On_Hold'] != 'SKATA']




# Summary_Stats_Watching
df['Summary_Stats_Watching'] = df['Summary_Stats_Watching'].str.replace(r'\D+', '')
df['Summary_Stats_Watching'] = df['Summary_Stats_Watching'].str.replace(',','').astype('int')

# Summary_Stats_Completed
df['Summary_Stats_Completed'] = df['Summary_Stats_Completed'].str.replace(r'\D+', '')
df['Summary_Stats_Completed'] = df['Summary_Stats_Completed'].str.replace(',','').astype('int')

# Summary_Stats_On_Hold
df['Summary_Stats_On_Hold'] = df['Summary_Stats_On_Hold'].str.replace(r'\D+', '')
df['Summary_Stats_On_Hold'] = df['Summary_Stats_On_Hold'].str.replace(',','').astype('int')

# Summary_Stats_Dropped
df['Summary_Stats_Dropped'] = df['Summary_Stats_Dropped'].str.replace(r'\D+', '')
df['Summary_Stats_Dropped'] = df['Summary_Stats_Dropped'].str.replace(',','').astype('int')

# Summary_Stats_Plan_To_Watch
df['Summary_Stats_Plan_To_Watch'] = df['Summary_Stats_Plan_To_Watch'].str.replace(r'\D+', '')
df['Summary_Stats_Plan_To_Watch'] = df['Summary_Stats_Plan_To_Watch'].str.replace(',','').astype('int')

# Summary_Stats_Total
df['Summary_Stats_Total'] = df['Summary_Stats_Total'].str.replace(r'\D+', '')
df['Summary_Stats_Total'] = df['Summary_Stats_Total'].str.replace(',','').astype('int')



df = df.fillna('0.0% (0 votes)')

# Summary_Stats_10  Summary_Stats_1
df[['Summary_Stats_10', 'Summary_Stats_10_Votes',
    'Summary_Stats_9', 'Summary_Stats_9_Votes',
    'Summary_Stats_8', 'Summary_Stats_8_Votes',
    'Summary_Stats_7', 'Summary_Stats_7_Votes',
    'Summary_Stats_6', 'Summary_Stats_6_Votes',
    'Summary_Stats_5', 'Summary_Stats_5_Votes',
    'Summary_Stats_4', 'Summary_Stats_4_Votes',
    'Summary_Stats_3', 'Summary_Stats_3_Votes',
    'Summary_Stats_2', 'Summary_Stats_2_Votes',
    'Summary_Stats_1', 'Summary_Stats_1_Votes']] = df['Summary_Stats'].str.split(',',expand=True)



df = df.drop(df.columns[5], axis=1)

colms = [7, 9, 11, 13, 15, 17, 19, 21 ,23, 25]
df = df.drop(df.columns[colms], axis=1)

df['Summary_Stats_10_Votes'] = df['Summary_Stats_10_Votes'].replace(np.nan, '0 % 0')
df['Summary_Stats_9_Votes'] = df['Summary_Stats_9_Votes'].replace(np.nan, '0 % 0')
df['Summary_Stats_8_Votes'] = df['Summary_Stats_8_Votes'].replace(np.nan, '0 % 0')
df['Summary_Stats_7_Votes'] = df['Summary_Stats_7_Votes'].replace(np.nan, '0 % 0')
df['Summary_Stats_6_Votes'] = df['Summary_Stats_6_Votes'].replace(np.nan, '0 % 0')
df['Summary_Stats_5_Votes'] = df['Summary_Stats_5_Votes'].replace(np.nan, '0 % 0')
df['Summary_Stats_4_Votes'] = df['Summary_Stats_4_Votes'].replace(np.nan, '0 % 0')
df['Summary_Stats_3_Votes'] = df['Summary_Stats_3_Votes'].replace(np.nan, '0 % 0')
df['Summary_Stats_2_Votes'] = df['Summary_Stats_2_Votes'].replace(np.nan, '0 % 0')
df['Summary_Stats_1_Votes'] = df['Summary_Stats_1_Votes'].replace(np.nan, '0 % 0')

# Summary_Stats_10  Summary_Stats_1
df[['Summary_Stats_10_Percentage', 'Summary_Stats_10_Votes']] = df['Summary_Stats_10_Votes'].str.split('%',expand=True)
df[['Summary_Stats_9_Percentage', 'Summary_Stats_9_Votes']] = df['Summary_Stats_9_Votes'].str.split('%',expand=True)
df[['Summary_Stats_8_Percentage', 'Summary_Stats_8_Votes']] = df['Summary_Stats_8_Votes'].str.split('%',expand=True)
df[['Summary_Stats_7_Percentage', 'Summary_Stats_7_Votes']] = df['Summary_Stats_7_Votes'].str.split('%',expand=True)
df[['Summary_Stats_6_Percentage', 'Summary_Stats_6_Votes']] = df['Summary_Stats_6_Votes'].str.split('%',expand=True)
df[['Summary_Stats_5_Percentage', 'Summary_Stats_5_Votes']] = df['Summary_Stats_5_Votes'].str.split('%',expand=True)
df[['Summary_Stats_4_Percentage', 'Summary_Stats_4_Votes']] = df['Summary_Stats_4_Votes'].str.split('%',expand=True)
df[['Summary_Stats_3_Percentage', 'Summary_Stats_3_Votes']] = df['Summary_Stats_3_Votes'].str.split('%',expand=True)
df[['Summary_Stats_2_Percentage', 'Summary_Stats_2_Votes']] = df['Summary_Stats_2_Votes'].str.split('%',expand=True)
df[['Summary_Stats_1_Percentage', 'Summary_Stats_1_Votes']] = df['Summary_Stats_1_Votes'].str.split('%',expand=True)



df['Summary_Stats_10_Votes'] = df['Summary_Stats_10_Votes'].str.replace(r'\D+', '').astype('int')
df['Summary_Stats_9_Votes'] = df['Summary_Stats_9_Votes'].str.replace(r'\D+', '').astype('int')
df['Summary_Stats_8_Votes'] = df['Summary_Stats_8_Votes'].str.replace(r'\D+', '').astype('int')
df['Summary_Stats_7_Votes'] = df['Summary_Stats_7_Votes'].str.replace(r'\D+', '').astype('int')
df['Summary_Stats_6_Votes'] = df['Summary_Stats_6_Votes'].str.replace(r'\D+', '').astype('int')
df['Summary_Stats_5_Votes'] = df['Summary_Stats_5_Votes'].str.replace(r'\D+', '').astype('int')
df['Summary_Stats_4_Votes'] = df['Summary_Stats_4_Votes'].str.replace(r'\D+', '').astype('int')
df['Summary_Stats_3_Votes'] = df['Summary_Stats_3_Votes'].str.replace(r'\D+', '').astype('int')
df['Summary_Stats_2_Votes'] = df['Summary_Stats_2_Votes'].str.replace(r'\D+', '').astype('int')
df['Summary_Stats_1_Votes'] = df['Summary_Stats_1_Votes'].str.replace(r'\D+', '').astype('int')






# Delete \xa0
df['Summary_Stats_10_Percentage'] = df['Summary_Stats_10_Percentage'].str.extract(r'([0-9]+[,.]+[0-9]+)').astype('float')
df['Summary_Stats_9_Percentage'] = df['Summary_Stats_9_Percentage'].str.extract(r'([0-9]+[,.]+[0-9]+)').astype('float')
df['Summary_Stats_8_Percentage'] = df['Summary_Stats_8_Percentage'].str.extract(r'([0-9]+[,.]+[0-9]+)').astype('float')
df['Summary_Stats_7_Percentage'] = df['Summary_Stats_7_Percentage'].str.extract(r'([0-9]+[,.]+[0-9]+)').astype('float')
df['Summary_Stats_6_Percentage'] = df['Summary_Stats_6_Percentage'].str.extract(r'([0-9]+[,.]+[0-9]+)').astype('float')
df['Summary_Stats_5_Percentage'] = df['Summary_Stats_5_Percentage'].str.extract(r'([0-9]+[,.]+[0-9]+)').astype('float')
df['Summary_Stats_4_Percentage'] = df['Summary_Stats_4_Percentage'].str.extract(r'([0-9]+[,.]+[0-9]+)').astype('float')
df['Summary_Stats_3_Percentage'] = df['Summary_Stats_3_Percentage'].str.extract(r'([0-9]+[,.]+[0-9]+)').astype('float')
df['Summary_Stats_2_Percentage'] = df['Summary_Stats_2_Percentage'].str.extract(r'([0-9]+[,.]+[0-9]+)').astype('float')
df['Summary_Stats_1_Percentage'] = df['Summary_Stats_1_Percentage'].str.extract(r'([0-9]+[,.]+[0-9]+)').astype('float')



df.to_csv(Save_Path, index=False)