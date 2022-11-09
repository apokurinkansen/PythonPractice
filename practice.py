
# --------------書き込みモードでのHTMLの取得------------------------
# import requests

# url="http://www.ymori.com/books/python2nen/test1.html"

# response=requests.get(url)

# response.encoding = response.apparent_encoding

# filename = "download.txt"

# with open(filename,mode="w") as f:
#     f.write(response.text)

#-----------------------------------------------------------------


# -------------Beautiful Soupで解析する-----------------------------
# import requests
# from bs4 import BeautifulSoup

# #Webページを取得して解析する
# load_url="https://www.ymori.com/books/python2nen/test1.html"
# html = requests.get(load_url)
# soup = BeautifulSoup(html.content,"html.parser")

# # HTML全体を表示
# print(soup)


# ---------------タグを探して表示する---------------------------
# import requests
# from bs4 import BeautifulSoup

# #Webページを取得して解析する
# load_url="https://www.ymori.com/books/python2nen/test1.html"
# html = requests.get(load_url)
# soup = BeautifulSoup(html.content,"html.parser")

# # title,h2,liタグを検索して表示する
# print(soup.find("title"))
# print(soup.find("h2"))
# print(soup.find("li"))

# ---------------全てのタグを探して表示する---------------------------
# import requests
# from bs4 import BeautifulSoup

# #Webページを取得して解析する
# load_url="https://www.ymori.com/books/python2nen/test2.html"
# html = requests.get(load_url)
# soup = BeautifulSoup(html.content,"html.parser")

# # 全てのliタグを検索して、その文字列を表示する
# for element in soup.find_all("li"):
#     print(element.text)


# ---------------idやclassで検索範囲を絞り込む---------------------------
# import requests
# from bs4 import BeautifulSoup

# # Webページを取得して解析する
# load_url = "https://www.ymori.com/books/python2nen/test2.html"
# html = requests.get(load_url)
# soup = BeautifulSoup(html.content,"html.parser")

# # IDで検索して、そのタグの中身を表示する
# chap2 = soup.find(id="chap2")
# print(chap2)

# ---------------classとliで検索範囲を絞り込む---------------------------
# import requests
# from bs4 import BeautifulSoup

# # Webページを取得して解析する
# load_url = "https://www.ymori.com/books/python2nen/test2.html"
# html = requests.get(load_url)
# soup = BeautifulSoup(html.content,"html.parser")

# # IDで検索し、その中の全てのliタグを検索して表示する
# chap2 = soup.find(id = "chap2")
# for element in chap2.find_all("li"):
#     print(element.text)


# ---------------デベロッパーツールを使って絞り込む---------------------------
# import requests
# from bs4 import BeautifulSoup

# # Webページを取得して解析する
# load_url = "https://www.yahoo.co.jp/"
# html = requests.get(load_url)
# soup = BeautifulSoup(html.content,"html.parser")

# # classで検索し、その中の全てのaタグを検索して表示する
# topic = soup.find(class_ = "_2jjSS8r_I9Zd6O9NFJtDN-")
# for element in topic.find_all("li"):
#     print(element.text)

# ---------------全てのリンクタグのhref属性を表示する---------------------------
# import requests
# from bs4 import BeautifulSoup

# # Webページを取得して解析する
# load_url = "https://www.ymori.com/books/python2nen/test2.html"
# html = requests.get(load_url)
# soup = BeautifulSoup(html.content,"html.parser")

# # 全てのaタグを検索して、リンクを表示する
# for element in soup.find_all("a"):
#     print(element.text)
#     url = element.get("href")
#     print(url)

# ---------------全てのリンクタグのhref属性を絶対URLで表示する---------------------------
# import requests
# from bs4 import BeautifulSoup
# import urllib

# # Webページを取得して解析する
# load_url = "https://www.ymori.com/books/python2nen/test2.html"
# html = requests.get(load_url)
# soup = BeautifulSoup(html.content,"html.parser")

# # 全てのaタグを検索して、リンクを絶対URLで表示する
# for element in soup.find_all("a"):
#     print(element.text)
#     url = element.get("href")
#     link_url = urllib.parse.urljoin(load_url,url)
#     print(link_url)


# ---------------全てのリンクタグのhref属性を絶対URLで表示する---------------------------
# import requests
# from bs4 import BeautifulSoup
# import urllib

