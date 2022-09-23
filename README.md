# MuViHand
 # **MuViHand** (**Mu**lti-view **Vi**deo based **Hand** Pose) Dataset
<p align="center">
  <img src="3D.gif" alt="animated" />
</p>
<br /> 

MuViHand is a synthetic hand pose dataset that is created with the help of [Mixamo](https://www.mixamo.com/#/), a free web-based service for 3D animations and characters, several images as backgrounds from [Pxfuel](https://www.pxfuel.com/) website, and [Blender](https://www.blender.org/) as a 3D computer graphics software for creating the data. The data have been captured from 10 distinct subjects with 12 cameras, where 6 cameras capture the whole body and the other 6 cameras track a specific hand. The dataset provides the 2D and 3D locations for 21 hand keypoints.
Please see this [paper](https://arxiv.org/abs/2109.11747) for more details.
<br /> 

# Download required files
- Download MuViHand datset [here](https://doi.org/10.5683/SP3/ZHCCZB);
- Unzip dataverse_files.zip to /path/to/MuViHand;
- Your dataset structure should be like:
```
MuViHand/
    F1_Subject.01.rar/ # Fixed cameras data for subject 1 
    F2_Subject.01.rar/ # Fixed cameras data for subject 1 
    T_Subject.01.rar/ # Tracking cameras data for subject 1 
    ...
     
    F1_Subject.10.rar/ # Fixed cameras data for subject 10 
    F2_Subject.10.rar/ # Fixed cameras data for subject 10
    T_Subject.10.rar/ # Tracking cameras data for subject 10 
```

- A scripts that shows the basic use of the data for python could be found [here](https://github.com/LeylaKhaleghi/MuViHand/blob/main/MuViHand.py);
- Keypoints available:
0: wrist, 1-4: thumb [palm to tip], 5-8: index, 9-12: middle, 13-16: ring,  17-20: pinkie;


# Useful tools
In this [video](https://www.youtube.com/watch?v=jEJHIXdPjfU) you can learn how to release your dataset in [Dataverse](https://dataverse.scholarsportal.info/).

# Citation 
Please cite our paper if this dataset helps your research.
```
@article{khaleghi2022multi,
  title={Multi-view video-based 3D hand pose estimation},
  author={Khaleghi, Leyla and Sepas-Moghaddam, Alireza and Marshall, Joshua and Etemad, Ali},
  journal={IEEE Transactions on Artificial Intelligence},
  year={2022},
  publisher={IEEE}
}

```

