# **********************************************************
# * Author        : Guoqing DU
# * Email         : guoqingdu@foxmail.com
# * Create time   : 2019-6-20 13:15
# * Last modified :
# * Filename      : PGM2PNG.py
# * Description   :
# **********************************************************

from PIL import Image
import os, glob  #glob模块用于查找符合规定的格式的文件
def batch_image(input_dir, output_dir):
    if not os.path.exists(output_dir):
        print(output_dir, 'is not existed')
        os.mkdir(output_dir)

    if not os.path.exists(input_dir):
        print(input_dir,'is not existed')
        return -1;

    count = 0
    for files in glob.glob(input_dir + '\\*.pgm'):
        filepath, filename = os.path.split(files)  #指定文件名用于分割，前面赋给文件路径，后面作为文件名
        filename, _ = filename.split('.')
        output_file = filename[0:10] + '.jpg'
        im = Image.open(files)
        new_path = os.path.join(output_dir, output_file)
        print(count, ',', new_path)
        count += 1
        im.save(os.path.join(output_dir, output_file))

if __name__ == '__main__':
    for i in range(1, 41):
        batch_image('D:\\AIML_Project\\faceRecognition\\att_faces\\orl_faces\\s'+ str(i), 'D:\\AIML_Project\\faceRecognition\\att_faces\\faceJpg\\s'+ str(i))

