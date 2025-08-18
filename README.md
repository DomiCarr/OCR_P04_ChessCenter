# ChessCenter
ChessCenter is an application that manage chess tournaments

## Application Architecture

The screenshot shows the overall structure of the application
The players and tournaments are stored in JSON files in the data directory

![Project Architecture](assets/wikibooks_architecture.png)



# Application Installation

This application need to be installed from the OCR_P04_ChessCenter repository that has been created in the company app by the git clone command
(git clone https://github.com/DomiCarr/OCR_P04_ChessCenter)

*** enter the application repository:**
OCR_P04_ChessCenter

### Create and activate the virtual environment
python -m venv env
source env/bin/activate

### Install the packages from requirements.txt
pip install -r requirements.txt

### Check that the packages has been installed
pip freeze

The result must have the 2 following lines bellow:

### Run the application
cd src
python ChessCenter.py

## Fabriqué avec
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)


## Releases
**First release :** 1.0

## Authors
* **Dominique Carrasco** _alias_ [@DomiCarr](https://github.com/DomiCarr)

## License

This project has an [OpenClassrooms](https://openclassrooms.com/fr/policies/terms-conditions) license




