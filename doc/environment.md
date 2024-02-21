# 仮想環境（任意）
授業では仮想環境を用いなかったが，
利用に慣れておくのが理想である．
仮想環境を用いることで
一つのパソコンの中で異なるバージョンのライブラリを利用したり，
別のパソコンでも同じ環境を簡単に構築できるようになったりする．
仮想環境を実現する手段はいくつかあるが，
Djangoの教科書にも書かれていた
pyenvが特に簡単．
詳細な説明は教科書や各種Webサイトに譲るとして，ここでは
コマンドの一例を示す．
```
mkdir -p ~/Desktop/Django/project  # ディレクトリ作成
cd ~/Dedktop/Django/project
python3 -m venv .env  # .で始まると隠しファイルになり表示にはls -aが必要
source .env/bin/activate
pip3 install django
pip3 freeze > requirements.txt  # pip3 freezeの実行結果をrequirements.txtに保存
```
最後の[requirements.txt](../requirements.txt)があれば，別のpc等で
```
pip3 install -r requirements.txt
```
とすることで同じバージョンの各ライブラリを一発で入れることができる．





