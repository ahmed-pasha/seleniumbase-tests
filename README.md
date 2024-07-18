# SeleniumBase Tests

[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/ahmed-pasha/seleniumbase-tests/blob/main/LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/ahmed-pasha/seleniumbase-tests)](https://github.com/ahmed-pasha/seleniumbase-tests/issues)
[![GitHub stars](https://img.shields.io/github/stars/ahmed-pasha/seleniumbase-tests)](https://github.com/ahmed-pasha/seleniumbase-tests/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/ahmed-pasha/seleniumbase-tests)](https://github.com/ahmed-pasha/seleniumbase-tests/network)

## Table of Contents
- [Project Description](#project-description)
- [Setup Instructions](#setup-instructions)
- [Running Tests](#running-tests)
- [Test Details](#test-details)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Project Description

This repository contains automated tests using SeleniumBase for testing various functionalities on the [the-internet.herokuapp.com](https://the-internet.herokuapp.com) website. The tests cover form authentication, file upload, JavaScript alerts, basic authentication, and dynamic controls.

## Setup Instructions

Follow these instructions to set up and run the tests on your local machine.

### Prerequisites

- Python 3.x
- pip (Python package installer)
- Git

### Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/ahmed-pasha/seleniumbase-tests.git
   cd seleniumbase-tests
2. **Create and activate a virtual environment (optional but recommended)**:
   ```sh
   python -m venv venv
   .\venv\Scripts\Activate  # On Windows
   source venv/bin/activate  # On macOS/Linux
3. **Install the required packages**:
   ```sh
    pip install seleniumbase
4. **To run the tests, execute the following command**:
   ```sh
   pytest -v tests.py



