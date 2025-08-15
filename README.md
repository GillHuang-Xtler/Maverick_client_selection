# Maverick_client_selection
Code repository for paper "Maverick Matters: Client Contribution and Selection in
Federated Learning", PAKDD2023.
The example dataset is FashionMNIST, the downloading and default model settings are already set in the maverick.py, you do not need to prepare by yourself.

# To run this file

- python version in the development environment:3.8.10 
- pip install -r requirements.txt
- python generate_data_distribution.py
- python generate_default_models.py
- python maverick.py

# Note
Experiment setting:
- arguments are in 'federated_learning/arguments.py' + maverick.py

For each running, to save the results:
- set a START_EXP_IDX in maverick.py and run maverick.py
- the logs/results data will be in the logs/res folder

