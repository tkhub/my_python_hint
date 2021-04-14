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

def fdlist(path:str, wildcard:str = '*') -> list:
    """
    @fn fdlist()
    @brief ファイルを再帰的に検索しリストに変換する 
    @param path ファイルパス (str)
    @param wildcard ワイルドカード (str)
    @retval pathlist 検索済みのファイルパスリスト ()
    @details 詳細な説明
    @warning 見つからなかった場合はFileExistsErrorを発行
    @note -
    """
    p =  Path(path)
    if not p.exists():
        raise FileExistsError("Path is NOT Exist")

    wildcard = '**/' +str(wildcard)
    plist = list(p.glob(wildcard))
    return plist

def filelist(path:str) -> list:
    """
    @fn filelist()
    @brief ファイルを再帰的に検索しリストに変換する 
    @param path ファイルパス (str)
    @param wildcard ワイルドカード (str)
    @retval pathlist 検索済みのファイルパスリスト ()
    @details 詳細な説明
    @warning 見つからなかった場合はFileExistsErrorを発行
    @note -
    """
    p =  Path(path)
    if not p.exists():
        raise FileExistsError("Path is NOT Exist")

    plist = [i for i in p.iterdir() if i.is_file()]
    return plist

def dirlist(path:str) -> list:
    """
    @fn dirlist()
    @brief ファイルを再帰的に検索しリストに変換する 
    @param path ファイルパス (str)
    @param wildcard ワイルドカード (str)
    @retval pathlist 検索済みのファイルパスリスト ()
    @details 詳細な説明
    @warning 見つからなかった場合はFileExistsErrorを発行
    @note -
    """
    p =  Path(path)
    plist = [i for i in p.iterdir() if i.is_dir()]
    return plist

def main(argv:str):
    """
    @fn main()
    @brief モジュール単体実行時の実行関数
    """
    print("## START! Stand Alone Operation ##")

    try:
        print(filelist("nothing"))
    except:
        print("not found...")
    else:
        pass
    finally:
        print("next")

    try:
        print(dirlist("files"))
    except:
        print("not found...")
    else:
        pass
    finally:
        print("next")

    try:
        print(filelist("files/src"))
    except:
        print("not found...")
    else:
        pass
    finally:
        print("next")

    try:
        print(fdlist("files","*.png"))
    except:
        print("not found...")
    else:
        pass
    finally:
        print("next")
    
    print("## END! Stand Alone Operation ##")

if __name__ == '__main__':
    
    try:
        main(sys.argv)
    except Exception as e:
        print("ERROR >> ", e)
        sys.exit(1)
    else:
        sys.exit(0)
