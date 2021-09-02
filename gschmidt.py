import torch
import torch.nn.functional as F
import cmath
 
def gram_schmidt(arr) -> torch.tensor:
    """
    Implementation of Gram-Schmidt orthogonalization
    :param arr: a tensor of shape (1,6)
    :return R: a recovered rotation matrix, i.e. (3,3)
    """
    a_1, a_2 = arr[:,:3], arr[:,3:]
    row_1 = F.normalize(a_1, dim=1)
    dot = torch.sum((row_1*a_2),dim=1).unsqueeze(1)
    row_2 = F.normalize(a_2 - dot*row_1, dim=1)
    row_3 = torch.cross(row_1, row_2)

    R = torch.cat((row_1, row_2, row_3), 1)
    R = R.view(-1,3,3).transpose(1,2)
    assert cmath.isclose(torch.linalg.det(R), 1, rel_tol=1e-04), torch.linalg.det(R)

    return R.view(3,3)


if __name__ == "__main__":
    input = torch.rand(1,6)
    print("Sample neural network output: \n", input.view(3,-1))
    recovered = gram_schmidt(input)
    print("\n")
    print("Recovered rotation matrix: \n", recovered)