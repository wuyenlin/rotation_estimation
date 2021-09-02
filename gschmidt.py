import torch
import torch.nn.functional as F
 
def normalize(x: torch.tensor) -> torch.tensor:
    return x/torch.linalg.norm(x)


def gram_schmidt(arr) -> torch.tensor:
    """
    Detail implementation of Gram-Schmidt orthogonalization
    :param arr: a tensor of shape (16,6)
    :return Rs: a stack of flattened rotation matrix, i.e. (16,9)
    """
    a_1, a_2 = arr[:,:3], arr[:,3:]
    row_1 = F.normalize(a_1, dim=1)
    dot = torch.sum((row_1*a_2),dim=1).unsqueeze(1)
    row_2 = F.normalize(a_2 - dot*row_1, dim=1)
    row_3 = torch.cross(row_1, row_2)
    R = torch.cat((row_1, row_2, row_3), 1) # stack + transpose
    R = R.view(-1,3,3).transpose(1,2)
    return R.reshape(-1,9)

if __name__ == "__main__":
    pass