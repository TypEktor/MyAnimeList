# import libraries 
from bs4 import BeautifulSoup
import requests
import pandas as pd
import time


Save_Path = ".../01 Anime Basics.csv"
urlsFile = ".../Page Anime Urls.csv"

# Connect to Website and pull in data
url = "https://myanimelist.net/topanime.php"


# Use two different Agents
headers1 = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36", "X-Amzn-Trace-Id": "Root=1-612b8224-14c65ade7e3e57ee0168ea6b"}
headers2 ={"User-Agent": "Bot of the gods"}


    
def get_attributes(bs):
    
    # 01 Get all the available data from this page. Getting these Data for all 50 Anime
    Title = [x.get_text() for x in bs.findAll(class_ = "hoverinfo_trigger fl-l fs14 fw-b anime_ranking_h3")]
    Info = [x.get_text() for x in bs.findAll("div", class_="information di-ib mt4")]
    Score = [x.get_text() for x in bs.findAll("div", class_="js-top-ranking-score-col di-ib al")]
    Rank = [x.get_text() for x in bs.findAll("td", class_="rank ac")]


    Info1 = [i.split("\n") for i in Info]
    Type_Ep = []
    Date = []
    Members = []
    for i in Info1:
        Type_Ep.append(i[1].strip())
        Date.append(i[2].strip())
        Members.append(i[3].strip())


    Type_Ep = [i.split(" ") for i in Type_Ep]

    Anime_Type = []
    Number_of_Episodes = []
    for i in Type_Ep:
        Anime_Type.append(i[0])
        Number_of_Episodes.append(i[1])

    Title = [i.strip() for i in Title]
    Score = [i.strip() for i in Score]
    Rank = [i.strip() for i in Rank]
            
    # 02 Moving on to the next page for getting more data for each specific Anime
    Anime_Link = [x.find('a')['href'] for x in bs.findAll(class_ = "hoverinfo_trigger fl-l fs14 fw-b anime_ranking_h3")]
    
    Score_Users = []
    Season = []
    Popularity = []
    Image = []
    Synopsis = []
    English_Title = []
    Status = []
    Broadcast = []
    Producers = []
    Licensors = []
    Studios = []
    Source = []
    Genres = []
    Duration = []
    Rating = []
    Favorites = []
    Related_Anime = []
    Openings = []
    Endings = []

    counter = 0
    
    # This will run 50 times
    for link in Anime_Link:
        
        page = requests.get(link, headers=headers1)
        bs = BeautifulSoup(page.text, "html.parser")
        
        # For avoiding reCAPTCHA
        test = bs.find('div', style="width: 225px")
        try:
           test = test.get_text() 
        except:
            print('A wild reCAPTCHA appeared, wait 5 minited!!')
            del test, page, bs
            time.sleep(300)
            page = requests.get(link, headers=headers1)
            bs = BeautifulSoup(page.text, "html.parser")
        

        # Users
        temp = bs.find('div',itemprop="aggregateRating")
        try:
            temp = temp.find(style='display: none').contents[0]
            Score_Users.append(temp)
        except:
            Score_Users.append(-1)


        # Season
        temp = bs.find('span', class_="information season")
        try:
            temp = temp.find('a').contents[0]
            Season.append(temp)
        except:
            Season.append("N/A")
        

        # # Popularity
        temp = bs.find('span', class_="numbers popularity")
        try:
            temp = temp.find('strong').contents[0]
            Popularity.append(temp)
        except:
            Popularity.append("-1")


        # Image
        temp = bs.find('div', style="text-align: center;")
        try:
            temp = temp.find('img')['data-src']
            Image.append(temp)
        except:
            Image.append("Ν/Α")

            
        # Synopsis
        temp = bs.find('p', itemprop="description")
        try:
            temp = temp.get_text()
            Synopsis.append(temp)
        except:
            Synopsis.append("Ν/Α")
        
        
        temp = bs.find('div', style="width: 225px")
        temp = temp.get_text() 
        list_of_words = temp.split('\n')   
        
        # English_Title
        English_Title_temp = 'N/A'
        for string in list_of_words:
            if string.startswith("English:"):
                English_Title_temp = string
        English_Title.append(English_Title_temp)
        
    
        # Status
        try:
            temp = list_of_words[list_of_words.index('Aired:') - 3]
            Status.append(temp)
        except:
            Status.append("Ν/Α")
            
         # Broadcast
        try:
            temp = list_of_words[list_of_words.index('Broadcast:') + 1]
            Broadcast.append(temp)
        except:
            Broadcast.append("Ν/Α")
        
        
        # Producers
        try:
            temp = list_of_words[list_of_words.index('Producers:') + 1]
            Producers.append(temp)
        except:
            Producers.append("Ν/Α")

        
        # Licensors
        try:
            temp = list_of_words[list_of_words.index('Licensors:') + 1]
            Licensors.append(temp)
        except:
            Licensors.append("Ν/Α")

        
        # Studios
        try:
            temp = list_of_words[list_of_words.index('Studios:') + 1]
            Studios.append(temp)
        except:
            Studios.append("Ν/Α")
            
            
        # Source
        try:
            temp = list_of_words[list_of_words.index('Source:') + 1]
            Source.append(temp)
        except:
            Source.append("Ν/Α")
            
            
        # Genres
        try:
            temp = list_of_words[list_of_words.index('Genres:') + 1]
            Genres.append(temp)
        except:
            Genres.append("Ν/Α")
            
        # Duration
        try:
            temp = list_of_words[list_of_words.index('Duration:') + 1]
            Duration.append(temp)
        except:
            Duration.append("Ν/Α")
            
            
     # Rating
        try:
            temp = list_of_words[list_of_words.index('Rating:') + 1]
            Rating.append(temp)
        except:
            Rating.append("Ν/Α")

         # Favorites
        try:
            temp = list_of_words[list_of_words.index('Favorites:') + 1]
            Favorites.append(temp)
        except:
            Favorites.append("Ν/Α")
            
            
            
        # Related_Anime
        temp = bs.find('table', class_="anime_detail_related_anime")
        
        try:
            temp1 = temp.get_text(separator='\n')
            Related_Anime.append(temp1)
        except:
            Related_Anime.append(temp)


        # Openings
        temp = bs.find('div', class_="theme-songs js-theme-songs opnening")
        try:
            Openings1 = temp.findAll('span', class_="theme-song")
            Openings1 = [x.get_text() for x in Openings1]
        except:
            Openings1 = ''
        Openings.append(Openings1)
        
        # Ending
        temp = bs.find('div', class_="theme-songs js-theme-songs ending")
        try:
            Endings1 = temp.findAll('span', class_="theme-song")
            Endings1 = [x.get_text() for x in Endings1]
        except:
            Endings1 = ''
        Endings.append(Endings1)

        # For getting live feedback of what is happening
        counter += 1
        print(counter)
    
        
        
    try:
        rows = pd.DataFrame(
        {'Title': Title,
         'Score': Score,
         'Rank': Rank,
         'Date': Date,
         'Members': Members,
         'Number_of_Episodes': Number_of_Episodes,
         'Anime_Type': Anime_Type,
         'Anime_Link': Anime_Link,
          'Score_Users': Score_Users,
          'Season': Season,
          'Popularity': Popularity,
          'Image': Image,
          'Synopsis': Synopsis,
          'English_Title': English_Title,
          'Status': Status,
          'Broadcast': Broadcast,
          'Producers':Producers,
          'Licensors':Licensors,
          'Studios':Studios,
          'Source':Source,
          'Genres':Genres,
          'Duration':Duration,
          'Rating':Rating,
          'Favorites':Favorites,
          'Openings':Openings,
          'Endings':Endings
        })
        
    except:
        rows = pd.DataFrame(
        {'Title': Title,
         'Score': Score,
         'Rank': Rank,
         'Date': Date,
         'Members': Members,
         'Number_of_Episodes': Number_of_Episodes,
         'Anime_Type': Anime_Type,
         'Anime_Link': Anime_Link,
          'Score_Users': Score_Users,
          'Season': Season,
          'Popularity': Popularity,
          'Image': Image,
          'Synopsis': Synopsis,
          'English_Title': English_Title,
          'Status': Status,
          'Broadcast': Broadcast,
          'Producers':Producers,
          'Licensors':Licensors,
          'Studios':Studios,
          'Source':Source,
          'Genres':Genres,
          'Duration':Duration,
          'Rating':Rating,
          'Favorites':Favorites,
          'Openings':Openings,
          'Endings':Endings
        })
    return rows


rows = pd.DataFrame(
    {'Title': [],
     'Score': [],
     'Rank': [],
     'Date': [],
     'Members': [],
     'Number_of_Episodes': [],
     'Anime_Type': [],
     'Anime_Link': [],
      'Score_Users': [],
      'Season': [],
      'Popularity': [],
      'Image': [],
      'Synopsis': [],
      'English_Title': [],
      'Status': [],
      'Broadcast': [],
      'Producers':[],
      'Licensors':[],
      'Studios':[],
      'Source':[],
      'Genres':[],
      'Duration':[],
      'Rating':[],
      'Favorites':[],
      'Openings':[],
      'Endings':[]

    })


paths = pd.read_csv(urlsFile, encoding= 'unicode_escape')

# Running for each group of 50 Anime
for index, url in paths.iterrows():
    
    page = requests.get(url['Url'], headers=headers1)
    bs = BeautifulSoup(page.text, "html.parser")
    rows1 = get_attributes(bs)
    frames = [rows, rows1]
    rows = pd.concat(frames, ignore_index=True)
    
    
rows.to_csv(Save_Path, index=False)