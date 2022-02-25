<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://www.spaceflightnewsapi.net/img/SNAPI_logo.png" alt="Project logo"></a>
</p>

<h3 align="center">Back-end Challenge 🏅 2021 - Space Flight News</h3>

<div align="center">

<p align="center">
	<a href="https://github.com/varini">
		<img alt="Author" src="https://img.shields.io/badge/author-Leonardo%20Varini-blue?style=flat" />
	</a>
</p>

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/varini/varini.svg)](https://github.com/varini/varini/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/varini/varini.svg)](https://github.com/varini/varini/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> Python Spaceflight News API
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Built Using](#built_using)

## 🚀 About <a name = "about"></a>

A REST API that uses data from the  [Space Flight API](https://spaceflightnewsapi.net/) project, a public API with information related to spaceflights. 
It includes CRUD routes and database synchronization consuming data from the original API.

> This project refers to a challenge by [Coodesh](https://.coodesh.com/)

## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Installing
#
Setup a Virtual Environment
```shell
virtualenv venv
```
Create a .env file according to the example
```
ADMIN_USER=admin_user
ADMIN_PASSWD=admin_pass
DATABASE=database
DOMAIN=domain

RETRY_WRITES=true
WRITE_CONCERN=majority

CONNECT_STR=mongodb+srv://${ADMIN_USER}:${ADMIN_PASSWD}@${DOMAIN}/${DATABASE}?retryWrites=${RETRY_WRITES}&w=${WRITE_CONCERN}
```
For Linux/Mac
```shell
source venv/bin/activate
```
For Windows
```shell
venv/Scripts/activate
```
Install packages
```shell
pip install -r .\requirements.txt
```
Populate database
```shell
python .\init_db.py
```
Start server 
```shell
uvicorn index:app --reload
```

## 🔧 Running the tests <a name = "tests"></a>

Install pytest
```
pip install pytest
```
Run pytest
```
python -m pytest
```
## 🎈 Usage <a name="usage"></a>

A brief explanatory video of this project: https://www.loom.com/share/ee82f13e62924a2faaaa6d7b7af21111

After running the API, you can also check its documentation by accessing: http://localhost:8000/docs


## ⛏️ Built Using <a name = "built_using"></a>

- [Python](https://www.python.org/) - Programming Language
- [MongoDB](https://www.mongodb.com/) - Database
- [FastAPI](https://fastapi.tiangolo.com/) - API Framework
- [PyTest](https://pytest.org/) - Test Framework
