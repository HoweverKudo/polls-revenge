from django.db import models

#タイムゾーンの取り扱いをするためのモジュール
import datetime
from django.db import models
from django.utils import timezone


class Question(models.Model):
    # Fieldクラスのインスタンスとして書くフィールドを表現する
    # ()内に引数を指定できる。ものによっては必須の引数をもつクラスもある。
    question_txt = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    # __str__()メソッドによって呼び出しを行い、
    # 出力結果を人間にとって理解できるものにする
    def __str__(self):
        return self.question_txt
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <=self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    # ForeignKeyクラスを使用してQuestionクラスとのリレーションを定義する
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_txt = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_txt