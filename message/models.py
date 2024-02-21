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

