from app.api.helpers.laborants import get_random_direction_name, get_random_number
from framework.api.api_requests import get, post, put, delete
from configs.config import get_data


class Programs:

    def __init__(self):
        self.base_url = get_data(file_name="browser_config.json")["base_url_programs"]
        self.url_weeks_of_program = "/weeks/"
        self.url_tasks_of_program = "/tasks/"

    def get_all_programs(self, headers: dict = None):
        """
        :return: requests.Response
        """
        response = get(url=f"{self.base_url}", headers=headers)
        return response

    def add_program(self, program_name: str = None, duration: int = None, testsQty: int = None, headers: dict = None):
        """
        :param testsQty: number of tests
        :param duration: duration in days
        :param program_name: the name of the new direction
        :param headers: request headers
        """
        title = get_random_direction_name()
        if program_name:
            title = program_name
        duration_number = get_random_number()
        if duration:
            duration_number = duration
        tests = get_random_number()
        if testsQty:
            tests = testsQty
        response = post(url=f"{self.base_url}",
                        json={"title": title,
                              "duration": duration_number,
                              "testsQty": tests},
                        headers=headers)
        return response

    def update_program(self, program_id: int, new_program_name: str = None,
                       new_duration: int = None, new_testsQty: int = None,
                       headers: dict = None):
        """
        :param program_id: the id of the new program
        :param new_program_name: new program name
        :param new_duration: new duration in days
        :param new_testsQty: new number of tests
        :param headers: request headers
        :return: requests.Response
        """
        new_title = get_random_direction_name()
        if new_program_name:
            new_title = new_program_name
        new_duration_number = get_random_number()
        if new_duration:
            new_duration_number = new_duration
        new_tests = get_random_number()
        if new_testsQty:
            new_tests = new_testsQty
        response = put(url=f"{self.base_url}{program_id}",
                       json={"title": new_title,
                             "duration": new_duration_number,
                             "testsQty": new_tests},
                       headers=headers)
        return response

    def get_program_by_id(self, program_id: int, headers: dict = None):
        """
        :param headers: request headers
        :param program_id: the id of the program
        :return: requests.Response
        """
        response = get(url=f"{self.base_url}{program_id}", headers=headers)
        return response

    def delete_program_by_id(self, program_id: int, headers: dict = None):
        """
        :param program_id: id of the direction
        :param headers: request headers
        :return: requests.Response
        """
        response = delete(url=f"{self.base_url}{program_id}/", headers=headers)
        return response

    def get_all_weeks_of_program(self, program_id: int):
        """
        :param program_id: id program
        :return: all weeks of the program
        """
        response = get(url=f"{self.base_url}{program_id}{self.url_weeks_of_program}")
        return response

    def get_all_tasks_of_program(self, program_id: int):
        """
        :param program_id: id program
        :return: all tasks of the program
        """
        response = get(url=f"{self.base_url}{program_id}{self.url_tasks_of_program}")
        return response

    def get_week_by_program_id_and_number(self, program_id: int, week_number: int):
        """
        :param program_id: id program
        :param week_number: the number of the week we want to watch
        :return: A certain week by its number in a certain program
        """
        response = get(url=f"{self.base_url}{program_id}/{week_number}{self.url_weeks_of_program}")
        return response
