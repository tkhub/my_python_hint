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
import time
# therd party module
import pygame
# my module


    

def main(argv:str):
    """
    @fn main()
    @brief モジュール単体実行時の実行関数
    """
    print("## START! Stand Alone Operation ##")
    print("init pygame")
    pygame.init()

    joy = pygame.joystick.Joystick(0) 
    joy.init()
    try:
        while True:
            strg = joy.get_axis(0) 
            accl = (joy.get_axis(5) + 1.0) / 2.0
            brk = (joy.get_axis(2) + 1.0) / 2.0
            print(f'{strg}:{accl}:{brk}')
            time.sleep(0.1)
    except(KeyboardInterrupt, SystemExit):
        print("exit")
    print("## END! Stand Alone Operation ##")

if __name__ == '__main__':
    
    try:
        main(sys.argv)
    except Exception as e:
        print("ERROR >> ", e)
        sys.exit(1)
    else:
        sys.exit(0)
