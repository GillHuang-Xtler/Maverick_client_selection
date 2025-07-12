from .label_replacement import apply_class_label_replacement
from .client_utils import log_client_data_statistics


def poison_data(logger, distributed_dataset, num_workers, poisoned_worker_ids, poison_effort):
    poisoned_dataset = []
    class_label_set = set()
    for i in range(num_workers):
        class_label_set = class_label_set | set(distributed_dataset[i][1])
    class_labels = list(class_label_set)

    logger.info("Poisoning data for workers: {}".format(str(poisoned_worker_ids)))

    for worker_idx in range(num_workers):
        if worker_idx in poisoned_worker_ids:
            if poison_effort == 'full':
                poisoned_dataset.append(apply_class_label_replacement(distributed_dataset[worker_idx][0],
                                                                      distributed_dataset[worker_idx][1]))
            elif poison_effort == 'half' and worker_idx in range(0, int(len(distributed_dataset) / 2)):
                poisoned_dataset.append(distributed_dataset[worker_idx])

            elif poison_effort == 'half' and worker_idx in range(int(len(distributed_dataset) / 2), int(len(distributed_dataset))):
                poisoned_dataset.append(apply_class_label_replacement(distributed_dataset[worker_idx][0],
                                                                      distributed_dataset[worker_idx][1]))
        else:
            poisoned_dataset.append(distributed_dataset[worker_idx])

    log_client_data_statistics(logger, class_labels, poisoned_dataset)

    return poisoned_dataset

