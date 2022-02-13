# import libraries 
from bs4 import BeautifulSoup
import requests
import pandas as pd
import time


Save_Path = ".../01 Stats Watching-Completed.csv"
urlsFile = ".../Page Anime sUrls.csv"

# Connect to Website and pull in data
url = "https://myanimelist.net/topanime.php"

# start = time.time()

headers1 = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36", "X-Amzn-Trace-Id": "Root=1-612b8224-14c65ade7e3e57ee0168ea6b"}



    
def get_attributes(bs, index):
    
    Title = [x.get_text() for x in bs.findAll(class_ = "hoverinfo_trigger fl-l fs14 fw-b anime_ranking_h3")]
    Title = [i.strip() for i in Title]
            
    Anime_Link = [x.find('a')['href'] for x in bs.findAll(class_ = "hoverinfo_trigger fl-l fs14 fw-b anime_ranking_h3")]
    


    Summary_Stats_Watching = []
    Summary_Stats_Completed = []


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
            if stats.startswith('Watching:'):
                Summary_Stats_Watching.append(stats)
            elif stats.startswith('Completed:'):
                Summary_Stats_Completed.append(stats)

    
        
    rows = pd.DataFrame(
    {'Title': Title,
        'Summary_Stats_Watching' : Summary_Stats_Watching,
        'Summary_Stats_Completed' : Summary_Stats_Completed
    })

        
    return rows


rows = pd.DataFrame(
    {'Title': [],
     'Summary_Stats_Watching':[],
     'Summary_Stats_Completed':[]
    })


paths = pd.read_csv(urlsFile, encoding= 'unicode_escape')


for index, url in paths.iterrows():
    
    
    if index in list:
        print(index)
        t0 = time.time()
        page = requests.get(url['Url'], headers=headers1)
        bs = BeautifulSoup(page.text, "html.parser")
        rows1 = get_attributes(bs, index)
        frames = [rows, rows1]
        rows = pd.concat(frames, ignore_index=True)
        end = time.time()
        print(f"Runtime of iteration: {index}  is  {end - t0}")
        rows.to_csv(Save_Path, index=False)

    


        



rows.to_csv(Save_Path, index=False)
    