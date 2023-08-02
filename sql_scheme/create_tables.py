import asyncio

from connection import connectionObject


async def table_creator():
    try:
        cursorObject = connectionObject.cursor()
        db_tables = """CREATE TABLE connection (
  src_id VARCHAR(255),
  dest_id VARCHAR(255),
  network_id int,
  protocol_type VARCHAR(255),
  FOREIGN KEY(src_id) REFERENCES device(id),
  FOREIGN KEY(dest_id) REFERENCES device(id),
  FOREIGN KEY(network_id) REFERENCES network(id)
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
