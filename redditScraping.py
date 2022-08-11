from bs4 import BeautifulSoup
import requests
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions

url = "https://www.reddit.com/top/?t=day"
result = requests.get(url).text
soup = BeautifulSoup(result, "lxml")

options = ChromeOptions()
options.add_argument("headless")
PATH = r"C:/Users/Pero/Downloads/chromedriver_win32/chromedriver.exe"
driver = Chrome(executable_path=PATH, options=options)

driver.get("https://www.reddit.com/top/?t=day")
html = driver.page_source
soupTwo = BeautifulSoup(html, "html.parser")

reddit_posts = soupTwo.find("div", class_="rpBJOHq2PR60pnwJlUyP0")

for index, post in enumerate(reddit_posts):
    try:
        reddit_post = post.div.div
        reddit_post_name = reddit_post.find("h3", class_="_eYtD2XCVieq6emjKBH3m").text
        reddit_upvotes = reddit_post.find("div", class_="_1E9mcoVn4MYnuBQSVDt1gC").div.text
        time_posted = reddit_post.find("span", class_="_2VF2J19pUIMSLJFky-7PEI").text

        subreddit_link = "https://www.reddit.com"
        subreddit_link += reddit_post.find("div", class_="_2dr_3pZUCk8KfJ-x0txT_l").a['href']

        username = reddit_post.find("a", {"data-click-id": "user"}).text

        reddit_user = "https://www.reddit.com/"
        reddit_user += reddit_post.find("a", {"data-click-id": "user"}).text

        post_link = "https://www.reddit.com"
        post_link += reddit_post.find("a", class_="SQnoC3ObvgnGjWt90zD9Z _2INHSNB8V5eaWp4P0rY_mE")['href']


        print(f"{index + 1}. {reddit_post_name} \n posted by {reddit_user} {time_posted}. They have {reddit_upvotes} up votes.")
        print(f"Posted on the subreddit {subreddit_link}")
        print(f"{post_link}")
        print("")
    except AttributeError:
        index -= 1
        continue
