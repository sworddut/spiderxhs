from PIL import Image
import os
from PyPDF2 import PdfMerger
import argparse
import re
from paXhs import mkdir


def main(args):

    path = args.d
    name = args.n or path

    def sortFiles(filesList):
        pattern = r"\d+"  # 匹配一个或多个数字
        print(filesList)
        filesList.sort(
            key=lambda fileName: int(re.findall(pattern, fileName)[0]) if len(fileName) >= 1 else None)
        return filesList

    def jpg2pdf(jpgFile):
        global imglist
        print(jpgFile)
        path, fileName = jpgFile.rsplit('/', 1)
        preName, postName = fileName.rsplit('.', 1)

        img = Image.open(jpgFile)
        width, height = img.size
        img = img.resize((750, int(750*height//width)), Image.ANTIALIAS)
        imglist.append(img)
        return img.save(path+"/pdf/"+preName+'.pdf', "PDF", resolution=100.0, save_all=True)

    def jpg2pdfByPath(pathName):
        global imglist

        imglist = []
        imgfile = ''
        files = os.listdir(pathName)
        # sortFiles(files)
        # print(files)
        mkdir(f'{path}/pdf')
        for f in files:
            if f.lower().find(".jpeg") > 0:
                jpg2pdf(f'{pathName}/{f}')
                imgfile = f

        # imgMerge = imglist.pop(0) #取出第一个图片示例
        # imgMerge.save(pathName+r'\merge.pdf',"PDF", resolution=100.0, save_all=True, append_images=imglist)
        print("all images processed!")

    jpg2pdfByPath(f'./{path}')
    target_path = f'./{path}/pdf'
    pdf_lst = [f for f in sortFiles(
        os.listdir(target_path)) if f.endswith('.pdf')]
    pdf_lst = [os.path.join(target_path, filename) for filename in pdf_lst]

    file_merger = PdfMerger()
    for pdf in pdf_lst:
        file_merger.append(pdf)     # 合并pdf文件

    file_merger.write(f'./{path}/{name}.pdf')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="请将本文件放在待打包文件夹的同一级")
    parser.add_argument("--d", type=str, help="需要打包的文件夹地址")
    parser.add_argument("--n", type=str, help="打包后pdf的名字")
    args = parser.parse_args()
    main(args)
