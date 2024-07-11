from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict
from openai import OpenAI

# client = OpenAI()

app = FastAPI()


def generate_from_openai_chat_completion(
    messages: list[dict[str, str]],
    model: str,
    temperature: float,
    max_tokens: int,
    top_p: float,
    context_length: int,
    stop_token: str | None = None,
    num_outputs: int = 1,
) -> Union[str, list[str]]:

    # client = AzureOpenAI(
    #     azure_endpoint=os.environ['AZURE_ENDPOINT'],
    #     api_key=os.environ['AZURE_API_KEY'],
    #     api_version=os.environ['API_VERSION']
    # )
    from openai import OpenAI
    client = OpenAI()
    import time
    import pdb; pdb.set_trace()
    start_time = time.time()

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p,
        n=num_outputs
    )
    print("Completion time:", time.time() - start_time)
    if num_outputs > 1:
        if num_outputs > 1:
            answer: list[str] = [x.message.content for x in response.choices]
        else:
            answer: str = response.choices[0].message.content


    return answer

class Item(BaseModel):
    data: Dict[str, str]

@app.post("/")
async def create_item(item: Item):
    open = item.data
    answer = generate_from_openai_chat_completion(
        open.messages,
        open.model,
        open.temperture,
        open.max_tokens,
        open.top_k,
        open.context_length,
        open.stop_token,
        open.num_outputs
    )
    return {"answer": answer}

# 如果你使用的是命令行启动，确保你有 uvicorn 安装。
# 启动命令：uvicorn main:app --reload
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
