# Tests for imdb 250 raiting

### Simple way to run this tests from scratch:

#### 1) Setup environment:
* install last version of python3 https://www.python.org/downloads/
* check Python version: <br/> 
```python -V```<br/> 
(version must be greater than 3.8.0. If not, add latest Python version to the PATH)
* go to the root of the project
* setup virtual environment (venv): <br/>
```python -m venv imdb-250-env```
* activate venv: <br/>
on Windows, run: <br/>
```imdb-250-env\Scripts\activate.bat``` <br/>
on Unix or MacOs, run: <br/>
```source imdb-250-env/bin/activate```
* install the necessary dependencies: <br/>
```pip install -r requirements.txt```
* install Chrome driver: <br/>
1) download latest version from https://chromedriver.chromium.org/ and place it:<br/>
for windows: ```C:\Windows``` <br/>
for linux or MacOs: ```/usr/local/bin```
*check chrome driver version: ```chromedriver -V```<br/>
version should be > 83

#### 2) Run autotests (automated cases #8 and #9): 
```python -m unittest tests/test_imdb_top_movies.py``` 

#### 3) Some test-cases, smoke-cases you can find there: 
```/tests/Test cases.txt```

