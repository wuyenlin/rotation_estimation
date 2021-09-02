# Rotation estimation

This repository gives a summary of contemporary  approaches to deep rotation estimation, as well as their implementations in Python.
Specifically, 3D rotation matrices have sworn to be the estimation target given the discontinuity [1] presented in simpler presentations including Euler angles, quaternion, and axis-angle.

There are 2 mainstream methods to recover a rotation matrix:

1. Gram-Schmidt orthogonalization [1] ([paper])(https://openaccess.thecvf.com/content_CVPR_2019/papers/Zhou_On_the_Continuity_of_Rotation_Representations_in_Neural_Networks_CVPR_2019_paper.pdf)
2. Singular Value Decomposition (SVD) [2] ([paper])(https://openaccess.thecvf.com/content/WACV2021/papers/Chu_A_Vector-Based_Representation_to_Enhance_Head_Pose_Estimation_WACV_2021_paper.pdf)


```
[1]
@inproceedings{Zhou_2019_CVPR,
title={On the Continuity of Rotation Representations in Neural Networks},
author={Zhou, Yi and Barnes, Connelly and Jingwan, Lu and Jimei, Yang and Hao, Li},
booktitle={The IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
month={June},
year={2019}
}

[2]
@inproceedings{NEURIPS2020_fec3392b,
 author = {Levinson, Jake and Esteves, Carlos and Chen, Kefan and Snavely, Noah and Kanazawa, Angjoo and Rostamizadeh, Afshin and Makadia, Ameesh},
 booktitle = {Advances in Neural Information Processing Systems},
 editor = {H. Larochelle and M. Ranzato and R. Hadsell and M. F. Balcan and H. Lin},
 pages = {22554--22565},
 publisher = {Curran Associates, Inc.},
 title = {An Analysis of SVD for Deep Rotation Estimation},
 url = {https://proceedings.neurips.cc/paper/2020/file/fec3392b0dc073244d38eba1feb8e6b7-Paper.pdf},
 volume = {33},
 year = {2020}
}
```
