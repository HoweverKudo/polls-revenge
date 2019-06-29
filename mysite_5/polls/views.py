#HTTPレスポンスを返すためのモジュールをインポート
from django.http import HttpResponse

#リクエストを引数としてHello〜を出力する関数を定義する
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