# # Webページを取得して解析する
# load_url = "https://www.ymori.com/books/python2nen/test2.html"
# html = requests.get(load_url)
# soup = BeautifulSoup(html.content,"html.parser")

# # ファイルを書き込みモードで開く
# filename = "linklist.txt"
# with open(filename,"w") as f:
#     # 全てのaタグを検索し、リンクを絶対URLで書き出す
#     for element in soup.find_all("a"):
#         url = element.get("href")
#         link_url = urllib.parse.urljoin(load_url,url)
#         f.write(element.text+"\n")
#         f.write(link_url+"\n")
#         f.write("\n")


# ---------------画像ファイルを読み込んで保存する---------------------------
# import requests

# # 画像ファイルを取得して解析する
# img_url = "https://www.ymori.com/books/python2nen/sample1.png"
# imgdata = requests.get(img_url)

# # URLから最後のファイル名を取り出す
# filename = img_url.split("/")[-1]

# # 画像データを、ファイルに書き出す
# with open(filename , mode = "wb") as f:
#     f.write(imgdata.content)


# ---------------ダウンロード用のフォルダを作って保存する---------------------------
# import requests
# from pathlib import Path

# # 保存用フォルダを作成
# out_folder = Path("download")
# out_folder.mkdir(exist_ok=True)

# # 画像ファイルを取得して解析する
# img_url = "https://www.ymori.com/books/python2nen/sample1.png"
# imgdata = requests.get(img_url)

# # URLから最後のファイル名を取り出して、保存フォルダ名と繋げる
# filename = img_url.split("/")[-1]
# out_path = out_folder.joinpath(filename)

# # 画像データを、ファイルに書き出す
# with open(out_path , mode = "wb") as f:
#     f.write(imgdata.content)


# ---------------全てのimgタグの画像ファイルURLを表示する--------------------------
# import requests
# from bs4 import BeautifulSoup
# import urllib

# # Webページを取得して解析する
# load_url = "https://www.ymori.com/books/python2nen/test2.html"
# html = requests.get(load_url)
# soup = BeautifulSoup(html.content,"html.parser")

# # 全てのimgタグを検索し、リンクを取得する
# for element in soup.find_all("img"):
#     src = element.get("src")

#     # 絶対URLと、ファイルを表示する
#     image_url = urllib.parse.urljoin(load_url,src)
#     filename = image_url.split("/")[-1]
#     print(image_url, ">>" ,filename)


# ---------------ページ内の画像を一括ダウンロードするプログラム--------------------------
# import requests
# from bs4 import BeautifulSoup
# from pathlib import Path
# import urllib
# import time

# # Webページを取得して解析する
# load_url = "https://www.ymori.com/books/python2nen/test2.html"
# html = requests.get(load_url)
# soup = BeautifulSoup(html.content,"html.parser")

# # 保存用のフォルダ作成
# out_folder = Path("download2")
# out_folder.mkdir(exist_ok=True)

# # 全てのimgタグを検索し、リンクを取得する
# for element in soup.find_all("img"):
#     src = element.get("src")

#     # 絶対URLを作成、画像データを取得する
#     img_url = urllib.parse.urljoin(load_url,src)
#     imgdata = requests.get(img_url)

#     # URLから最後のファイル名を取り出して、保存フォルダ名と繋げる
#     filename = img_url.split("/")[-1]
#     out_path = out_folder.joinpath(filename)

#     #画像データを、ファイルに書き出す
#     with open(out_path,mode="wb") as f:
#         f.write(imgdata.content)

#     # 1回アクセスしたので1秒待つ
#     time.sleep(1)


# ---------------CSVファイルを読み込む--------------------------
# import pandas as pd

# # CSVファイルを読み込む
# df = pd.read_csv("test.csv")
# print = (df)

# ---------------CSVファイルを読み込む--------------------------
# import pandas as pd

# # CSVファイルを読み込む
# df = pd.read_csv("test.csv")

# # 表データの情報を表示
# print("データの件数 =",len(df))
# print("項目名      =", df.columns.values)
# print("インデックス =",df.index.values)

# ---------------列データ、行データを表示する--------------------------
# import pandas as pd

# # CSVファイルを読み込む
# df = pd.read_csv("test.csv")

# # 1列のデータを表示
# print("国語の列データ\n",df["国語"])

# # 複数の列のデータを表示
# print("国語と数学の列データ\n",df[["国語","数学"]])

# ---------------列データ、行データを表示する--------------------------
# import pandas as pd

