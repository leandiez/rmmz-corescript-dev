"""
RPG Maker MZ Tools - Python wrapper for programmatic game creation
"""
import json
import os
import shutil
from typing import Dict, List, Any, Optional, Union
from pydantic import BaseModel, Field

class EventCommand(BaseModel):
    """Represents a single event command in RPG Maker MZ"""
    code: int
    parameters: List[Any] = Field(default_factory=list)
    indent: int = 0

class EventPage(BaseModel):
    """Represents a page in an event with conditions and commands"""
    conditions: Dict[str, Any] = Field(default_factory=dict)
    image: Dict[str, Any] = Field(default_factory=dict)
    move_type: int = 0
    move_speed: int = 3
    move_frequency: int = 3
    move_route: Dict[str, Any] = Field(default_factory=dict)
    walk_anime: bool = True
    step_anime: bool = False
    direction_fix: bool = False
    through: bool = False
    priority_type: int = 1
    trigger: int = 0  # 0=Action, 1=Player Touch, 2=Event Touch, 3=Autorun, 4=Parallel
    list: List[EventCommand] = Field(default_factory=list)

class MapEvent(BaseModel):
    """Represents an event on the map"""
    id: int
    name: str
    x: int
    y: int
    pages: List[EventPage] = Field(default_factory=list)

class MapInfo(BaseModel):
    """Map metadata for the MapInfos.json file"""
    id: int
    name: str
    expanded: bool = True
    order: int
    parent_id: int = 0
    scroll_x: int = 0
    scroll_y: int = 0

class Tileset(BaseModel):
    """Represents a tileset definition"""
    id: int
    name: str
    mode: int = 1
    tilesetNames: List[str] = Field(default_factory=list)
    flags: List[int] = Field(default_factory=list)

class Actor(BaseModel):
    """Represents a game character/actor"""
    id: int
    name: str
    nickname: str = ""
    class_id: int = 1
    initial_level: int = 1
    max_level: int = 99
    profile: str = ""
    equips: List[int] = Field(default_factory=list)

class Class(BaseModel):
    """Represents a character class"""
    id: int
    name: str
    exp_params: List[int] = Field(default_factory=list)
    params: List[List[int]] = Field(default_factory=list)
    traits: List[Dict[str, Any]] = Field(default_factory=list)
    learnings: List[Dict[str, Any]] = Field(default_factory=list)

class Skill(BaseModel):
    """Represents a skill that can be used by actors"""
    id: int
    name: str
    description: str = ""
    icon_index: int = 0
    mp_cost: int = 0
    tp_cost: int = 0
    message1: str = ""
    message2: str = ""
    scope: int = 0  # Target scope (0=None, 1=1 Enemy, etc.)
    occasion: int = 0  # When usable (0=Always, 1=Battle, 2=Menu, 3=Never)
    speed: int = 0
    success_rate: int = 100
    hit_type: int = 0  # (0=Certain, 1=Physical, 2=Magical)
    damage_type: int = 0  # (0=None, 1=HP damage, 2=MP damage, etc.)
    element_id: int = 0
    formula: str = "0"
    effects: List[Dict[str, Any]] = Field(default_factory=list)

