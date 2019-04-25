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
flag1 = False
flag2 = False
flag3 = False
flag4 = False

if flag1:
    trainDataset = YoutubeVOSDataset()
    for i, data in enumerate(trainDataset):
        if i <= 11:
            datax, datay, metadata = data
            # print(datax.shape)
            # print(datay.shape)
            X, y = datax[0], datay[0]
            print(X.size(), y.size())
            X = X / 255
            y = y / 255
            fig = plt.figure()
            ax = plt.subplot(1, 2, 1)
            plt.tight_layout()
            ax.set_title('X 1')
            ax.axis('off')
            plt.imshow(X)
            ax = plt.subplot(1, 2, 2)
            plt.tight_layout()
            ax.set_title('y 2')
            ax.axis('off')
            plt.imshow(y)
            plt.show()
        if i > 10:
            break

if flag2:
    trainDataset = YoutubeVOSDataset(is_all_frames=True, mode='test')
    for i, data in enumerate(trainDataset):
        if i <= 11:
            datax, metadata = data
            # print(datax.shape)
            # print(datay.shape)
            X = datax[0]
            print(X.size())
            X = X / 255
            fig = plt.figure()
            ax = plt.subplot(1, 1, 1)
            plt.tight_layout()
            ax.set_title('X 1')
            ax.axis('off')
            plt.imshow(X)
            plt.show()
        if i > 10:
            break

if flag3:
    trainDataset = YoutubeVOSDataset(mode='val', num_per=20, is_loss=False)
    for i, data in enumerate(trainDataset):
        if i <= 11:
            datax, metadata = data
            # print(datax.shape)
            # print(datay.shape)
            X = datax[0]
            print(X.size())
            X = X / 255
            fig = plt.figure()
            ax = plt.subplot(1, 1, 1)
            plt.tight_layout()
            ax.set_title('X 1')
            ax.axis('off')
            plt.imshow(X)
            plt.show()
        if i > 10:
            break

if flag4:
    trainDataset = YoutubeVOSDataset(is_all_frames=True, mode='val', num_per=20, is_loss=False)
