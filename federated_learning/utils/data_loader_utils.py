import numpy
from .label_replacement import apply_class_label_replacement
import os
import pickle
import random
from ..datasets import Dataset
import torch.utils.data


def generate_data_loaders_from_distributed_dataset(distributed_dataset, batch_size):
    data_loaders = []
    for worker_training_data in distributed_dataset:
        data_loaders.append(Dataset.get_data_loader_from_data(batch_size, worker_training_data[0], worker_training_data[1], shuffle=True))

    return data_loaders

def load_train_data_loader(logger, args):
    if os.path.exists(args.get_train_data_loader_pickle_path()):
        return load_data_loader_from_file(logger, args.get_train_data_loader_pickle_path())
    else:
        logger.error("Couldn't find train data loader stored in file")

        raise FileNotFoundError("Couldn't find train data loader stored in file")

def generate_train_loader(args, dataset):
    train_dataset = dataset.get_train_dataset()
    X, Y = shuffle_data(args, train_dataset)

    return dataset.get_data_loader_from_data(args.get_batch_size(), X, Y)

def load_test_data_loader(logger, args):
    if os.path.exists(args.get_test_data_loader_pickle_path()):
        return load_data_loader_from_file(logger, args.get_test_data_loader_pickle_path())
    else:
        logger.error("Couldn't find test data loader stored in file")

        raise FileNotFoundError("Couldn't find train data loader stored in file")

def load_data_loader_from_file(logger, filename):
    logger.info("Loading data loader from file: {}".format(filename))

    with open(filename, "rb") as f:
        return load_saved_data_loader(f)

def generate_test_loader(args, dataset):
    test_dataset = dataset.get_test_dataset()
    X, Y = shuffle_data(args, test_dataset)

    return dataset.get_data_loader_from_data(args.get_test_batch_size(), X, Y)

def shuffle_data(args, dataset):
    data = list(zip(dataset[0], dataset[1]))
    random.shuffle(data)
    X, Y = zip(*data)
    X = numpy.asarray(X)
    Y = numpy.asarray(Y)

    return X, Y

def load_saved_data_loader(file_obj):
    return pickle.load(file_obj)

def save_data_loader_to_file(data_loader, file_obj):
    pickle.dump(data_loader, file_obj)
