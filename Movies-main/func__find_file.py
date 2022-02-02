import os


def find_file():
    playlist = []
    for file in os.listdir():
        base, ext = os.path.splitext(file)
        if ext == '.mp4':
            playlist.append('{}'.format(file))
    return playlist
