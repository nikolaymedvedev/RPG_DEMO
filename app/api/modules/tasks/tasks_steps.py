from app.api.modules.tasks.api_requests_tasks import Tasks
from framework.utils.checks import CommonCheckers


# view the task by its id
def get_task_by_id(task_id: int, headers: dict = None):
    task = Tasks().get_task_by_id(task_id=task_id, headers=headers)
    CommonCheckers().check_status_code_200(response=task)
    return task


# creating a new task
def create_new_task(weekID: int, title: str = None, description: str = None,
                    deadline: str = None, timeSpent: int = None, priority: str = None,
                    status: str = None, headers: dict = None):
    task = Tasks().create_task(weekID=weekID, title=title, description=description,
                               deadline=deadline, timeSpent=timeSpent, priority=priority,
                               status=status, headers=headers)
    CommonCheckers().check_status_code_201(response=task)
    return task


# updating a task
def update_task(task_id: int, weekID: int, title: str = None, description: str = None,
                deadline: str = None, timeSpent: int = None, priority: str = None,
                status: str = None, headers: dict = None):
    new_task = Tasks().update_task(task_id=task_id, weekID=weekID, title=title, description=description,
                                   deadline=deadline, timeSpent=timeSpent, priority=priority,
                                   status=status, headers=headers)
    CommonCheckers().check_status_code_200(response=new_task)
    return new_task


# deleting a task by id
def delete_new_task_by_id(task_id: int, headers: dict = None):
    delete = Tasks().delete_task_by_id(task_id=task_id, headers=headers)
    CommonCheckers().check_status_code_200(response=delete)
    return delete
