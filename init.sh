# Download pretrained models
mkdir -p model
mkdir -p model/pretrained_model
if [ ! -f model/pretrained_model/resnet-101-caffe.pth ]; then
    curl http://www.yuwenxiong.com/pretrained_model/resnet-101-caffe.pth -o model/pretrained_model/resnet-101-caffe.pth
fi
if [ ! -f model/pretrained_model/resnet-50-caffe.pth ]; then
    curl http://www.yuwenxiong.com/pretrained_model/resnet-50-caffe.pth -o model/pretrained_model/resnet-50-caffe.pth
fi

# Install essential python packages

pip install pyyaml pycocotools
pip install opencv-python

# Download panopticapi devkit
# git clone https://github.com/cocodataset/panopticapi lib/dataset_devkit/panopticapi

# Build essential operators

# build cython modules
cd net/bbox || exit; python setup.py build_ext --inplace
cd ../rpn || exit; python setup.py build_ext --inplace
cd ../nms || exit; python setup.py build_ext --inplace
# build operators
cd ../operators || exit
python build_deform_conv.py build_ext --inplace 
python build_roialign.py build_ext --inplace






