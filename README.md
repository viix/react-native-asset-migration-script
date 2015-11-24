# react-native-asset-migration-script
React Native 0.14 use new asset management system, with static image resource.
see http://facebook.github.io/react-native/docs/images.html

## Intro
this script is used to migrate image assets from handled by iOS bundle, to handled by packager -- especially for upgrade from 0.13 to 0.14. it will add each asset to the corresponding component, sibling folder `./img`, and change `<Image source={require('image!my-icon')} />` to `<Image source={require('./img/my-icon.png')} />`.


## Usage
put script into the root folder of project, and `python script.py`

## Tips
this is just experimental, welcome to make pr.
