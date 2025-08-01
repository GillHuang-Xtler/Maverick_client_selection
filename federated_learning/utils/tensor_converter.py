import numpy

def convert_distributed_data_into_numpy(distributed_dataset):
    converted_distributed_dataset = []

    for worker_idx in range(len(distributed_dataset)):
        worker_training_data = distributed_dataset[worker_idx]

        X_ = numpy.array([tensor.numpy() for batch in worker_training_data for tensor in batch[0]])
        Y_ = numpy.array([tensor.numpy() for batch in worker_training_data for tensor in batch[1]])

        converted_distributed_dataset.append((X_, Y_))

    return converted_distributed_dataset
