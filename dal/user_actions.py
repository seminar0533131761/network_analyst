from connection import connectionObject

try:
    with connectionObject.cursor() as cursor:
        user_name = "chani"
        hashed_password = "$2b$12$.X4X85HuA0mLzsrClKknOuSLsXeB93usqiKsR3WXynVfCIb0a1fAq"
        phone = "0533131761"
        email = "chani0533131761@gmail.com"

        values = (user_name, hashed_password, phone, email)
        insert_res = cursor.execute(
            "INSERT INTO users (user_name, hashed_password, phone, email) VALUES (%s, %s, %s, %s)", values)
        print(insert_res)
except Exception as e:
    print(e)
    connectionObject.rollback()
else:
    print('success')
    connectionObject.commit()
finally:
    connectionObject.close()
