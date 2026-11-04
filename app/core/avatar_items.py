# 쌀포인트 상점 "아바타" 탭에서 파는 아이템 목록.
# 그림이 프론트 코드(lib/avatar/hd.ts)에 있어서 DB가 아니라 여기서 관리하며,
# 프론트 lib/avatar/shopItems.ts와 id·slot을 반드시 맞춰야 한다. 가격은 이 값이 기준.
AVATAR_ITEMS: dict[str, dict] = {
    "outfit-jacket": {"name": "가죽 재킷 세트", "price": 3000, "slot": "outfit"},
    "hat-cap": {"name": "갈색 캡모자", "price": 2000, "slot": "hat"},
    "held-flowers": {"name": "빨간 꽃다발", "price": 1500, "slot": "held"},
}

# 착용 칸 — 칸마다 아이템 하나씩. 머리 모양은 무료라 칸이 아니다 (schemas/avatar.py의 hair)
AVATAR_ITEM_SLOTS = ("outfit", "hat", "held")
