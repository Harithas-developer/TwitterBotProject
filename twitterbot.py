import tweepy
import time

print("hello world")

CONSUMER_KEY="UR0LjluHQL4SlBNoPmCYReMXT"
CONSUMER_SECRET="Y41MTVhhQffULP4t0uVbCU1Lx6btYfeRgmGPH1RjGYGGXWvFYT"
ACCESS_KEY="1284340157001330688-QjSTVjmY6XtKm56lgG0bjRttgtPexY"
ACCESS_SECRET="BdtDO0mcXq7aVYuZz3OzbLs6hWksMio4miPauQKBw2r7j"

auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY,ACCESS_SECRET)
api= tweepy.API(auth)



FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return


def reply_to_tweets():     
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
        # NOTE: We need to use tweet_mode='extended' below to show
        # all full tweets (with full_text). Without it, long tweets
        # would be cut off.
    mentions = api.mentions_timeline(
                            last_seen_id,
                            tweet_mode='extended')

    for mention in reversed(mentions):
            print(str(mention.id) + ' - ' + mention.full_text, flush=True)
            last_seen_id = mention.id
            store_last_seen_id(last_seen_id, FILE_NAME)
            if '#helloword' in mention.full_text.lower():
                print('found #helloworld!', flush=True)
                print('responding back...', flush=True)
                api.update_status('@' + mention.user.screen_name + '#HelloWorld back to you!', mention.id)


while(True):
    reply_to_tweets()
    time.sleep(15)