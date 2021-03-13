from torchvision import transforms
from torchvision.datasets import ImageFolder
from torch.utils.data import DataLoader, Dataset

from config import Config


class Dataset(Dataset):
    def __init__(self, batch_size: int=Config.batch_size, data_root: str=Config.train_dir):
        self.data_root = data_root
        self.transforms = transforms.Compose([
                transforms.ToTensor(),
                transforms.Resize((224, 224)),
                transforms.RandomHorizontalFlip(),
                transforms.Normalize((.5, .5, .5), (.5, .5, .5)),
            ]
        )
        self.batch_size = batch_size
        return

    def get_dataloader(self): 
        imagefolder = self._get_imagefolder()
        dataloader = DataLoader(imagefolder, batch_size=self.batch_size, shuffle=True)
        return dataloader

    def _get_imagefolder(self):
        return ImageFolder(root=self.data_root, transform=self.transforms)
    