# # CSVファイルを読み込む
# df = pd.read_csv("test.csv")

# # 1行のデータを表示
# print("C子のデータ\n",df.loc[2])

# # 複数のデータを表示
# print("C子とD郎のデータ\n",df.loc[[2,3]])

# # 指定した行の指定した列のデータを表示
# print("C子の国語データ\n",df.loc[2]["国語"])

# ---------------列データ、行データを追加する--------------------------
# import pandas as pd

# # CSVファイルを読み込む
# df = pd.read_csv("test.csv")

# # 1列のデータを追加
# df["美術"] = [68,35,75,24,78,99]
# print("列データ(美術)を追加\n",df)

# # 1行データを追加
# df.loc[6] = ["G渓",80,39,56,75,88,48]
# print("行データ(G渓)を追加\n",df)

# ---------------列データ、行データを追加する--------------------------
# import pandas as pd

# # CSVファイルを読み込む
# df = pd.read_csv("test.csv")

# # 「名前」の列を削除
# print("「名前」の列を削除\n",df.drop("名前",axis=1))

# # インデックス2の行を削除
# print("インデックス2の行を削除\n",df.drop(2,axis=0))


# ---------------必要な情報を抽出する--------------------------
# import pandas as pd

# # CSVファイルを読み込む
# df = pd.read_csv("test.csv")

# # 条件に合うデータを抽出する
# data_s = df[df["国語"] >= 90]
# print("国語が90点以上\n",data_s)

# data_c = df[df["数学"] < 70]
# print("数学が70点未満",data_c)

# ---------------データを集計する--------------------------
# import pandas as pd

# # CSVファイルを読み込む
# df = pd.read_csv("test.csv")

# # 集計(最大値、最小値、平均値、中央値、合計など)をして表示
# print("数学の最高点 =",df["数学"].max())
# print("数学の最低点 =",df["数学"].min())
# print("数学の平均点 =",df["数学"].mean())
# print("数学の中央値 =",df["数学"].median())
# print("数学の合計 =",df["数学"].sum())

# ---------------データを並び替える--------------------------
# import pandas as pd

# # # CSVファイルを読み込む
# df = pd.read_csv("test.csv")

# # ソート(並び替え)をして表示
# kokugo = df.sort_values("国語",ascending=False)
# print("国語の点数が高いもの順でソート\n",kokugo)


# ---------------行と列を入れ替える--------------------------
# import pandas as pd

# # # CSVファイルを読み込む
# df = pd.read_csv("test.csv")

# # 行と列を入れ替える
# print("行と列を入れ替える\n",df.T)

# # データをリスト化する
# print("Pythonのリストデータ化\n",df.values)


# ---------------CSVファイルに出力する--------------------------
# import pandas as pd

# # # CSVファイルを読み込む
# df = pd.read_csv("test.csv")

# # ソート(国語の点数が高いもの順)
# kokugo = df.sort_values("国語",ascending=False)

# # CSVファイルに出力する
# kokugo.to_csv("export1.csv")


# ---------------CSVファイルに出力する--------------------------
# import pandas as pd

# # # CSVファイルを読み込む
# df = pd.read_csv("test.csv")

# # ソート(国語の点数が高いもの順)
# kokugo = df.sort_values("国語",ascending=False)

# # CSVファイルに出力する(インデックスを削除)
# kokugo.to_csv("export2.csv",index=False)


# ---------------CSVファイルに出力する--------------------------
# import pandas as pd

# # CSVファイルを読み込む
# df = pd.read_csv("test.csv")

# # ソート(国語の点数が高いもの順)
# kokugo = df.sort_values("国語",ascending=False)

# # CSVファイルに出力する(インデックスとヘッダーを削除)
# kokugo.to_csv("export3.csv",index=False,header=False)

# ---------------CSVファイルに出力する--------------------------
# import pandas as pd
# import matplotlib.pyplot as plt
# import japanize_matplotlib

# # CSVファイルを読み込む
# df = pd.read_csv("test.csv")

# # グラフを作って表示する
# df.plot()
# plt.show()

# ---------------さまざまな種類のグラフを表示する--------------------------
# from inspect import stack
# import pandas as pd
# import matplotlib.pyplot as plt
# import japanize_matplotlib

# # CSVファイルを読み込む(名前の列をインデックスで)
# df = pd.read_csv("test.csv",index_col=0)

