# This is a simple practice regarding Fastapi and Pytest
- Implementing bookstore server API with Fastapi 
- Testing Restful API with Pytest framework
- Generate allure report of the test results

## Fastapi
Installation
```sh
pip install fastapi
pip install "uvicorn[standard]"
```
Run the server
```sh
uvicorn main:app --reload
```
## Implementing bookstore server API
![bookstore server API](https://i.imgur.com/NkJmVZZ.png)

## Pytest
Installation
```sh
pip install pytest
```
## Testing with Pytest framework
```sh
python pytest
```
![Restful API with Pytest](https://i.imgur.com/fWh6Vhp.png)

## Allure tool
Installation
```sh
pip install allure-pytest
```
## Generate the allure report of the test results
```sh
python pytest --alluredir=.\test_report
```
![Allure report](https://i.imgur.com/ZmkzEL8.png)

## References
[FastAPI Python Tutorial - Learn How to Build a REST API](https://www.youtube.com/watch?v=34cqrIp5ANg&ab_channel=pixegami)\
[PyTest • REST API Integration Testing with Python](https://www.youtube.com/watch?v=7dgQRVqF1N0&t=1515s&ab_channel=pixegami)

## Useful Links
[Fastapi](https://fastapi.tiangolo.com/) \
[Pytest](https://docs.pytest.org/en/7.4.x/) \
[Allure](https://allurereport.org/)

## TODO list and known issues
- Code optimization and/or refactor
- [PyCharm unable to find fixtures in conftest.py](https://intellij-support.jetbrains.com/hc/en-us/community/posts/12897247432338-PyCharm-unable-to-find-fixtures-in-conftest-py)