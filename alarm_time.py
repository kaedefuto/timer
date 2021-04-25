import PySimpleGUI as sg
import time
import wave
#import pyaudio # 鳴らすとき使う

#音声を使う場合はコメントを外してください
"""
# 'rb'で読み込みモード
wf = wave.open('alarm.wav', mode='rb')
"""

def time_as_int():
    return int(round(time.time() * 100))

"""
def music(): 
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True) # このストリ
    chunk = 1024 # チャンク単位でストリームに出力し音声を再生
    wf.rewind() # ポインタを先頭にする  
    data = wf.readframes(chunk)
    while data:
        stream.write(data)
        data = wf.readframes(chunk)
    stream.close()
    p.terminate()
"""        

# GUIテーマ。sg.theme_previewer()で使えるテーマを確認できる。
sg.theme('Black')

# tab1(表示部)
layout1 = [
    # 表示テキスト font設定は各々の環境を参照してください。
    [sg.Text('', size=(10,1), font=('Bauhaus 93',180), justification='c', pad=((50,50),(20,0)), key='text')],

    [sg.Combo([i for i in range(0,60)] + [''], default_value='0',size=(5,5) , font=('Helvetica', 20), pad=((281,0),(0,0)), key='min'),
    sg.Text(':', font=('Helvetica', 20)),
    sg.Combo([i for i in range(0,60)] + [''], default_value='0',size=(5,5), font=('Helvetica', 20),key='sec')],

    [sg.Text('')],

    [sg.Combo([i for i in range(0,60)] + [''], default_value='0',size=(5,5) , font=('Helvetica', 20), pad=((281,0),(0,0)), key='add_min'),
    sg.Text(':', font=('Helvetica', 20)),
    sg.Combo([i for i in range(0,60)] + [''], default_value='0',size=(5,5), font=('Helvetica', 20), key='add_sec'),
    sg.Text('', font=('Helvetica', 20))],

    [sg.Text('')],

    [sg.Combo([i for i in range(0,60)] + [''], default_value='0',size=(5,5) , font=('Helvetica', 20), pad=((281,0),(0,0)), key='add2_min'),
    sg.Text(':', font=('Helvetica', 20)),
    sg.Combo([i for i in range(0,60)] + [''], default_value='0',size=(5,5), font=('Helvetica', 20), key='add2_sec'),
    sg.Text('', font=('Helvetica', 20))],

    # 開始/停止・リセット・終了ボタン
    [sg.Button('開始',font=('Helvetica', 18), button_color=('white', 'Darkred'),pad=((105,50),(30,0)) ,key='-RUN-PAUSE-'),
    sg.Exit('終了',button_color=('white', 'Green'),font=('Helvetica', 18), pad=((0,0),(30,0)),key='-QUIT1-'),
    sg.Button('リセット', font=('Helvetica', 18),button_color=('white', 'Blue'), pad=((50,110),(30,0)),key='-RESET-')]]


# 表示。タイトル無し、ボタンリサイズ無し、最前面表示、どこ掴んでもいい
window= sg.Window('プレゼンタイマー', layout1,
    auto_size_buttons=False,
    keep_on_top=True,
    grab_anywhere=True,
    element_padding=(0, 0),
    size=(780, 550))

# 変数の初期化
start_time, paused_time, paused = 0, 0, True
first_flag = True
hold_flag,hold_flag2 = True, True
hold_time =0
color ="White"
#count =0
while True:

    if not paused:  # Run状態 10msで読み込み、与えた時間とその変化を記述・追加時間がある場合の制御
        event, values = window.read(timeout=10)
        current_time = 0 * 100 * 60 + 0 * 100
        add_time = 0 * 100 * 60 + 0 * 100
        current_time -= start_time - time_as_int()

        if current_time > values['min'] * 100 * 60 + values['sec'] * 100: # 監視している時間変数が0を下回ると追加時間を加算
            if hold_flag:
                hold_flag = not hold_flag
                #count =1
                color="Yellow"
            else:
                count=0   
            if current_time > values['add_min'] * 100 * 60 + values['add_sec'] * 100: # 追加時間があれば時間説明の書き換え
                if hold_flag2:
                    hold_flag2 = not hold_flag2
                    #count =1
                    color="Red"
                else:
                    count=0
                if current_time > values['add2_min'] * 100 * 60 + values['add2_sec'] * 100:
                    if current_time - add_time == hold_time:
                        current_time = 0
                    else: # 追加時間がなければ0とする
                        event = '-RUN-PAUSE-'
                        current_time = values['add2_min'] * 100 * 60 + values['add2_sec'] * 100
                        color="White"
                        #music()
                        #count =0

    else:   # 待機（pause）状態 起動時の諸々を処理
        event, values = window.read(timeout=20)
        if first_flag:
            current_time = 0 * 100 * 60 + 0 * 100
            #初期値
            window['text'].update('{:02d}:{:02d}'.format((current_time // 100) // 60, (current_time // 100) % 60))

    window['text'].update('{:02d}:{:02d}'.format((current_time // 100) // 60, (current_time // 100) % 60),text_color=color)
    """
    if count ==1:
        music()
    """

    if event in (sg.WIN_CLOSED, '-QUIT1-'):    # QUIT押下
        break
    if event in (sg.WIN_CLOSED, '-QUIT2-'):
        break

    if event == '-RESET-':  # RESET押下
        paused_time = start_time = time_as_int()
        current_time = 0 * 100 * 60 + 0 * 100
        color="White"
        start_time, paused_time, paused = 0, 0, True
        first_flag = True
        hold_time = 0
        hold_flag,hold_flag2 = True, True
        #count =0

    elif event == '-RUN-PAUSE-':    # 0秒 or Run/Pause押下
        if first_flag: # 起動時の諸々を処理
            paused_time = time_as_int()
            window['-RUN-PAUSE-'].update('一時停止')
            paused = not paused
            first_flag = not first_flag
            start_time = time_as_int()
            continue

        paused = not paused
        if paused:
            paused_time = time_as_int()
        else:
            start_time += time_as_int() - paused_time
        window['-RUN-PAUSE-'].update('開始' if paused else '一時停止')

window.close()
