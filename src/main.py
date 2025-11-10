import tkinter as tk

import flet as ft

from front.page.helloPage import hello_page


def config_window(page: ft.Page) -> None:
  # tkinterを使って画面解像度を取得
  root = tk.Tk()
  screen_width = root.winfo_screenwidth()  # 画面の幅
  screen_height = root.winfo_screenheight()  # 画面の高さ
  root.destroy()  # 不要になったtkinterのルートウィンドウを閉じる

  # アプリの目標サイズ
  APP_WIDTH = 400
  APP_HEIGHT = 300
  WINDOWS_TASKBAR_HEIGHT = 50  # タスクバーの高さを考慮

  # 右下隅の座標を計算
  window_left = screen_width - APP_WIDTH
  window_top = screen_height - APP_HEIGHT - WINDOWS_TASKBAR_HEIGHT

  # ページタイトルの設定
  page.title = "ページタイトル"

  # コントロール配置の設定
  page.vertical_alignment = ft.MainAxisAlignment.START

  # ウィンドウサイズの設定
  page.window.width = APP_WIDTH
  page.window.height = APP_HEIGHT
  # page.window.min_width = 800
  # page.window.min_height = 600

  page.window.top = window_top
  page.window.left = window_left


def main(page: ft.Page) -> None:
  config_window(page)
  hello_page(page)


ft.app(main)
