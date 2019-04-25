"""
测试 class YoutubeVOSJsonParser
了解 youtubeVOS的数据结构
数据结构信息保存在了data_information.txt
了解 youtubeVOS的图像信息
"""
# debug
# from .youtubeVOSJsonParser import YoutubeVOSJsonParser

# runtime
from youtubeVOSJsonParser import YoutubeVOSJsonParser

import os
import skimage.io

# 控制代码块输出
flag1 = False
flag2 = False
flag3 = False
flag4 = True

# 测试train部分的读取
if flag1:
    tmp = YoutubeVOSJsonParser('./YouTubeVOS_2018/train/meta.json')
    train_json = tmp.get_parser()
    ans = 0
    object_num = []
    painting_num = []
    videos = train_json['videos']
    for key1 in videos:
        video = videos[key1]
        tmp1 = 0
        objects = video['objects']
        for key2 in objects:
            tmp1 += 1
            tmp2 = 0
            core = objects[key2]
            for key3 in core['frames']:
                tmp2 += 1
            painting_num.append(tmp2)
        object_num.append(tmp1)
        ans += 1
    out_object_num = {}
    for key in object_num:
        if key in out_object_num:
            out_object_num[key] += 1
        else:
            out_object_num[key] = 1
    out_painting_num = {}
    for key in painting_num:
        if key in out_painting_num:
            out_painting_num[key] += 1
        else:
            out_painting_num[key] = 1
    print('train:')
    print('  videos: ', ans)
    print('  video objects: ')
    for key in out_object_num:
        print('    object_num: ', key, ' count: ', out_object_num[key])
    print('  video paintings:')
    for key in out_painting_num:
        print('    painting_num: ', key, ' count: ', out_painting_num[key])

# 测试test_all_frames的读取
if flag2:
    tmp = YoutubeVOSJsonParser('./YouTubeVOS_2018/test_all_frames/meta.json')
    train_json = tmp.get_parser()
    ans = 0
    object_num = []
    painting_num = []
    videos = train_json['videos']
    for key1 in videos:
        video = videos[key1]
        tmp1 = 0
        objects = video['objects']
        for key2 in objects:
            tmp1 += 1
            tmp2 = 0
            core = objects[key2]
            for key3 in core:
                tmp2 += 1
            painting_num.append(tmp2)
        object_num.append(tmp1)
        ans += 1
    out_object_num = {}
    for key in object_num:
        if key in out_object_num:
            out_object_num[key] += 1
        else:
            out_object_num[key] = 1
    out_painting_num = {}
    for key in painting_num:
        if key in out_painting_num:
            out_painting_num[key] += 1
        else:
            out_painting_num[key] = 1
    print('test_all_frames:')
    print('  videos: ', ans)
    print('  video objects: ')
    for key in out_object_num:
        print('    object_num: ', key, ' count: ', out_object_num[key])
    print('  video paintings:')
    for key in out_painting_num:
        print('    painting_num: ', key, ' count: ', out_painting_num[key])

# 测试get_list方法
if flag3:
    tmp = YoutubeVOSJsonParser('./YouTubeVOS_2018/train/meta.json', mode='train')
    out_list = tmp.get_list()
    for num, out_dict in enumerate(out_list):
        if num == 0:
            for key2 in out_dict:
                print(key2, ': ', out_dict[key2])
    print(len(out_list))

    tmp = YoutubeVOSJsonParser('./YouTubeVOS_2018/test_all_frames/meta.json', mode='test')
    out_list = tmp.get_list()
    for num, out_dict in enumerate(out_list):
        if num == 0:
            for key2 in out_dict:
                print(key2, ': ', out_dict[key2])
    print(len(out_list))

# 查看图像信息
if flag4:
    tmp = YoutubeVOSJsonParser('./YouTubeVOS_2018/train/meta.json', mode='train')
    out_list = tmp.get_list()
    for num, out_dict in enumerate(out_list):
        img_file = os.path.join('./YouTubeVOS_2018/train', 'JPEGImages', out_dict['id'],
                                out_dict['file_list'][0]+'.jpg')
        img = skimage.io.imread(img_file)
        print(num, ': ', img.shape)
    for num, out_dict in enumerate(out_list):
        img_file = os.path.join('./YouTubeVOS_2018/train', 'Annotations', out_dict['id'],
                                out_dict['file_list'][0] + '.png')
        img = skimage.io.imread(img_file)
        print(num, ': ', img.shape)
