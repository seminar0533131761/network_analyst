from fastapi import APIRouter, UploadFile, File, Request

from my_modules.parse_pcap import handle_file

router = APIRouter()


# only pcap files are expected otherwise many errors can be occurred
@router.post("/upload")
async def upload_pcap(request: Request, file: UploadFile = File(...)):
    # data is dict
    network_info = await request.json()
    file_content = await file.read()
    # network info is location and the client_id
    await handle_file(file_content, network_info)
    return {file.filename: "uploaded successfully"}
