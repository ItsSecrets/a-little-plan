# coding:utf-8
"""
    移植项目，原项目用的碎图，整个项目的资源在一个文件夹。新项目需要替换资源准备
    打成plist+png的大图，所以筛选出用的到的资源，根据不同的csd文件放到对应的文件
    夹，然后把对应文件夹的碎图直接替换，没用到的直接删除。
    脚本目录下需要包含csb文件夹，里面包含csd文件以及用到的资源文件
"""
import  xml.dom.minidom
import os
import shutil
import time
import sys

#########因为文件夹名字是中文，需要加这个处理一下转成utf-8编码
if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')


"""
    筛选出每个csd文件用到的图片资源
"""
root_csd_path = os.path.join(os.getcwd(), 'csb')
root_backup_csd_path = os.path.join(os.getcwd(), 'backup_csb')

#csb文件中可能会有资源的标签
CONFIG_DATA = [
    'FileData',
    'PressedFileData',
    'DisabledFileData',
    'NormalFileData',
    'BackGroundData',
    'ProgressBarData',
    'BallNormalData',
    'BallPressedData',
    'BallDisabledData',
    'LabelAtlasFileImage_CNB',
    'ImageFileData',
]

##获取csd文件中的图片路径信息
def getImgPath(xmlName):
    imag_paths = []
    # 打开xml文档
    dom = xml.dom.minidom.parse(xmlName)
    # 得到文档元素对象
    root = dom.documentElement
    count = 0
    for attrKey in CONFIG_DATA:
        item_count = 0
        dateInfo = root.getElementsByTagName(attrKey)
        if dateInfo:
            for fileDataInfo in dateInfo:
                count = count + 1
                item_count = item_count+1
                resPath = fileDataInfo.getAttribute("Path")
                imag_paths.append(resPath)
        # print attrKey, ":", item_count
    print "image count: ", count
    # print imag_paths
    return imag_paths

#拷贝用到的碎图资源到自己的文件夹
def copyRes(resList, csdName):
    desPath = os.path.join(root_backup_csd_path, csdName)
    if os.path.exists(desPath):
        os.removedirs(desPath)
    #保证每次的资源都是新拷贝的需要的
    os.makedirs(desPath)
    print os.getcwd()
    for resName in resList:
        srcRes = os.path.join(root_csd_path, resName)
        names = os.path.split(resName)
        desRes = os.path.join(desPath, names[1])
        if os.path.isfile(srcRes):
            shutil.copy(srcRes, desRes)
        else:
            print resName+' not found'

##重命名csd文件为xml
def reNameCsbToXml():
    #备份csd
    backupCsd()

    files = []
    dirs = os.listdir(root_backup_csd_path)
    for file in dirs:
        names = os.path.splitext(file)
        if names[1] == '.csd':
            des = os.path.join(root_backup_csd_path, '%s.xml' % (names[0]))
            src = os.path.join(root_backup_csd_path, file)
            os.rename(src, des)
            files.append(des)

##备份一下csd文件
def backupCsd():
    backup_path = os.path.join(os.getcwd(), 'backup_csb')
    if os.path.exists(backup_path):
        shutil.rmtree(backup_path)
    shutil.copytree(os.path.join(os.getcwd(), 'csb'), os.path.join(os.getcwd(), 'backup_csb'))
if  __name__=="__main__":
    files = reNameCsbToXml()

    time.sleep(1)
    lsitfile = os.listdir(root_backup_csd_path)
    for file in lsitfile:
        names = os.path.splitext(file)
        if names[1] == '.xml':
            print '--------------------------',file,'---------------------------'
            # print os.path.join(root_backup_csd_path, file)
            resList = getImgPath(os.path.join(root_backup_csd_path, file))
            copyRes(resList,names[0])
            time.sleep(2)
            print '--------------------------',file,'---------------------------'
            print
            print
            print
