import torch

if __name__ == "__main__":
    x = torch.tensor(3.0)
    y = torch.tensor(2.0)

    result = x + y, x * y, x / y, x ** y
    print(result)

    z = torch.arange(4)
    print(z)

    len(z)

    A = torch.arange(20).reshape(5, 4)
    print(A)
    print(A[0,2])

    print(A.T)

    B = torch.tensor([[1, 2, 3], [2, 0, 4], [3, 4, 5]])
    print(B)

    print(B == B.T)

    X = torch.arange(24).reshape(2,3,4)
    print(X)