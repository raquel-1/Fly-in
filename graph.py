from models import Zone, Connection, ZoneType


class Graph:
    """Network of zones and the connections between them"""

    def __init__(self) -> None:
        self._zones: dict[str, Zone] = {}
        self._connections: dict[str, Connection] = {}
        self._neighbors: dict[str, list[str]] = {}
        self._name_start_zone: str | None = None
        self._name_end_zone: str | None = None

    def add_zone(self, new_zone: Zone) -> None:
        """Add zone to map and update start/end if needed"""
        if new_zone.name in self._zones:
            raise ValueError(f"Duplicate zone name: {new_zone.name}")
        self._zones[new_zone.name] = new_zone
        self._neighbors[new_zone.name] = []

        if new_zone.is_start:
            self._name_start_zone = new_zone.name
        if new_zone.is_end:
            self._name_end_zone = new_zone.name

    def get_zone(self, name: str) -> Zone:
        """Returns a Zone object given name"""
        if name not in self._zones:
            raise KeyError(f"Zone '{name}' not exist in the map")
        return self._zones[name]

    def get_all_zones(self) -> list[Zone]:
        """Returns all zones(hubs) of map"""
        return list(self._zones.values())

    def add_connection(self, new_connection: Connection) -> None:
        """Add a bidirectional connection between two _zones"""
        name_a = new_connection.zone_a
        name_b = new_connection.zone_b

        if name_a not in self._zones or name_b not in self._zones:
            raise ValueError(
                f"Unknown zone in connection: {new_connection.name}"
            )
        if f"{name_a}-{name_b}" in self._connections:
            raise ValueError(f"Duplicate connection: {new_connection.name}")

        self._connections[f"{name_a}-{name_b}"] = new_connection
        self._connections[f"{name_b}-{name_a}"] = new_connection
        self._neighbors[name_a].append(name_b)
        self._neighbors[name_b].append(name_a)

    def get_connection(self, a: str, b: str) -> Connection:
        """Returns the connection between Zone A and Zone B"""
        conec_name = f"{a}-{b}"

        if conec_name not in self._connections:
            raise KeyError(f"Connection between '{a}' and '{b}' not exist")
        return self._connections[conec_name]

    def get_all_connections(self) -> list[Connection]:
        """Returns a list of all unique connections (no duplicates)"""
        unique_connections: list[Connection] = []

        for key, connection in self._connections.items():
            if key == connection.name:
                unique_connections.append(connection)
        return unique_connections

    def neighborhood(
            self, name: str, include_blocked: bool = False
    ) -> list[Zone]:
        """
        Returns the list of neighboring Zone objects
        if include_blocked == False, blocked hub not included
        """
        neighbors_name = self._neighbors[name]

        zone_objects: list[Zone] = []
        for n in neighbors_name:
            obj = self._zones[n]
            if not include_blocked and obj.zone_type == ZoneType.BLOCKED:
                continue
            zone_objects.append(obj)
        return zone_objects

    @property
    def start(self) -> Zone:
        """Property to directly get the starting hub"""
        if self._name_start_zone is None:
            raise ValueError("Start zone is not defined in the map")
        return self._zones[self._name_start_zone]

    @property
    def end(self) -> Zone:
        """Property to directly get the ending hub"""
        if self._name_end_zone is None:
            raise ValueError("End zone is not defined in the map")
        return self._zones[self._name_end_zone]
