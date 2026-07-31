from pydantic import BaseModel
from typing import List, Optional

class GestureResponse(BaseModel):
    which_hand: Optional[str]
    finger_statuses: List[int]
    raised_fingers: int
    action: Optional[str]
