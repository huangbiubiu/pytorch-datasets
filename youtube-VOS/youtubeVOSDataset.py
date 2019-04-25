from torch.utils.data.dataset import Dataset
# debug
# from .youtubeVOSJsonParser import YoutubeVOSJsonParser

# runtime
from youtubeVOSJsonParser import YoutubeVOSJsonParser

import torch
import os
import skimage.io
import numpy as np


class YoutubeVOSDataset(Dataset):

    """ 这个类用于数据读入的初始化 """

    def __getitem__(self, item):

        """
        :param item: 混淆前的第item个
        :return: datax 原始连续帧
                 datay annotations 后的连续帧
                 data_dict 部分连续帧的信息 id 视频号
                                          file_list 连续帧号
                                          objects 对象个数
                                          category 对象种类
        """

        item_shuffle = item
        if self.shuffle:
            item_shuffle = self.shuffle(item)
        data_dict = self.data_list[item_shuffle]
        data_path = self.middle_path
        datax_path = os.path.join(data_path, 'JPEGImages', data_dict['id'])
        datax = np.zeros((self.num_per, ))
        for i, key in enumerate(data_dict['file_list']):
            img = skimage.io.imread(os.path.join(datax_path, key+'.jpg'))
            if self.crop:
                img = self.crop(img)
            if i == 0:
                datax = np.zeros(np.append(self.num_per, img.shape))
            datax[i] = img
        if self.transform:
            datax = self.transform(datax)
        datax = torch.from_numpy(datax)
        if self.mode == 'train':
            datay_path = os.path.join(data_path, 'Annotations', data_dict['id'])
            for i, key in enumerate(data_dict['file_list']):
                img = skimage.io.imread(os.path.join(datay_path, key+'.png'))
                if len(img.shape) == 3:
                    img = img[:, :, 0:3]
                else:
                    img_tmp = np.zeros(np.append(img.shape, 3))
                    img_tmp[:, :, 0] = img
                    img_tmp[:, :, 1] = img
                    img_tmp[:, :, 2] = img
                    img = img_tmp
                if self.crop:
                    img = self.crop(img)
                if i == 0:
                    datay = np.zeros(np.append(self.num_per, img.shape))
                datay[i] = img
            datay = torch.from_numpy(datay)
            return datax, datay, data_dict
        else:
            return datax, data_dict

    def __len__(self):

        """
        :return: 返回数据条数

        """

        return len(self.data_list)

    def __init__(self, is_all_frames=False, mode='train', shuffle=None, root_dir=None, transform=None,
                 num_per=10, is_loss=True, crop=None):

        """

        :param is_all_frames: {True, False} 确认数据是否需要更高的精度
        :param mode: {'train', 'val', 'test'} 选择数据集类型
                        warning: is_all_frames 为 False 时没有 'test' 模式
                                 is_all_frames 为 True 时没有 'valid' 模式
                        warning: 只有'train' 模式下有 annotations
        :param shuffle: 给出了一个打乱数据的接口，只需提供一个x->f(x)的映射即可
        :param root_dir: 指出数据文件所在的根目录
                         e.g. ~/Documents/Github/pytorch-datasets/youtube-VOS/
        :param transform: 给出了一个diy数据格式的接口，比如flatten(x)
        :param num_per: 指出每条数据的连续帧数
                        e.g. all_frames模式下(is_all_frames=True) [00001,00002,00003] num_per=3
                             简化模式下(is_all_frames=False) [00000,00005,00010] num_per=3
                        warning: 可能会造成部分数据重复或者部分数据丢失
        :param is_loss: {True, False} True 代表生成相同帧数的数据时采取丢弃剩余帧数的策略
                                      False 代表生成相同帧数的数据时采用重复数据的策略
        :param crop: 裁剪函数，使用dataloader之前需要裁齐所有图片
                     输入一张图片 (x, y, 3)
                     输出一张图片 (x', y', z')

        """

        if is_all_frames not in [True, False]:
            raise RuntimeError('Class YoutubeVOSDataset def __init__: incorrect param is_all_frames!')
        self.is_all_frames = is_all_frames
        if mode not in ['train', 'val', 'test']:
            raise RuntimeError('Class YoutubeVOSDataset def __init__: incorrect param mode!')
        self.mode = mode
        if (not is_all_frames and mode == 'train') or (is_all_frames and mode == 'val'):
            raise RuntimeError('Class YoutubeVOSDataset def __init__: dataset don\'t have this mode!')
        self.shuffle = shuffle
        if not root_dir:
            root_dir = os.getcwd()
        self.root_dir = root_dir
        self.transform = transform
        if type(num_per) != int or num_per <= 0:
            raise RuntimeError('Class YoutubeVOSDataset def __init__: incorrect param num_per!')
        self.num_per = num_per
        if is_loss not in [True, False]:
            raise RuntimeError('Class YoutubeVOSDataset def __init__: incorrect param is_loss!')
        if not crop:
            print('Class YoutubeVOSDataset def __init__: no function crop!')
        self.crop = crop

        middle_path = os.path.join(root_dir, 'YouTubeVOS_2018')
        if is_all_frames:
            if mode == 'train':
                middle_path = os.path.join(middle_path, 'train_all_frames')
            elif mode == 'val':
                middle_path = os.path.join(middle_path, 'valid_all_frames')
            else:
                middle_path = os.path.join(middle_path, 'test_all_frames')
        elif mode == 'train':
            middle_path = os.path.join(middle_path, 'train')
        else:
            middle_path = os.path.join(middle_path, 'valid')
        self.middle_path = middle_path
        meta_file = os.path.join(self.middle_path, 'meta.json')
        parser = YoutubeVOSJsonParser(meta_file, mode)
        meta_list = parser.get_list()

        data_list = []
        for key_dict in meta_list:
            if len(key_dict['file_list']) < num_per:
                continue
            for i in range(len(key_dict['file_list']) // num_per):
                dict_tmp = dict()
                dict_tmp['id'] = key_dict['id']
                if mode == 'train':
                    dict_tmp['category'] = key_dict['category']
                dict_tmp['objects'] = key_dict['objects']
                dict_tmp['file_list'] = key_dict['file_list'][i*num_per:(i+1)*num_per]
                data_list.append(dict_tmp)
            if (not is_loss) and (len(key_dict['file_list']) % num_per != 0):
                dict_tmp = dict()
                dict_tmp['id'] = key_dict['id']
                if mode == 'train':
                    dict_tmp['category'] = key_dict['category']
                dict_tmp['objects'] = key_dict['objects']
                file_list = key_dict['file_list']
                dict_tmp['file_list'] = file_list[len(key_dict['file_list'])-num_per:len(key_dict['file_list'])]
                data_list.append(dict_tmp)
        self.data_list = data_list
