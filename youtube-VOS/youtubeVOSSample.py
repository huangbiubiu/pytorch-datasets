"""

用于测试youtubeVOSDataset
当然你也可以自己实现

"""

# debug
# from .youtubeVOSDataset import YoutubeVOSDataset

# runtime
from youtubeVOSDataset import YoutubeVOSDataset

from torch.utils.data.dataloader import DataLoader
import matplotlib.pyplot as plt

# 代码块测试
flag1 = True

if flag1:
    trainDataset = YoutubeVOSDataset()
    dataLoader = DataLoader(dataset=trainDataset, batch_size=5)
    for i, data in enumerate(dataLoader):
        if i <= 10:
            datax, datay, metadata = data
            # print(datax.shape)
            # print(datay.shape)
        if i > 10:
            break
