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
```
virtualenv venv
```
For Linux/Mac
```
source venv/bin/activate
```
For Windows
```
source venv/Scripts/activate
```
Install packages
```
pip install -r .\requirements.txt
```
Populate database
```
python .\init_db.py
```
Start server 
```
uvicorn index:app --reload
```

## 🔧 Running the tests <a name = "tests"></a>

How to run the automated tests for this project.

### Break down into end to end tests

What these tests test and why.

```
Examples...
```

## 🎈 Usage <a name="usage"></a>

A brief explanatory video of this project: https://www.loom.com/share/

You can check the API's documentation by accessing: http://localhost:8000/docs


## ⛏️ Built Using <a name = "built_using"></a>

- [Python](https://www.python.org/) - Programming Language
- [MongoDB](https://www.mongodb.com/) - Database
- [FastAPI](https://fastapi.tiangolo.com/) - API Framework