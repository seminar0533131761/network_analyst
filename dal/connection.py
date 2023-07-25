import pymysql.cursors

dbServerName = "sql6.freesqldatabase.com"

dbUser = "sql6635065"

dbPassword = "6laeqv8dZC"

dbName = "sql6635065"

charSet = "utf8mb4"

cusrorType = pymysql.cursors.DictCursor

connectionObject = pymysql.connect(host=dbServerName, user=dbUser, password=dbPassword,

                                   db=dbName, charset=charSet, cursorclass=cusrorType)
