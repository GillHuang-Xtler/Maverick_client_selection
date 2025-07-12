from abc import abstractmethod

class SelectionStrategy:

    @abstractmethod
    def select_round_workers(self, workers, poisoned_workers, kwargs):
        raise NotImplementedError("select_round_workers() not implemented")
