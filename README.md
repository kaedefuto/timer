# timer
PysimpleGUIで作成した学会タイマー<br>

### 概要<br>
* 学会発表でよく使われるタイマーを再現しました<br>
![画像](https://github.com/kaedefuto/timer/blob/main/2021-04-26%20114655.png" サンプル")
<img src="https://github.com/kaedefuto/timer/blob/main/2021-04-26%20114655.png" alt="エビフライトライアングル" title="サンプル">
### 環境<br>
* Windows10<br>
* PySimpleGUI 4.34.0
* PyAudio     0.2.11
### 使い方<br>
```bash
python alarm_time.py
```

### インストール<br>
```bash
pip install PySimpleGUI
```
または
```bash
python -m pip install PySimpleGUI
```
* 音声を使う場合はpyaudioのインストールとコメントアウトを外す
* 別途でフリーのwavファイルが必要
```bash
pip install PyAudio
```
* 問題点として音声を入れるラグくなる

### 参考サイト<br>
PysimpleGUI<br>
http://www.k-techlabo.org/www_python/PySimpleGUI.pdf<br> 
https://qiita.com/nemous_nuke/items/8ddd0a4290209410d25d<br>

pyaudio<br>
https://qiita.com/musaprg/items/34c4c1e0e9eb8e8cc5a1<br>
https://qiita.com/bayachin/items/68f7659d31fa6c836317<br>
