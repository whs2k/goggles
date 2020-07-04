import requests
import pandas as pd
import tweepy #for twitter
import os
import constants
#from bs4 import BeautifulSoup
#import praw #for reddit
#import requests
#import requests.auth

def getTweetsBySearch(search_terms=['counterfeit','amazonHelp']):
	consumer_key = '6CM1Yqk0Qz6KUXsDQUS8xmahS'
	consumer_secret = 'LMSBfoJWMTlder205Ihr2t1JDgwJD2XgKQeWYau25gJix4lm24'
	access_token = '753302551840198656-Qx1HSVIZlqjShSsUeWY4BhRaVEbWVAP'
	access_token_secret = 'iwtFUe30YrmDlMyGACLLNYrpZQutuW2e8QzX03YwOlz97'
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)


	cfit_tweets = api.search(q=search_terms, count=1000)

	df = pd.DataFrame()
	df['text'] = [x.text for x in cfit_tweets]
	df['source'] = ['twitter: "counterfiet, amazonelp"' for x in cfit_tweets]
	df['url'] = [x.text[x.text.find('http'):].split('\n')[0] for x in cfit_tweets]
	df['retweets'] = [x.retweet_count for x in cfit_tweets]
	df['favorites'] = [x.favorite_count for x in cfit_tweets]
	df['iframe'] = ['https://twitframe.com/show?url=https://twitter.com/{}/status/{}'.format(x.user.screen_name, x.id) for x in cfit_tweets]

	keys = ['t'+str(x) for x in range(len(df['iframe'].tolist()))]
	values = list(set(df['iframe'].tolist()))
	return dict(zip(keys, values))

def getHomeTimeline_df(user_name='twttter'):
	consumer_key = constants.API_key#'6CM1Yqk0Qz6KUXsDQUS8xmahS'
	consumer_secret = constatnts.API_secret_key#'LMSBfoJWMTlder205Ihr2t1JDgwJD2XgKQeWYau25gJix4lm24'
	access_token = #'753302551840198656-Qx1HSVIZlqjShSsUeWY4BhRaVEbWVAP'
	access_token_secret = #'iwtFUe30YrmDlMyGACLLNYrpZQutuW2e8QzX03YwOlz97'
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)


	homePage_tweets = api.home_timeline(id=user_name, count=1000)

	df = pd.DataFrame()
	df['text'] = [x.text for x in homePage_tweets]
	#df['source'] = ['twitter: "counterfiet, amazonelp"' for x in cfit_tweets]
	df['url'] = [x.text[x.text.find('http'):].split('\n')[0] for x in homePage_tweets]
	df['retweets'] = [x.retweet_count for x in homePage_tweets]
	df['favorites'] = [x.favorite_count for x in homePage_tweets]
	df['iframe'] = ['https://twitframe.com/show?url=https://twitter.com/{}/status/{}'.format(x.user.screen_name, x.id) for x in homePage_tweets]

	keys = ['t'+str(x) for x in range(len(df['iframe'].tolist()))]
	values = list(set(df['iframe'].tolist()))
	return df

def getReddits():
	'''
	#1. Get Token
	client_auth = requests.auth.HTTPBasicAuth('BXTDVNZqv8SFyw', 'LQtvysbgBqkh-Zjwl1XyLZMdoD4')
	post_data = {"grant_type": "password", "username": "whs2k", "password": "osrno1"}
	headers = {"User-Agent": "ChangeMeClient/0.1 by YourUsername"}
	response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)
	#response.json()


	#2. Use Token 
	headers = {"Authorization": "bearer 56034692712-UGJkxFNvT1OAn_LGs3XOO645V5Y", "User-Agent": "ChangeMeClient/0.1 by YourUsername"}
	response = requests.get("https://oauth.reddit.com/api/v1/me", headers=headers)
	#response.json()
	'''

	reddit = praw.Reddit(client_id='BXTDVNZqv8SFyw',
                     client_secret='LQtvysbgBqkh-Zjwl1XyLZMdoD4',
                     password='osrno1',
                     user_agent='testscript by /u/whs2k',
                     username='whs2k')
	if reddit.read_only:
		print('We Are Connected to Reddit!')

	#search terms controversial, gilded, hot, new, rising, top'''
	png_urls = [x.url for x in reddit.subreddit('FulfillmentByAmazon').new(limit=500) if '.png' in x.url]
	title_txts = [x.title for x in reddit.subreddit('FulfillmentByAmazon').new(limit=500) if '.png' in x.url]
	print('We have {} png urls'.format(len(png_urls)))

	png_keys = ['r'+str(x) for x in range(len(png_urls))]
	title_keys = ['r_title'+str(x) for x in range(len(title_txts))]
	return dict(zip(png_keys, png_urls)), dict(zip(title_keys, title_txts))


def getTweetsDF():
	consumer_key = '6CM1Yqk0Qz6KUXsDQUS8xmahS'
	consumer_secret = 'LMSBfoJWMTlder205Ihr2t1JDgwJD2XgKQeWYau25gJix4lm24'
	access_token = '753302551840198656-Qx1HSVIZlqjShSsUeWY4BhRaVEbWVAP'
	access_token_secret = 'iwtFUe30YrmDlMyGACLLNYrpZQutuW2e8QzX03YwOlz97'
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)


	cfit_tweets = api.search(q=['counterfeit','amazonHelp'], count=1000)
	fake_tweets = api.search(q=['fake','amazonHelp'], count=1000)

	df = pd.DataFrame()
	df['text'] = [x.text for x in cfit_tweets]
	df['source'] = ['twitter: "counterfiet, amazonelp"' for x in cfit_tweets]
	df['url'] = [x.text[x.text.find('http'):].split('\n')[0] for x in cfit_tweets]
	df['retweets'] = [x.retweet_count for x in cfit_tweets]
	df['favorites'] = [x.favorite_count for x in cfit_tweets]
	df['iframe'] = ['https://twitframe.com/show?url=https://twitter.com/{}/status/{}'.format(x.user.screen_name, x.id) for x in cfit_tweets]

	df1 = pd.DataFrame()
	df1['text'] = [x.text for x in fake_tweets]
	df1['source'] = ['twitter: "fake, amazonHelp"' for x in fake_tweets]
	df1['url'] = [x.text[x.text.find('http'):].split('\n')[0] for x in fake_tweets]
	df1['retweets'] = [x.retweet_count for x in fake_tweets]
	df1['favorites'] = [x.favorite_count for x in fake_tweets]
	df1['iframe'] = ['https://twitframe.com/show?url=https://twitter.com/{}/status/{}'.format(x.user.screen_name, x.id) for x in fake_tweets]


	df_final = df.append(df1)
	df_final.sort_values('retweets',ascending=False).drop_duplicates(['text','source']).reset_index().head(50)

	keys = ['t1', 't2']
	keys = ['t'+str(x) for x in range(len(df1['iframe'].tolist()))]
	values = df1['iframe'].tolist()
	return dict(zip(keys, values))

