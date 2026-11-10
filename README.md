Design and implement an efficient drone routing system that navigates multiple autonomous drones from a central base to a target location through a dynamic network. This Python project challenges learners to create a custom pathfinding algorithm that handles simultaneous drone movement while respecting zone occupancy rules, movement costs, and conflict resolution. The system must parse complex map files, implement object-oriented design principles, and optimize for minimal simulation turns. Learners will develop skills in graph algorithms, concurrent pathfinding, and performance optimization while working with real-world constraints such as restricted zones, bottlenecks, and deadlock prevention.

---

### Technical Choice: `@dataclass` vs. Traditional Classes

In `models.py`, we purposely implemented Python's `@dataclass` for data-heavy structures (`Zone`, `Connection`, `Drone`) instead of writing traditional classes. 

#### Code Comparison:

**Traditional Class approach:**
```python
class Zone:
    def __init__(self, name: str, x: int, y: int, max_drones: int = 1):
        self.name = name
        self.x = x
        self.y = y
        self.max_drones = max_drones

    def __repr__(self) -> str:
        return f"Zone(name={self.name}, x={self.x}, y={self.y}, max_drones={self.max_drones})"
```

**`@dataclass` approach used in our project:**

```python
@dataclass
class Zone:
    name: str
    x: int
    y: int
    max_drones: int = 1
```

Why we chose `@dataclass`: 
 *Boilerplate Elimination.* It automatically generates the `__init__` constructor based on type annotations, drastically reducing repetitive self-assignment code (`self.x = x`).

