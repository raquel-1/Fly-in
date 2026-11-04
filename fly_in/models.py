from dataclasses import dataclass
from enum import Enum


class ZoneType(Enum):
    """Types of zones available in the drone network"""
    NORMAL = "normal"
    BLOCKED = "blocked"
    RESTRICTED = "restricted"
    PRIORITY = "priority"


@dataclass
class Zone:
    """A hub in the drone network"""
    name: str
    x: int
    y: int
    zone_type: ZoneType = ZoneType.NORMAL
    color: str | None = None
    max_drones: int = 1
    is_start: bool = False
    is_end: bool = False

    def move_cost(self) -> int:
        """Turns needed to enter this zone"""
        if self.zone_type == ZoneType.RESTRICTED:
            return 2
        return 1


@dataclass
class Connection:
    """Bidirectional link between two zones"""
    zone_a: str
    zone_b: str
    max_link_capacity: int = 1
