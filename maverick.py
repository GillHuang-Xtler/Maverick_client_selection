from federated_learning.worker_selection import RandomSelectionStrategy
from federated_learning.server import run_exp

if __name__ == '__main__':
    START_EXP_IDX = 2025
    NUM_EXP = 3
    NUM_POISONED_WORKERS = 0
    KWARGS = {
        "NUM_WORKERS_PER_ROUND" : 5
    }

    for experiment_id in range(START_EXP_IDX, START_EXP_IDX + NUM_EXP):
        run_exp(NUM_POISONED_WORKERS, KWARGS, RandomSelectionStrategy(), experiment_id)