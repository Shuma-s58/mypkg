![test](https://github.com/melonsuika58/mypkg/actions/workflows/test.yml/badge.svg)

# mypkg
これは、ros2のパッケージです。
* できること
  * 数字をカウントアップして、トピック/countupを通じて送信できる。
  * メッセージの型は、16ビット符号つき整数です。
  ```sh
  # 実行 (端末1)
  ros2 launch mypkg talk_listen.launch.py
  # ^Cで終了
  ```
  * その他のファイルの説明は、以下の「ファイルの説明」をご覧ください。
* 使用したコマンド
  * cat, grepを使用

# ファイルの説明
* README.md:
  * このリポジトリについての説明です。最初にお読みください。
* talker.py(場所: ./mypkg/mypkg/talker.py):
  * "listener.py"に対し、数字のカウントアップを伝達するパブリッシャーを1つ持つ。。
  * 注意：このノードは"listener.py"と並行して使用するノードです。
  ```sh
  # 実行
  ros2 run mypkg talker
  # ^Cで終了
  ```
* listener.py(場所: ./mypkg/mypkg/listener.py):
  * "talker.py"から送られてた数字を受け取るサブスクライバーを１つ持つ。
  * 注意：このノードは"talker.py"と並行して使用するノードです。
  ```sh
  # 実行(talker.pyを起動後、別の端末で実行してください。)
  ros2 run mypkg listener
  # ^Cで終了
  ```
* talk_listen.launch.py(場所: ./mypkg/launch/talk_listen.launch.py):
  * 上記の"talker.py"と"listener.py"を同時に起動させる。
  ```sh
  # 実行
  ros2 launch mypkg talk_listen.launch.py
  # ^Cで終了
  ```
* test.bash(場所: ./mypkg/test/test.bash):
  * talk_listen.launch.pyに対するテスト
  ```sh
  # 移動
  cd ./mypkg/test
  # 実行
  ./test.bash
  ```

* LICENSE:
  * 3条項BSDライセンス

# 必要なソフトウェア
* Python
  * テスト済み: 3.7～3.10

# テスト環境
* Ubuntu 22.04.01 LTS
# 参考にしたもの
* grepコマンドとは？
  * https://academy.gmocloud.com/lesson/20191009/7620
 
# ライセンスについて
* このソフトウェアパッケージは、3条項BSDライセンスの下、再分布および使用が許可されています
。
* © 2022 Shuma Suzuki
