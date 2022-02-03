import matplotlib.pyplot as plt

from PIL import Image, ImageFilter
from os.path import basename, dirname, join

def filterMode():
    boxFilter = ["none", ImageFilter.BLUR, ImageFilter.EDGE_ENHANCE, ImageFilter.EDGE_ENHANCE_MORE, ImageFilter.EMBOSS, ImageFilter.SHARPEN, 
                    ImageFilter.CONTOUR, ImageFilter.SMOOTH_MORE]
    return boxFilter
                                                                                    # readImage(fname)略去，集成到其他地方去了
def saveFilterImage(fname):
    image = Image.open(fname)
    boxFilter = filterMode()
    directName = dirname(fname)
    fileName = basename(fname)
    subName = fileName.split(".")[0]
    extenName = fileName.split(".")[1]

    for i, name in enumerate(boxFilter):
        if name != "none" :
            name = (str(boxFilter[i]).split(".")[-1].lower()).split("'")[0]         # 这么长的表达式实际上返回所用模式名字的全字母小写（连接处依然使用下划线）
            saveDirectory = join(directName, f"{subName}_{name}.{extenName}")
            image.filter(boxFilter[i]).save(f"{saveDirectory}")                     # 此处相当于将临时对象（即刚用滤镜处理，但没改变原图）立即保存

def showFilterImage(fname):
    image = Image.open(fname)
    font = dict(family="monospace", weight="black")
    
    boxFilter = filterMode()
    rows, cols, k = 2, 4, 0
    fig, ax = plt.subplots(rows, cols)

    for row in range(rows):
        for col in range(cols):
            if boxFilter[k] != "none" :
                ax[row, col].imshow(image.filter(boxFilter[k]))
                ax[row, col].set_title((str(boxFilter[k]).split(".")[-1].lower()).split("'")[0], **font)
                ax[row, col].set_axis_off()
            else :
                ax[row, col].imshow(image)
                ax[row, col].set_title("source_image", **font)
                ax[row, col].set_axis_off()
            k+=1

    fig.subplots_adjust(left=0.03, right=0.97, bottom=0.15, top=0.85, hspace=0.005, wspace=0.02)

    plt.show()

def main(fname):
    saveFilterImage(fname)
    showFilterImage(fname)

if __name__ == "__main__" :
    try:
        main(r"tree_image.jpg")
    except Exception as exc:
        print(exc)