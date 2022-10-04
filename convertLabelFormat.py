import os, glob
import cv2

def convertBBox(img_size, box):
    x = ((box[0] + box[1])/2.0)/img_size[0]
    y = ((box[2] + box[3])/2.0)/img_size[1]
    w = (box[1] - box[0])/img_size[0]
    h = (box[3] - box[2])/img_size[1]
    return (x,y,w,h)
def run_convert():
    read_path = 'datasets/old_labels/train'
    save_path = 'datasets/yolo_labels/train'
    image_path='datasets/images/train'
    count=0
    for filename in glob.glob(os.path.join(read_path, '*.txt')):
        count+=1
        print('--'+str(count)+'--'+filename)
        
        name=filename.replace('datasets/old_labels/train/','')
        name=name.replace('.txt','')
        img = cv2.imread(image_path+'/'+name+'.png')
        h,w,c=img.shape
        img_size=[float(w),float(h)]
        print(img_size)
        
        w = open(save_path+'/'+name+'.txt', 'w')
        
        with open(filename, 'r') as f: 
            lines = f.readlines()
            for line in lines:
                s=(line.strip('\n')).split(',')
                label_c=int(s[0])
                xMin=float(s[1])
                yMin=float(s[2])
                xMax=float(s[1])+float(s[3])
                yMax=float(s[2])+float(s[4])
                
                box=[xMin,xMax,yMin,yMax]
                yoloX,yoloY,yoloW,yoloH=convertBBox(img_size,box)
                #print("%d %f %f %f %f" %(label_c,yoloX,yoloY,yoloW,yoloH))
                w.write("%d %f %f %f %f\n" %(label_c,yoloX,yoloY,yoloW,yoloH))
            f.close()
        w.close()
        
run_convert()
