from dal.client_actions import is_client_connect_to_user


async def check_permission(client_id, user_id):
    client_in_user = await is_client_connect_to_user(client_id, user_id)
    if not client_in_user:
        # TODO : log
        return "no authorization", 401
    return client_in_user
