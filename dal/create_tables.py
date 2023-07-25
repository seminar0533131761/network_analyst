import asyncio

from connection import connectionObject


async def table_creator():
    try:
        cursorObject = connectionObject.cursor()
        db_tables = """CREATE TABLE user (
          id int PRIMARY KEY AUTO_INCREMENT,
          user_name VARCHAR(255),
          hashed_password VARCHAR(255),
          phone VARCHAR(255),
          email VARCHAR(255)
        ),
        CREATE TABLE client (
          id INT PRIMARY KEY AUTO_INCREMENT,
          name VARCHAR(255),
          phone VARCHAR(255)
        ),
        CREATE TABLE network (
          id int PRIMARY KEY AUTO_INCREMENT,
          subnet_musk VARCHAR(255),
          client_id int,
          location VARCHAR(255),
          FOREIGN KEY(client_id) REFERENCES client(id)
        ),
        CREATE TABLE device (
          id VARCHAR(255) PRIMARY KEY,
          device_type VARCHAR(255),
          vendor VARCHAR(255),
          network_id int,
          ip_address VARCHAR(255),
          FOREIGN KEY(network_id) REFERENCES network(id)
        ),
        CREATE TABLE client_user (
          user_id int,
          client_id int,
          FOREIGN KEY(user_id) REFERENCES user(id),
          FOREIGN KEY(client_id) REFERENCES client(Id)
        ),
        CREATE TABLE connection (
          src_id VARCHAR(255),
          dest_id VARCHAR(255),
          FOREIGN KEY(src_id) REFERENCES device(id),
          FOREIGN KEY(dest_id) REFERENCES device(id)
        )
        """
        await cursorObject.execute(db_tables)

        sqlQuery = "show tables"

        cursorObject.execute(sqlQuery)

        rows = cursorObject.fetchall()

        for row in rows:
            print(row)

    except Exception as e:

        print("Exeception occured:{}".format(e))

    finally:
        connectionObject.close()
tables = asyncio.run(table_creator())