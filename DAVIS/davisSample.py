# debug
# from DAVIS.davisDataset import DavisDataset

# runtime
from davisDataset import DavisDataset

from torch.utils.data.dataloader import DataLoader
import matplotlib.pyplot as plt

testDataset = DavisDataset(data_type='test', image_definition='480p')
trainDataset = DavisDataset(data_type='train', image_definition='480p')
valDataset = DavisDataset(data_type='val', image_definition='480p')

dataLoader1 = DataLoader(dataset=testDataset, batch_size=5, shuffle=True)
dataLoader2 = DataLoader(dataset=trainDataset, batch_size=5, shuffle=True)
dataLoader3 = DataLoader(dataset=valDataset, batch_size=5, shuffle=True)

for i, data in enumerate(dataLoader1):
    if i <= 3:
        X, y = data
        print(X.size(), y.size())
        fig = plt.figure(i)
        ax = plt.subplot(1, 2, 1)
        plt.tight_layout()
        ax.set_title('X 1')
        ax.axis('off')
        plt.imshow(X[0])
        ax = plt.subplot(1, 2, 2)
        plt.tight_layout()
        ax.set_title('y 2')
        ax.axis('off')
        plt.imshow(y[0])
        plt.show()
    else:
        break

for i, data in enumerate(dataLoader2):
    if i <= 3:
        X, y = data
        print(X.size(), y.size())
        fig = plt.figure()
        ax = plt.subplot(1, 2, 1)
        plt.tight_layout()
        ax.set_title('X 1')
        ax.axis('off')
        plt.imshow(X[0])
        ax = plt.subplot(1, 2, 2)
        plt.tight_layout()
        ax.set_title('y 2')
        ax.axis('off')
        plt.imshow(y[0])
        plt.show()
    else:
        break

for i, data in enumerate(dataLoader3):
    if i <= 3:
        X, y = data
        print(X.size(), y.size())
        fig = plt.figure(i)
        ax = plt.subplot(1, 2, 1)
        plt.tight_layout()
        ax.set_title('X 1')
        ax.axis('off')
        plt.imshow(X[0])
        ax = plt.subplot(1, 2, 2)
        plt.tight_layout()
        ax.set_title('y 2')
        ax.axis('off')
        plt.imshow(y[0])
        plt.show()
    else:
        break
