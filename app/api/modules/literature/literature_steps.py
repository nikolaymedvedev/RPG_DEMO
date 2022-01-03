from app.api.modules.literature.api_requests_literature import Literature
from framework.utils.checks import CommonCheckers


# add new literature
def add_literature(week_id: int, literature_title: str = None):
    literature = Literature().add_literature(week_id=week_id, literature_title=literature_title)
    CommonCheckers().check_status_code_201(response=literature)
    return literature


# delete literature
def delete_literature(literature_id: int):
    delete = Literature().delete_literature(literature_id=literature_id)
    CommonCheckers().check_status_code_201(response=delete)
    return delete
