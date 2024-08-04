# SeleniumBase Tests

[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/ahmed-pasha/seleniumbase-tests/blob/main/LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/ahmed-pasha/seleniumbase-tests)](https://github.com/ahmed-pasha/seleniumbase-tests/issues)
[![GitHub stars](https://img.shields.io/github/stars/ahmed-pasha/seleniumbase-tests)](https://github.com/ahmed-pasha/seleniumbase-tests/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/ahmed-pasha/seleniumbase-tests)](https://github.com/ahmed-pasha/seleniumbase-tests/network)

# SeleniumBase Tests for The Internet Herokuapp

This repository contains automated tests using SeleniumBase for various functionalities on the "the-internet.herokuapp.com" website. The tests cover form authentication, file upload, JavaScript alerts, basic authentication, and dynamic controls.

## Test Cases

1. **Form Authentication**
2. **File Upload**
3. **JavaScript Alerts**
4. **Basic Authentication**
5. **Dynamic Controls** (Deliberately set to fail)

## Prerequisites

- Python 3.6+
- Pip (Python package installer)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/seleniumbase-tests.git
    cd seleniumbase-tests
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Running the Tests

To run the tests, use the following command:
```bash
pytest -v tests.py
