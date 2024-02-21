# `message`アプリ
DM機能を実装する（このリポジトリの根幹）．
一般に，DMやグループでのメッセージのやりとりを実装する場合は
- userテーブル
- roomテーブル
- messageテーブル
の３つが必要です．
それぞれのテーブル間の関係は
- userテーブルとmessageテーブル: 1人のユーザーは複数のメッセージを送信する→一対多
- 1つのルームは複数のmessageを持つ→一対多
- userテーブル--roomテーブル: 1人のユーザーは複数のroomに所属し，1つのroomには複数のユーザーが所属する→多対多
です．ここで，一対多は多側に一を格納するカラムを作ればいいので簡単ですが，
多対多はどうでしょうか．
ある行のある列には一つのデータしか格納できません．
そこで登場するのが中間テーブルで，２つのモデルの関係性を保存します．
例えば，３人のユーザーがあるルームに参加していれば，user_idとroom_id
の２つのカラムからなる中間テーブルで
- user_id=1, room_id=1
- user_id=2, room_id=1
- user_id=3, room_id=1
とすれば良いです．

よってこれを実装しても良いのですが，Djangoのmodelsには
`ManyToManyField`という，
**多対多を
中間テーブル無しで実現できる便利な仕組みがあります**．
詳細は各自でググっていただきたいですが，
結論としては[messageアプリのmodels.py](../message/models.py)
に以下のように記述します．
```
from django.db import models
from accounts.models import CustomUser 

class RoomTable(models.Model):
  name = models.CharField(max_length=100)
  members = models.ManyToManyField(CustomUser, related_name="room_user")
  # 本来であれば中間テーブルが必要だが，
  # DjangoでManyToManyFieldを用いれば自動で作成される.
  # memberを追加するときは`self.members.add(user)`
  # memberを削除するときは`self.members.remove(user)`
  # memberを参照するときは`self.members.all()`

class MessageTable(models.Model):
  room = models.ForeignKey(RoomTable, on_delete=models.CASCADE)
  sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
  message = models.CharField(max_length=1000)
  at = models.DateTimeField(auto_now_add=True)
```
その後忘れないうちに[admin.py](../message/admin.py)に登録しておく．
```
from django.contrib import admin
from .models import RoomTable, MessageTable

admin.site.register(RoomTable)
admin.site.register(MessageTable)
```
`ManyToManyField`の使い方はコメントアウトでの記述の通り．
これにより，擬似的にある行のある列に複数のUserを登録できます．
あとはこれを使って
[views.py](../message/views.py)，
[forms.py](../message/views.py)，
[urls.py](../message/urls.py)
を作成し，必要なHTMLファイルは[index.html](../templates/message/index.html)，
[room.html](../templates/message/room.html)を参照のこと．

[views.py](../message/views.py)では関数ベースを利用しています．
流派もあるでしょうが，典型でない処理をするときにはこの方が便利だったりします．
`index`関数は一覧表示，`room`関数はルームのヒュージ，
`direct`関数が相手のuser_id
と自分のrequest（自分のuser情報あり）
からDMのルームが存在するか確認し，存在すればDMのルームに`redirect`，
存在しなければルームを作成してから`redirect`します．
`redirect`が何なのか忘れてしまった人は教科書189ページを参照しましょう．
また，`direct`関数における
```
rooms = RoomTable.objects.annotate(
num_members=Count('members')
).filter(
members=request.user
).filter(
members=recipient
).filter(
num_members=2
)
```
の部分は，SQLにおける`group by`のような運用がなされています．
この部分をSQLに書き直すとどのようになるか，各自ググりながら考えてみましょう．
































