import asyncio
import logging

from my_modules.self_logging import MyLogger
from sql_scheme.connection import connectionObject

my_logger = MyLogger(log_level=logging.INFO)
logger = my_logger.get_logger()


# general comment -commit is extremely important because it save the changes to the db

# TODO : handle connect.close (meanwhile it is close because it cause many problems)

# insert one row
async def general_insert(my_query, *args):
    try:
        with connectionObject.cursor() as cursor:
            values = args
            cursor.execute(
                my_query, values)
            connectionObject.commit()
            res = cursor.lastrowid
            return res
    except Exception as e:
        # TODO: replace with log instead
        logger.error(f"error in inserting one row on {my_query} and {args} ")
        connectionObject.rollback()
        return False
    # finally:
    #     print("finish")
    #     connectionObject.close()


# insert multi rows
async def general_insert_many(my_query, lst_of_tuples):
    try:
        with connectionObject.cursor() as cursor:
            _id = cursor.executemany(my_query, lst_of_tuples)
        connectionObject.commit()
        print("Multiple rows inserted successfully.")
        return True
    except Exception as e:
        connectionObject.rollback()
        logger.error(f"error in inserting to {my_query} values {lst_of_tuples}")
        return False

    # finally:
    #     connectionObject.close()


async def general_get_all(my_query):
    try:
        with connectionObject.cursor() as cursor:
            cursor.execute(my_query)
            all_rows = cursor.fetchall()
            return all_rows

    except Exception as e:
        logger.error(f"error in get all {my_query}")
        return False
    # finally:
    #     connectionObject.close()


async def get_row_by_condition(my_query, condition):
    try:
        with connectionObject.cursor() as cursor:
            # case multi conditions
            if not isinstance(condition, int):
                if len(condition) > 1:
                    cursor.execute(my_query, condition)
            else:
                cursor.execute(my_query, (condition,))
            data = cursor.fetchone()
            return data  # Returns a dictionary representing the user's data, or None if user_name doesn't exist
    except Exception as e:
        logger.error(f"error in get a row by condition {my_query}")
        return False
    # finally:
    #     connectionObject.close()


async def general_get_multi_row_by_condition(my_query, conditions):
    try:
        with connectionObject.cursor() as cursor:
            if not isinstance(conditions, int):
                if len(conditions) > 1:
                    cursor.execute(my_query, conditions)
            else:
                cursor.execute(my_query, (conditions,))
            data = cursor.fetchall()
            return data
    except Exception as e:
        logger.error(f"error in get multi rows by condition {conditions} and the query {my_query}")
        print("Error occurred:", e)
        return False
    # finally:
    #     connectionObject.close()


async def general_delete_data(my_query):
    try:
        with connectionObject.cursor() as cursor:
            cursor.execute(my_query)
        connectionObject.commit()
        print("All rows deleted successfully.")
        return True
    except Exception as e:
        connectionObject.rollback()
        logger.error(f"error in delete data from {my_query}")
        return False

# asyncio.run(general_delete_data("DELETE FROM device"))
# print(asyncio.run(general_get_all("SELECT * FROM device")))

# print(asyncio.run(general_get_multi_row_by_condition("SELECT * FROM connection WHERE connection.network_id=%s",11)))
