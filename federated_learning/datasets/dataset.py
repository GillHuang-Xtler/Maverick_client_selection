from abc import abstractmethod
from torch.utils.data import DataLoader
from torch.utils.data import TensorDataset
import torch

class Dataset:

	def __init__(self, args):
		self.args = args

		self.train_dataset = self.load_train_dataset()
		self.test_dataset = self.load_test_dataset()

	def get_args(self):
		return self.args

	def get_train_dataset(self):
		return self.train_dataset

	def get_test_dataset(self):
		return self.test_dataset

	@abstractmethod
	def load_train_dataset(self):
		raise NotImplementedError("load_train_dataset() isn't implemented")

	@abstractmethod
	def load_test_dataset(self):
		raise NotImplementedError("load_test_dataset() isn't implemented")

	def get_train_loader(self, batch_size, **kwargs):
		return Dataset.get_data_loader_from_data(batch_size, self.train_dataset[0], self.train_dataset[1], **kwargs)

	def get_test_loader(self, batch_size, **kwargs):
		return Dataset.get_data_loader_from_data(batch_size, self.test_dataset[0], self.test_dataset[1], **kwargs)

	@staticmethod
	def get_data_loader_from_data(batch_size, X, Y, **kwargs):
		X_torch = torch.from_numpy(X).float()

		if "classification_problem" in kwargs and kwargs["classification_problem"] == False:
			Y_torch = torch.from_numpy(Y).float()
		else:
			Y_torch = torch.from_numpy(Y).long()
		dataset = TensorDataset(X_torch, Y_torch)

		kwargs.pop("classification_problem", None)

		return DataLoader(dataset, batch_size=batch_size, **kwargs)

	@staticmethod
	def get_tuple_from_data_loader(data_loader):
		return (next(iter(data_loader))[0].numpy(), next(iter(data_loader))[1].numpy())
