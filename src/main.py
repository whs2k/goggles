from flask import Flask, redirect, render_template
import os
import helper

app = Flask(__name__)

#https://twitter.com/rufnknme/status/1066006390680866816
@app.route('/')
def carousel():
	return render_template('hello.html')

@app.route('/twitter/')
def carousel_t():
	twitter_handle = 'theebillyporter'#'whs2k'
	df_echo = helper.getHomeTimeline_df(user_name=twitter_handle)
	keys = ['t'+str(x) for x in range(len(df_echo['iframe'].tolist()))]
	values = list(set(df_echo['iframe'].tolist()))
	twit_url_dict = dict(zip(keys, values))
	return render_template('carousel_t.html', **twit_url_dict,
							h2='Goggles',
							h3=twitter_handle)


'''

def goToInsta(hashtag='fakeamazon'):
	return redirect("https://www.instagram.com/explore/tags/fakeamazon/?hl=en",
		code=302)
twit_url_dict = getTweets(search_terms=['amazonHelp', 'counterfeit']) #keys = [t1,t2,t3....]s
red_png_dict, red_title_dict = getReddits() #keys = r1. r2 ... titleKepys = r_title1,

#https://twitter.com/rufnknme/status/1066006390680866816
@app.route('/')
def carousel():
	return render_template('hello.html')

@app.route('/taxi/')
def carousel_ex_taxi():
	return render_template('ex_taxi.html')

@app.route('/twitter/')
def carousel_t():
	return render_template('carousel_t.html', **twit_url_dict)

@app.route('/reddit/')
def carousel_r():
	return render_template('carousel_r.html', 
							**red_png_dict, **red_title_dict)
def goToInsta(hashtag='fakeamazon'):
	return redirect("https://www.instagram.com/explore/tags/fakeamazon/?hl=en",
		code=302)'''


if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5005))
	app.run(debug=True, port=port) #host='0.0.0.0', port=9999