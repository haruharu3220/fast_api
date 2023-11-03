from fastapi import APIRouter
from fastapi import Request,Response,HTTPException
from fastapi.encoders import jsonable_encoder
from schemas import Todo,TodoBody,SuccessMsg
from starlette.status import HTTP_201_CREATED
from database import db_create_todo,db_get_todos,db_update_todo,db_get_single_todo,db_delete_todo
from typing import List
router = APIRouter()


@router.post("/api/todo", response_model = Todo)
async def create_todo(request:Request,response: Response, data:TodoBody):
    todo = jsonable_encoder(data)
    res = await db_create_todo(todo)
    response.status_code = HTTP_201_CREATED
    if res:
        return res
    return HTTPException(
        status_code = 404, detail = "Could not create"
    )

@router.get("/api/todos",response_model=List[Todo])
async def get_todos():
    res = await db_get_todos()
    return res

@router.get("/api/todo/{id}",response_model=Todo)
async def get_single_todo(id:str):
    res = await db_get_single_todo(id)
    if res:
        return res
    raise HTTPException(
        #f=文字列と変数の結合を示す
        status_code=404, detail=f"Task of ID:{id} dosen't exist")

@router.put("/api/todo/{id}",response_model=Todo)
async def update_todo(id:str,data:TodoBody):
    todo = jsonable_encoder(data)
    res = await db_update_todo(id,todo)
    if res:
        return res
    raise HTTPException(
        status_code=404, detail=f"Task of ID:{id} dosen't exist")

@router.delete("/api/todo/{id}",response_model=SuccessMsg)
async def delete_todo(id:str):
    res = await db_delete_todo(id)
    if res:
        return {'message': 'Successfully deleted'}
    raise HTTPException(status_code=404, detail=f"Delete task failed")