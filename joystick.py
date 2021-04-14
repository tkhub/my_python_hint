#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *

# ジョイスティックの初期化
pygame.joystick.init()
try:
   # ジョイスティックインスタンスの生成
   joystick = pygame.joystick.Joystick(0)
   joystick.init()
   print('ジョイスティックの名前:', joystick.get_name())
   print('ボタン数 :', joystick.get_numbuttons())
except pygame.error:
   print('ジョイスティックが接続されていません')

# pygameの初期化
pygame.init()

# 画面の生成
screen = pygame.display.set_mode((320, 320))

# ループ
active = True
while active:
   # イベントの取得
   for e in pygame.event.get():
       # 終了ボタン
       if e.type == QUIT:
           active = False

       # ジョイスティックのボタンの入力
       if e.type == pygame.locals.JOYAXISMOTION:
           print('十時キー:', joystick.get_axis(0), joystick.get_axis(1))
       elif e.type == pygame.locals.JOYBUTTONDOWN:
           print('ボタン'+str(e.button)+'を押した')
       elif e.type == pygame.locals.JOYBUTTONUP:
           print('ボタン'+str(e.button)+'を離した')