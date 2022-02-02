import vlc
import func__find_file as findF


player = vlc.MediaListPlayer()
paths = findF.find_file()


def set_movie_list():
    playList = vlc.MediaList(paths)
    player.set_media_list(playList)
    player.set_playback_mode(vlc.PlaybackMode.loop)
