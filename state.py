from typing import TypedDict, Annotated

class ImageDesciptionState(TypedDict):
    user_id : Annotated[str , "사용자 ID"]
    image_path : Annotated[str, "이미지 경로"]
    description : Annotated[str, "이미지 설명"]
    image_id : Annotated[int , "이미지 DB PK"]
    model_name : Annotated[str, "분석 LLM 모델 이름"]
    b64_image : Annotated[str, "이미지 Base64 인코딩 문자열"]

