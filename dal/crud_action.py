import pymysql

from dal.connection import connectionObject


# insert one row
async def general_insert(query, *args):
    try:
        with connectionObject.cursor() as cursor:
            values = args
            cursor.execute(
                query, values)
            # connectionObject.commit()
            return cursor.lastrowid
    except Exception as e:
        # TODO: replace with log instead
        print(e)
        connectionObject.rollback()
        return False
    finally:
        connectionObject.close()


async def general_insert_many(query, lst_of_tuples):
    try:
        with connectionObject.cursor() as cursor:
            cursor.executemany(query, lst_of_tuples)
        connectionObject.commit()
        print("Multiple rows inserted successfully.")
    except pymysql.Error as e:
        print(f"Error: {e}")
    finally:
        connectionObject.close()


async def general_get_all(query):
    try:
        with connectionObject.cursor() as cursor:

            cursor.execute(query)
            all_rows = cursor.fetchall()
            connectionObject.commit()
            return all_rows

    except Exception as e:
        print("Error occurred:", e)
        return False
    finally:
        connectionObject.close()


async def get_row_by_condition(query, condition):
    try:
        with connectionObject.cursor() as cursor:
            cursor.execute(query, (condition,))
            data = cursor.fetchone()
            connectionObject.commit()
            return data  # Returns a dictionary representing the user's data, or None if user_name doesn't exist
    except Exception as e:
        print("Error occurred:", e)
        return False
    # finally:
    #     connectionObject.close()


async def general_get_multi_row_by_condition(query, condition):
    try:
        with connectionObject.cursor() as cursor:
            cursor.execute(query, (condition,))
            data = cursor.fetchall()
            connectionObject.commit()
            return data  # Returns a dictionary representing the user's data, or None if user_name doesn't exist
    except Exception as e:
        print("Error occurred:", e)
        return False
    # finally:
    #     connectionObject.close()
