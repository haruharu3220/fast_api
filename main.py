from fastapi import FastAPI

#インスタンスの生成
app = FastAPI()

#エンドポイントのパスを定義
@app.get("/")
def read_root():
    return {"messeage":"Welcome to Fast API"}