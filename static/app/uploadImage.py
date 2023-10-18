from flask import Flask, request, Response, render_template, Blueprint
from werkzeug.utils import secure_filename
# 导入工具类
from static.app import response as util
import os
from static.app import mongoClient

import uuid
UploadImage = Blueprint('uploadImage', __name__, template_folder='templates')

# 设置允许上传的文件格式
ALLOW_EXTENSIONS = ['png', 'jpg', 'jpeg']
# 设置图片保存文件夹
UPLOAD_FOLDER = 'E://serviceimage//blogPic'
# 设置图片返回的域名前缀
image_url = "http://111.180.190.112:5000/serviceimage//blogPic//"



# 判断文件后缀是否在列表中
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[-1] in ALLOW_EXTENSIONS

# 上传图片
@UploadImage.route("/upload_image", methods=['POST', "GET"])
def uploads():
    print('请求成功')
    if request.method == 'POST':
        # 获取文件
        file = request.files['file']
        # 检测文件格式
        if file and allowed_file(file.filename):
            # secure_filename方法会去掉文件名中的中文，获取文件的后缀名
            file_name_hz = secure_filename(file.filename).split('.')[-1]
            # 使用uuid生成唯一图片名
            first_name = str(uuid.uuid4())
            # 将 uuid和后缀拼接为 完整的文件名
            file_name = first_name + '.' + file_name_hz
            # 保存原图
            file.save(os.path.join(UPLOAD_FOLDER, file_name))
            imgData = {
                "id":uuid.uuid4(),
                "file_name":file_name,
                "image_url":image_url + file_name,
                "isDelete":"Y"
            }
            mongo = mongoClient.MongoDB()
            data = mongo.insert_one('serviceimage', 'blogPic', imgData)
            if data is None:
                return util.response(message='照片保存失败', code=500)
            else:
                return util.response(message='上传成功',data=imgData)
            mongo.close()
        else:
            return util.response(message='格式错误，仅支持jpg、png、jpeg格式文件',code=500)
    return util.response(message='仅支持post方法',code=503)

@UploadImage.route("/getImgs", methods=["GET"])
def getImgs():
    mongo = mongoClient.MongoDB()
    data = mongo.select_all_collection('serviceimage', 'blogPic', {"isDelete":"Y"})
    if data is None:
        return util.response(message='照片保存失败', code=500)
    else:
        return util.response(data=data)
    mongo.close()