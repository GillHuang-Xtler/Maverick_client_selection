def log_client_data_statistics(logger, label_class_set, distributed_dataset):
    for client_idx in range(len(distributed_dataset)):
        client_class_nums = {class_val : 0 for class_val in label_class_set}
        for target in distributed_dataset[client_idx][1]:
            try:
                client_class_nums[target] += 1
            except:
                continue

        logger.info("Client #{} has data distribution: {}".format(client_idx, str(list(client_class_nums.values()))))
