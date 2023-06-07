# Deep Convolutional Networks for Single Image Super-Resolution

This project focuses on using deep convolutional neural networks for single image super-resolution. It implements three super-resolution network models: EDSR, VDSR, and SRResNet.

## Introduction

Single image super-resolution (SISR) aims to generate a high-resolution image from a low-resolution input image. Deep convolutional neural networks have shown remarkable performance in achieving state-of-the-art results in SISR tasks. This project explores three popular network architectures for SISR: EDSR, VDSR, and SRResNet.

## Dependencies
- python >=3.6
- pytorch
- numpy
- skimage
- imageio
- matplotlib
- tqdm
- PIL

## Usage

### VDSR

To run VDSR on your own images. You should put the ground truth images in the floader:

`/super resolution/pytorch-vdsr/image/GT`

put the LR images(after bicubic  interpolation) in the floader:

`/super resolution/pytorch-vdsr/image/x4`

then :

```
cd ./super resolution/pytorch-vdsr
python test.py --cuda
```
You can get the result in `/super resolution/pytorch-vdsr/result`
### SRResNet

To run SRResNet on your own images. You should use `Matlab`  to convert  images to mat format. And then, put them in the dtestsets floader. 
```
cd ./super resolution/pytorch-SRResNet
python test.py --cuda --dataset  Set5 --scale 4
```
### EDSR

To run EDSRon your own images. You should put images in the test floader. And then run:

```
cd ./super resolution/EDSR-PyTorch/src/
python main.py --data_test Demo --scale 4 --pre_train download --test_only --save_results
```
You can find the result in :
 `super resolution\EDSRPyTorch\experiment\test\results-Demo`

## Eval

First, put the ground true image in  `\super resolution\image_process\GT`.Then put the SR images in `\super resolution\image_process\SR`.

```
cd \super resolution\image_process
python eval.py
```

You can get the PSNR and SSIM of the SR images.

