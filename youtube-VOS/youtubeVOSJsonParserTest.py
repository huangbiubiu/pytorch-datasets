"""
测试 class YoutubeVOSJsonParser
了解 youtubeVOS的数据结构
"""
# debug
# from .youtubeVOSJsonParser import YoutubeVOSJsonParser

# runtime
from youtubeVOSJsonParser import YoutubeVOSJsonParser

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
