
#ベースイメージを指定する
#公式のpython:3を元となるイメージとして使う
FROM python:3

#標準出力のバッファが効いていると途中経過が見れず不便
#バッファを無効にする
ENV PYTHONUNBUFFERED 1

#/app_dirディレクトリを作成、そこで作業したい
RUN mkdir /app_dir
WORKDIR /app_dir/mysite_5


#現在のディレクトリ内部のファイルをコンテナにコピー
ADD . /app_dir

#自分でこのファイルと同ディレクトリにつくった
#requirements_5.txtを参照してインストールする？
#なんか知らんけど、以下のコマンドは手動で実行しないと参照が失敗する
RUN pip install -r requirements.txt

                                             