import os
import re
from dota_utils import GetFileFromThisRootDir
import dota_utils as util

def poly2oripoly(poly, x, y, rate):
    oripoly = []
    assert len(poly) == 8
    for i in range(len((poly)/2)):
        tmp_x = float(poly[i * 2] + x) / float(rate)
        tmp_y = float(poly[i * 2 + 1] + y) / float(rate)
        oripoly.append(tmp_x)
        oripoly.append(tmp_y)
    return oripoly

def main():
    srcPath = "/home/yanggang/data/DOTA_SPLIT/val/detect_out/"
    dstPath = "/home/yanggang/data/DOTA_SPLIT/val/merged/"
    filelist = GetFileFromThisRootDir(srcPath)
    for fullname in filelist:
        name = util.custombasename(fullname)
        print ("processing : " + fullname)
        with open(fullname, "r") as f_in:
            #nameboxdict = {}
            lines = f_in.readlines()
            splitlines = [x.strip().split(' ') for x in lines]
            for splitline in splitlines:
                subname = splitline[0]
                det = ' '.join(splitline)
                splitname = subname.split('__')
                #oriname = splitname[0]
                #pattern1 = re.compile(r'__\d+___\d+')

                #x_y = re.findall(pattern1, subname)
                #x_y_2 = re.findall(r'\d+',x_y[0])
                #x,y = int(x_y_2[0]), int(x_y_2[1])

                #pattern2 = re.compile(r'__([\d+\.]+)__\d+___')
                #rate = re.findall(pattern2, subname)[0]

                #confidence = splitline[1]
                #poly = list(map(float, splitline[2:-1]))
                #oripoly = poly2oripoly(poly,x,y,rate)
                pred_cls = splitline[-1]
                dstTxtPath = os.path.join(dstPath,pred_cls + '.txt')
                if not os.path.exists(dstPath):
                    os.mkdir(dstPath)
                with open(dstTxtPath,"a+") as f_out:
                    f_out.write(det +"\n")





if __name__ == "__main__":
    main()
