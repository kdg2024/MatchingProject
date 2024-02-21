from .models import MessageTable
from django import forms

class MessageForm(forms.ModelForm):
  class Meta:
    model = MessageTable
    fields = ('message',)  # 要素数1のタプルにするためにカンマをつける
    widgets = {
      'message': forms.Textarea(
        attrs={
          # ここに書いたものがHTMLの属性として出力される
          'class': 'message-form',  # クラスを指定しているが特に利用はしていない
          'style': 'width: 300px;',  # テキストエリアの幅を指定，同様にheightで高さも指定可能
          'rows': 1,   # 行数を指定，同様にcolsで列数（1行の文字数）も指定可能
        }
      ),
    }
