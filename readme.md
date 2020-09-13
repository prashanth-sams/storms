# Storms

## Installation
Install python libraries

    pip3 install -r requirements.txt

## Test Runner

| Action         | Command            |
| -------------- | ---------          |
| Bash runner    | `bash runner/android/smoke_run.sh` |
| Default        | `python3 -m pytest src/spec/* --app=android` |
| Rerun failures | `python3 -m pytest src/spec/home_test.py --app=android --reruns 1` |
| Parallel Test  | `python3 -m pytest src/spec/home_test.py --app=android -v -n2` |

## Test Report
| Type           | Command            |
| -------------- | ---------          |
| HTML Report    | `python3 -m pytest src/spec/*.py --html-report=./report` |
| JSON Report    | `python3 -m pytest src/spec/*.py --json=report/json/report.json` |