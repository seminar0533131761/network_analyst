from fastapi import APIRouter, UploadFile, File, Depends

from my_modules.module_authentication import UserInDB, get_current_active_user
from my_modules.parse_pcap import handle_file

router = APIRouter()


# only pcap files are expected otherwise many errors can be occurred
@router.post("/upload")
async def upload_pcap(file: UploadFile = File(...)):
    # print(f"curren in cap upload {current_user}")
    file_content = await file.read()
    await handle_file(file_content)
    return {file.filename: "uploaded successfully"}
