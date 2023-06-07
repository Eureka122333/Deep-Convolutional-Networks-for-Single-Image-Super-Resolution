import os
import time
import cv2 as cv

filePath = os.path.dirname(os.path.abspath(__file__))

# 获取当前文件夹下的文件名列表
def readname():
  names = None
  try:
    names = os.listdir(filePath+'/x4/')
  except Exception as e:
    print(e)
    print('获取文件名列表失败！')
  else:
    print('获取文件名列表成功！')
    return names

# 图片转换
def handleImage(names):
  for name in names:
    suffixs = name.split('.')
    img = cv.imread(filePath+'/x4/'+name)
    cv.imwrite('./png/'+suffixs[0]+'_bic.png', img)
    print(f'=================suffixs[0]转换成功==================')

# 转换所用时间的计算
def loopHandleFile():
  start = time.time()
  startTime = int(round(start * 1000))
  names = readname()
  try:
    if not os.path.exists(f'./png/'):
      os.makedirs(f'./png/')
    handleImage(names)
  except Exception as e:
    print(e)
    print('批量转换图片失败！')
  else:
    print('批量转换图片成功！')
    end = time.time()
    endTime = int(round(end * 1000))
    print('本次转换用时：' + str(endTime - startTime) + ' ms')

if __name__ == "__main__":
  loopHandleFile()