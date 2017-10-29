from twitter import *

t = Twitter(auth=OAuth('122479502-v3zaf7X5YAdVC701ob4FPYEEdQIzSMEQ56hwJa5b',
                       '3xFzlb4NuJrP5t2y1BWlyu1MgExe0VvLPFLisJBCgmQef',
                       'GL8eSnBLjH5gGCdfvu3fDOMLg',
                       'huBPaRIw0tR2ARbKbOMqGjuB2QU6OQU7LcdVt4o69gBaOurXej'))

pythonStatuses = t.statuses.user_timeline(screen_name='montypython', count=5)

print(pythonStatuses)
# pythonTweets = t.search.tweets(q='#python')
# print(pythonTweets)




