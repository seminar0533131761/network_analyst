from fastapi import APIRouter, UploadFile, File, Form, Depends, Response

from dal.client_actions import is_client_connect_to_user
from dal.user_actions import get_by_user_name
from my_modules.handle_pcap import handle_file
from my_modules.module_authentication import User, get_current_active_user

router = APIRouter()


# only pcap files are expected otherwise many errors can be occurred
@router.post("/upload")
async def upload_pcap(file: UploadFile = File(...), client_id: int = Form(...), location: str = Form(...),
                      current_user: User = Depends(get_current_active_user)):
    client_in_user = is_client_connect_to_user(client_id, current_user["id"])
    if not client_in_user:
        return Response("no authorization", status_code=401)
    # data is dict
    user_id = await get_by_user_name(current_user["user_name"])
    network_info = {"location": location, "client_id": client_id, "user_id": user_id["id"]}
    file_content = await file.read()
    # network info is location and the client_id
    is_file_processed_successfully = await handle_file(file_content, network_info)
    if is_file_processed_successfully:
        return {file.filename: "uploaded successfully"}
    return {"sorry": "but the file could not be uploaded"}
