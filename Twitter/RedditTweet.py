################################
## Sheev Bot For Twitter v1.0 ##
################################

#Written by bobvader2001

import requests
import json
import twitter
import schedule
import time

#JSON File Request
def requestJson():
	while(True):
		print("Requesting JSON File...")
		try:
			input_request = requests.get("https://reddit.com/r/prequelmemes/hot.json", headers={"User-agent":"Sheev Bot v1.0"})
			break
		except:
			print("Failed.\nRetrying In 1 Minute.\n")
			time.sleep(60)
			continue

	print("Success!\n")
	return input_request


#Tweet The Post
def tweetPost(url, title, author, upvotes, post_counter, api):
	positions = {2:"2nd", 3:"3rd", 4:"4th", 5:"5th", 6:"6th", 7:"7th", 8:"8th", 9:"9th", 10:"10th"}
	if(post_counter != 1):
		tweet_content = "The current " + positions[post_counter] + " top post on /r/PrequelMemes is:\n\n" + title + "\nWith " + str(upvotes) + " upvotes\nBy /u/" + author
	else:
		tweet_content = "The current top post on /r/PrequelMemes is:\n\n" + title + "\nWith " + str(upvotes) + " upvotes\nBy /u/" + author

	while(True):
		print("Tweeting...")
		#try:
		api.PostUpdate(tweet_content, media=url)
		break
		'''except:
			print("Failed.\nRetrying In 1 Minute.\n")
			time.sleep(60)
			continue'''
		
	print("Success!\n")


#Processing the JSON
def processJson(input_data, api):
	extensions = {".jpg", ".gif", ".png", ".mp4", "gifv"}
	post_counter = 1
	input_json = json.loads(input_data)
	for post in input_json["data"]["children"]:
		if(post["data"]["url"][-4:] not in extensions and post["data"]["stickied"] is False):
			print("Post " + str(post_counter) + " was not in a valid file format")
			post_counter += 1
			continue
		if(post["data"]["stickied"] is False):
			print("Selected post with title: \"" + post["data"]["title"] + "\" by " + post["data"]["author"] + "with " + str(post["data"]["ups"]) + " upvotes")
			tweetPost(post["data"]["url"], post["data"]["title"], post["data"]["author"], post["data"]["ups"], post_counter, api)
			post_counter = 1
			break


def loopedTask(api):
	input_data = requestJson().text
	while("Too Many Requests" in input_data):
		print("Too Many Requests Error Detected!\nRetrying In 1 Minute.")
		time.sleep(60)
		input_data = requestJson().text

	processJson(input_data, api)

def main():
	print("\nInitialising...")

	#Twitter Login
	print("Authenticating Twitter Login...")
	try:
		api = twitter.Api(consumer_key="No u", consumer_secret="No u", access_token_key="No u", access_token_secret="No u")
	except:
		print("Failed.\nExiting...")
		exit(1)
	print("Success!\n")

	loopedTask(api)
	schedule.every(2).hours.do(loopedTask, api)
	try:
		while(True):
			schedule.run_pending()
			time.sleep(120)
	except(KeyboardInterrupt):
		print("\nExiting...\n")
	
main()
