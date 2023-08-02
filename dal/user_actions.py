import asyncio

from dal.crud_action import general_insert, general_get_all, get_row_by_condition


# TODO: decorator for errors and for logging's

async def insert(query, user_name, hashed_password, phone, email):
    return await general_insert(query, user_name, hashed_password, phone, email)


# the function returns all users on success and false on failed
async def get_all():
    query = "SELECT * FROM user"
    return await general_get_all(query)


async def get_by_user_name(user_name):
    query = "SELECT * FROM user WHERE user_name = %s"
    return await get_row_by_condition(query, user_name)

# res = asyncio.run(insert("INSERT INTO user (user_name, hashed_password, phone, email) VALUES (%s, %s, %s, %s)",
#                          "sari", "$2b$12$ethrNO82tOX32ZSK1jf5guiFTU46OVX.uCtfB2dSQN9Kgl5Upouui",
#                          "050", "sari@gmail.com"))
# # print(res)
# print(asyncio.run(general_get_all("SELECT * from user")))
# print(asyncio.run(get_by_user_name("bat")))
