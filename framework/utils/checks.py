import requests


class CommonCheckers:

    # Status code checkers

    @staticmethod
    def check_status_code(response: requests.Response, expected_code: int):
        """
        :param response: requests.Response
        :param expected_code: status code
        """
        error_message = f"Actual status code '{response.status_code}' not equal expected status code '{expected_code}'"
        assert response.status_code == expected_code, error_message

    def check_status_code_200(self, response):
        self.check_status_code(response=response, expected_code=200)

    def check_status_code_201(self, response):
        self.check_status_code(response=response, expected_code=201)

    def check_status_code_400(self, response):
        self.check_status_code(response=response, expected_code=400)

    def check_status_code_401(self, response):
        self.check_status_code(response=response, expected_code=401)
