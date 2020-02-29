apikey = 'AIzaSyC053n6_uqpUiOd1X4YfD0Vkx1QcTL-0R8'
playlist = 'PL_MH8gOS_ETiNT1NF8B46JYHZe6fXWfVW'

from pyyoutube import Api
import random
api = Api(api_key=apikey)

videos = []
playlist_item_by_playlist = api.get_playlist_items(playlist_id=playlist, count=None).items
for item in iter(playlist_item_by_playlist):
    resource = item.snippet.resourceId
    if resource.kind == 'youtube#video':
        videos.append(resource.videoId)
random_video = videos[random.randint(0, len(videos) - 1)]
print('https://www.youtube.com/watch?v='+ random_video)