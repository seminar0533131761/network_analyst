from fastapi import APIRouter, UploadFile, File, Request, Form

from my_modules.parse_pcap import handle_file

router = APIRouter()


# only pcap files are expected otherwise many errors can be occurred
@router.post("/upload")
async def upload_pcap(file: UploadFile = File(...), client_id: int = Form(...), location: str = Form(...),
                      id: int = Form(...)):
    # data is dict
    network_info = {"location": location, "client_id": client_id, "id": id}
    file_content = await file.read()
    # network info is location and the client_id
    await handle_file(file_content, network_info)
    return {file.filename: "uploaded successfully"}
