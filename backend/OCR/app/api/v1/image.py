from app.libs.error_code import UploadSuccess, FileTypeError, DeleteSuccess
from app.libs.redprint import Redprint
import random,string
from flask import  jsonify, request
from werkzeug.utils import secure_filename
from app.models.Image import Img
from app.models.base import db

api=Redprint('image')

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])   # 允许上传的文件类型
def allowed_file(filename):   # 验证上传的文件名是否符合要求，文件名必须带点并且符合允许上传的文件类型要求，两者都满足则返回 true
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@api.route('',methods=['POST'])
def image_upload():
    ran_str=''.join(random.sample(string.ascii_letters+string.digits,4))
    file = request.files['file']  # 获取上传的文件
    if file and allowed_file(file.filename):  # 如果文件存在并且符合要求则为 true
        ran_str=''.join(random.sample(string.ascii_letters+string.digits,4))
        img = secure_filename(file.filename)  # 获取上传文件的文件名
        filename=ran_str+'+'+img
        file_path='app/static/img_save/'+filename
        file.save(file_path)  # 保存文件
        Img.upload_img(file_path)
        return UploadSuccess()  # 返回保存成功的信息
    else:
        raise FileTypeError()

@api.route('/<int:uid>',methods=['GET'])
def get_user(uid):
    #url不应该包含动词
    img=Img.query.filter_by(id=uid).first_or_404()
    return jsonify(img)

@api.route('/<int:uid>',methods=['DELETE'])
def super_delete_user(uid):
    with db.auto_commit():
        img=Img.query.filter_by(id=uid).first_or_404()
        img.delete()
    return DeleteSuccess()