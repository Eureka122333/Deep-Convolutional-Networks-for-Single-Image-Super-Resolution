import os
import cv2
import numpy as np

 
def ssim(img1, img2):
    C1 = (0.01 * 255)**2
    C2 = (0.03 * 255)**2
 
    img1 = img1.astype(np.float64)
    img2 = img2.astype(np.float64)
    kernel = cv2.getGaussianKernel(11, 1.5)
    window = np.outer(kernel, kernel.transpose())
 
    mu1 = cv2.filter2D(img1, -1, window)[5:-5, 5:-5]  # valid
    mu2 = cv2.filter2D(img2, -1, window)[5:-5, 5:-5]
    mu1_sq = mu1**2
    mu2_sq = mu2**2
    mu1_mu2 = mu1 * mu2
    sigma1_sq = cv2.filter2D(img1**2, -1, window)[5:-5, 5:-5] - mu1_sq
    sigma2_sq = cv2.filter2D(img2**2, -1, window)[5:-5, 5:-5] - mu2_sq
    sigma12 = cv2.filter2D(img1 * img2, -1, window)[5:-5, 5:-5] - mu1_mu2
 
    ssim_map = ((2 * mu1_mu2 + C1) * (2 * sigma12 + C2)) / ((mu1_sq + mu2_sq + C1) *
                                                            (sigma1_sq + sigma2_sq + C2))
    return ssim_map.mean()
 
def PSNR(img1, img2, shave_border=0):
    height, width = img1.shape[:2]
    img1 = img1[shave_border:height - shave_border, shave_border:width - shave_border]
    img2 = img2[shave_border:height - shave_border, shave_border:width - shave_border]
    imdff = img1 - img2
    rmse = np.sqrt(np.mean(imdff ** 2))
    if rmse == 0:  
        return 100
    return 20 * np.log10(255.0 / rmse)
    
def calculate_ssim(img1, img2):
    '''calculate SSIM
    the same outputs as MATLAB's
    img1, img2: [0, 255]
    '''
    if not img1.shape == img2.shape:
        raise ValueError('Input images must have the same dimensions.')
    if img1.ndim == 2:
        return ssim(img1, img2)
    elif img1.ndim == 3:
        if img1.shape[2] == 3:
            ssims = []
            for i in range(3):
                ssims.append(ssim(img1, img2))
            return np.array(ssims).mean()
        elif img1.shape[2] == 1:
            return ssim(np.squeeze(img1), np.squeeze(img2))
    else:
        raise ValueError('Wrong input image dimensions.')
 
if __name__=='__main__':

    filepath=os.path.dirname(os.path.abspath(__file__))
    GT_path=os.listdir(filepath+'/GT/')
    SR_path=os.listdir(filepath+'/SR/')
    for s in GT_path:
        image_GT=cv2.imread(filepath+'/GT/'+s)
        for p in SR_path:
            print('#'*20)
            filename=p.split('.')
            filename.pop()
            name=filename.pop()
            print('The image is processing:',name)
            image_SR=cv2.imread(filepath+'/SR/'+p)
            ss = calculate_ssim(image_GT,image_SR)
            ps = PSNR(image_GT,image_SR)
            print('the PSNR of this image is',ps)
            print('the SSIM of this image is',ss)
