from connection import connectionObject

try:
    cursorObject = connectionObject.cursor()
    user_table = """CREATE TABLE user (
      id int PRIMARY KEY AUTO_INCREMENT,
      user_name VARCHAR(255),
      hashed_password VARCHAR(255),
      phone VARCHAR(255),
      email VARCHAR(255)
    )
    """

    cursorObject.execute(user_table)

    sqlQuery = "show tables"

    cursorObject.execute(sqlQuery)

    rows = cursorObject.fetchall()

    for row in rows:
        print(row)

except Exception as e:

    print("Exeception occured:{}".format(e))

finally:

    connectionObject.close()
