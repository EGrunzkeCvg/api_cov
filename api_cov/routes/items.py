from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None


def _make_item(name, price, is_offer):
    return Item(name=name, price=price, is_offer=is_offer)


store = {
    1: _make_item("mouse", 50, False),
    2: _make_item("keyboard", 80, True),
}


@router.get("/item/{item_id}")
async def read_item(item_id: int):
    item = store.get(item_id, None)
    return item


@router.post("/item")
async def read_item(item_id: int, item: Item):
    if item_id in store:
        raise ValueError(f"Item ID {item_id} already exists")
    else:
        store[item_id] = item_id
        return item

