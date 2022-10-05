from datetime import datetime
import os, glob
import csv
import cv2

def yolobbox2bbox(x,y,w,h,img_size):
    x1, y1 = (x-w/2)*img_size[0], (y-h/2)*img_size[1]
    x2, y2 = (x+w/2)*img_size[0], (y+h/2)*img_size[1]
    return x1, y1, x2, y2

def run_convert():
    read_path = 'yolov5/runs/detect/exp/labels'
    save_path = 'result'
    image_path= 'datasets/test/public/'
    count=0
    csv_filename= datetime.now().isoformat()
    with open(save_path+'/result'+csv_filename+'.csv','w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for filename in glob.glob(os.path.join(read_path, '*.txt')):
            count+=1

            name=filename
            name=name.replace('yolov5/runs/detect/exp/labels/','').replace('.txt','')
            
            img = cv2.imread(image_path+'/'+name+'.png')
            h,w,c=img.shape
            img_size=[float(w),float(h)]
        
            print('--'+str(count)+'-- '+name)
            print(img_size)
            with open(filename,'r') as f:
                lines=f.readlines()
                for line in lines:
                    line=line.strip('\n').split(' ')
                    #print(line)
                    class_id=line[0]
                    YoloX=float(line[1])
                    YoloY=float(line[2])
                    YoloW=float(line[3])
                    YoloH=float(line[4])
                    x1,y1,x2,y2=yolobbox2bbox(YoloX,YoloY,YoloW,YoloH,img_size)
                    w = round(x2-x1)
                    h = round(y2-y1)
                    x1 = round(x1)
                    y1 = round(y1)
                    # x1=int(x1)
                    # y1=int(y1)
                    # w=int(x2-x1)
                    # h=int(y2-y1)
                    print("%s %s %d %d %d %d" %(name,class_id,x1,y1,w,h))
                    writer.writerow([name,class_id,x1,y1,w,h])
run_convert()