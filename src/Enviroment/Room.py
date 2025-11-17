from typing import Any, Dict, List, Optional

# A general-purpose room.
class Room:
    def __init__(self, name: str, description: str, actors: Optional[List[Any]] = None):
        self.name: str = name
        self.description: str = description
        self.actors: List[Any] = actors or []
        self.items: List[Any] = []
        self.exits: Dict[str, "Room"] = {}

    # Actor management
    def add_actor(self, actor: Any) -> None:
        if actor in self.actors:
            return
        self.actors.append(actor)

    def remove_actor(self, actor: Any) -> None:
        try:
            self.actors.remove(actor)
        except ValueError:
            raise ValueError("Actor not present in room")

    def list_actors(self) -> List[Any]:
        return list(self.actors)

# A classroom with a limited capacity.
class Classroom(Room):
    def __init__(self, capacity: int, actors: Optional[List[Any]] = None):
        super().__init__(name, description, actors)
        self.capacity = int(capacity)

    def add_actor(self, actor: Any) -> None:
        if len(self.actors) >= self.capacity:
            raise ValueError("Classroom is full")
        super().add_actor(actor)

    #TODO - Implement Room class
    print("Room class is under construction")
    