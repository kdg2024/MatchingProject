# カスタムユーザーとログイン機能（accoutnsアプリ）
通常のUserモデルは汎用性が無い（カラムを追加できない）ので
カスタムユーザーを用いる．
方法は簡単．`AbstractUser`を継承するだけ．
[accountsアプリのmodels.py](../accounts/models.py)に以下のように記述する．
```
from django.db import models
from django.contrib.auth.models import AbstractUser
TYPE = (
  ("mentor", "メンター"),
  ("mentee","メンティー"),
  )
class CustomUser(AbstractUser):
  registration_type = models.CharField(max_length=10, choices=TYPE)
  profile = models.TextField(null=True,  blank=True)
```
そして，[settings.py](../MatchingProject/settings.py)に以下を追記する．
```
AUTH_USER_MODEL = 'accounts.CustomUser'
```
その後，[admin.py](../accounts/admin.py)には少しテクニカルに見えるかもだが
以下のように記述する．
```
from django.contrib import admin
from django.contrib.auth import get_user_model

CustomUser = get_user_model()
admin.site.register(CustomUser)
```
これで準備完了．この`CustomUser`を`User`の代わり用いる．
なお，ここまで記述するよりも前に
```
python3 manage.py migrate
```
を実行してしまうと厄介（というかダメだった気がする）ので注意．

次に[forms.py](../accounts/forms.py)を作成する．
```
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
  class Meta:
    model = CustomUser
    fields = ('username', 'password1', 'password2', 'registration_type')

class CustomUserEditForm(forms.ModelForm):
  class Meta:
    model = CustomUser
    fields = ("last_name", "first_name", "registration_type","profile")
```
サインアップのためのフォーム（`CustomUserCreationForm`）は，`UserCreationForm`を継承するのは
教科書と同じであるものの，
`model`を`CustomUser`にしないといけないのが決定的な違い．
また，プロフィールを編集するためのフォーム（`CustomUserEditForm`）
は普通に作成する．
教科書においては主にクラスベースで製作されているため
`UpdateView`を持ちいて`forms.py`を用いずに更新を実現しているが，
今回はPaiza等でも紹介されている
**関数ベースでの更新**を用いる．
以下の
[views.py](../accounts/views.py)
によく着目すること．

[views.py](../accounts/views.py)
```
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserEditForm

class SignUpView(generic.CreateView):
  # form_class = UserCreationForm
  form_class = CustomUserCreationForm
  success_url = reverse_lazy('login')
  template_name = 'accounts/signup.html'


@login_required
def CustomUserEdit(request):
  # 自分の情報を編集しか認めないためidはいらない
  user = request.user
  if request.method == 'POST':
    form = CustomUserEditForm(request.POST, instance=user)
    if form.is_valid():
      form.save()
      return redirect("matching:index")
  else:
    form = CustomUserEditForm(instance=user)
    context = {
      "form":form
    }
    return render(request, 'accounts/edit.html', context)

@login_required
def CustomUserDetail(request, id):
  user_object = CustomUser.objects.get(pk=id)
  context = {
    "user_object":user_object
  }
  return render(request, 'accounts/detail.html', context)
```
続いて[urls.py](../accounts/urls.py)
```
from django.urls import path
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView
from . import views

app_name = 'accounts'

urlpatterns = [
  path('login/',LoginView.as_view(), name='login'),
  path('logout/',LogoutView.as_view(), name='logout'),
  path('signup/', views.SignUpView.as_view(), name='signup'),
  path('edit/', views.CustomUserEdit, name='edit'),
  path('detail/<int:id>', views.CustomUserDetail, name='detail'),
]

```
必要なHTMLファイルは以下を参照して作成．
デザインは微塵も考えていないのでカスタマイズ推奨．
場所は`templates/accounts/<ここ>`だが，`login.html`は
`templates/registration/login.html`である．本リポジトリを
要確認．
- [detail.html](../templates/accounts/detail.html)
- [edit.html](../templates/accounts/edit.html)
- [signup.html](../templates/accounts/signup.html)
- [login.html](../templates/registration/login.html)（配置場所に注意）

あと，`settings.py`に以下を追記しておく．
```
LOGIN_URL = "accounts:login"
```
これは`urls.py`で設定した名前に基づいて指定されている．

## 参考
- https://paiza.jp/works/django/primer/beginner-django3











