import torch
import cmath
 
def svd(arr) -> torch.tensor:
    """
    Implementation of Singular Value Decomposition (SVD) orthogonalization
    :param arr: a tensor of shape (1,9)
    :return R: a recovered rotation matrix, i.e. (3,3)
    """

    U, _, V = torch.linalg.svd(arr.reshape(3,3))
    R = U@V

    if cmath.isclose(torch.linalg.det(R), -1, rel_tol=1e-04):
        middle = torch.eye(3)
        middle[2,2] = -1
        R = U @ middle @ V
    assert cmath.isclose(torch.linalg.det(R), 1, rel_tol=1e-04), torch.linalg.det(R)

    return R.view(3,3)


if __name__ == "__main__":
    input = torch.rand(1,9)
    print("Sample neural network output: \n", input.view(3,-1))
    recovered = svd(input)
    print("\n")
    print("Recovered rotation matrix: \n", recovered)