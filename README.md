# mtk_scatter_editor(Japanese)

Mediatek端末のパーティションサイズを変更することができます。

## 使い方

1,python .\mtk_scatter_editor.py 編集するファイル名 編集後のファイル名

2,一覧から編集対象のパーティション番号を入力する。ここではrecoveryを選択する。
```
 python .\mtk_scatter_editor.py .\MT8167_Android_scatter_default.txt test.txt
+--------+-----------+------------+------------+-------------+------------------+
|   番号 | 名前      |    開始(B) |    終了(B) |   サイズ(B) | サイズ(最適化)   |
+========+===========+============+============+=============+==================+
|      0 | preloader |          0 |          0 |           0 | 0.0KB            |
+--------+-----------+------------+------------+-------------+------------------+
|      1 | pgpt      |          0 |     524288 |      524288 | 512.0KB          |
+--------+-----------+------------+------------+-------------+------------------+
|      2 | proinfo   |     524288 |    3670016 |     3145728 | 3.0MB            |
+--------+-----------+------------+------------+-------------+------------------+
|      3 | nvram     |    3670016 |    8912896 |     5242880 | 5.0MB            |
+--------+-----------+------------+------------+-------------+------------------+
|      4 | protect1  |    8912896 |   19398656 |    10485760 | 10.0MB           |
+--------+-----------+------------+------------+-------------+------------------+
|      5 | protect2  |   19398656 |   29884416 |    10485760 | 10.0MB           |
+--------+-----------+------------+------------+-------------+------------------+
|      6 | persist   |   29884416 |   80216064 |    50331648 | 48.0MB           |
+--------+-----------+------------+------------+-------------+------------------+
|      7 | seccfg    |   80216064 |   80478208 |      262144 | 256.0KB          |
+--------+-----------+------------+------------+-------------+------------------+
|      8 | lk        |   80478208 |   80871424 |      393216 | 384.0KB          |
+--------+-----------+------------+------------+-------------+------------------+
|      9 | lk2       |   80871424 |   81264640 |      393216 | 384.0KB          |
+--------+-----------+------------+------------+-------------+------------------+
|     10 | boot      |   81264640 |   98041856 |    16777216 | 16.0MB           |
+--------+-----------+------------+------------+-------------+------------------+
|     11 | recovery  |   98041856 |  114819072 |    16777216 | 16.0MB           |
+--------+-----------+------------+------------+-------------+------------------+
|     12 | para      |  114819072 |  115343360 |      524288 | 512.0KB          |
+--------+-----------+------------+------------+-------------+------------------+
|     13 | logo      |  115343360 |  123731968 |     8388608 | 8.0MB            |
+--------+-----------+------------+------------+-------------+------------------+
|     14 | expdb     |  123731968 |  134217728 |    10485760 | 10.0MB           |
+--------+-----------+------------+------------+-------------+------------------+
|     15 | tee1      |  134217728 |  139460608 |     5242880 | 5.0MB            |
+--------+-----------+------------+------------+-------------+------------------+
|     16 | tee2      |  139460608 |  144703488 |     5242880 | 5.0MB            |
+--------+-----------+------------+------------+-------------+------------------+
|     17 | kb        |  144703488 |  146800640 |     2097152 | 2.0MB            |
+--------+-----------+------------+------------+-------------+------------------+
|     18 | dkb       |  146800640 |  150994944 |     4194304 | 4.0MB            |
+--------+-----------+------------+------------+-------------+------------------+
|     19 | factory   |  150994944 |  167772160 |    16777216 | 16.0MB           |
+--------+-----------+------------+------------+-------------+------------------+
|     20 | metadata  |  167772160 |  201326592 |    33554432 | 32.0MB           |
+--------+-----------+------------+------------+-------------+------------------+
|     21 | system    |  201326592 | 2348810240 |  2147483648 | 2.0GB            |
+--------+-----------+------------+------------+-------------+------------------+
|     22 | cache     | 2348810240 | 3422552064 |  1073741824 | 1.0GB            |
+--------+-----------+------------+------------+-------------+------------------+
|     23 | userdata  | 3422552064 | 3422552064 |           0 | 0.0KB            |
+--------+-----------+------------+------------+-------------+------------------+
|     24 | flashinfo | 4294901892 | 4294901892 |           0 | 0.0KB            |
+--------+-----------+------------+------------+-------------+------------------+
|     25 | sgpt      | 4294901764 | 4294901764 |           0 | 0.0KB            |
+--------+-----------+------------+------------+-------------+------------------+
パーティション番号：11
```
3,拡張、もしくは縮小を選ぶ。ここでは2MB拡張する
```
拡張:1
縮小:2
選択：1
```
4,サイズを入力する。単位なしの場合はバイト、k/Kを末尾につけた場合はKB、m/Mを末尾につけた場合はMB、g/Gを末尾につけた場合GBとして扱われる。
```
サイズを入力してください(例：120 100K 10M 2G)
サイズ：2M
```
５，自動で処理が始まり保存が完了する。このファイルはsp flash toolで利用可能。


