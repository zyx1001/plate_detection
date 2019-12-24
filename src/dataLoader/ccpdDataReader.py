# 车牌所需字符
provinces = ["皖", "沪", "津", "渝", "冀", "晋", "蒙", "辽", "吉", "黑", "苏", "浙", "京", "闽", "赣", "鲁", "豫", "鄂", "湘", "粤", "桂",
             "琼", "川", "贵", "云", "藏", "陕", "甘", "青", "宁", "新", "警", "学", "O"]

ads = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
       'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'O']

class ccpdDataReader(object):

    # 返回图片对应的车牌框位置
    @staticmethod
    def readCCPDtoRectangle(path):
        list=path.split('-')
        loc_rectangle=list[2]
        left_top=loc_rectangle.split('_')[0]
        right_bottom=loc_rectangle.split('_')[1]
        left=left_top.split('&')[0]
        top=left_top.split('&')[1]
        right=right_bottom.split('&')[0]
        bottom=right_bottom.split('&')[1]
        return left,right,bottom,top

    # 返回图片对应的车牌号码
    @staticmethod
    def readCCPDtoPlateNum(path):
        list = path.split('-')
        pln=[]
        pln_oringin=list[4]
        pln_oringin=pln_oringin.split('_')
        pln.append(provinces[int(pln_oringin[0])])
        for i in range(1,7):
            pln.append(ads[int(pln_oringin[i])])
        return pln
example='025-95_113-154&383_386&473-386&473_177&454_154&383_363&402-0_0_22_27_27_33_16-37-15.jpg'
print(ccpdDataReader.readCCPDtoPlateNum(example))

