from bs4 import BeautifulSoup
import requests
from flask import jsonify

HEADER = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}
link = "https://www.youtube.com/watch?v=qZp5gf9xgnE"

def extract(link):
    response = requests.get(link, headers=HEADER)
    soup = BeautifulSoup(response.text, "html.parser")

    titleSoupMeta = soup.find("meta", property="og:title")
    thumbSoupMeta = soup.find("meta", property="og:image")

    videoTitle = titleSoupMeta["content"] if titleSoupMeta else "NotFound"
    videoImage = thumbSoupMeta["content"] if thumbSoupMeta else "NotFound"
    videoViews = soup.find(attrs={"class": "watch-view-count"}).text
    videoPublished = soup.find(attrs={"class": "watch-time-text"}).text
    videoCategory = soup.find(attrs={"class": "watch-info-tag-list"})
    likeButon = soup.find(attrs={"class": "like-button-renderer-like-button"})
    dislikeButon = soup.find(attrs={"class": "like-button-renderer-dislike-button"})

    # print("Title", videoTitle)
    # print("Thumbnail", videoImage)
    # print("Total Views", videoViews)
    # print(videoPublished)
    # print("Catgory", videoCategory.li.a.text)
    # print("Likes", likeButon.span.text)
    # print("Dislikes", dislikeButon.span.text)

    response = jsonify(
        title=videoTitle,
        thumbnail=videoImage,
        views=videoViews,
        published=videoPublished,
        category=videoCategory.li.a.text,
        likes=likeButon.span.text,
        dislikes=dislikeButon.span.text
    )
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

