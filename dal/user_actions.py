import asyncio

from connection import connectionObject


# TODO decortor for errors and for loggings

# the function returns bool result rather success or failed
async def insert_user():
    try:
        print('success')
        with connectionObject.cursor() as cursor:
            user_name = "chani"
            hashed_password = "$2b$12$.X4X85HuA0mLzsrClKknOuSLsXeB93usqiKsR3WXynVfCIb0a1fAq"
            phone = "0533131761"
            email = "chani0533131761@gmail.com"

            values = (user_name, hashed_password, phone, email)
            cursor.execute(
                "INSERT INTO user (user_name, hashed_password, phone, email) VALUES (%s, %s, %s, %s)", values)
            connectionObject.commit()
            return True
    except Exception as e:
        print(e)
        connectionObject.rollback()
        return False

    finally:
        print("got to final")
        connectionObject.close()


# the function returns all users on success and false on failed
async def get_all_users():
    try:
        with connectionObject.cursor() as cursor:
            sql_query = "SELECT * FROM user"
            cursor.execute(sql_query)
            # all_users is list of dict
            all_users = cursor.fetchall()
            connectionObject.commit()
            return all_users

    except Exception as e:
        print("Error occurred:", e)
        return False
    finally:
        connectionObject.close()


print(asyncio.run(get_all_users()))
