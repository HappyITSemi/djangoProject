# memo DJANGO_SETTINGS_MODULE=dockerproject.settings

# pip show django-allauth

# Django installation

# if you using the anaconda, you should activate or deactivate <basic env>.

# $> conda activate / deactivate

# make venv > virtual env

$> python3 -m venv <your_venv>

# python3 manage.py migrate Create a DB for management.

# Create migration file

$> python3 manage.py makemigrations

# Adapt migrations to database.

$> python3 manage.py migrate

# List migrations (by app/name)

$> python3 manage.py showmigrations

- - - - - - - - - - - - - - - - - - - - -

# Install superuser

$> python3 manage.py createsuperuser $> python3 manage.py createsuperuser --username=admin --email=admin@email.com

# Change superuser's password

$ python3 manage.py changepassword admin

# Create the application

# python3 manage.py startapp XXXXXX
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

sudo update-alternatives --config python
- - - - - - - - - - - - - - - - - - - - -
■registrations
https://django-registration.readthedocs.io/en/3.2/index.html

