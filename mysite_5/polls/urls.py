#pathを設定したいからpathモジュールを使う？
from django.urls import path

#このファイルと同じ場所（階層）からviws.pyの中身を参照してそのまま利用する：インポートをすればよい
from . import views

urlpatterns = [
    #URLについて、polls/の下に何もないときは、views.pyを参照
        #views.py内で定義したindex関数を呼び出す
        #name=で、このURLパターンに名前をつけて実際のURLを取得できる
    path('', views.index, name='index'),
]