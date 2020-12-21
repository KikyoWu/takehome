from app.libs.error import APIException

#客户端类型错误
class ClientTypeError(APIException):
    #401未授权 403禁止访问 404没有找到资源
    #500服务器产生一个未知的错误
    #200查询成功 201创建、更新成功 204删除成功
    #301 302重定向
    code=400#请求参数错误
    msg="client is invalid"
    error_code = 1006

#公共参数异常
class ParameterException(APIException):
    code=400
    msg='invalid parameter'
    error_code=1000

#服务器未知 错误
class ServerError(APIException):
    code = 500  # 错误状态码500服务器产生一个未知的错误
    msg = 'sorry,we have a mistake 😆'
    error_code = 999  # 错误代码，未知错误

#没找到账号
class NotFound(APIException):
    code = 404  # 404没有找到资源
    msg = '对不起，资源没有找到'
    error_code = 1001  # 没找到资源

#删除成功
class DeleteSuccess(Success):
    code=202
    msg='成功删除'
    error_code = -1

#上传成功
class UploadSuccess(Success):
    code=201
    msg='成功上传'
    error_code = 1

#文件类型错误
class FileTypeError(APIException):
    code = 406  # 406not acceptable无法满足请求头中条件
    msg = "对不起，上传文件必须以['.png', '.jpg', '.jpeg', '.gif']为后缀名"
    error_code = 1010  # 后缀名错误


