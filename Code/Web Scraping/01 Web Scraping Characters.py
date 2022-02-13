# import libraries 
from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
from bs4 import SoupStrainer

import Functions




urlsFile = ".../Page Anime Urls.csv"
Save_Path = ".../01 Anime Characters.csv"


start = time.time()

# Use two different Agents
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36", "X-Amzn-Trace-Id": "Root=1-612b8224-14c65ade7e3e57ee0168ea6b"}
headers2 = {'User-agent': 'Super Bot Power Level Over 9000'}         

    

    
def get_attributes(bs, index):
    Title = [x.get_text() for x in bs.findAll(class_ = "hoverinfo_trigger fl-l fs14 fw-b anime_ranking_h3")]
    Rank = [x.get_text() for x in bs.findAll("td", class_="rank ac")]

    # 50 Anime per page
    Anime_Link = [x.find('a')['href'] for x in bs.findAll(class_ = "hoverinfo_trigger fl-l fs14 fw-b anime_ranking_h3")]
    
    index_Flag, rowsFinal, Character, Role, Favorites, Voice_Actor, Nationality = [], [], [], [], [], [], []

    # only_tags = SoupStrainer('div')
    for link in Anime_Link:
        
        
        CharactersUrl = link + '/characters'
        
        requests_session = requests.Session()
        page = requests_session.get(CharactersUrl)
        bs = BeautifulSoup(page.text, "html.parser")
        

        Character1 = [i.get_text() for i in bs.findAll('div', class_="js-chara-roll-and-name")]
        if not Character1:
            Character.append('')
        else:
            Character.append(Character1)

        Favorites1 = [i.get_text() for i in bs.findAll('div', class_="js-anime-character-favorites")]
        if not Favorites1:
            Favorites.append(-1)
        else:
            Favorites.append(Favorites1)


        Nationality1 = [i.get_text() for i in bs.findAll('div', class_="spaceit_pad js-anime-character-language")]
        if not Nationality1:
            Nationality.append('')
        else:
            Nationality.append(Nationality1) 

        Voice_Actor1 = [i.get_text() for i in bs.findAll(class_="js-anime-character-va")]
        if not Voice_Actor1:
            Voice_Actor.append('')
        else:
            Voice_Actor.append(Voice_Actor1)

        Role1 = [i.get_text() for i in bs.findAll(class_="js-anime-character-table")]
        if not Role1:
            Role.append('')
        else:
            Role.append(Role1)
        index_Flag.append(index)

    rows = [Title, Rank, Character, Favorites, Voice_Actor, Nationality, Role, index_Flag]
    rowsFinal.append(rows)
    
    # Fastest approach to unpack the list of lists
    finall = Functions.flatten(rowsFinal)
    

    Title = finall[0]
    Rank = finall[1]
    Character = finall[2]
    Favorites = finall[3]
    Voice_Actor = finall[4]
    Nationality = finall[5]
    Role = finall[6]
    index_Flag = finall[7]


    TitleN, RankN, CharacterN, FavoritesN, Voice_ActorN, index_FlagN = [], [], [], [], [], []
    

    
    counter = 0
    for title in Title: # gia kathe anime
        counter2 = 0
        if not Character[counter]:
            TitleN.append(title)
            RankN.append(Rank[counter])
            CharacterN.append('')
            FavoritesN.append(-1)
            Voice_ActorN.append('')
            index_FlagN.append(index_Flag[counter])
        else:
            for char in Character[counter]: # gia kathe xarakthra
                TitleN.append(title)
                RankN.append(Rank[counter])
                CharacterN.append(char)
                FavoritesN.append(Favorites[counter][counter2])
                Voice_ActorN.append(Voice_Actor[counter][counter2])
                index_FlagN.append(index_Flag[counter])
                counter2 += 1
        
        counter += 1


    Anime_Characters = pd.DataFrame(
        {'Title': TitleN,
         'Rank': RankN,
         'Character': CharacterN,
         'Favorites': FavoritesN,
         'Voice_Actors':Voice_ActorN,
         'Index_Flag':index_FlagN
         })

    return Anime_Characters
    


Anime_Characters = pd.DataFrame(
        {'Title': [],
         'Rank': [],
         'Character': [],
         'Favorites': [],
         'Voice_Actors':[]
         })

paths = pd.read_csv(urlsFile, encoding= 'unicode_escape')



for index, url in paths.iterrows():
    t0 = time.time()
        
        
    only_a_tags = SoupStrainer("a")

    requests_session = requests.Session()
    page = requests_session.get(url['Url'])
    bs = BeautifulSoup(page.text, "html.parser")
        
    Anime_Characters1 = get_attributes(bs, index)
    frames = [Anime_Characters, Anime_Characters1]
    Anime_Characters = pd.concat(frames, ignore_index=True)
        
    requests_session = requests.Session()
    page = requests_session.get(url['Url'])
    bs = BeautifulSoup(page.text, "html.parser")
    
    Anime_Characters1 = get_attributes(bs,index)
    frames = [Anime_Characters, Anime_Characters1]
    Anime_Characters = pd.concat(frames, ignore_index=True)

        

Anime_Characters.to_csv(Save_Path, index=False)