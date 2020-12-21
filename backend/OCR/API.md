[TOC]

# 功能

- 上传图片，并将图片中的英文字母识别出来，将识别结果保存进数据库以备将来使用
- 获取图片识别内容，将结果作为JSON返回给用户
- 删除识别记录，使用户无法获取该图片识别内容，但依旧存于数据库中

# 调用方式

## 上传图片

**请求格式**

- POST方式调用
- 调用地址：localhost:5000/v1/image

**返回格式**

- 格式：JSON格式

- 成功示例

  ```json
  {
      "error_code": 1,
      "msg": "成功上传",
      "request": "POST /v1/image"
  }
  ```

**请求格式支持**：PNG、JPG、JPEG

## 获取图片识别内容

**请求格式**

- GET方式调用
- 调用地址：localhost:5000/v1/image/<uid>

**返回格式**

- 格式：JSON格式

- 内容示例

  ```json
  {
      "content": "['station B . umbers', '. Use Ref . 2018 . pdf', 'OOK', 'REE5 Rah', 'Q SR', '13248-aa1ti9 , , , , , , , , , , , , , , , , , AI 2 % 0FPA58', 't 0 T19E7 EA , , , , , , , , , , , , , B50 -', 'F : * * 1851 2z4', 'VPF6-NR4U-YY64-8KQT-07LE-BXFZ', 'ERSE', 'EO', 'KYg', 'BeA : ta Macintosh HD \" &', '2ia', 'F = E0RELBIFFREB', 'Fa R . ?', 'EA ERRR F , , , h']"
  }
  ```

## 删除数据库中图片转换记录

**请求格式**

- DELETE方式调用
- 调用地址：localhost:5000/v1/image/<uid>

**返回格式**

- 格式：JSON格式

- 内容示例

  ```json
  {
      "error_code": -1,
      "msg": "成功删除",
      "request": "DELETE /v1/image/1"
  }
  ```

**注意：**该删除格式为软删除，只是改变数据库中status状态，使GET方法无法获取转换内容，彻底删除需在数据库中删除

# 错误码

若请求错误，服务器将返回的JSON文本包含以下参数：

- **error_code**：错误码。
- **msg**：错误描述信息，帮助理解和解决发生的错误。
- **request**：发送错误的请求地址。

|      |
| ---- |
|      |