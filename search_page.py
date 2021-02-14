from psaw import PushshiftAPI
import datetime as dt
import config
import psycopg2
import psycopg2.extras

connection = psycopg2.connect(host=config.DB_HOST, database=config.DB_NAME, user=config.DB_USER, password=config.DB_PASS)
# Dictionary cursor to loop through results as a dictionary
cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
cursor.execute("""
    SELECT * FROM stock
""")
rows = cursor.fetchall()
print(rows)

# stocks = {}
# for row in rows:
#     stocks['$' + row['symbol']] = row['id']

# api = PushshiftAPI()

# start_epoch = int(dt.datetime(2021, 2, 10).timestamp())

# """
# Old Version using list
# submissions = list(api.search_submissions(after = start_epoch,
#                             subreddit='politics',
#                             filter = ['url', 'author', 'title', 'subreddit'],
#                             limit=10))
# """

# submissions = api.search_submissions(after = start_epoch,
#                             subreddit = 'soccer',
#                             filter = ['url', 'author', 'title', 'subreddit'])

# for sub in submissions:
#     words = sub.title.split()
#     name_tags = list(set(filter(lambda word: word.lower().startswith('[optajose]'), words)))

#     if len(name_tags) > 0:
#         print(name_tags)
#         print(sub.title)


# send contents to file "python search_page.py >> <filename.txt>"