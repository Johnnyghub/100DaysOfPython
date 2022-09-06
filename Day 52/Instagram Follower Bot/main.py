from insta_follower import InstaFollower

INSTA_USERNAME = '100DOTBOT'
INSTA_PASSWORD = '100DOTInstaBot'
SIMILAR_ACCOUNT = 'chefsteps'
FOLLOWS_DESIRED = 150

bot = InstaFollower()
bot.login(INSTA_USERNAME, INSTA_PASSWORD)
bot.find_followers(SIMILAR_ACCOUNT, FOLLOWS_DESIRED)
bot.follow()
