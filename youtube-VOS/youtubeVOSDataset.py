from torch.utils.data.dataset import Dataset
import torch
import numpy as np
import os
import skimage.io


class YoutubeVOSDataset(Dataset):

    """ 这个类用于数据读入的初始化 """

    def __getitem__(self, item):
        pass

    def __len__(self):
        pass

    def __init__(self, is_all_frames=False, data_type='train', shuffle=None, root_dir=None, transform=None, num_per=10):
        """

        :param is_all_frames: {True, False} 确认数据是否需要更高的精度
        :param data_type: {'train', 'valid', 'test'} 选择数据集类型
                        warning: is_all_frames 为 False 时没有 'test' 模式
                        warning: 只有 'train' 模式下有 annotations
        :param shuffle: 给出了一个打乱数据的借口，只需提供一个x->f(x)的映射即可
        :param root_dir: 指出数据文件所在的根目录
        :param transform: 给出了一个diy数据格式的接口，比如flatten(x)
        :param num_per: 指出每条数据的帧数
                        warning: 可能会造成部分数据重复或者部分数据丢失

        """
        pass
