from typing import List, Optional
from Actors.Actor_Main import ActorMain


class Room:
    """
    Represents a room in the school environment.
    A room can contain actors (students/staff), items, and exits to other rooms.
    """

    def __init__(self, name: str, description: str, actors: Optional[List[ActorMain]] = None):
        self.name = name
        self.description = description

        # Who is inside the room?
        self.actors = actors if actors is not None else []

        # Items located in the room
        self.items: List[str] = []

        # Dictionary of exits: {"north": <Room>, "south": <Room>}
        self.exits: dict[str, "Room"] = {}

        print(f"Room '{self.name}' created.")

    # -------------------------------------------------------
    # Actor management
    # -------------------------------------------------------

    def add_actor(self, actor: ActorMain):
        """Place an actor (student/staff) into the room."""
        self.actors.append(actor)
        actor.location = self.name

    def remove_actor(self, actor: ActorMain):
        """Remove an actor from the room."""
        if actor in self.actors:
            self.actors.remove(actor)

    # -------------------------------------------------------
    # Item management
    # -------------------------------------------------------

    def add_item(self, item: str):
        """Add an item to the room."""
        self.items.append(item)

    def remove_item(self, item: str):
        """Remove an item from the room."""
        if item in self.items:
            self.items.remove(item)

    # -------------------------------------------------------
    # Room linking
    # -------------------------------------------------------

    def add_exit(self, direction: str, target_room: "Room"):
        """Link this room to another room with a direction."""
        self.exits[direction] = target_room

    def get_exit(self, direction: str):
        """Return the room in the given direction, if it exists."""
        return self.exits.get(direction)

    # -------------------------------------------------------
    # Debug / String output
    # -------------------------------------------------------

    def __str__(self):
        return (
            f"Room: {self.name}\n"
            f"Description: {self.description}\n"
            f"Actors: {[a.name for a in self.actors]}\n"
            f"Items: {self.items}\n"
            f"Exits: {list(self.exits.keys())}\n"
        )
