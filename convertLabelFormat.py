import os, glob
import cv2

def convertBBox(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = ((box[0] + box[1])/2.0)*dw
    y = ((box[2] + box[3])/2.0)*dh
    w = (box[1] - box[0])*dw
    h = (box[3] - box[2])*dh
    return (x,y,w,h)
def run_convert():
    read_path = 'datasets/labels/train'
    save_path = 'datasets/yolo_labels/train'
    image_path='datasets/images/train'
    count=0
    for filename in glob.glob(os.path.join(read_path, '*.txt')):
        count+=1
        print('--'+str(count)+'--')        
        
        name=filename.strip('.txt').strip('datasets/labels/train').strip('\\')
        img = cv2.imread(image_path+'/'+name+'.png')
        h,w,c=img.shape
        size=[float(h),float(w)]
        
        w = open(save_path+'/'+name+'.txt', 'w')
        with open(os.path.join(os.getcwd(), filename), 'r') as f: 
            lines = f.readlines()
            for line in lines:
                s=(line.strip('\n')).split(',')
                label_c=int(s[0])
                xMin=float(s[1])
                yMin=float(s[2])
                xMax=float(s[1])+float(s[3])
                yMax=float(s[2])+float(s[4])
                
                box=[xMin,xMax,yMin,yMax]
                
                yoloW,yoloY,yoloW,yoloH=convertBBox(size,box)
                #print("%d %f %f %f %f" %(label_c,yoloW,yoloY,yoloW,yoloH))
                w.write("%d %f %f %f %f\n" %(label_c,yoloW,yoloY,yoloW,yoloH))
            f.close()
        w.close()