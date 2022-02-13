# import libraries 
from bs4 import BeautifulSoup
import requests
import pandas as pd



# Csv containing the link for each group of Anime. Each group contains 50 Anime 
urlsFile = ".../00 Page Anime Urls.csv"
# Path for saving the link for each Anime
Save_Path = ".../00 All Anime Urls.csv"


# Function for getting the Data
def get_attributes(bs, index):
    Title = [x.get_text() for x in bs.findAll(class_ = "hoverinfo_trigger fl-l fs14 fw-b anime_ranking_h3")]
    Rank = [x.get_text() for x in bs.findAll("td", class_="rank ac")]
    # 50 Anime per page
    Anime_Urls = [x.find('a')['href'] for x in bs.findAll(class_ = "hoverinfo_trigger fl-l fs14 fw-b anime_ranking_h3")]

    href = pd.DataFrame(
        {'Title':Title,
         'Rank':Rank,
         'Anime_Urls': Anime_Urls})
    return href
    

# An empty dataframe, for initially concat the exctracted data
href = pd.DataFrame(
        {'Title':[],
         'Rank':[],
         'Anime_Urls': []})


paths = pd.read_csv(urlsFile, encoding= 'unicode_escape')


# For each group of Anime
for index, url in paths.iterrows():
    requests_session = requests.Session()
    page = requests_session.get(url['Url'])
    bs = BeautifulSoup(page.text, "html.parser")
        
    href1 = get_attributes(bs, index)
    frames = [href, href1]
    href = pd.concat(frames, ignore_index=True)
        


    print(index)




href.to_csv(Save_Path, index=False)
