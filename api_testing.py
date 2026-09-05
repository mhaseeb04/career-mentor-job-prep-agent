import requests

api_key = REDACTED
query = "python tutorial"
url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={query}&type=video&key={api_key}"

response = requests.get(url)
data = response.json()

if "items" in data:
    for item in data["items"]:
        title = item["snippet"]["title"]
        description = item["snippet"]["description"]
        author = item["snippet"]["channelTitle"]
        video_id = item["id"]["videoId"]
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        print(f"Title: {title}")
        print(f"Description: {description}")
        print(f"Author: {author}")
        print(f"Link: {video_url}")
        print("-----------")
else:
    print("❌ No items found. Error or quota issue:")
    print(data)
