from federated_learning.worker_selection import RandomSelectionStrategy
from federated_learning.server import run_exp
from federated_learning.nets import FashionMNISTCNN
import pathlib
from federated_learning.arguments import Arguments
from federated_learning.datasets import FashionMNISTDataset
from federated_learning.utils import generate_train_loader
from federated_learning.utils import generate_test_loader
from federated_learning.utils import save_data_loader_to_file

import os
import torch
from loguru import logger

def generate_data_distribution():
    args = Arguments(logger)
    dataset = FashionMNISTDataset(args)
    TRAIN_DATA_LOADER_FILE_PATH = "data_loaders/fashion-mnist/train_data_loader.pickle"
    TEST_DATA_LOADER_FILE_PATH = "data_loaders/fashion-mnist/test_data_loader.pickle"

    if not os.path.exists("data_loaders/fashion-mnist"):
        pathlib.Path("data_loaders/fashion-mnist").mkdir(parents=True, exist_ok=True)

    train_data_loader = generate_train_loader(args, dataset)
    test_data_loader = generate_test_loader(args, dataset)

    with open(TRAIN_DATA_LOADER_FILE_PATH, "wb") as f:
        save_data_loader_to_file(train_data_loader, f)

    with open(TEST_DATA_LOADER_FILE_PATH, "wb") as f:
        save_data_loader_to_file(test_data_loader, f)


def generate_default_models():
    args = Arguments(logger)
    if not os.path.exists(args.get_default_model_folder_path()):
        os.mkdir(args.get_default_model_folder_path())
    full_save_path = os.path.join(args.get_default_model_folder_path(), "FashionMNISTCNN.model")
    torch.save(FashionMNISTCNN().state_dict(), full_save_path)

if __name__ == '__main__':
    generate_data_distribution()
    generate_default_models()
    START_EXP_IDX = 2025
    NUM_EXP = 3
    NUM_POISONED_WORKERS = 0
    KWARGS = {
        "NUM_WORKERS_PER_ROUND" : 5
    }

    for experiment_id in range(START_EXP_IDX, START_EXP_IDX + NUM_EXP):
        run_exp(NUM_POISONED_WORKERS, KWARGS, RandomSelectionStrategy(), experiment_id)