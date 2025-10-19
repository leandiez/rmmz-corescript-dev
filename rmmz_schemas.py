"""
RPG Maker MZ Schemas - Pydantic models for game data structures
"""
from typing import Dict, List, Any, Optional, Union
from pydantic import BaseModel, Field
from enum import Enum

# Enums for common types

class TriggerType(int, Enum):
    """Event trigger types"""
    ACTION_BUTTON = 0
    PLAYER_TOUCH = 1
    EVENT_TOUCH = 2
    AUTORUN = 3
    PARALLEL = 4

class DamageType(int, Enum):
    """Skill damage types"""
    NONE = 0
    HP_DAMAGE = 1
    MP_DAMAGE = 2
    HP_RECOVER = 3
    MP_RECOVER = 4
    HP_DRAIN = 5
    MP_DRAIN = 6

class ItemScope(int, Enum):
    """Item and skill target scopes"""
    NONE = 0
    ONE_ENEMY = 1
    ALL_ENEMIES = 2
    ONE_RANDOM_ENEMY = 3
    TWO_RANDOM_ENEMIES = 4
    THREE_RANDOM_ENEMIES = 5
    ONE_ALLY = 6
    ALL_ALLIES = 7
    ONE_ALLY_DEAD = 8
    ALL_ALLIES_DEAD = 9
    USER = 10
    ONE_ALLY_WEAPON_EQUIPPED = 11

class HitType(int, Enum):
    """Skill hit types"""
    CERTAIN = 0
    PHYSICAL = 1
    MAGICAL = 2

# Base Models

class GameMetadata(BaseModel):
    """Game metadata and basic settings"""
    title: str
    version: str = "1.0.0"
    creator: str = ""
    description: str = ""
    resolution: Dict[str, int] = {"width": 816, "height": 624}

class GameLocation(BaseModel):
    """Represents a location/map in the game"""
    id: Optional[int] = None
    name: str
    description: str = ""
    width: int = 20
    height: int = 15
    tileset_id: int = 1
    background_music: Optional[Dict[str, Any]] = None
    encounter_list: List[Dict[str, Any]] = Field(default_factory=list)
    encounter_rate: int = 30
    features: List[str] = Field(default_factory=list)
    notes: str = ""

class GameCharacter(BaseModel):
    """Represents a character in the game (player or NPC)"""
    id: Optional[int] = None
    name: str
    type: str = "npc"  # "player", "npc", "enemy"
    description: str = ""
    appearance: Dict[str, Any] = Field(default_factory=dict)
    class_id: Optional[int] = None
    level: int = 1
    stats: Dict[str, int] = Field(default_factory=dict)
    equipment: List[Dict[str, Any]] = Field(default_factory=list)
    skills: List[int] = Field(default_factory=list)
    personality: str = ""
    backstory: str = ""
    dialogue: Dict[str, List[str]] = Field(default_factory=dict)

class GameQuest(BaseModel):
    """Represents a quest in the game"""
    id: Optional[int] = None
    name: str
    description: str = ""
    objectives: List[str] = Field(default_factory=list)
    rewards: Dict[str, Any] = Field(default_factory=dict)
    start_location: Union[int, str] = ""
    prerequisite_quests: List[int] = Field(default_factory=list)
    prerequisite_conditions: Dict[str, Any] = Field(default_factory=dict)
    steps: List[Dict[str, Any]] = Field(default_factory=list)

class DialogueData(BaseModel):
    """Represents a dialogue interaction"""
    id: Optional[int] = None
    speaker: str
    text: List[str]
    face_name: str = ""
    face_index: int = 0
    choices: Optional[List[Dict[str, Any]]] = None
    condition: Optional[Dict[str, Any]] = None
    actions: Optional[List[Dict[str, Any]]] = None

class CutsceneData(BaseModel):
    """Represents a cutscene sequence"""
    id: Optional[int] = None
    name: str
    description: str = ""
    location: Union[int, str]
    actors: List[Dict[str, Any]] = Field(default_factory=list)
    sequences: List[Dict[str, Any]] = Field(default_factory=list)

class BattleEncounter(BaseModel):
    """Represents a battle encounter"""
    id: Optional[int] = None
    name: str = "Random Encounter"
    troop_id: Optional[int] = None
    enemies: List[Dict[str, Any]] = Field(default_factory=list)
    background: str = ""
    battle_events: List[Dict[str, Any]] = Field(default_factory=list)
    loot_table: List[Dict[str, Any]] = Field(default_factory=list)

