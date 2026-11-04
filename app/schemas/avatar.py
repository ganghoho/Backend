from typing import Literal, Optional
from pydantic import BaseModel, ConfigDict, Field

# 픽셀 캐릭터 설정 (v3). 그림은 프론트 lib/avatar/hd.ts에 있고, 여기는 무엇을 입었는지만 저장한다.
# 머리 모양은 무료, 옷·모자·손은 쌀포인트 상점 아이템 id (core/avatar_items.py).
# 예전 형식(v2)으로 저장된 값은 DB에 그대로 남아 있어도 되고, 프론트가 읽을 때 새 형식으로 바꿔 그린다.
class AvatarConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    v: Literal[3] = 3
    hair: Literal["buns", "short"]
    # 착용 아이템 — 보유한 아이템만 착용할 수 있다 (routers/user.py에서 확인)
    outfit: Optional[str] = Field(default=None, max_length=64)
    hat: Optional[str] = Field(default=None, max_length=64)
    held: Optional[str] = Field(default=None, max_length=64)


class AvatarItemResponse(BaseModel):
    item_id: str
    name: str
    price: int   # 쌀포인트
    slot: Literal["outfit", "hat", "held"]


class AvatarItemPurchaseResponse(BaseModel):
    item_id: str
    points_spent: int
    remaining_ssal_point: int
