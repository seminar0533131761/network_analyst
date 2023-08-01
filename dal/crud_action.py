import asyncio

from dal.connection import connectionObject


# general comment commit is extremely important because it save the changes to the db
# TODO : handle connect.close (meanwhile it is close because it cause many problems)
# insert one row
async def general_insert(my_query, *args):
    print(args)
    try:
        with connectionObject.cursor() as cursor:
            print("args in general insert :", args)
            values = args
            cursor.execute(
                my_query, values)
            connectionObject.commit()
            res = cursor.lastrowid
            print("res in general", res)
            return res
    except Exception as e:
        # TODO: replace with log instead
        print(e)
        connectionObject.rollback()
        return False
    # finally:
    #     print("finish")
    #     connectionObject.close()


# insert multi rows
async def general_insert_many(my_query, lst_of_tuples):
    print("general insert first")
    try:
        print("got to general insert many ", lst_of_tuples[:2])
        with connectionObject.cursor() as cursor:
            _id = cursor.executemany(my_query, lst_of_tuples)
            print("last_id", _id)
        connectionObject.commit()
        print("Multiple rows inserted successfully.")
        return True
    except Exception as e:
        connectionObject.rollback()
        print(f"Error: {e}")
        return False

    # finally:
    #     connectionObject.close()


async def general_get_all(my_query):
    try:
        with connectionObject.cursor() as cursor:

            cursor.execute(my_query)
            all_rows = cursor.fetchall()
            print(all_rows)
            return all_rows

    except Exception as e:
        print("Error occurred:", e)
        return False
    # finally:
    #     connectionObject.close()


async def get_row_by_condition(my_query, condition):
    try:
        with connectionObject.cursor() as cursor:
            print("query: ", my_query)
            print("condition: ", condition)
            cursor.execute(my_query, condition)
            data = cursor.fetchone()
            print("data: ", data)
            return data  # Returns a dictionary representing the user's data, or None if user_name doesn't exist
    except Exception as e:
        print("Error occurred:", e)
        return False
    # finally:
    #     connectionObject.close()


async def general_get_multi_row_by_condition(my_query, condition):
    try:
        with connectionObject.cursor() as cursor:
            cursor.execute(my_query, (condition,))
            data = cursor.fetchall()
            return data  # Returns a dictionary representing the user's data, or None if user_name doesn't exist
    except Exception as e:
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
        print(f"Error: {e}")
        return False


# asyncio.run(general_delete_data("DELETE FROM device"))
# print(asyncio.run(general_get_all("SELECT * FROM device")))

# print(asyncio.run(general_get_multi_row_by_condition("SELECT * FROM connection WHERE connection.network_id=%s",11)))
