import numpy as np
import pandas as pd
import cv2
 
img =cv2.imread('../pic/15.png')
index=['color','color_name','hex','R','G','B']
csv=pd.read_csv('colors.csv',names=index,header=None)
#指定行数用来作为列名，数据开始行数。如果文件中没有列名，则默认为0，否则设置为None。如果明确设定header=0 就会替换掉原来存在列名。header参数可以是一个list例如：[0,1,3]，这个list表示将文件中的这些行作为列标题（意味着每一列有多个标题），介于中间的行将被忽略掉
#names : array-like, default None 用于结果的列名列表，如果数据文件中没有列标题行，就需要执行header=None。默认列表中不能出现重复，除非设定参数mangle_dupe_cols=True
clicked=False #初始化
r=g=b=xpos=ypos=0 #初始化
 
def recognize_color(R,G,B):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R- int(csv.loc[i,"R"])) + abs(G- int(csv.loc[i,"G"]))+ abs(B- int(csv.loc[i,"B"]))
        if(d<=minimum):
            minimum = d
            cname = csv.loc[i,"color_name"]
    return cname
 
def mouse_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b,g,r,xpos,ypos, clicked
        clicked = True
        xpos = x
        ypos = y
        b,g,r = img[y,x]
        b = int(b)
        g = int(g)
        r = int(r)
 
cv2.namedWindow('Color Recognition App')#创建一个窗口
cv2.setMouseCallback('Color Recognition App',mouse_click)#调用鼠标双击功能
 
while (1):
    cv2.imshow("Color Recognition App", img)
    if (clicked):
 
        # cv2.rectangle(image, startpoint, endpoint, color, thickness)-1 fills entire rectangle
        cv2.rectangle(img, (20, 20), (750, 60), (b, g, r), -1) # (x1, y1), (x2, y2) -1代表颜色填充满整个矩形
        # Creating text string to display( Color name and RGB values )
        text = recognize_color(r, g, b) + ' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)
 
        # cv2.putText(img,text,start,font(0-7),fontScale,color,thickness,lineType )
        cv2.putText(img, text, (50, 50), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)
        #图片，添加的文字，左上角坐标，字体，字体大小，颜色，字体粗细
        # For very light colours we will display text in black colour
        if (r + g + b >= 600):
            cv2.putText(img, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)
 
        clicked = False
 
        #Break the loop when user hits 'esc' key
    if cv2.waitKey(20) & 0xFF ==27:
        break
cv2.destroyAllWindows()