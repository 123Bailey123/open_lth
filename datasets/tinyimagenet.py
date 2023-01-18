class Dataset(base.ImageDataset):
    """Tiny-Image"""
    @staticmethod
    def num_train_examples(): return 100000

    @staticmethod
    def num_test_examples(): return 10000

    @staticmethod
    def num_classes(): return 200
    