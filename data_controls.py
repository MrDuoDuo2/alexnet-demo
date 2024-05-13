import torch;

if __name__ == "__main__":
    x = torch.arange(12)
    print(x)
    print(x.shape)
    print(x.numel())

    x = x.reshape(3, 4)  # 3行4列
    print(x)

    x = x.reshape(-1, 4)  # 知道列个数自动计算行
    print(x)

    x = x.reshape(3, -1)  # 知道行个数自动计算列
    print(x)

    zeros = torch.zeros((2, 3, 4))  # torch.zeros((形状:z,y,x))
    print(zeros)

    ones = torch.ones((2, 3, 4))  # torch.ones((形状:z,y,x))
    print(ones)

    randoms = torch.randn((2, 3, 4))
    print(randoms)

    tensor = torch.tensor([[2, 1, 4, 3], [1, 2, 3, 4], [4, 3, 2, 1]])
    print(tensor)

    x = torch.tensor([1.0, 2, 4, 8])
    y = torch.tensor([2, 2, 2, 2])
    result = x + y, x - y, x * y, x / y, x ** y  # **运算符是求幂运算
    print(result)

    e = torch.exp(x)  # e为底的指数函数
    print(e)

    # ？
    X = torch.arange(12, dtype=torch.float32).reshape((3, 4))
    # print(X)
    Y = torch.tensor([[2.0, 1, 4, 3], [1, 2, 3, 4], [4, 3, 2, 1]])
    result = torch.cat((X, Y), dim=0), torch.cat((X, Y), dim=1)  # cat :concatenate 连结
    print(result)
    # print(Y)

    print(X == Y)
    print("X < Y:", X < Y)
    print("X > Y:", X > Y)

    print(X.sum())

    # 广播机制
    a = torch.arange(3).reshape((3, 1))
    b = torch.arange(2).reshape((1, 2))
    result = a, b
    print(result)

    print(a + b)

    tmp1 = torch.tensor([[1], [3], [5]])
    tmp2 = torch.tensor([2, 4])
    print(tmp1 + tmp2)

    print(X[-1], X[1:3])
    X[1, 2] = 9
    print(X)

    X[0:2, :] = 12
    print(X)

    Z = torch.zeros_like(Y)
    print('id(Z):', id(Z))
    Z[:] = X + Y
    print('id(Z):', id(Z))

    # before = id(X)
    # X += Y
    # print(id(X) == before)
    #
    # X = X + Y
    # print(id(X) == before)

    A = X.numpy()
    B = torch.tensor(A)
    result = type(A), type(B)
    print(result)

    # a = torch.tensor([3.5,12.])  a Tensor with 2 elements cannot be converted to Scalar
    a = torch.tensor([3.5])
    b = torch.tensor([3.5])
    result = a, a.item(), float(a), int(a)
    print(result)
    print(a == b)