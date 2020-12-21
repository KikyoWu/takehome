from sqlalchemy import Column, Integer, String,DateTime
from sqlalchemy.dialects.mysql import MEDIUMTEXT
from app.models.base import Base, db
from datetime import datetime,date
from aip import AipOcr
import os.path


#User模型，继承自定义的base.py中的Base类
class Img(Base):
    id=Column(Integer,primary_key=True)
    addtime = Column(DateTime, index=True, default=datetime.now)  # 添加时间
    filename=Column(String(100),unique=True,nullable=False)
    content=Column(MEDIUMTEXT)

    def keys(self):
        return ['content']

    #获取上传文件内容
    @staticmethod#在对象下面再创建对象本身不合理，要用静态方法
    def upload_img(file_path):
        #在数据库中使用auto_commit()方法新增用户
        filename=os.path.basename(file_path)
        #APP_ID = "15433908"
        #API_KEY = "tcHjIKc51txVe73RNA2Pt7pY"
        #SECRET_KEY = "08OvI17ZHWt6Q9PoL4o885LXxRFvdSLG"
        #APP_ID = '21372704'
        #API_KEY = 'YKpXQwN5zj79g99fZK8i4Kn1'
        #SECRET_KEY = 'RTIAaFrvvgHbej7eALMKmjR0uF93rHCQ'
        APP_ID = '23181719'
        API_KEY = 'fcZTDk8j1L2sNGtMbzR8pAUu'
        SECRET_KEY = 'NrtmklBogj4HPaK76mnL9xFftPNGZPpM'
        client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
        options = {}
        options["language_type"] = "ENG"
        with open(file_path, 'rb') as i:
            word = i.read()
        message_dict = client.basicGeneral(word,options)  # 用client.basicGeneral(img_save)来获取一组信息。
        """
        {'log_id': 6412010709116467009,
        'words_result': [{'words': '价格可以随便乱调吗辣'}],
        'words_result_num': 1}
        """
        message_list= message_dict.get('words_result')
        words=[]
        with open('app/static/word/' + filename + '.txt', 'a') as f:
            for i in message_list:
                words.append(i.get('words'))
                f.write(str(i.get('words'))+'\n')
        with db.auto_commit():
            img=Img()
            img.filename=filename
            img.content=str(words)
            db.session.add(img)

