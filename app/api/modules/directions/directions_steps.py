from framework.utils.checks import CommonCheckers
from app.api.modules.directions.api_requests_directions import Directions


# creating a new direction
def create_direction(headers: dict, direction_name: str = None, ):
    direction = Directions().add_direction(headers=headers, direction_name=direction_name)
    CommonCheckers().check_status_code_201(response=direction)
    return direction


# create invalid direction
def create_invalid_direction(headers: dict, direction_name: str = None, ):
    direction = Directions().add_direction(headers=headers, direction_name=direction_name)
    CommonCheckers().check_status_code_400(response=direction)
    return direction


# creating an existing direction
def create_existing_direction(headers: dict, direction_name: str = None, ):
    existing_direction = Directions().add_direction(headers=headers, direction_name=direction_name)
    CommonCheckers().check_status_code_400(response=existing_direction)
    return existing_direction


# delete direction by id
def delete_direction_by_id(direction_id: int, headers: dict):
    delete_direction = Directions().delete_direction_by_id(direction_id=direction_id, headers=headers)
    CommonCheckers().check_status_code_200(response=delete_direction)
    return delete_direction


# delete direction by name
def delete_direction_by_name(direction_name: str, headers: dict):
    delete_direction = Directions().delete_direction_by_name(direction_name=direction_name, headers=headers)
    CommonCheckers().check_status_code_200(response=delete_direction)
    return delete_direction


# update direction name
def update_direction(direction_id: int, new_direction_name: str = None, headers: dict = None):
    new_direction = Directions().update_direction(direction_id=direction_id,
                                                  new_direction_name=new_direction_name,
                                                  headers=headers
                                                  )
    CommonCheckers().check_status_code_200(response=new_direction)
    return new_direction
