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
タイムゾーンを変更しておく．
```
TIME_ZONE = 'Asia/Tokyo'
```
テンプレート（HTMLファイル）の置き場も設定しておく．
```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
    ...
```
今回，全アプリで共通のcssを利用し，その置き場所を`BASE_DIR`直下の`static_local`とする．
単に`static`としないのは`STATIC_ROOT`と重複しないようにするため．
その`STATIC_ROOT`は本番環境で静的ファイルを集約する場所である．
```
STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static_local"),]
if not DEBUG:
  STATIC_ROOT = os.path.join(BASE_DIR,'static') 
```
次に，**環境によって違う設定になる部分を分離する**．
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
[settings_local_sample.py](../MatMatchingProject/settings_local_sample.py)
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
を作っておく．
本リポジトリではデザインは最低限に留めているため，
教科書も参考にしながら各自で自由に作ってほしい．









