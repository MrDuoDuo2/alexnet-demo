import torch
import os
import pandas as pd

def write():
    os.makedirs(os.path.join('.', 'data'), exist_ok=True)
    data_file = os.path.join('.', 'data', 'house_tiny.csv')
    with open(data_file, 'w') as f:
        f.write('NumRooms,Alley,Price\n')  # 列名
        f.write('NA,Pave,127500\n')  # 每行表示一个数据样本
        f.write('2,NA,106000\n')
        f.write('4,NA,178100\n')
        f.write('NA,NA,140000\n')

if __name__ == "__main__":
    # write()
    print("hello world")
    data_file = os.path.join('.', 'data', 'house_tiny.csv')
    data = pd.read_csv(data_file)
    print(data)

    inputs, outputs = data.iloc[:, 0:2], data.iloc[:, 2]
    inputs = inputs.fillna(inputs.mean(numeric_only=True)) #mean 默认数字转换为false
    print(inputs)

    inputs = pd.get_dummies(inputs, dummy_na=True)
    print(inputs)

    X = torch.tensor(inputs.to_numpy(dtype=float))
    Y = torch.tensor(outputs.to_numpy(dtype=float))
    result = X,Y
    print(result)

    nan_count = data.isnull().sum(axis=0) # isna也可以 axis：0 为列 1 为行
    print(data)
    print(nan_count)
    data.drop(nan_count[nan_count == max(nan_count)].index, axis=1, inplace=True)
    print(data)
