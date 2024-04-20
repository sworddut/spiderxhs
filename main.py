from paXhs import main as paXhs
from toPdf import main as toPdf
import argparse


class ArgsfortoPdf:
    def __init__(self, d, n):
        self.d = d
        self.n = n


def main(args):
    url = args.u
    path = args.d
    name = args.n or path
    argsfortoPdf = ArgsfortoPdf(path, name)
    print(argsfortoPdf.d)
    paXhs(url)
    toPdf(argsfortoPdf)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="本项目用于爬取小红书上的图片")
    parser.add_argument("--u", type=str, help="需要打包的文件夹地址")
    parser.add_argument("--d", type=str, help="需要打包的文件夹地址")
    parser.add_argument("--n", type=str, help="打包后pdf的名字")
    args = parser.parse_args()
    main(args)
