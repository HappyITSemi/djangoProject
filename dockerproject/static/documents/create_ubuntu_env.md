インスタンスのbashの設定を変更する。

vi ~/.bashrc

下記のように記述。

HISTSIZE=100000 HISTFILESIZE=200000 HISTTIMEFORMAT='%y/%m/%d %H:%M:%S '

この設定を読み込ませる。これでhistoryコマンドを打つとコマンドを打った日付が確認できて便利。

source ~/.bashrc

全パッケージの更新

sudo apt update && sudo apt -y upgrade && sudo apt -y autoremove

pip、PostgreSQL、Nginx等、必要なパッケージをインストール

sudo apt install python3-pip python3-dev libpq-dev postgresql postgresql-contrib nginx

postresはdockerの場合： sudo apt install python3-pip python3-dev nginx

virtualenvのインストール

sudo -H pip3 install --upgrade pip

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
---------------------------------------
git fetch origin git reset --hard origin/master

- - - - - - - - - - - - - - - - - - - - -
Priorityを選択して切り替える方法 sudo apt install -y software-properties-common

sudo update-alternatives --config python

リポジトリ追加

sudo apt install -y software-properties-common sudo add-apt-repository ppa:deadsnakes/ppa

sudo apt update

Python 各バージョンインストール

sudo apt install -y python3.9 python3.9-venv sudo apt install -y python3.8 python3.8-venv sudo apt install -y python3.7
python3.7-venv sudo apt install -y python3.6 python3.6-venv

定義

sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.9 130 sudo update-alternatives --install
/usr/bin/python python /usr/bin/python3.8 120 sudo update-alternatives --install /usr/bin/python python
/usr/bin/python3.7 110 sudo update-alternatives --install /usr/bin/python python /usr/bin/python2.7 10

sudo update-alternatives --config python pip install --upgrade pip
- - - - - - - - - - - - - - - - - - - - -
https://docs.docker.com/engine/install/ubuntu/
インストール sudo apt update sudo apt-get install \
ca-certificates \
curl \
gnupg \
lsb-release

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o
/usr/share/keyrings/docker-archive-keyring.gpg echo \
"
deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
$(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt update sudo apt install docker-ce docker-ce-cli containerd.io apt-cache madison docker-ce

sudo apt-get install docker-ce=5:20.10.12~3-0~ubuntu-bionic docker-ce-cli=5:20.10.12~3-0~ubuntu-bionic containerd.io
sudo apt-get install docker-ce=<VERSION_STRING> docker-ce-cli=<VERSION_STRING> containerd.io

docker version
- - - - - - - - - - - - - - - - - - - - -

アンインストール $ sudo apt-get purge docker-ce docker-ce-cli containerd.io

$ sudo rm -rf /var/lib/docker $ sudo rm -rf /var/lib/containerd
- - - - - - - - - - - - - - - - - - - - -

docker-composeをインストール curlでインストール sudo curl
-L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o
/usr/local/bin/docker-compose sudo chmod +x /usr/local/bin/docker-compose sudo ln -s /usr/local/bin/docker-compose
/usr/bin/docker-compose

$ docker-compose -v

アップデート $ docker-compose migrate-to-labels

アンインストール $ sudo rm /usr/local/bin/docker-compose

- - - - - - - - - - - - - - - - - - - - -
git-remote-codecommitのインストール

aws-cliインストール pip install

1、AWS CLI インストール 2、AWS Secret Access Keyを作成する 3、aws configureファイルの設定 4、gitconfigファイルの設定 5、git keychainを無効にする 6、認証情報の取得
7、git clone

１）AWS CLI インストール sudo pip3 install awscli --upgrade --user sudo apt install awscli aws --version

２）AWS Secret Access Key

３）aws configureファイルの設定 ・・・ アクセスキー/シークレットキー AKIA53XDSVSHXAV24UXA twL0r1I5Ykk6yNkjLOL6q+E/xxp3YDb61oCBFXnf 非表示

４）git configファイルの設定 3つのGitの設定ファイルは、 ①system, ②global, ③localの順に読み込まれる。

# .git/config

[core]                                                                                                                                                 
repositoryformatversion = 0 filemode = true bare = false logallrefupdates = true ignorecase = true precomposeunicode =
true
[remote "origin"]
url = https://git-codecommit.ap-northeast-1.amazonaws.com/v1/repos/django-vue
fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
remote = origin merge = refs/heads/main
[user]
name = [ユーザ名]
email = nakashima.toshio@icloud.com

sudo python3 -m pip install awscli==1.18.105 sudo python3 -m pip install botocore==1.17.28