# mtk_scatter_editor(English)

You can change the partition size on your Mediatek device.

## Usage

1,python . \mtk_scatter_editor.py File name to be edited File name after editing

2,Enter the partition number of the partition to be changed from the list. In this case, select ``recovery''.
```
 python .\mtk_scatter_editor.py .\MT8167_Android_scatter_default.txt test.txt
+--------+-----------+------------+------------+-------------+------------------+
|   Num | Name      |    Start(B) |    End(B) |   Size(B) | Size(optimized)   |
+========+===========+============+============+=============+==================+
|      0 | preloader |          0 |          0 |           0 | 0.0KB            |
+--------+-----------+------------+------------+-------------+------------------+
|      1 | pgpt      |          0 |     524288 |      524288 | 512.0KB          |
+--------+-----------+------------+------------+-------------+------------------+
|      2 | proinfo   |     524288 |    3670016 |     3145728 | 3.0MB            |
+--------+-----------+------------+------------+-------------+------------------+
|      3 | nvram     |    3670016 |    8912896 |     5242880 | 5.0MB            |
+--------+-----------+------------+------------+-------------+------------------+
|      4 | protect1  |    8912896 |   19398656 |    10485760 | 10.0MB           |
+--------+-----------+------------+------------+-------------+------------------+
|      5 | protect2  |   19398656 |   29884416 |    10485760 | 10.0MB           |
+--------+-----------+------------+------------+-------------+------------------+
|      6 | persist   |   29884416 |   80216064 |    50331648 | 48.0MB           |
+--------+-----------+------------+------------+-------------+------------------+
|      7 | seccfg    |   80216064 |   80478208 |      262144 | 256.0KB          |
+--------+-----------+------------+------------+-------------+------------------+
|      8 | lk        |   80478208 |   80871424 |      393216 | 384.0KB          |
+--------+-----------+------------+------------+-------------+------------------+
|      9 | lk2       |   80871424 |   81264640 |      393216 | 384.0KB          |
+--------+-----------+------------+------------+-------------+------------------+
|     10 | boot      |   81264640 |   98041856 |    16777216 | 16.0MB           |
+--------+-----------+------------+------------+-------------+------------------+
|     11 | recovery  |   98041856 |  114819072 |    16777216 | 16.0MB           |
+--------+-----------+------------+------------+-------------+------------------+
|     12 | para      |  114819072 |  115343360 |      524288 | 512.0KB          |
+--------+-----------+------------+------------+-------------+------------------+
|     13 | logo      |  115343360 |  123731968 |     8388608 | 8.0MB            |
+--------+-----------+------------+------------+-------------+------------------+
|     14 | expdb     |  123731968 |  134217728 |    10485760 | 10.0MB           |
+--------+-----------+------------+------------+-------------+------------------+
|     15 | tee1      |  134217728 |  139460608 |     5242880 | 5.0MB            |
+--------+-----------+------------+------------+-------------+------------------+
|     16 | tee2      |  139460608 |  144703488 |     5242880 | 5.0MB            |
+--------+-----------+------------+------------+-------------+------------------+
|     17 | kb        |  144703488 |  146800640 |     2097152 | 2.0MB            |
+--------+-----------+------------+------------+-------------+------------------+
|     18 | dkb       |  146800640 |  150994944 |     4194304 | 4.0MB            |
+--------+-----------+------------+------------+-------------+------------------+
|     19 | factory   |  150994944 |  167772160 |    16777216 | 16.0MB           |
+--------+-----------+------------+------------+-------------+------------------+
|     20 | metadata  |  167772160 |  201326592 |    33554432 | 32.0MB           |
+--------+-----------+------------+------------+-------------+------------------+
|     21 | system    |  201326592 | 2348810240 |  2147483648 | 2.0GB            |
+--------+-----------+------------+------------+-------------+------------------+
|     22 | cache     | 2348810240 | 3422552064 |  1073741824 | 1.0GB            |
+--------+-----------+------------+------------+-------------+------------------+
|     23 | userdata  | 3422552064 | 3422552064 |           0 | 0.0KB            |
+--------+-----------+------------+------------+-------------+------------------+
|     24 | flashinfo | 4294901892 | 4294901892 |           0 | 0.0KB            |
+--------+-----------+------------+------------+-------------+------------------+
|     25 | sgpt      | 4294901764 | 4294901764 |           0 | 0.0KB            |
+--------+-----------+------------+------------+-------------+------------------+
Partition number：11
```
3, Select "expand" or "shrink". In this case, choose 2MB expansion.
```
Extension:1
Extended:1
shrink:2
Selection: 1
```
4, Enter the size. If no unit is given, it is treated as bytes; if k/K is added at the end, it is treated as KB; if m/M is added at the end, it is treated as MB; if g/G is added at the end, it is treated as GB.
```
Enter size (e.g. 120 100K 10M 2G)
Size: 2M
```
5，Automatic processing will start and saving will be completed. This file can be used with sp flash tool.

