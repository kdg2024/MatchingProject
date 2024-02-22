# 初期設定
プロジェクト名は
`MatchingProject`とし，
アプリは
`matching`，`message`，`accounts`
の３つを作成する．
```
django-admin startproject MatchingProject
cd MatchingProject
python3 manage.py startapp matching
python3 manage.py startapp message
python3 manage.py startapp accounts
```
その後，`MatchingProject/settings.py`の`INSTALLED_APPS`に作成したアプリを登録する．
これらは
**各アプリの`apps.py`に記述されたクラスである**．
```
INSTALLED_APPS = [
    ...
    'matching.apps.MatchingConfig',
    'message.apps.MessageConfig',
    'accounts.apps.AccountsConfig',
]
```
言語とタイムゾーンを変更しておく．
```
LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'
```
テンプレート（HTMLファイル）の置き場も設定しておく．
このとき，`os`を使うか`pathlib`を使うかは好みであるが，
前者を使う場合は
```
import os
```
を加えたうえで
```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
    ...
```
となる．礼として，
```
print(os.path.join("DIR1","DIR2","filename"))
```
の実行結果は以下の通り．
```
DIR1/DIR2/filename
```

今回，全アプリで共通のcssを利用し，その置き場所を`BASE_DIR`直下の`static_local`とする．
単に`static`としないのは`STATIC_ROOT`と重複しないようにするため．
その`STATIC_ROOT`は本番環境で静的ファイルを集約する場所である．
`STATIC_URL`はデフォルト通りでよく，`STATICFILES_DIRS`と`STATIC_ROOT`を追記する．
```
STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static_local"),]
if not DEBUG:
  STATIC_ROOT = os.path.join(BASE_DIR,'static') 
```
次に，**環境によって違う設定になる部分を分離する（しなくても動くので飛ばしても良い）**．
`git`の管理化にあるファイルを編集すると`git pull`ができなくなるなどするため
割と重要．
手段としては環境変数を用いる等が一般的だが，今回は簡易化のため
`settings_local.py`をimportすることにする．
**`settings_local.py`は`git`の管理化に入れない**．
`settings.py`の`SECRET_KEY`と`DEBUG`と
`ALLOWD_HOSTS`と`DATABASES`を`settings_local.py`に移動させる．
注意点として，`DATABASES`に`sqlite3`を用いる場合は
パスの指定で`BADE_DIR`が必要になるので
`BASE_DIR`も`settings_local.py`に入れること
（`settings.py`と`settings_local.py`に同じものがあっても問題は無い）．
また，そのサンプルとして
[settings_local_sample.py](../MatchingProject/settings_local_sample.py)
をコピーにより作成して`git`の管理化に加える．
その後，`settings.py`に以下を加える．
```
from .settings_local import *
```
なお，`SECRET_KEY`は以下のプログラムで新規生成が可能である．
```
from django.core.management.utils import get_random_secret_key
key = get_random_secret_key()
```
その後，[プロジェクトのurls.py](../MatchonMatchingProject/urls.py)に
各アプリの`urls.py`を読み込む記述をする．
下記2行目で`include`をimportするのを忘れずに．
```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
  path('admin/', admin.site.urls),
  path('accounts/', include('accounts.urls')),
  path('message/',include('message.urls')),
  path('',include('matching.urls')),
]
```
続いて，[base.html](../templates/base.html)
と[custom.css](../static_local/css/custom.css)
を作っておく．
本リポジトリではデザインは最低限に留めているため，
教科書も参考にしながら各自で自由に作ってほしい（コピペでも問題ない）．

## **注意**
Djangoの最新版（2023年末以降？）ではLogoutViewのGETメソッドが廃止されたようで，
教科書を参照して`base.html`を作成するとログアウト時にエラーが発生します．
仮想環境を使わない場合は以前にインストールしたバージョンで問題ないかもしれませんが，
新しいパソコンや仮想環境で迂闊に
`pip3 install django`としてしまうと最新版が入ってしまいます．
こういうことがあるので，[requirements.txt](../requrequirements.txt)
などバージョン指定は重要なんですね．

本リポジトリの
[base.html](../templates/base.html)
は最新版に対応しています．
```
{# <a class="navbar-item" href="{% url 'accounts:logout' %}"> #}
{#   {{ user }} - Logout #}
{# </a> #}
<form action="{% url 'accounts:logout' %}" method="post">
  {% csrf_token %}
  <button type="submit" class="btn btn-primary">{{ user }} - Logout</button>
</form>
```
今までは単にaタグでよかったですが，最新版では`form`タグで囲って明示的に`post`にする必要があるようです．
（本文執筆時点で得られた情報）








