# 目標

1. 動画を再生する

2. ボタンを押したとき動画を再生する

3. 動画を連続で再生する

4. ボタンを押したとき次の動画にスキップする

5. ボタンを押したとき前の動画に戻って再生する

6. 4と5を二つのボタンで同時に実装する


***

## 1. 動画を再生する（成功）

<br>
pythonからvlcで動画を再生することができた。

<br>

## 2. ボタンを押したとき動画を再生する（成功）
```Python
import RPi.GPIO as GPIO
from time import sleep
import function_setMovieList as setML


pinInput = 12


GPIO.setmode(GPIO.BCM)
GPIO.setup(pinInput, GPIO.IN)


setML.set_movieList()


try:
    while True:
        if GPIO.input(pinInput) == GPIO.HIGH:
            setML.player.play()
        sleep(0.5)
except(KeyboardInterrupt, SystemExit, SystemError):
    print('exit')
    GPIO.cleanup()
```

## 3. 動画を連続で再生する（成功）

<br>

`メインのファイル内部`
```Python
import RPi.GPIO as GPIO
from time import sleep
import func__set_movie_list as setML


PIN_INPUT = 12


GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_INPUT, GPIO.IN)


setML.set_movie_list()


try:
    while True:
        if GPIO.input(PIN_INPUT) == GPIO.HIGH:
            setML.player.play()
        sleep(0.5)
except(KeyboardInterrupt, SystemExit, SystemError):
    print('exit')
    GPIO.cleanup()
```

<br>

`他ファイル`

```python
import os


def find_file():
    playlist = []
    for file in os.listdir():
        base, ext = os.path.splitext(file)
        if ext == '.mp4':
            playlist.append('{}'.format(file))
    return playlist
```
<br>


```Python
import vlc
import func__find_file as findF


player = vlc.MediaListPlayer()
paths = findF.find_file()


def set_movie_list():
    playList = vlc.MediaList(paths)
    player.set_media_list(playList)
    player.set_playback_mode(vlc.PlaybackMode.loop)

```

<br>

あらはあるだろうけどとりあえずループ再生に成功した。

<br>

## 4. ボタンを押したとき次の動画にスキップする
<br>

~~ループ再生が続いているので、それをなんとかしなければならない。<br>
`set_movieList`関数の書き換えをする。~~
<br>

### `csv`ファイルを用意してそこに必要な情報を書き込めばよいのでは？ ~~超アナログな手法だけど~~

CSVの中身を下記の表のようにしておけば簡単に手入力もできる


|No|動画ファイルの名前 |再生時間|
|:-:|:-:|:-:|
|---|---|---|
|1 |IMG_1161.mp4   |3 |
|2 |opening_now.mp4|6 |
|3 |uiire.mp4      |  |




















<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>




## 5. ボタンを押したとき前の動画に戻って再生する

## 6. 5と6を二つのボタンで同時に実装する