""" meta.json的读取 """

import json


class YoutubeVOSJsonParser(object):

    def __init__(self, file_name=None):
        if not file_name:
            raise RuntimeError('Class youtubeVOSJsonParser def __init__: file_name is None')
        file = open(file_name)
        json_str = file.read()
        self.parser = json.loads(json_str)

    def get_parser(self):
        return self.parser
