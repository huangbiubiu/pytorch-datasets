from torch.utils.data.dataset import Dataset
import torch
import numpy as np
import os
import skimage.io


class DavisDataset(Dataset):

    """ 这个类用于数据集读入的初始化。"""

    def __getitem__(self, item):
        """
        :param item: 要求获取第item个训练数据
        :return: 返回单个训练数据和该数据的标签

        """
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
        """
        :return:该函数返回数据集长度，长度由数据集结构文件直接确定

        """
        return self.data_file_list.shape[0]

    def __init__(self, txt_file_path='/ImageSets', dataset_dir='/davis-master/data/DAVIS', root_dir=None,
                 image_definition='480p', data_type='train', transform=None):

        """

        :param txt_file_path: 指出存放数据文件位置的文件的文件夹
        :param dataset_dir: 指出存放数据的文件夹
        :param root_dir: 如果不特别指定，该类将会自动填充项目文件所在位置的绝对路径，如果在其他项目调用该类，
                        请务必手动填充davisDataset.py文件所在位置，或者将项目文件和该类置于同一目录。
        :param image_definition: 你的选择范围为{‘480p’, ’1080p’}，分别代表不同像素的图片（输入数据）。
        :param data_type: 你的选择范围为{‘train’, ‘val’, ‘test’}，分别代表不同类型的数据集
        :param transform: transform可以为自定义函数，用于diy数据格式，比如flatten(x)。

        下面是必需的文件结构，当然你可以参考该工程
        "root_dir"
        |-------...
        |-------README.md
        |-------davisDataset.py
        |-------davisSample.py
        |       |--------------"dataset_dir"
        |       |              |----------get_davis.sh
        |       |              |----------"txt_file_path"
        |       |              |          |------------480p
        |       |              |          |------------1080p
        |       |              |----------...


        """

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