class RPGMakerTools:
    """Tools for interacting with RPG Maker MZ data programmatically"""
    
    def __init__(self, project_path: str):
        """Initialize with path to RPG Maker MZ project"""
        self.project_path = project_path
        self.data_path = os.path.join(project_path, "data")
        
        # Ensure data directory exists
        if not os.path.exists(self.data_path):
            raise ValueError(f"Data directory not found at {self.data_path}")
        
        # Load common data files
        self._load_data()
    
    def _load_data(self):
        """Load essential data files"""
        # System data
        self.system = self._load_json("System.json")
        
        # Map info
        self.map_infos = self._load_json("MapInfos.json")
        
        # Database files
        self.actors = self._load_json("Actors.json")
        self.classes = self._load_json("Classes.json")
        self.skills = self._load_json("Skills.json")
        self.items = self._load_json("Items.json")
        self.weapons = self._load_json("Weapons.json")
        self.armors = self._load_json("Armors.json")
        self.enemies = self._load_json("Enemies.json")
        self.troops = self._load_json("Troops.json")
        self.states = self._load_json("States.json")
        self.animations = self._load_json("Animations.json")
        self.tilesets = self._load_json("Tilesets.json")
        self.common_events = self._load_json("CommonEvents.json")
        
    def _load_json(self, filename: str) -> Dict[str, Any]:
        """Load a JSON file from the data directory"""
        filepath = os.path.join(self.data_path, filename)
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Warning: {filename} not found, returning empty dict")
            return {}
        except json.JSONDecodeError:
            print(f"Warning: {filename} is not valid JSON, returning empty dict")
            return {}
    
    def _save_json(self, data: Dict[str, Any], filename: str) -> bool:
        """Save data to a JSON file in the data directory"""
        filepath = os.path.join(self.data_path, filename)
        try:
            # Create backup
            if os.path.exists(filepath):
                backup_path = filepath + ".bak"
                shutil.copy2(filepath, backup_path)
            
            # Save file
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            return True
        except Exception as e:
            print(f"Error saving {filename}: {e}")
            return False
    
    # Map Management Tools
    
    def get_map(self, map_id: int) -> Dict[str, Any]:
        """Get map data by ID"""
        map_file = f"Map{map_id:03d}.json"
        return self._load_json(map_file)
    
    def create_map(self, name: str, width: int, height: int, tileset_id: int) -> int:
        """Create a new map and return its ID"""
        # Find next available map ID
        map_ids = [info.get('id', 0) for info in self.map_infos.values() if isinstance(info, dict)]
        next_id = max(map_ids) + 1 if map_ids else 1
        
        # Create map info entry
        self.map_infos[str(next_id)] = {
            "id": next_id,
            "name": name,
            "expanded": True,
            "order": next_id,
            "parentId": 0,
            "scrollX": 0,
            "scrollY": 0
        }
        
        # Create basic map data
        map_data = {
            "autoplayBgm": False,
            "autoplayBgs": False,
            "battleback1Name": "",
            "battleback2Name": "",
            "bgm": {"name": "", "pan": 0, "pitch": 100, "volume": 90},
            "bgs": {"name": "", "pan": 0, "pitch": 100, "volume": 90},
            "disableDashing": False,
            "displayName": "",
            "encounterList": [],
            "encounterStep": 30,
            "height": height,
            "note": "",
            "parallaxLoopX": False,
            "parallaxLoopY": False,
            "parallaxName": "",
            "parallaxShow": True,
            "parallaxSx": 0,
            "parallaxSy": 0,
            "scrollType": 0,
            "specifyBattleback": False,
            "tilesetId": tileset_id,
            "width": width,
            "data": [0] * (width * height * 6),  # 6 layers of map data
            "events": {}
        }
        
        # Save map data and map info
        self._save_json(map_data, f"Map{next_id:03d}.json")
        self._save_json(self.map_infos, "MapInfos.json")
        
        return next_id
    
    def create_event(self, map_id: int, name: str, x: int, y: int, pages: List[EventPage] = None) -> int:
        """Create a new event on a map and return its ID"""
        # Load map
        map_data = self.get_map(map_id)
        if not map_data:
            raise ValueError(f"Map {map_id} not found")
        
        # Find next available event ID
        events = map_data.get("events", {})
        event_ids = [int(k) for k in events.keys() if k != "null" and k is not None]
        next_id = max(event_ids) + 1 if event_ids else 1
        
        # Default page if none provided
        if not pages:
            pages = [EventPage(
                conditions={
                    "actorId": 1,
                    "actorValid": False,
                    "itemId": 1,
                    "itemValid": False,
                    "selfSwitchCh": "A",
                    "selfSwitchValid": False,
                    "switch1Id": 1,
                    "switch1Valid": False,
                    "switch2Id": 1,
                    "switch2Valid": False,
                    "variableId": 1,
                    "variableValid": False,
                    "variableValue": 0
                },
                image={
                    "characterIndex": 0,
                    "characterName": "",
                    "direction": 2,
                    "pattern": 1,
                    "tileId": 0
                },
                list=[
                    EventCommand(code=0, parameters=[])  # End event
                ]
            )]
        
        # Create event
        event_data = {
            "id": next_id,
            "name": name,
            "note": "",
            "pages": [page.dict() for page in pages],
            "x": x,
            "y": y
        }
        
        # Add to map
        events[str(next_id)] = event_data
        map_data["events"] = events
        
        # Save map
        self._save_json(map_data, f"Map{map_id:03d}.json")
        
        return next_id
    
    # Character System Tools
    
    def create_actor(self, name: str, class_id: int, initial_level: int = 1) -> int:
        """Create a new actor/character and return their ID"""
        # Find next available actor ID
        actor_ids = [actor.get('id', 0) for actor in self.actors if isinstance(actor, dict)]
        next_id = max(actor_ids) + 1 if actor_ids else 1
        
        # Create actor data
        actor_data = {
            "id": next_id,
            "name": name,
            "nickname": "",
            "classId": class_id,
            "initialLevel": initial_level,
            "maxLevel": 99,
            "characterName": "",
            "characterIndex": 0,
            "faceName": "",
            "faceIndex": 0,
            "battlerName": "",
            "equips": [0, 0, 0, 0, 0],
            "profile": "",
            "traits": [],
            "meta": {}
        }
        
        # Add to actors array
        self.actors.append(actor_data)
        
        # Save actors
        self._save_json(self.actors, "Actors.json")
        
        return next_id
    
    def create_class(self, name: str) -> int:
        """Create a new character class and return its ID"""
        # Find next available class ID
        class_ids = [cls.get('id', 0) for cls in self.classes if isinstance(cls, dict)]
        next_id = max(class_ids) + 1 if class_ids else 1
        
        # Create class data with default parameters
        class_data = {
            "id": next_id,
            "name": name,
            "expParams": [30, 20, 30, 30],  # Base, Extra, Acceleration, Growth
            "traits": [],
            "learnings": [],  # Skills learned
            "params": [[1, 1, 1, 1, 1, 1, 1, 1]] * 100,  # Stats progression (simplified)
            "meta": {}
        }
        
        # Add to classes array
        self.classes.append(class_data)
        
        # Save classes
        self._save_json(self.classes, "Classes.json")
        
        return next_id
    
    # Battle System Tools
    
    def create_skill(self, name: str, description: str, mp_cost: int, damage_type: int, 
                     formula: str, icon_index: int = 0) -> int:
        """Create a new skill and return its ID"""
        # Find next available skill ID
        skill_ids = [skill.get('id', 0) for skill in self.skills if isinstance(skill, dict)]
        next_id = max(skill_ids) + 1 if skill_ids else 1
        
        # Create skill data
        skill_data = {
            "id": next_id,
            "name": name,
            "description": description,
            "iconIndex": icon_index,
            "mpCost": mp_cost,
            "tpCost": 0,
            "message1": "%1 uses %2!",
            "message2": "",
            "requiredWtypeId1": 0,
            "requiredWtypeId2": 0,
            "scope": 1,  # Single enemy
            "occasion": 1,  # Battle only
            "speed": 0,
            "successRate": 100,
            "hitType": 1,  # Physical
            "animationId": 1,
            "damage": {
                "critical": True,
                "elementId": 0,
                "formula": formula,
                "type": damage_type,
                "variance": 20
            },
            "effects": [],
            "note": "",
            "meta": {}
        }
        
        # Add to skills array
        self.skills.append(skill_data)
        
        # Save skills
        self._save_json(self.skills, "Skills.json")
        
        return next_id
    
    def create_enemy(self, name: str, max_hp: int, attack: int, defense: int, 
                     gold: int, exp: int) -> int:
        """Create a new enemy and return its ID"""
        # Find next available enemy ID
        enemy_ids = [enemy.get('id', 0) for enemy in self.enemies if isinstance(enemy, dict)]
        next_id = max(enemy_ids) + 1 if enemy_ids else 1
        
        # Create enemy data
        enemy_data = {
            "id": next_id,
            "name": name,
            "battlerName": "",
            "battlerHue": 0,
            "exp": exp,
            "gold": gold,
            "params": [max_hp, 0, attack, defense, 0, 0, 0, 0],  # HP, MP, ATK, DEF, MAT, MDF, AGI, LUK
            "traits": [],
            "actions": [
                {
                    "conditionParam1": 0,
                    "conditionParam2": 0,
                    "conditionType": 0,
                    "rating": 5,
                    "skillId": 1  # Basic attack
                }
            ],
            "dropItems": [
                {"dataId": 1, "denominator": 1, "kind": 0},
                {"dataId": 1, "denominator": 1, "kind": 0},
                {"dataId": 1, "denominator": 1, "kind": 0}
            ],
            "note": "",
            "meta": {}
        }
        
        # Add to enemies array
        self.enemies.append(enemy_data)
        
        # Save enemies
        self._save_json(self.enemies, "Enemies.json")
        
        return next_id
    
    # Event Command Tools
    
    def add_message_command(self, text: str, face_name: str = "", face_index: int = 0) -> EventCommand:
        """Create a message display command"""
        return EventCommand(
            code=101,  # Show Text
            parameters=[face_name, face_index, 0, 0, text]
        )
    
    def add_text_command(self, text: str) -> EventCommand:
        """Create a text continuation command"""
        return EventCommand(
            code=401,  # Additional Text Data
            parameters=[text]
        )
    
    def add_choice_command(self, choices: List[str], cancel_type: int = 0) -> List[EventCommand]:
        """Create a set of commands for showing choices"""
        commands = [
            EventCommand(
                code=102,  # Show Choices
                parameters=[choices, cancel_type]
            )
        ]
        
        # Add choice branches
        for i in range(len(choices)):
            commands.append(
                EventCommand(
                    code=402,  # When [choice]
                    parameters=[0, i]
                )
            )
            # Add end choice branch
            commands.append(
                EventCommand(
                    code=0,  # End Event Processing
                    parameters=[]
                )
            )
        
        # Add cancel branch if needed
        if cancel_type > 0:
            commands.append(
                EventCommand(
                    code=403,  # When Cancel
                    parameters=[]
                )
            )
            commands.append(
                EventCommand(
                    code=0,  # End Event Processing
                    parameters=[]
                )
            )
        
        return commands
    
    def add_change_variable_command(self, variable_id: int, operation: int, value: Any) -> EventCommand:
        """Create a command to change a variable
        operation: 0=Set, 1=Add, 2=Sub, 3=Mult, 4=Div, 5=Mod
        """
        return EventCommand(
            code=122,  # Change Variables
            parameters=[variable_id, variable_id, operation, 0, value]
        )
    
    def add_change_switch_command(self, switch_id: int, value: bool) -> EventCommand:
        """Create a command to change a switch"""
        return EventCommand(
            code=121,  # Change Switch
            parameters=[switch_id, switch_id, value and 0 or 1]
        )
    
    def add_conditional_branch(self, condition_type: int, param1: int, 
                               param2: int = 0) -> EventCommand:
        """Create a conditional branch command
        condition_type: 0=Switch, 1=Variable, 2=Self Switch, etc.
        """
        return EventCommand(
            code=111,  # Conditional Branch
            parameters=[condition_type, param1, param2]
        )
    
    def add_else_branch(self) -> EventCommand:
        """Create an else branch command"""
        return EventCommand(
            code=411,  # Else
            parameters=[]
        )
    
    def add_end_branch(self) -> EventCommand:
        """Create an end branch command"""
        return EventCommand(
            code=412,  # End Branch
            parameters=[]
        )
    
    # Helper Methods
    
    def get_common_event(self, event_id: int) -> Dict[str, Any]:
        """Get a common event by ID"""
        for event in self.common_events:
            if isinstance(event, dict) and event.get('id') == event_id:
                return event
        return None
    
    def create_common_event(self, name: str, trigger: int, commands: List[EventCommand]) -> int:
        """Create a common event with the given commands
        trigger: 0=None, 1=Autorun, 2=Parallel
        """
        # Find next available common event ID
        event_ids = [event.get('id', 0) for event in self.common_events if isinstance(event, dict)]
        next_id = max(event_ids) + 1 if event_ids else 1
        
        # Create common event data
        event_data = {
            "id": next_id,
            "name": name,
            "switchId": 1,
            "trigger": trigger,
            "list": [cmd.dict() for cmd in commands] + [{"code": 0, "parameters": []}]  # Add end event
        }
        
        # Add to common events array  
        self.common_events.append(event_data)
        
        # Save common events
        self._save_json(self.common_events, "CommonEvents.json")
        
        return next_id
