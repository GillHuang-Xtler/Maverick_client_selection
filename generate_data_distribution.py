from loguru import logger
import pathlib
import os
from federated_learning.arguments import Arguments
from federated_learning.datasets import FashionMNISTDataset
# from federated_learning.datasets import TRECDataset
from federated_learning.utils import generate_train_loader
# from federated_learning.utils import generate_benign_loader, generate_malicious_loader, generate_free_loader
from federated_learning.utils import generate_test_loader
from federated_learning.utils import save_data_loader_to_file
