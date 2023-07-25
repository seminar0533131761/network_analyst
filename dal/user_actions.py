import asyncio

from connection import connectionObject


async def insert_user():
    try:
        print('success')
        with connectionObject.cursor() as cursor:
            user_name = "chani"
            hashed_password = "$2b$12$.X4X85HuA0mLzsrClKknOuSLsXeB93usqiKsR3WXynVfCIb0a1fAq"
            phone = "0533131761"
            email = "chani0533131761@gmail.com"

            values = (user_name, hashed_password, phone, email)
            insert_res = cursor.execute(
                "INSERT INTO user (user_name, hashed_password, phone, email) VALUES (%s, %s, %s, %s)", values)
            print(insert_res)
    except Exception as e:
        print(e)
        connectionObject.rollback()
        return False
    else:
        print('success')
        connectionObject.commit()
        return
    finally:
        print("got to final")
        connectionObject.close()


async def get_all_users():
    try:
        with connectionObject.cursor() as cursor:
            sql_query = "SELECT * FROM user"
            cursor.execute(sql_query)
            # Fetch all rows
            all_users = cursor.fetchall()
            for user in all_users:
                print(user)  # This will print each user's details as a dictionary
            # return all_users

    except Exception as e:
        print("Error occurred:", e)
        return False
    else:
        print('success')
        connectionObject.commit()
        return True

    finally:
        connectionObject.close()


asyncio.run(get_all_users())
