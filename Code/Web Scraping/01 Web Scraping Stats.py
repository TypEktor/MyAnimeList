# import libraries 
from bs4 import BeautifulSoup
import requests
import pandas as pd
import time


Save_Path = ".../01 Stats Rest.csv"
urlsFile = ".../Page Anime Urls.csv"
# Connect to Website and pull in data
url = "https://myanimelist.net/topanime.php"

start = time.time()

headers1 = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36", "X-Amzn-Trace-Id": "Root=1-612b8224-14c65ade7e3e57ee0168ea6b"}



    
def get_attributes(bs):
    
    Title = [x.get_text() for x in bs.findAll(class_ = "hoverinfo_trigger fl-l fs14 fw-b anime_ranking_h3")]
    Rank = [x.get_text() for x in bs.findAll("td", class_="rank ac")]


    Title = [i.strip() for i in Title]
    Rank = [i.strip() for i in Rank]
            
    Anime_Link = [x.find('a')['href'] for x in bs.findAll(class_ = "hoverinfo_trigger fl-l fs14 fw-b anime_ranking_h3")]
    

    counter = 0
    Summary_Stats_On_Hold = []
    Summary_Stats_Dropped = []
    Summary_Stats_Plan_To_Watch = []
    Summary_Stats_Total = []
    Summary_Stats_10 = []
    Summary_Stats_9 = []
    Summary_Stats_8 = []
    Summary_Stats_7 = []
    Summary_Stats_6 = []
    Summary_Stats_5 = []
    Summary_Stats_4 = []
    Summary_Stats_3 = []
    Summary_Stats_2 = []
    Summary_Stats_1 = []

    for link in Anime_Link:
        
        EpisodesUrl = link + '/stats'
        page = requests.get(EpisodesUrl, headers=headers1)
        bs = BeautifulSoup(page.text, "html.parser")
        

        # For avoiding reCAPTCHA
        test = bs.findAll('div', id="horiznav_nav")
        try:
            test
        except:
            print('A wild reCAPTCHA appeared, wait 5 minited!!')
            del test, page, bs
            time.sleep(300)
            page = requests.get(link, headers=headers1)
            bs = BeautifulSoup(page.text, "html.parser")

        Summary_Stats = [i.get_text() for i in bs.findAll('div', class_="spaceit_pad")]

        
        for stats in Summary_Stats:
            if stats.startswith('On-Hold:'):
                Summary_Stats_On_Hold.append(stats)
            elif stats.startswith('Dropped:'):
                Summary_Stats_Dropped.append(stats)
            elif stats.startswith('Plan to Watch:'):
                Summary_Stats_Plan_To_Watch.append(stats)
            elif stats.startswith('Total:'):
                Summary_Stats_Total.append(stats)
        
            
        Scores1_10 = [i.get_text() for i in bs.findAll('table', class_="score-stats")]
        
        

        for scores in Scores1_10:
            Scores1_10 = list(filter(bool, scores.splitlines()))


            
            try:
                Summary_Stats_10.append(Scores1_10[1])
            except:
                Summary_Stats_10.append('')

            try:
                Summary_Stats_9.append(Scores1_10[3])
            except:
                Summary_Stats_9.append('')
                
            try:
                Summary_Stats_8.append(Scores1_10[5]) 
            except:
                Summary_Stats_8.append('')
                
            try:
                Summary_Stats_7.append(Scores1_10[7])
            except:
                Summary_Stats_7.append('')
                
            try:
                Summary_Stats_6.append(Scores1_10[9]) 
            except:
                Summary_Stats_6.append('')
                
            try:
                Summary_Stats_5.append(Scores1_10[11]) 
            except:
                Summary_Stats_5.append('')
                
            try:
                Summary_Stats_4.append(Scores1_10[13]) 
            except:
                Summary_Stats_4.append('')
                
            try:
                Summary_Stats_3.append(Scores1_10[15]) 
            except:
                Summary_Stats_3.append('')
                
            try:
                Summary_Stats_2.append(Scores1_10[17])  
            except:
                Summary_Stats_2.append('')
                
            try:
                Summary_Stats_1.append(Scores1_10[19]) 
            except:
                Summary_Stats_1.append('')
        
            
        counter += 1
        if counter%10 ==0:
            print(counter)
    
        
        


    rows = pd.DataFrame(
        {'Title': Title,
         'Rank': Rank,
         'Summary_Stats_On_Hold' : Summary_Stats_On_Hold,
         'Summary_Stats_Dropped' : Summary_Stats_Dropped,
         'Summary_Stats_Plan_To_Watch' : Summary_Stats_Plan_To_Watch,
         'Summary_Stats_Total' : Summary_Stats_Total,
         'Summary_Stats_10' : Summary_Stats_10,
         'Summary_Stats_9' : Summary_Stats_9,
         'Summary_Stats_8' : Summary_Stats_8,
         'Summary_Stats_7' : Summary_Stats_7,
         'Summary_Stats_6' : Summary_Stats_6,
         'Summary_Stats_5' : Summary_Stats_5,
         'Summary_Stats_4' : Summary_Stats_4,
         'Summary_Stats_3' : Summary_Stats_3,
         'Summary_Stats_2' : Summary_Stats_2,
         'Summary_Stats_1' : Summary_Stats_1
    })

        
    return rows


rows = pd.DataFrame(
    {'Title': [],
     'Rank': [],
     'Summary_Stats_On_Hold':[],
     'Summary_Stats_Dropped':[],
     'Summary_Stats_Plan_To_Watch':[],
     'Summary_Stats_Total':[],
     'Summary_Stats_10':[],
     'Summary_Stats_9':[],
     'Summary_Stats_8':[],
     'Summary_Stats_7':[],
     'Summary_Stats_6':[],
     'Summary_Stats_5':[],
     'Summary_Stats_4':[],
     'Summary_Stats_3':[],
     'Summary_Stats_2':[],
     'Summary_Stats_1':[]
    })


paths = pd.read_csv(urlsFile, encoding= 'unicode_escape')


for index, url in paths.iterrows():
    
    


    page = requests.get(url['Url'], headers=headers1)
    bs = BeautifulSoup(page.text, "html.parser")
    rows1 = get_attributes(bs)
    frames = [rows, rows1]
    rows = pd.concat(frames, ignore_index=True)


rows.to_csv(Save_Path, index=False)
    