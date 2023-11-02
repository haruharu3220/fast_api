from pydantic import BaseModel


#レスポンスが返すjsonの型を定義
class Todo(BaseModel):
    id: str
    title: str
    description: str


class TodoBody(BaseModel):
    title: str
    description: str


class SuccessMsg(BaseModel):
    message: str