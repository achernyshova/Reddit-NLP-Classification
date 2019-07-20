import requests
import time
import pandas as pd
import os.path

def load_posts(posts, direction, limit, url):
    headers = {'User-agent': 'Bleep bot 0.1'}
    pagingId = None
    #create while loop, it'll be work until 'after'/'before' gets None
    #it allows me to avoid collecting duplicates
    while True:
        #setting direction 'after'/'before' equal to none
        if pagingId == None:
            params = {'limit': limit}
        else:
            params = {direction: pagingId, 'limit': limit}
        #create request
        res = requests.get(url, params = params, headers=headers)
        #if we don't have errors we collect posts until 'after'/'before' gets None again.
        if res.status_code == 200:
            the_json = res.json()
            posts.extend(the_json['data']['children'])
            if the_json['data'][direction] == None:
                break;
            pagingId = the_json['data'][direction]
        #if we get an error break the loop and print code of an error
        else:
            print(res.status_code)
            break
        time.sleep(3)

def load_subreddit(name):
    posts = [] #create empty list for collecting data
    url = 'https://www.reddit.com/r/' + name + '/new/.json' #create url using an argument name
    #check if there is a file with posts of the subreddit
    #if 'no file' parse all available posts and create new dataframe
    if os.path.exists('/home/ubuntu/project/data/'+ name + '.csv') == False:
        load_posts(posts, 'after', 100, url)
        df = pd.DataFrame([p['data'] for p in posts]).drop_duplicates(subset='name')
    #if there is a file
    #load file, parse new posts, add new posts to existed posts and delete duplicates
    else:
        old_posts_df = pd.read_csv('/home/ubuntu/project/data/'+ name + '.csv')
        old_posts_df.drop(['Unnamed: 0'], axis=1,inplace=True)
        load_posts(posts, 'before', 50, url)
        new_posts_df = pd.DataFrame([p['data'] for p in posts]).drop_duplicates(subset='name')
        df = pd.concat([old_posts_df,new_posts_df]).drop_duplicates(subset='name')
    #save data to csv
    df.to_csv('/home/ubuntu/project/data/'+ name + '.csv')
    #check how many posts we have
    print(name, df.shape)
    return (name, df.shape[0])

def save_stat(stats):
    f = open('/home/ubuntu/project/data/stat.txt','a+')
    f.write('***********' + str(time.ctime())  + os.linesep)
    for stat in stats:
        name = stat[0]
        count = str(stat[1])
        f.write(name +', ' + count + os.linesep)
    f.close() 

sport_topics = ['nba', 'baseball', 'soccer','mls', 'hockey', 'mma', 'boxing', 'FIFA']
other_topics = ['Futurology','AskEngineers','AskReddit','AskScience','History','gameofthrones','gottheories','apple','android','mac','MacSucks','iphone',
'Dogfree','aww','dogs']

stats = []
for x in sport_topics + other_topics:
    stats.append(load_subreddit(x))
save_stat(stats)
