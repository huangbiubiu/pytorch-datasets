import json


class YoutubeVOSJsonParser(object):
    """ meta.json的相关操作 """

    def __init__(self, file_name=None, mode='train'):

        """
        :param file_name:指出文件路径
        :param mode: {'train', 'val', 'test'}

        """

        if mode not in ['train', 'val', 'test']:
            raise RuntimeError('Class YoutubeVOSJsonParser def __init__: incorrect data_type!')
        self.mode = mode
        if not file_name:
            raise RuntimeError('Class youtubeVOSJsonParser def __init__: file_name is None')
        file = open(file_name)
        json_str = file.read()
        self.parser = json.loads(json_str)

    def get_parser(self):

        """
        :return: 返回json的字典对象
        """

        return self.parser

    def get_list(self):

        """

        :return: 返回一个列表，里面每一个都是一个字典 list<dict>
                字典中   id: 视频id
                        category: object 的类型 （只有'train'模式有）
                        file_list: 列表 保存所有该视频的帧地址
                        objects: 指出该段视频 object 的数量
        """

        train_json = self.parser
        videos = train_json['videos']
        list_all = []
        for key1 in videos:
            dict_tmp = {}
            video = videos[key1]
            objects = video['objects']
            obj_count = 0
            for key2 in objects:
                core = objects[key2]
                if self.mode == 'train' or self.mode == 'val':
                    if 'file_list' not in dict_tmp:
                        dict_tmp['file_list'] = core['frames']
                    else:
                        dict_tmp['file_list'] = self.combine(dict_tmp['file_list'], core['frames'])
                else:
                    if 'file_list' not in dict_tmp:
                        dict_tmp['file_list'] = core
                    else:
                        dict_tmp['file_list'] = self.combine(dict_tmp['file_list'], core)
                obj_count += 1
                if self.mode == 'train':
                    if 'category' not in dict_tmp:
                        dict_tmp['category'] = []
                    dict_tmp['category'].append(core['category'])
            dict_tmp['objects'] = obj_count
            dict_tmp['id'] = key1
            list_all.append(dict_tmp)
        return list_all

    @staticmethod
    def combine(list1, list2):

        """
        :param list1: 接受一个列表
        :param list2: 接受一个列表
        :return: 返回两个列表连接、去重、排序后的结果

        """

        list_tmp = list1 + list2
        list_tmp = list(set(list_tmp))
        list_tmp.sort()
        return list_tmp
