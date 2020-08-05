import os
import urllib.request
import zipfile

if not os.path.exists('data'):
  os.mkdir('data')
if not os.path.exists('data/coco/'):
  os.mkdir('data/coco/')
if not os.path.exists('data/coco/images'):
  os.mkdir('data/coco/images')

if not os.path.exists('data/coco/images'):
  print('Downloading images...')

  url_val = 'http://images.cocodataset.org/zips/val2017.zip'  
  urllib.request.urlretrieve(url_val, 'data/coco/images/val2017.zip')
  
  url_train = 'http://images.cocodataset.org/zips/train2017.zip'
  urllib.request.urlretrieve(url_train, 'data/coco/images/train2017.zip')
  
  with zipfile.ZipFile('data/coco/images/val2017.zip', 'r') as zip_ref:
    zip_ref.extractall('data/coco/images/.')

  with zipfile.ZipFile('data/coco/images/train2017.zip', 'r') as zip_ref:
    zip_ref.extractall('data/coco/images/.')
    
  print('Done!')

if not os.path.exists('data/coco/annotations'):
  print('Downloading annotations...')
  
  url_anot1 = 'http://images.cocodataset.org/annotations/panoptic_annotations_trainval2017.zip'  
  urllib.request.urlretrieve(url_anot1, 'data/coco/panoptic_annotations_trainval2017.zip')
  
  url_anot2 = 'http://images.cocodataset.org/annotations/annotations_trainval2017.zip'
  urllib.request.urlretrieve(url_anot2, 'data/coco/annotations_trainval2017.zip')
    
  with zipfile.ZipFile('data/coco/panoptic_annotations_trainval2017.zip', 'r') as zip_ref:
       zip_ref.extractall('data/coco/.')
       
  with zipfile.ZipFile('data/coco/annotations_trainval2017.zip', 'r') as zip_ref:
       zip_ref.extractall('data/coco/.')    
  
  with zipfile.ZipFile('data/coco/annotations/panoptic_train2017.zip', 'r') as zip_ref:
       zip_ref.extractall('data/coco/annotations/.')
  
  with zipfile.ZipFile('data/coco/annotations/panoptic_val2017.zip', 'r') as zip_ref:
       zip_ref.extractall('data/coco/annotations/.')
  
  print('Done!')

if not os.path.exists('model/upsnet_resnet_50_coco_90000.pth'):
  print('Downloading models...')
  
  url_model = 'https://www.dropbox.com/s/nbt215ecosqdh5i/upsnet_resnet_50_coco_70000.pth?dl=1'  
  urllib.request.urlretrieve(url_model, 'model/upsnet_resnet_50_coco_70000.pth')
  
  print('Done!')
