# `matching`アプリ
マッチングの根幹をなす部分だが，DM機能を分離しており
他の機能は一覧表示くらいしか実装していないためたいした量は無い．  
まず，[urls.py](../mamatching/urls.py)は以下の通り:
```
from django.urls import path
from . import views

app_name = "matching"

urlpatterns = [
  path('', views.index, name='index'),
]
```
そして[views.py](../matching/views.py)は以下の通り:
```
from django.shortcuts import render
from accounts.models import CustomUser
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

@login_required
def index(request):
  if request.user.registration_type == 'mentee':
    objects = CustomUser.objects.filter(registration_type='mentor')
  elif request.user.registration_type == 'mentor':
    objects = CustomUser.objects.filter(registration_type='mentee')
  else:
    return redirect('accounts:edit')
  context = {
    'objects': objects,
  }
  return render(request, 'matching/index.html', context)
```
HTMLファイルは以下を参照しながら自由に作成すること．
- [index.html](../templates/matching/index.html)
関数ベースで一覧機能のみなので`models.py`や`forms.py`は無し．
注意点は，ユーザーがメンターなのかメンティーなのかで
挙動が変化することくらい．
自分がメンターであればメンティー一覧，といった具合．

最後に，ログインしたあとこの一覧ページに遷移するように，
`settings.py`に以下を追記します．
```
LOGIN_REDIRECT_URL = "matching:index"
LOGOUT_REDIRECT_URL = "matching:index"  
````


