from psaw import PushshiftAPI
import datetime as dt 


api = PushshiftAPI()

start_epoch = int(dt.datetime(2021, 1, 30).timestamp())

submissions = list(api.search_submissions(after = start_epoch,
                            subreddit='politics',
                            filter = ['url', 'author', 'title', 'subreddit'],
                            limit=10))

for i,t in enumerate(submissions):
    print(i, t)
    print('#############')



# send contents to file "python search_page.py >> <filename.txt>"
