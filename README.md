# bookbot

BookBot is my first [Boot.dev](https://www.boot.dev) project!

## Installation python
1. Install python first in one of the following ways:
- from [python.org](https://www.python.org/downloads)
- Or use a package manager:
```
apt install python3 #Ubuntu/WSL
choco install python #Windows
```
2. Verify Installation of python:
```
python3 --version #Ubuntu/WSL
python --version #Windows
```

## Download project
1. Find a folder for the project. example: ```workspace/<website_com>/<user_name>/<project_name>``` for me that works out to >> ```workspace/github_com/levi_goossens_pxl```
2. Assuming you have installed [Git](https://git-scm.com/downloads) on your system use the following command in the folder you want the project folder to exist:
```
git clone https://github.com/LeviGoossensPXL/bookbot
```

## Usage
if u open the project folder in a terminal you can now use the following command to get a short book report about any text file:
```
python3 main.py <path_to_book> #Ubuntu/WSL
python main.py <path_to_book> #Windows
```
