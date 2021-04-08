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

import sys
from typing import Final 

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


    

def main(argv:str):
    """
    @fn main()
    @brief モジュール単体実行時の実行関数
    """
    print("## START! Stand Alone Operation ##")
    members = ['John', 'Pole', 'Ring','George']
    for i, name in enumerate(members, 1):
        print(f'{i}:{name}')
    print("## END! Stand Alone Operation ##")

if __name__ == '__main__':
    
    try:
        main(sys.argv)
    except Exception as e:
        print("ERROR >> ", e)
        sys.exit(1)
    else:
        sys.exit(0)