# # 棒グラフを作って表示する
# df.plot.bar()
# plt.legend(loc = "lower right")
# plt.show()

# # 棒グラフ(水平)を作って表示する
# df.plot.barh()
# plt.legend(loc="lower left")
# plt.show()

# # 積み上げ棒グラフを作って表示する
# df.plot.bar(stacked=True)
# plt.legend(loc="lower right")
# plt.show()

# # 箱ひげグラフを作って表示する
# df.plot.box()
# plt.show()

# # 面グラフを作って表示する
# df.plot.area()
# plt.legend(loc="lower right")
# plt.show()

# ---------------個別のデータをグラフで表示する--------------------------
# from tkinter.ttk import LabeledScale
# import pandas as pd
# import matplotlib.pyplot as plt
# import japanize_matplotlib

# # CSVファイルを読み込む
# df = pd.read_csv("test.csv",index_col=0)

# # 国語の棒グラフを作って表示する
# df["国語"].plot.barh()
# plt.legend(loc="lower left")
# plt.show()


# # 国語と数学の棒グラフを作って表示する
# df[["国語","数学"]].plot.barh()
# plt.legend(loc="lower left")
# plt.show()

# # C子の棒グラフを作って表示する
# df.loc["C子"].plot.barh()
# plt.legend(loc="lower left")
# plt.show()

# # C子の円グラフを作って表示する
# df.loc["C子"].plot.pie(labeldistance=0.6)
# plt.legend(loc="lower left")
# plt.show()


# ---------------個別のデータをグラフで表示する--------------------------
# import pandas as pd
# import matplotlib.pyplot as plt
# import japanize_matplotlib

# # CSVファイルを読み込む
# df = pd.read_csv("test.csv",index_col=0)

# # 棒グラフを作って表示する
# df.T.plot.bar()
# plt.legend(loc="lower right")
# plt.show()


# ---------------個別のデータをグラフで表示する--------------------------
# import pandas as pd
# import matplotlib.pyplot as plt
# import japanize_matplotlib

# # CSVファイルを読み込む(名前の列をインデックスで)
# df = pd.read_csv("test.csv",index_col=0)

# # 棒グラフを作って表示する
# colorlist = ["skyblue","steelblue","tomato","cadetblue","orange","sienna"]
# df.T.plot.bar(color = colorlist)
# plt.legend(loc="lower right")
# plt.show()

# ---------------個別のデータをグラフで表示する--------------------------
# import pandas as pd
# import matplotlib.pyplot as plt
# import japanize_matplotlib

# # CSVファイルを読み込む(名前の列をインデックスで)
# df = pd.read_csv("test.csv",index_col=0)

# # 棒グラフを作って画像ファイル出力する
# colorlist = ["skyblue","steelblue","tomato","cadetblue","orange","sienna"]
# df.T.plot.bar(color=colorlist)
# plt.legend(loc="lower right")
# plt.savefig("bargraph.png")


# ---------------Excelファイルに出力する--------------------------
# import pandas as pd
# import matplotlib.pyplot as plt
# import japanize_matplotlib

# # CSVファイルを読み込む
# df = pd.read_csv("test.csv")

# # ソート(国語の点数が高いもの順)
# kokugo = df.sort_values("国語",ascending=False)

# # Excelファイルに出力する
# kokugo.to_excel("csv_to_excel1.xlsx")


# ---------------Excelファイルに出力する--------------------------
# import pandas as pd
# import openpyxl

# # CSVファイルを読み込む
# df = pd.read_csv("test.csv")

# # ソート(国語の点数が高いもの順)
# kokugo = df.sort_values("国語",ascending=False)

# # 1つのExcelファイルに複数のシートで出力する
# with pd.ExcelWriter("csv_to_excel3.xlsx") as writer:
#     df.to_excel(writer,index=False,sheet_name="元のデータ")
#     kokugo.to_excel(writer,index=False,sheet_name="国語でソート")


# ---------------Excelファイルに出力する--------------------------
# import pandas as pd
# import openpyxl

# # Excelファイルを読み込む
# df = pd.read_excel("csv_to_excel1.xlsx")
# print(df)

# ---------------CSVファイルを読み込む-------------------------
# import pandas as pd

# # データフレームを読み込む
# df = pd.read_csv("13TOKYO.CSV",header=None,encoding="shift_jis")
# print(len(df))
# print(df.columns.values)

# ---------------CSVファイルを読み込む-------------------------
# import pandas as pd

