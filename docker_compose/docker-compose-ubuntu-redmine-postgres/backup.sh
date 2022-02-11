#!/bin/sh

# バックアップファイルを何日分残しておくか
period='+7'
# バックアップファイルを保存するディレクトリ
dirpath='./backupfolder'

#バックアップ元フォルダ
backupfolder="./storage"

# ファイル名を定義(※ファイル名で日付がわかるようにしておきます)
mydate=`date +%y%m%d%H%M%S`
filename="images_$mydate.tar.gz"
#backup実行
tar -zcvf $dirpath/$filename $backupfolder

# パーミッション変更
chmod 700 $dirpath/$filename

# 古いバックアップファイルを削除
find $dirpath -type f -daystart -mtime $period -exec rm {} \;
