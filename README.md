# 面向边缘智能光学感知的航空紧固件旋转检测
符长虹, 陈锟辉, 鲁昆瀚, 郑光泽, 赵吉林. 面向边缘智能光学感知的航空紧固件旋转检测[J]. 应用光学. 2022, 43(3):1-9.

## Install OLAFDet

```
git clone https://github.com/vision4robotics/OLAFDet.git
cd OLAFDet
pip install -r requirements.txt
cd utils/nms_rotated
python setup.py develop  #or "pip install -v -e ."

cd ../..
cd DOTA_devkit
sudo apt-get install swig
swig -c++ -python polyiou.i
python setup.py build_ext --inplace
```
## Preprocessing
Download weight: [weights.zip 提取码：aufh](https://pan.baidu.com/s/1T_lXq3t3v0jGBmaiabNjvw)

Download dataset: [fastener.zip 提取码：vu8k](https://pan.baidu.com/s/1XdAgfWd06VFXbeYn8ADu4w)

Make sure the labels format is [poly classname diffcult], e.g., 
```
  x1      y1       x2        y2       x3       y3       x4       y4       classname     diffcult

1686.0   1517.0   1695.0   1511.0   1711.0   1535.0   1700.0   1541.0   large-vehicle      1
```
**(*Note: You can set **diffcult=0**)**

If you need to split the dataset. 
```shell
python DOTA_devkit/ImgSplit_multi_process.py
```


## train


```
python train.py --weights weights/yolov5s.pt --cfg models/olafdet_dota_v1.yaml  --data data/olafdet_dota_v1.yaml --device 0

python train.py --weights weights/dota_v1.pt --cfg models/olafdet.yaml  --data data/olafdet_fastener.yaml --device 0
```

## detect

```
python detect.py --weights weights/dota_v1.pt --source dataset/dota

python detect.py --weights weights/fastener.pt --source dataset/fastener
```
## Acknowledgments

We sincerely thank the contribution of following repos: [yolov5_obb](https://github.com/hukaixuan19970627/yolov5_obb), [yolov5](https://github.com/ultralytics/yolov5) and [CSL_RetinaNet_Tensorflow](https://github.com/Thinklab-SJTU/CSL_RetinaNet_Tensorflow)
## Contact

If you have any questions, please contact Kunhui Chen at chenkunhui@tongji.edu.cn 