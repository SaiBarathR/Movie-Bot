import json
import requests
mov_ls = []
def get_deets(name,year,rp):
    if(rp == 1):
        mov_ls = []
        deets = get_url("http://www.omdbapi.com/?apikey=[Your API Key]&s="+name)
        js = json.loads(deets)
        for i in range (len(js['Search'])):
            if(str(js['Search'][i]['Type']) != 'game'):
                mov_ls.append(str(js['Search'][i]['Title'])+ "--" + str(js['Search'][i]['Year']) + "--"+str(js['Search'][i]['Type']))
        return mov_ls
    elif(rp == 2 and year != -1):
        deets = get_url("http://www.omdbapi.com/?apikey=[Your API Key]&t=" + name + "&y=" + year)
        js = json.loads(deets)
        return get_str(js)

def convert_to_str(movie_list):
    st = ""
    for i in range(len(movie_list)):
        st = st + movie_list[i] + "\n"

    return st


def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_str(movie):
    for i in range(len(movie)):
        if movie[list(movie.keys())[i]] == "N/A":
            movie[list(movie.keys())[i]] = "Not Available"

    req = ['Title', 'Type', 'Year', 'Rated', 'Released', 'Runtime', 'Genre', 'Director', 'Writer', 'Actors', 'Plot',
           'Language', 'Awards']
    l = []
    for i in range(len(req)):
        if req[i] == 'Type':
            l.append("\n" + str(req[i]) + " : " + str(movie[req[i]]).capitalize())
        else:
            l.append("\n" + str(req[i]) + " : " + str(movie[req[i]]))

    st = ""
    for i in range(len(l)):
        st = st + l[i] + "\n"
    return st + "\nFind more at imdb.com"
def split_title(movie):
    a = movie.split(", ")
    return a
