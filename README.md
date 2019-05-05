# wave_gui

現状製作途中のため、今後、リファクタリングを行っていく予定

## 実装済み機能一覧

* 参照ボタン-LoadするCSVファイルの選択
* Loadボタン-参照ボタンで選択したファイルのLoad及び、Wave選択ボックス追加
* Quitボタン-終了
* Wave選択ボックス-一番下のボタンの処理をされる波形選択
* Displayボタン-Wave選択ボックスで選んだ物をグラフ表示
* Save_CSVボタン-Wave選択ボックスで選んだ物をCSV形式で保存

## 未実装機能一覧

* Analyze選択ボックス
* Tableボタン
* Analyzeボタン

## 使い方

1. ターミナルで実行

```
$ python wave_gui.py
```

![Main_img](https://raw.githubusercontent.com/ryo1107/wave_gui/master/img/wave_gui.png)

2. するとウィンドウが出てくるので、参照ボタンをクリックし、LoadしたいCSVファイルを選択し、Loadボタンをクリックする。
3. Wave選択ボックスにCSVのファイル名の選択肢が追加されるので、選択をし、一番下の段のボタンをクリックする。
