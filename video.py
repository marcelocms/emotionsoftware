from pyyoutube import Api
import random

apikey = 'AIzaSyC053n6_uqpUiOd1X4YfD0Vkx1QcTL-0R8'

playlists_by_mood = {
    'happy': 'PLLBp1zryraCFnmCRbc6Mrwxdo7NH1AvHC',
    'sad' : 'PL_PYHDxk5NdoRh-e4POzCmiQr58o4Y2IH',
    'angry': 'PL_MH8gOS_ETiNT1NF8B46JYHZe6fXWfVW',
    'stressed': 'PLZbV9oqiU7CIYfDmtW9DItbqzol96mRa6'
}

movie_by_mood = {
     'happy': ['Grown Ups', 'Blended', 'Ride Along', 'Daddy Day Care', 'Are We There Yet?', 'Matilda'],
     'sad':['Titanic', 'Marley & Me', 'Fault in Our Stars', 'The Last Song', 'The Notebook', 'You Before Me'],
     'angry':['The Karate Kid', 'Avengers', 'Fast and Furious', 'Saw', 'Escape Room', 'The Shallows'],
     'stressed': ['Alladin', 'Moana', 'Tangled', 'Hercules', 'Pinocchio', 'Peter Pan']
}

def random_video(mood):
    api = Api(api_key=apikey)

    videos = []
    playlist_item_by_playlist = api.get_playlist_items(playlist_id=playlists_by_mood[mood], count=None).items
    for item in iter(playlist_item_by_playlist):
        resource = item.snippet.resourceId
        if resource.kind == 'youtube#video':
            videos.append(resource.videoId)

    video = videos[random.randint(0, len(videos) - 1)]
    return 'https://www.youtube.com/watch?v=' + video

def random_movie(mood):
    movies = movie_by_mood[mood]
    movie = movies[random.randint(0, len(movies)-1)]
    return movie