# Game Data Schema - Top level container for all game data

class GameDataSchema(BaseModel):
    """Complete game data structure used by agents"""
    metadata: GameMetadata
    locations: List[GameLocation] = Field(default_factory=list)
    characters: List[GameCharacter] = Field(default_factory=list)
    quests: List[GameQuest] = Field(default_factory=list)
    dialogues: List[DialogueData] = Field(default_factory=list)
    cutscenes: List[CutsceneData] = Field(default_factory=list)
    battles: List[BattleEncounter] = Field(default_factory=list)
    variables: Dict[str, Dict[str, Any]] = Field(default_factory=dict)
    switches: Dict[str, Dict[str, Any]] = Field(default_factory=dict)
    
    class Config:
        arbitrary_types_allowed = True

# Agent State Schemas

class AgentTask(BaseModel):
    """Represents a task for an agent to perform"""
    id: str
    type: str  # "map_creation", "event_creation", "character_setup", etc.
    description: str
    priority: int = 1
    dependencies: List[str] = Field(default_factory=list)
    status: str = "pending"  # "pending", "in_progress", "completed", "failed"
    assigned_to: Optional[str] = None
    data: Dict[str, Any] = Field(default_factory=dict)
    result: Optional[Dict[str, Any]] = None

class AgentState(BaseModel):
    """Base state for all agents"""
    agent_id: str
    agent_type: str
    current_task: Optional[AgentTask] = None
    completed_tasks: List[str] = Field(default_factory=list)
    knowledge_base: Dict[str, Any] = Field(default_factory=dict)
    working_data: Dict[str, Any] = Field(default_factory=dict)

class DirectorAgentState(AgentState):
    """State for the director agent"""
    task_queue: List[AgentTask] = Field(default_factory=list)
    agent_assignments: Dict[str, List[str]] = Field(default_factory=dict)
    implementation_progress: Dict[str, float] = Field(default_factory=dict)

class WorldBuilderAgentState(AgentState):
    """State for the world builder agent"""
    maps_created: List[int] = Field(default_factory=list)
    maps_in_progress: Dict[int, float] = Field(default_factory=dict)
    location_interpretations: Dict[str, Dict[str, Any]] = Field(default_factory=dict)

class EventEngineerAgentState(AgentState):
    """State for the event engineer agent"""
    events_created: List[Dict[str, Any]] = Field(default_factory=list)
    dialogue_created: List[Dict[str, Any]] = Field(default_factory=list)
    cutscenes_created: List[Dict[str, Any]] = Field(default_factory=list)

class CombatSystemAgentState(AgentState):
    """State for the combat system agent"""
    skills_created: List[int] = Field(default_factory=list)
    enemies_created: List[int] = Field(default_factory=list)
    troops_created: List[int] = Field(default_factory=list)
    balance_metrics: Dict[str, Any] = Field(default_factory=dict)

class AssetManagerAgentState(AgentState):
    """State for the asset manager agent"""
    assets_required: Dict[str, List[str]] = Field(default_factory=dict)
    assets_available: Dict[str, List[str]] = Field(default_factory=dict)
    asset_mappings: Dict[str, str] = Field(default_factory=dict)

class TestingAgentState(AgentState):
    """State for the testing agent"""
    test_scenarios: List[Dict[str, Any]] = Field(default_factory=list)
    test_results: Dict[str, Dict[str, Any]] = Field(default_factory=dict)
    issues_found: List[Dict[str, Any]] = Field(default_factory=list)

# Workflow State Schema

class GameImplementationState(BaseModel):
    """Overall state for the game implementation process"""
    game_data: GameDataSchema
    director: DirectorAgentState
    world_builder: Optional[WorldBuilderAgentState] = None
    event_engineer: Optional[EventEngineerAgentState] = None
    combat_system: Optional[CombatSystemAgentState] = None
    asset_manager: Optional[AssetManagerAgentState] = None
    tester: Optional[TestingAgentState] = None
    
    current_stage: str = "planning"  # "planning", "implementation", "testing", "refinement"
    implementation_progress: float = 0.0
    log: List[Dict[str, Any]] = Field(default_factory=list)
    
    class Config:
        arbitrary_types_allowed = True
