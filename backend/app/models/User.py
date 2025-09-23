from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional 

@dataclass
class User:
    user_id: int
    username: str
    email: str
    password_hash: str
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = None
    is_active: bool = True

    def to_dict(self) -> dict:
        return {
            "user_id": self.user_id,
            "username": self.username,
            "email": self.email,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
            "is_active": self.is_active,
        }
    
