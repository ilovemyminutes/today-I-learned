from dataclasses import dataclass

@dataclass
class Config:
    batch_size: int=128
    train_dir: str='../../datasets/imagenet-mini/train'
    valid_dir: str='../../datasets/imagenet-mini/val'