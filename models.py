from dataclasses import dataclass, field
from enum import Enum


class ZoneType(Enum):
    """Types of zones available in the drone network"""
    NORMAL = "normal"
    BLOCKED = "blocked"
    RESTRICTED = "restricted"
    PRIORITY = "priority"


class DroneState(Enum):
    """Types of states of the drone"""
    IN_ZONE = "in_zone"
    IN_TRANSIT = "in_transit"
    DELIVERED = "delivered"


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
class Drone:
    """A drone moving through the network"""
    drone_id: int
    zone: str
    state: DroneState = DroneState.IN_ZONE
    destination: str | None = None
    turns_left: int = 0
    path: list[str] = field(default_factory=list)

    @property
    def name(self) -> str:
        """
        dynamicaly generates the drone name
        based on its drone_id to avoid data redundancy
        and synchronization errors
        """
        return f"D{self.drone_id}"


@dataclass
class Connection:
    """Bidirectional link between two zones"""
    zone_a: str
    zone_b: str
    max_link_capacity: int = 1

    @property
    def name(self) -> str:
        """Return the connection name combining both zones"""
        return f"{self.zone_a}-{self.zone_b}"
