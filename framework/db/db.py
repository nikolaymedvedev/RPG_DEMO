import psycopg2
from configs.config import get_data
from framework.logger.logger import Logger


def query(sql_query: str, module_name: str):
    logger = Logger.get_logger()
    try:
        db_config = get_data(file_name="db_config.json")[module_name]
        logger.debug(f"Try to connect to DB {db_config['POSTGRES_DB']}")
        with psycopg2.connect(dbname=db_config["POSTGRES_DB"],
                              user=db_config["POSTGRES_USER"],
                              password=db_config["POSTGRES_PASSWORD"],
                              host=db_config["POSTGRES_HOST"],
                              port=db_config["POSTGRES_PORT"]) as db_connection:
            logger.debug("Connection successfully established")
            cursor = db_connection.cursor()
            try:
                logger.debug(f"Execute SQL query: '{sql_query}'")
                cursor.execute(sql_query)
                db_response = cursor.fetchall()
                logger.debug(f"DB response: {db_response}")
                return db_response
            except psycopg2.ProgrammingError as error:
                logger.error(f"SQL query execution was unsuccessfully: {error.diag.message_primary}")
                raise
            finally:
                cursor.close()
    except psycopg2.OperationalError as error:
        logger.error(f"Operational error: {error}")
        raise
