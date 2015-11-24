#!/usr/bin/python

import os
import re
import shutil
from collections import defaultdict

#  <Image source={require('image!my-icon')} />
#  <Image source={require('./img/my-icon.png')} />

def find_asset(folder_path):
  asset_path = folder_path + '/iOS/Images.xcassets/'
  assets = defaultdict(list)
  for root,dirs,files in os.walk(asset_path):
    for file in files:
      if file.split('.')[-1] == 'png':
        file_name = file.split('.')[0].split('@')[0]
        file_path = os.path.join(root, file)
        assets[file_name].append(file_path)

  return assets


def copy_asset(pic_name, target_path):
  pic_paths = assets[pic_name]
  target_path = target_path + '/img/'
  if not os.path.exists(target_path):
    os.makedirs(target_path)
  for path in pic_paths:
    shutil.copy(path, target_path)

  print pic_name + ' has been migrated.'


def replace_src(folder, file_name, assets):
  src_reg = re.compile(r'image!\w+')
  file_path = os.path.join(folder, file_name)
  with open(file_path, 'r+') as f:
    content = f.read()
    matches = src_reg.findall(content)
    for m in matches: 
      src = m.replace('image!', './img/') + '.png'
      content = content.replace("'" + m + "'", "'" + src + "'")

      # create new asset file
      pic = m.split('!')[-1]
      copy_asset(pic, folder)

    f.seek(0)
    f.write(content)
    f.truncate()


def loop_folder(folder_path, assets):
  folder_path = folder_path + '/app/'
  for root,dirs,files in os.walk(folder_path):
    for file in files:
      if file.split('.')[-1] == 'js':
        replace_src(root, file, assets)


if __name__ == "__main__":
  folder_path = os.getcwd()
  assets = find_asset(folder_path)
  loop_folder(folder_path, assets)
