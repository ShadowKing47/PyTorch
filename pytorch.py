import torch
"""print(torch.__version__)
print("Entry to torch")


print(torch.cuda.is_available())  # For ROCm, this also applies to AMD GPUs
print(torch.device("cuda" if torch.cuda.is_available() else "cpu"))

s = torch.tensor(7)

print(s.ndim, s.item(), s)
print(" ")

v = torch.tensor([7, 7])
print(v,v.ndim,v.shape)


print(" ")
M = torch.tensor([[7,8],[3,4]])
print(M.ndim,M.shape)

T = torch.tensor([[[1, 2, 3], [23, 45, 89], [12, 54, 65]]])
print(T.ndim,T.shape)"""

rt=torch.rand(size=(3, 4))
print(rt)
print(rt.dtype)

z = torch.zeros(size=(3, 4))
print(z)
print(z.dtype)

o = torch.ones(size=(5, 4))
print(o)
print(o.dtype)