# RPG - Internal web project for monitoring and managing the process of passing the laboratory

## Requirements:
* python 3.8 or latest
* Install all dependencies: "pip install -r requirements.txt"
    
## Run tests:
* Run one test: "pytest tests/<module_name>/<test_name>"
* Run all tests: "pytest tests/"
* Run using pytest-xdist: "pytest -n <n>"

## Allure reports:
* Save test results in allure: "--alluredir=allure_report"
* Clear allure results of previous test run: "--clean-alluredir"
* Generate allure report: "allure serve allure_report/"

## MR's crating rules:
* Template of MR's name, example: "TASK-1: Short changes descriptions"
* Run artifacts: Screenshots of test's runs
