![test](https://github.com/melonsuika58/mypkg/actions/workflows/test.yml/badge.svg)

# mypkg
これは、ros2のパッケージです。
* ノードは、/talkerと/listenerの２つです。
  * /talker: パブリッシャーを1つ持つ。
  * /listener: サブスクライバーを1つ持つ。
* トピックと型
  *  トピックは、/countupです。
  *  メッセージの型は、16ビット符号つき整数です。

* できること
  * カウントアップした数字を/countupを通じて送信できる。(/talker)
  * /countupからメッセージをもらって表示できる。(/listener)
  ```sh
  # パターン1
  # 実行 (端末1)
  ros2 run mypkg talker   
  # 実行 (端末2)
  ros2 run mypkg listener
  # どちらも^Cで終了
  ```
  ```sh
  # パターン2
  # 実行
  ros2 launch mypkg talk_listen.launch.py
  # ^Cで終了
  ```
  * その他のファイルの説明は、以下の「ファイルの説明」をご覧ください。
* 使用したコマンド
  * cat, grepを使用

# ファイルの説明
* README.md:
  * このリポジトリについての説明です。最初にお読みください。
* talker.py(場所: `./mypkg/mypkg/talker.py`):
  * 数字のカウントアップを/countupを通じて伝達する。
  * パブリッシャーを1つ持つ。
  * 注意：このノードは/listenerと並行して使用するノードです。
  ```sh
  # 実行
  ros2 run mypkg talker
  # ^Cで終了
  ```
* listener.py(場所: `./mypkg/mypkg/listener.py`):
  * /countupから送られたメッセージを表示する。
  * サブスクライバーを１つ持つ。
  * 注意：このノードは/talkerと並行して使用するノードです。
  ```sh
  # 実行(talker.pyを起動後、別の端末で実行してください。)
  ros2 run mypkg listener
  # ^Cで終了
  ```
* talk_listen.launch.py(場所: `./mypkg/launch/talk_listen.launch.py`):
  * /talkerと/listenerを同時に起動させる。
  ```sh
  # 実行
  ros2 launch mypkg talk_listen.launch.py
  # ^Cで終了
  ```
* test.bash(場所: `./mypkg/test/test.bash`):
  * talk_listen.launch.pyに対するテスト
  ```sh
  # 移動
  cd ./mypkg/test
  # 実行
  ./test.bash
  ```

# テスト環境
* Ubuntu 22.04.01 LTS
# 参考にしたもの
* grepコマンドとは？
  * https://academy.gmocloud.com/lesson/20191009/7620
 
# ライセンスについて
* このソフトウェアパッケージは、3条項BSDライセンスの下、再分布および使用が許可されています
。
* © 2022 Shuma Suzuki
