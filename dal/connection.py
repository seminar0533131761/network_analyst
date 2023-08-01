import pymysql.cursors

dbServerName = "sql7.freesqldatabase.com"

dbUser = "sql7636747"

dbPassword = "nFdqlclL9B"

dbName = "sql7636747"

charSet = "utf8mb4"

cusrorType = pymysql.cursors.DictCursor

connectionObject = pymysql.connect(host=dbServerName, user=dbUser, password=dbPassword,

                                   db=dbName, charset=charSet, cursorclass=cusrorType)
