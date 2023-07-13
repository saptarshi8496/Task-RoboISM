import cv2
import math

test = 'angles2.png'
img = cv2.imread(test)
pt_list = []

def coordinates(event,x,y,flag,para):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),3,(255,0,0),-1)
        pt_list.append([x,y])

def slope(a,b):
    m = (b[1]-a[1])/(b[0]-a[0])
    return m

def angle(pt_list):
    o = pt_list[-3]
    a = pt_list[-2]
    b = pt_list[-1]
    
    if slope(o,a)*slope(o,b)==-1:
        angle = (math.pi)/2
    else:
        m1 = slope(o,a)
        m2 = slope(o,b)
        ts = (m2-m1)/(1+m1*m2)
        if ts<0:
            arg = abs(ts)
            angle = math.atan(arg)
            a = 180 - round(math.degrees(angle))
        else:
            arg = abs(ts)
            angle = math.atan(arg)
            a = round(math.degrees(angle))
    cv2.putText(img,str(a),(o[0]-30,o[1]+30),cv2.FONT_HERSHEY_COMPLEX,
                1,(255,0,0),2)
    
while True:
    if len(pt_list)==3:
        angle(pt_list)
        pt_list=[]
            
    cv2.imshow('Image',img)
    cv2.setMouseCallback('Image',coordinates)    
    
    if cv2.waitKey(1) & 0xFF == ord('a'):
        pt_list = []
        img = cv2.imread(test)

