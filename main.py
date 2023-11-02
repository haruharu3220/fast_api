from fastapi import FastAPI
from routers import route_todo
from schemas import SuccessMsg
#インスタンスの生成
app = FastAPI()
app.include_router(route_todo.router)

#エンドポイントのパスを定義
@app.get("/")
def root():
    return {"messeage":"Welcome to Fast API"}