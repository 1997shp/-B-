import win32api
import win32con
import win32gui
import time
import PIL
from PIL import  Image
from PIL import  ImageGrab
import random
import aircv as ac


time.sleep(2)
def LeftClick(x, y):    # 鼠标左键点击屏幕上的坐标(x, y)
	win32api.SetCursorPos((x, y))    # 鼠标定位到坐标(x, y)

	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 1, 1)    # 鼠标左键按下
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 1, 1)    # 鼠标左键弹起
	# win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN + win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)    # 测试


def get_window_info(wdname):  # 获取窗口信息   #wdname = u'游戏名'
    handle = win32gui.FindWindow(0, wdname)  # 获取窗口句柄
    if handle == 0:

        return None
    else:
        return win32gui.GetWindowRect(handle)

def matchimg(img_old,img_new):   #img_old,img_new):
    imsrc = ac.imread(img_old)
    imobj = ac.imread(img_new)
    result = ac.find_template(imobj,imsrc,0.8)
    #if result is not None:
        #result['shape']= (imsrc.shape[1],imsrc.shape[0])

    return result['rectangle'][0], result['rectangle'][3]

def daguai(img_1,img_2,img_3,img_da):   #img_old,img_new):
    imsrc1 = ac.imread(img_1)
    imsrc2 = ac.imread(img_2)
    imsrc3 = ac.imread(img_3)
    imobj = ac.imread(img_da)
    result = ac.find_template(imobj,imsrc1,0.8)
    #if result is not None:
        #result['shape']= (imsrc.shape[1],imsrc.shape[0])
    if result is not None:
        return result['rectangle'][0], result['rectangle'][3]
    elif result is None:
        result = ac.find_template(imobj, imsrc2, 0.8)
        if result is not None:
            return result['rectangle'][0], result['rectangle'][3]
        else :
            result = ac.find_template(imobj, imsrc3, 0.8)
            return result['rectangle'][0], result['rectangle'][3]


def random_in_range(min, max):		# 在给定范围内进行随机数
	return min + int((max - min) * random.random())


def zuobiao(zidian):                # 从matchimg函数返回值中获取点的坐标值
    list1 = []
    zuobiao1 = list(zidian[0])      # 将元组转化为列表取出坐标x，y 的值
    zuobiao2 = list(zidian[1])
    zuobiaox1 = zuobiao1[0]
    zuobiaoy1 = zuobiao1[1]
    zuobiaox2 = zuobiao2[0]
    zuobiaoy2 = zuobiao1[1]
    list1 = [zuobiaox1,zuobiaoy1,zuobiaox2,zuobiaoy2]   # 将取出的值重新组成一个列表
    return list1



if __name__ == "__main__":

    wdname = u'碧蓝航线 - MuMu模拟器'     #  wdname 为游戏窗口的名称，必须写完整
    window_size = get_window_info(wdname)
    if window_size is not None:         #  如果成功获取到窗口的坐上和右下坐标，将坐标传入下面的变量
        initxl = window_size[0]
        inityl = window_size[1]
        initxr = window_size[2]
        inityr = window_size[3]
    img = ImageGrab.grab(bbox=(initxl,inityl,initxr,inityr))        # 根据坐标截取屏幕
    #img.show()
    img.save('F:\\apk\BILAN\datu.png')                              # 截取到的窗口图片保存在下面路径
    #img_n = Image.open('datu.png')
    #img_o=Image.open('chuji.png')
    #print(matchimg('F:\\apk\BILAN\dianji.png','F:\\apk\BILAN\datu.png'))
    l1 = matchimg('F:\\apk\BILAN\huodong1.png','F:\\apk\BILAN\datu.png')   #  第一个参数是本地的小图片，第二个参数是截取到的游戏窗口图，函数为在第二个图片上寻找第一个图片的坐标
    #print (l1)
    l11 = list(l1)                                                          # 函数的返回值是一个元组，转换为列表
    l111 = zuobiao(l11)                                                        # 通过zuobiao（）函数，取到左上和右下x，y的值返回为一个列表
    #print(l3)
    #print(zuobiao(l2))
    #chuji1 = chuji[0]
    #chuji2 = chuji[1]
    LeftClick( initxl+random_in_range(l111[0],l111[2]), inityl+random_in_range(l111[1],l111[3]))   #  点击出击的按钮
    time.sleep(3)
    img = ImageGrab.grab(bbox=(initxl, inityl, initxr, inityr))  # 根据坐标截取屏幕
    # img.show()
    img.save('F:\\apk\BILAN\B3tu.png')
    time.sleep(1)
    l2 = matchimg('F:\\apk\BILAN\huodong2.png', 'F:\\apk\BILAN\B3tu.png')       # 选择B3
    #print(l2)
    l22 = list(l2)  # 函数的返回值是一个元组，转换为列表
    l222 = zuobiao(l22)
    LeftClick(initxl + random_in_range(l222[0], l222[2]), inityl + random_in_range(l222[1], l222[3])) # 点击1-2

    time.sleep(3)
    img = ImageGrab.grab(bbox=(initxl, inityl, initxr, inityr))  # 根据坐标截取屏幕
    # img.show()
    img.save('F:\\apk\BILAN\likeqianwang.png')
    time.sleep(1)
    l3 = matchimg('F:\\apk\BILAN\huodong3.png', 'F:\\apk\BILAN\likeqianwang.png')

    # print(l2)
    l33 = list(l3)  # 函数的返回值是一个元组，转换为列表
    l333 = zuobiao(l33)
    LeftClick(initxl + random_in_range(l333[0], l333[2]), inityl + random_in_range(l333[1], l333[3])) # 点击立刻前往

    time.sleep(3)
    img = ImageGrab.grab(bbox=(initxl, inityl, initxr, inityr))  # 根据坐标截取屏幕
    # img.show()
    img.save('F:\\apk\BILAN\likeqianwang1.png')
    time.sleep(1)
    l4 = matchimg('F:\\apk\BILAN\huodong4.png', 'F:\\apk\BILAN\likeqianwang1.png')

    # print(l2)
    l44 = list(l4)  # 函数的返回值是一个元组，转换为列表
    l444 = zuobiao(l44)
    LeftClick(initxl + random_in_range(l444[0], l444[2]), inityl + random_in_range(l444[1], l444[3]))  # 点击立刻前往

    time.sleep(4)
    img = ImageGrab.grab(bbox=(initxl, inityl, initxr, inityr))  # 根据坐标截取屏幕
    # img.show()
    img.save('F:\\apk\BILAN\\xiaoguai1.png')
    time.sleep(6)
    l5 = daguai('F:\\apk\BILAN\huodong14.png','F:\\apk\BILAN\huodong13.png','F:\\apk\BILAN\huodong15.png', 'F:\\apk\BILAN\\xiaoguai1.png')

    # print(l2)
    l55 = list(l5)  # 函数的返回值是一个元组，转换为列表
    l555 = zuobiao(l55)
    pianyi = 50
    LeftClick(initxl + random_in_range(l555[0], l555[2]), inityl + random_in_range(l555[1], l555[3]) + pianyi)  # 点击立刻前往




