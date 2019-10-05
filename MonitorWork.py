# 监督工作，不定时截屏

# 作者：Crow·Lu
# 链接：https://www.zhihu.com/question/21065451/answer/681896589
# 来源：知乎
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

#python3 author Crow Lu
import time
from PIL import ImageGrab
ts = 0
print('{times}{formats} '.format(times = ts ,formats ='.png'))
#print(time.localtime())

def Screenshot():
        nowtime = time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime(time.time()))
        print(nowtime)

        im = ImageGrab.grab()
        im.save('png\{times}.png'.format(times = nowtime))


while True:
    print("开始工作！")
    Screenshot()

    print("休息中……")
    print("\n")
    # 30 minutes = 1800s
    time.sleep(1800)