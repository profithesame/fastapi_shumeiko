from typing import Annotated
from repository import TaskRepository
from fastapi import APIRouter, Depends, Body

from schemas import STask, STaskAdd, STaskId, OddEvenResponse, Number
from examples import odd_examples, odd_responses


router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"],
)


@router.post("")
async def add_task(
    task: Annotated[STaskAdd, Depends()],
) -> STaskId:
    task_id = await TaskRepository.add_one(task)
    return {
        'ok': True,
        'task_id': task_id
    }

@router.get("")
async def get_tasks() -> list[STask]:
    tasks = await TaskRepository.find_all()
    return tasks

#############################################
# Odd or even number
#############################################

router_number = APIRouter(
    prefix="/check_number",
    tags=["Numbers"],
)

@router_number.post(
    "",
    response_model=OddEvenResponse,
    responses=odd_responses)

async def check_number(
        number: Annotated[
            Number, Body(
                openapi_examples=odd_examples
            )
        ]
        ) -> OddEvenResponse:
    
    return OddEvenResponse(
        code=200,
        message="Success",
        result=number.value % 2)
