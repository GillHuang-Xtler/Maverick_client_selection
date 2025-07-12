import csv
import json
import os

def generate_json_repr_for_worker(worker_id, is_worker_poisoned, test_set_results):
    return {
        "worker_id" : worker_id,
        "is_worker_poisoned" : is_worker_poisoned,
        "test_set_results" : test_set_results
    }

def convert_test_results_to_json(epoch_idx, accuracy, loss, class_precision, class_recall):
    return {
        "epoch" : epoch_idx,
        "accuracy" : accuracy,
        "loss" : loss,
        "class_precision" : class_precision,
        "class_recall" : class_recall
    }

def save_results(results, filename):
    dirname = 'res'
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    with open(os.path.join(dirname,filename), 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')

        for experiment in results:
            writer.writerow(experiment)

def read_results(filename):
    data = []
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')

        for row in reader:
            data.append(row)

    return data

def save_results_v2(results, filename):
    with open(filename, "w") as f:
        json.dump(results, f, indent=4, sort_keys=True)

def read_results_v2(filename):
    with open(filename, "r") as f:
        return json.load(f)
