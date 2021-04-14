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
from pathlib import Path
from typing import Final 
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


def filelists(path:str, wildcard:str = '*') -> list:
    """
    @fn filelists()
    @brief ファイルを再帰的に検索しリストに変換する 
    @param path ファイルパス (str)
    @param wildcard ワイルドカード (str)
    @retval pathlist 検索済みのファイルパスリスト ()
    @details 詳細な説明
    @warning 見つからなかった場合はFileExistsErrorを発行
    @note -
    """
    wildcard = '**/' +str(wildcard)
    p =  Path(path)
    plist = list(p.glob(wildcard))
    if len(plist) == 0:
        raise FileExistsError("Path is NOT Exist")
    return plist

def main(argv:str):
    """
    @fn main()
    @brief モジュール単体実行時の実行関数
    """
    print("## START! Stand Alone Operation ##")
    test = class_name('abc')

    try:
        print(filelists("file"))
    except:
        print("not found...")
    else:
        print("next path")

    try:
        print(filelists("files","*.png"))
    except:
        print("not found...")
    else:
        pass

    
    print("## END! Stand Alone Operation ##")

if __name__ == '__main__':
    
    try:
        main(sys.argv)
    except Exception as e:
        print("ERROR >> ", e)
        sys.exit(1)
    else:
        sys.exit(0)
