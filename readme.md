## install
pip install fastapi uvicorn

## openai
export OPENAI_API_KEY='your-api-key-here'
## runing
uvicorn main:app --reload

## visiting api
import requests
import json

### 定义要发送的数据
data = {
    "data": {
        "key1": "value1",
        "key2": "value2"
    }
}

### 将数据转换为 JSON 格式
json_data = json.dumps(data)

### 发送 POST 请求
response = requests.post("http://127.0.0.1:8000/", headers={"Content-Type": "application/json"}, data=json_data)

### 打印响应内容
print(response.json())