# # データフレームを読み込む
# df = pd.read_csv("13TOKYO.CSV",header=None,encoding="shift_jis")


# # 2の列が「160006」の住所を抽出して表示
# results = df[df[2] == 1600006]
# print(results[[2,6,7,8]])

# ---------------データを抽出する-------------------------
# import pandas as pd

# # データフレームを読み込む
# df = pd.read_csv("13TOKYO.CSV",header=None,encoding="shift_jis")

# # 8の列が「四谷」の住所を抽出して表示
# results = df[df[8] == "四谷"]
# print(results[[2,6,7,8]])

# # 8の列に「四谷」の文字が含まれる住所を抽出して表示
# results = df[df[8].str.contains("四谷")]
# print(results[[2,6,7,8]])


# ---------------データを抽出する-------------------------
# import pandas as pd

# # データフレームを読み込む
# df = pd.read_csv("FEH_00200524_221101140612.csv",index_col="全国・都道府県",encoding="shift_jis")

# print(len(df))
# print(df.columns.values)


# ---------------データをグラフで表示する-------------------------
# import pandas as pd
# import matplotlib.pyplot as plt
# import japanize_matplotlib

# # データフレームを読み込む
# df = pd.read_csv("FEH_00200524_221101140612.csv",index_col="全国・都道府県",encoding="shift_jis")

# print(df["平成30年"])
# # 平成30年の列データで棒グラフを作って表示する
# df["平成30年"] = pd.to_numeric(df["平成30年"].str.replace(",",""))
# df["平成30年"].plot.bar()
# plt.show()


# ---------------データをグラフで表示する-------------------------
# import pandas as pd
# import matplotlib.pyplot as plt
# import japanize_matplotlib

# # データフレームを読み込む
# df = pd.read_csv("FEH_00200524_221101140612.csv",index_col="全国・都道府県",encoding="shift_jis")

# # 平成30年の列データで棒グラフを作って表示する
# df = df.drop("全国",axis=0)
# df["平成30年"] = pd.to_numeric(df["平成30年"].str.replace(",",""))
# df["平成30年"].plot.bar(figsize=(10,6))
# plt.show()


# ---------------データをグラフで表示する-------------------------
# import pandas as pd
# import matplotlib.pyplot as plt
# import japanize_matplotlib

# # データフレームを読み込む
# df = pd.read_csv("FEH_00200524_221101140612.csv",index_col="全国・都道府県",encoding="shift_jis")

# # 平成30年の列データで棒グラフを作って表示する
# df = df.drop("全国",axis=0)
# df["平成30年"] = pd.to_numeric(df["平成30年"].str.replace(",",""))
# df = df.sort_values("平成30年",ascending=False)
# df["平成30年"].plot.bar(figsize=(10,6))
# plt.show()

# ---------------データをグラフで表示する-------------------------
# import pandas as pd
# import matplotlib.pyplot as plt
# import japanize_matplotlib

# # データフレームを読み込む
# df = pd.read_csv("FEH_00200524_221101140612.csv",index_col="全国・都道府県",encoding="shift_jis")

# # 平成30年の列データで棒グラフを作って表示する
# df = df.drop("全国",axis=0)
# df["平成29年"] = pd.to_numeric(df["平成29年"].str.replace(",",""))
# df["平成30年"] = pd.to_numeric(df["平成30年"].str.replace(",",""))
# df["人口増減"] = df["平成30年"] - df["平成29年"]
# df = df.sort_values("人口増減",ascending=False)
# df["人口増減"].plot.bar(figsize=(10,6))
# plt.show()


# ---------------データをグラフで表示する-------------------------
# import pandas as pd
# import matplotlib.pyplot as plt
# import japanize_matplotlib

# # データフレームを読み込む
# df = pd.read_csv("FEH_00200524_221101140612.csv",index_col="全国・都道府県",encoding="shift_jis")

# # 平成30年の列データで棒グラフを作って表示する
# df = df.drop("全国",axis=0)
# df["平成29年"] = pd.to_numeric(df["平成29年"].str.replace(",",""))
# df["平成30年"] = pd.to_numeric(df["平成30年"].str.replace(",",""))
# df["人口増減"] = df["平成30年"] - df["平成29年"]
# df = df.sort_values("人口増減",ascending=False)
# df["人口増減"].plot.bar(figsize=(10,6))
# plt.ylim(-40,14000)
# plt.show()


