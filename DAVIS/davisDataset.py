from torch.utils.data.dataset import Dataset
import torch
import numpy as np
import os
import skimage.io


class DavisDataset(Dataset):

    def __getitem__(self, item):
        path_x = self.path + self.data_file_list[item, 0]
        path_y = self.path + self.data_file_list[item, 1]
        image_x = skimage.io.imread(path_x)
        image_y = skimage.io.imread(path_y)
        if self.transform:
            image_x = self.transform(image_x)
            image_y = self.transform(image_y)
        # print(image_x.shape, image_y.shape)
        image_x = torch.from_numpy(image_x)
        image_y = torch.from_numpy(image_y)
        return image_x, image_y

    def __len__(self):
        return self.data_file_list.shape[0]

    def __init__(self, txt_file_path='/ImageSets', dataset_dir='/davis-master/data/DAVIS', root_dir=None,
                 image_definition='480p', data_type='train', transform=None):

        # 判断data_type
        if data_type == 'train':
            file_name = 'train.txt'
        elif data_type == 'val':
            file_name = 'trainval.txt'
        elif data_type == 'test':
            file_name = 'val.txt'
        else:
            raise RuntimeError('Class DavisDataset def __init__: incorrect data_type!')
        self.data_type = data_type

        # 判断image_definition
        if image_definition == '480p':
            middle_path = '480p'
        elif image_definition == '1080p':
            middle_path = '1080p'
        else:
            raise RuntimeError('Class DavisDataset def __init__: incorrect image_definition!')
        self.image_definition = image_definition

        self.transform = transform

        # 获得调用该类的文件位置
        if not root_dir:
            root_dir = os.getcwd()
        self.root_dir = root_dir

        self.dataset_dir = dataset_dir
        self.txt_file_path = txt_file_path

        # 读入数据结构文件
        try:
            path = root_dir + dataset_dir + txt_file_path
            path = os.path.join(path, middle_path, file_name)
            self.data_file_list = np.loadtxt(path, delimiter=' ', dtype=np.str)
        except Exception as e:
            print(e)
            raise RuntimeError('Class DavisDataset def __init__: have an issue on dataset structure files!')

        self.path = root_dir + dataset_dir
