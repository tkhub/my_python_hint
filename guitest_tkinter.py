#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@file ファイル名
@version バージョン番号
@author 作成者・更新者
@date パッケージの作成日時・更新日時
@brief 簡単な説明
@details 詳細な説明
@warning 警告メッセージ
@note メモ
"""

"""
@package パッケージの名前
@version バージョン番号
@author 作成者・更新者
@date 作成日時・更新日時
@brief 説明(簡単)
@details 説明（詳細）
@warning 警告メッセージ
@note メモ
"""

# Standard module
import sys
from typing import Final 
# from tkinter import ttk
from tkinter import *
from tkinter import ttk
# from tkinter import filedialog
import tkinter.filedialog

# therd party module

# my module

GCONSTVAL:Final[int] = 3

class class_name:
    """
    @class class_name
    @brief This is class brief
    @details This is class discription
    @warning 
    """
    classval:str
    CCONSTVAL:Final[str] = "Python"
    def __init__(self, arg:str) -> None:
        """
        @fn __init__()
        @brief Class Init
        @param arg
        @detail This is Init
        @warning Warning Message
        @note memo
        """
        self.classval = arg
    
    def sumdiff(self, a:float, b:float) -> tuple:
        """
        @fn sumdiff()
        @brief 2つの値の和と差を計算します
        @param a 1つ目の値（float）
        @param b 2つ目の値（float)
        @retval sum_ab aとbの和（float）
        @retval sub_ab aとbの差（float）
        @details 詳細な説明
        @warning 警告メッセージ
        @note メモ
        """

        sum_ab = a+b
        sub_ab = a-b
        return sum_ab, sub_ab

def simple_textin():
    mainform = Tk()
    mainform.title('GUI test ぐいてすと')

    frame1 = ttk.Frame(mainform, padding=16)
    label1 = ttk.Label(frame1, text='Input テキスト')
    t = StringVar()
    entry1 = ttk.Entry(frame1, textvariable=t)
    button1 = ttk.Button(
        frame1,
        text='OK',
        command=lambda: print(f'入力値は{t.get()}')
    )
    frame1.pack()
    label1.pack(side=LEFT)
    entry1.pack(side=LEFT)
    button1.pack(side=LEFT)

    mainform.mainloop()


def file_readDialog():

    # ファイル選択ダイアログの表示
    file_path = tkinter.filedialog.askopenfilename()

    if len(file_path) != 0:
        # ファイルが選択された場合

        # ファイルを開いて読み込んでdataに格納
        f = open(file_path)
        data = f.read()
        f.close()
    else:
        # ファイル選択がキャンセルされた場合

        # dataは空にする
        data = ''

    return data


class Application(tkinter.Tk):
    def __init__(self):
        super().__init__()

        # アプリのタイトル
        self.title("ファイル読み込み")

        # テキスト表示キャンバスの作成と配置
        self.text_canvas = tkinter.Canvas(
            self,
            width=600,
            height=400,
            bg="#D0D0D0"
        )
        self.text_canvas.pack()

        # 読み込みボタンの作成と配置
        self.read_button = tkinter.Button(
            self,
            text='ファイル読み込み',
            command=self.read_button_func
        )
        self.read_button.pack()

    def read_button_func(self):
        '読み込みボタンが押された時の処理'

        # ファイルを読み込み
        data = file_readDialog()

        # 読み込んだ結果を画面に描画
        self.text_canvas.create_text(300, 200, text=data)

def fileload():
    # GUIアプリ生成
    app = Application()
    app.mainloop()

def main(argv:str):
    """
    @fn main()
    @brief モジュール単体実行時の実行関数
    """
    simple_textin()
    fileload()

if __name__ == '__main__':
    
    try:
        main(sys.argv)
    except Exception as e:
        print("ERROR >> ", e)
        sys.exit(1)
    else:
        sys.exit(0)
