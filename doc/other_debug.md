# その他・デバッグ　
ここまでできたら，データベースに反映してとりあえず `runserver`しましょう．
必要に応じてスーパーユーザーも作ります．
```
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver
```
もしエラーが出たら，そのメッセージに沿って直してください．
