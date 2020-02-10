def org_tweets(fetched_tweets_file) :
    tweetDB = open(fetched_tweets_file, "r")
    for line in tweetDB :
        element = line.split(',"text":"')[1].split('","screen_name')[0]
        print(element)
        print()

fetched_tweets_file = "tweets.txt"

org_tweets(fetched_tweets_file)
