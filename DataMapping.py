# -*- coding: UTF-8 -*-
import numpy as np
import pandas as pd

class Datamapping:
    def __init__(self):
        source_file = ''

    '''
    读取源文件中的字符
    返回文件字符内容
    '''
    def getSourceFileExcel(self,file_path,sheetname):
        print("getSourceFileExcel")
        print("file path : " + file_path)
        print("sheet name : "+ sheetname)
        source_file = pd.read_excel(file_path,sheetname)
        #print(source_file)
        print(source_file.query('jiraid=="TMSI-1787"'))
        #print(source_file.isin(['预录入编号:']))
        #print(source_file.tail(5))
        #print(source_file.loc[:10,['jiraid','summary']])
        #print(source_file.iloc[1:10,1:3])
        #print(source_file.to_numpy())
        #通过位置获取值
        #print(source_file.iloc[16:37,6:8])
        #获取0-3行和指定列
        #print(source_file['jiraid'][0:3])
        #获取多行和指定列
        #print(source_file.loc[:10,['jiraid','summary']])
       # print(source_file.columns)
        file_str_matrix = ''
        return file_str_matrix


    '''
    将源文件中的字符匹配到目标文件
    '''
    def getTargetFile(self,source_file):
        print("getTargetFile")
        target_file = ''

        return target_file

testcase = Datamapping()
testcase.getSourceFileExcel('D:\瑞格丝\SynologyDrive\产品管理\FreeManualInputMVP\data\workhoursdata.xls','Sheet1')
#testcase.getSourceFileExcel('D:\瑞格丝\SynologyDrive\产品管理\FreeManualInputMVP\data\报关单数据\PACKING LIST-065B.xls','PACKING LIST')
#testcase.getSourceFileExcel('D:\inv.xls','INV')
#testcase.getSourceFileExcel('D:\瑞格丝\SynologyDrive\产品管理\FreeManualInputMVP\data\E000419100006\原始资料.xlsx','出口报关建议书2')


