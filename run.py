import praw
import time

class Bot:
	user_agent = 'Gfycat Link Fixing bot by conogarcia'
	version = '0.1'
	username = ''
	password = ''
	reddit = praw.Reddit(user_agent=user_agent)

	def __init__(self, username=username, password=password):
		self.reddit.login(self.username, self.password)


	def msg(self, user, title ,msg):
		self.reddit.send_message(user, title, msg)


	def listen(self, subreddit):
		for post in self.reddit.get_subreddit(subreddit).get_new(limit=10):
			if post.url[-4:] == '.gif' and 'gfycat' in post.url:
				print post.url, 'incorrect linking in %s' %post.title

				post.add_comment('This post has bad gfy linking.')



Bot().listen(subreddit = 'choripan')