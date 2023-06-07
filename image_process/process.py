import cv2 as cv
import sys,os

if __name__ == '__main__':
    #读取图像并判断是否读取成功
    filepath=os.path.dirname(os.path.abspath(__file__))
    images=os.listdir(filepath+'/original/')


    for p in images:
        print(p)
        suffixs = p.split('.')
        suffixs.pop()
        name = suffixs.pop()
        #需要放大的部分
        image=cv.imread(filepath+'/original/'+p)
        #cv.imshow('origin',image)
        #cv.waitKey(0)
        part = image[50:150,50:150]
        #双线性插值法
        mask = cv.resize(part, (300, 300), fx=0, fy=0, interpolation=cv.INTER_LINEAR)
        if image is None is None:
            print('Failed to read picture')
            sys.exit()
        cv.imwrite(filepath+'/part/'+name+'_part.png',mask)


        #画框并连线
        cv.rectangle(image,(50,50),(100,100),(0,255,0),1)

        cv.imwrite(filepath+'/add_rectangle/'+name+'1.png',image)

