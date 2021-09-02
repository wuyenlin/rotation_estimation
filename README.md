# Rotation estimation

This repository gives a summary of contemporary  approaches to deep rotation estimation, as well as their implementation in Python.
Specifically, rotation matrices have sworn to be the estimation target given the discontinuity presented in simpler presentations including Euler angles, quaternion, and axis-angle.

There are 2 mainstream methods to recover a rotation matrix:

1. Gram-Schmidt orthogonalization
2. Singular Value Decomposition (SVD)


```
1.
@inproceedings{Zhou_2019_CVPR,
title={On the Continuity of Rotation Representations in Neural Networks},
author={Zhou, Yi and Barnes, Connelly and Jingwan, Lu and Jimei, Yang and Hao, Li},
booktitle={The IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
month={June},
year={2019}
}

2.
```