# ---------------データをグラフで表示する-------------------------
# import pandas as pd

# # データフレームを読み込む
# df = pd.read_csv("200.csv",encoding="Shift-jis")


# # 消火栓のある地点(緯度、経度)をリスト化する
# hydrant = df[["緯度","経度"]].values
# print(len(hydrant))
# print(hydrant)


# ---------------データをグラフで表示する-------------------------
# from math import hypot
# import folium

# # 地図を作って書き出す
# m = folium.Map(location=[35.941957,136.198863],zoom_start = 16)
# folium.Marker([35.942957,136.198863]).add_to(m)
# m.save("megane.html")


# ---------------地図上に表示-------------------------
# import pandas as pd
# import folium

# # データフレームを読み込む
# df =pd.read_csv("200.csv",encoding="shift-jis")

# # 消火栓のある地点(緯度、経度)をリスト化する
# hydrant = df[["緯度","経度"]].values

# # 地図を作って書き出す
# m = folium.Map(location=[35.941957,136.198863],zoom_start = 16)
# for data in hydrant:
#     folium.Marker([data[0],data[1]]).add_to(m)
# m.save("hydrant.html")


# ---------------WebAPIを使用して天気を取得-------------------------
# import requests
# import json

# # 現在の天気を取得する：神戸
# url = "http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&lang=ja&units=metric"
# url = url.format(city="Kobe,JP",key="985e8ef8f6274791fdab24dc9ede1f06")

# jsondata = requests.get(url).json()
# print(jsondata)




# ---------------WebAPIを使用して天気を取得-------------------------
# import requests
# import json


# # 現在の天気を取得する：神戸
# url = "http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&lang=ja&units=metric"
# url = url.format(city="Fukuoka,JP",key="e895b2438511f483606664851f13ce40")

# jsondata = requests.get(url).json()
# print("都市名  =",jsondata["name"])
# print("気温   =",jsondata["main"]["temp"])
# print("天気   =",jsondata["weather"][0]["main"])
# print("天気詳細 =",jsondata["weather"][0]["description"])


# ---------------5日間の天気を取得してみよう-------------------------
# import requests
# import json


# # 現在の天気を取得する：神戸
# url = "http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={key}&lang=ja&units=metric"
# url = url.format(city="Fukuoka,JP",key="e895b2438511f483606664851f13ce40")

# jsondata = requests.get(url).json()
# print(jsondata)


# ---------------5日間の天気を取得してみよう-------------------------
# import requests
# import json
# from datetime import datetime,timedelta,timezone

# # 現在の天気を取得する：東京
# url = "http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={key}&lang=ja&units=metric"
# url = url.format(city="Tokyo,JP",key="e895b2438511f483606664851f13ce40")

# jsondata = requests.get(url).json()
# tz = timezone(timedelta(hours=+9),'JST')
# for dat in jsondata["list"]:
#     jst = str(datetime.fromtimestamp(dat["dt"],tz))[:-9]
#     print("UST={ust}, JST={jst}".format(ust=dat["dt_txt"],jst=jst))



#####実践プログラム作成##################

# 一括取得(URLとタイトル)---------------------------------------------
# import requests
# from bs4 import BeautifulSoup

# # urlをsoupで加工する準備
# loadUrl = "http://qiita.com/advent-calendar/2016/crawler"
# html = requests.get(loadUrl)
# soup = BeautifulSoup(html.content,"html.parser")

# # 各項目ごとでurlとテキストを取得して書き込み
# for a in soup.select('.adventCalendarCalendar_comment a'):
#     print(a['href'], a.text)

#------------------------------------------------------------------


# サイトから画像を取って保存する----------------------------------------
import requests
from bs4 import BeautifulSoup
from pathlib import Path
import urllib
import time

load_url = "http://maima.me/"
html = requests.get(load_url)
soup = BeautifulSoup(html.content,"html.parser")

# 保存先作成
out_folder = Path("download4")
out_folder.mkdir(exist_ok=True)

# タグごとに検索して保存
for element in soup.find_all("img"):
    src = element.get("src")

    image_url = urllib.parse.urljoin(load_url,src)
    imgdata = requests.get(image_url)

    filename = image_url.split("/")[-1]
    out_path = out_folder.joinpath(filename)

    with open(out_path,mode ="wb") as f:
        f.write(imgdata.content)

    time.sleep(1)

#------------------------------------------------------------------


