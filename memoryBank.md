# RPG Maker MZ - Memory Bank

This document serves as a comprehensive analysis of the RPG Maker MZ codebase to identify components that can be wrapped as tools for agentic workflows.

## rmmz_core Folder

The `rmmz_core` folder contains fundamental classes and utilities for the RPG Maker MZ engine. These form the foundation of the engine's functionality and provide essential services for rendering, input handling, data serialization, and more.

### Core.js
- **Description**: Extends JavaScript's built-in objects with utility methods.
- **Key Features**:
  - Extensions for Array, Math, Number, and String prototypes
  - Methods for array manipulation, number formatting, and string operations
- **Tool Potential**: Utility functions for data manipulation in our agent framework

### Utils.js
- **Description**: Static class with general utility methods for the engine.
- **Key Features**:
  - Platform detection (browser, mobile, etc.)
  - Feature capability detection (WebGL, Audio API, etc.)
  - File handling utilities (URI encoding, file name extraction)
  - Encryption/decryption utilities for game assets
- **Tool Potential**: Helper utilities for file operations and platform compatibility checks

### JsonEx.js
- **Description**: Handles serialization of JavaScript objects to JSON and back, preserving class prototypes.
- **Key Features**:
  - `stringify`: Converts objects to JSON strings with class information
  - `parse`: Reconstructs objects from JSON strings, restoring class prototypes
  - `makeDeepCopy`: Creates deep copies of objects
- **Tool Potential**: 
  - Essential for saving/loading game data in our agent framework
  - Creating and manipulating game objects programmatically
  - An agent could use this to produce new game data objects with proper prototypes

### Graphics.js
- **Description**: Manages the rendering system, including canvas setup and PIXI.js integration.
- **Key Features**:
  - Canvas initialization and scaling
  - Screen transitions and effects
  - Rendering loop management
  - Error display handling
- **Tool Potential**: 
  - Rendering pipeline access for advanced effects
  - Screen management for automated testing
  - Visual debugging tools

### Input.js
- **Description**: Handles keyboard and gamepad input processing.
- **Key Features**:
  - Key mapping and state tracking
  - Input detection methods (isPressed, isTriggered, etc.)
  - Direction pad calculations
  - Gamepad support
- **Tool Potential**: 
  - Input simulation for automated testing
  - Custom input handling for agent-driven gameplay
  - Event automation tools

### Bitmap.js, Sprite.js, Tilemap.js
- **Description**: Core visual components for game graphics.
- **Key Features**:
  - Image loading and manipulation
  - Sprite rendering and animation
  - Tilemap handling for game maps
- **Tool Potential**:
  - Resource generation and manipulation
  - Automated map creation tools
  - Visual asset management

### WebAudio.js
- **Description**: Audio playback system for game sounds, music, and effects.
- **Key Features**:
  - Audio loading and playback
  - Sound effect processing
  - Music streaming
- **Tool Potential**:
  - Sound effect generation
  - Audio integration for AI-generated content

### Window.js
- **Description**: UI window system for menus and dialogs.
- **Key Features**:
  - Window creation and styling
  - Text rendering and formatting
  - UI component management
- **Tool Potential**:
  - Custom UI generation
  - Dialog and menu creation tools

## Core Components as Agent Tools

The `rmmz_core` components provide several opportunities for creating agent tools:

1. **Data Serialization Tools**
   - Wrap JsonEx for creating, saving, and loading game objects
   - Provide schema validation for proper object structures

2. **Resource Management Tools**
   - Handle image, audio, and video resources
   - Generate and modify visual assets

3. **UI Generation Tools**
   - Create windows, menus, and dialogs programmatically
   - Design consistent UI flows

4. **Testing Tools**
   - Simulate input for automated gameplay testing
   - Verify visual and audio output

The core components form the foundation upon which we'll build higher-level tools using the managers and game objects from other directories.

## rmmz_managers Folder

The `rmmz_managers` folder contains static classes that manage various aspects of the game system, from data handling to audio and battle mechanics.

### DataManager.js
- **Description**: Manages game data loading, saving, and database access.
- **Key Features**:
  - Loading game database files (actors, items, maps, etc.)
  - Saving/loading game progress
  - Creating game objects
  - Extracting metadata from notes
  - Managing save files
- **Tool Potential**: 
  - Data manipulation for game content creation
  - Automated save/load operations
  - Game state management
  - Metadata extraction and injection

### StorageManager.js
- **Description**: Handles low-level storage operations for saving/loading game data.
- **Key Features**:
  - Object to JSON conversion
  - Data compression/decompression
  - File system operations
  - IndexedDB storage for web
- **Tool Potential**: 
  - Custom save data formats
  - Efficient data storage handling
  - Cross-platform data persistence

### BattleManager.js
- **Description**: Controls the battle system flow and mechanics.
- **Key Features**:
  - Battle setup and initialization
  - Turn management
  - Action processing
  - Battle state tracking
  - Victory/defeat handling
  - Rewards processing
- **Tool Potential**: 
  - Custom battle system creation
  - Automated battle testing
  - Enemy AI behavior design
  - Battle balancing tools

### AudioManager.js
- **Description**: Manages all game audio including BGM, BGS, ME, and SE.
- **Key Features**:
  - Audio playback control
  - Volume management
  - Fading effects
  - Audio buffer handling
- **Tool Potential**: 
  - Dynamic audio generation
  - Sound effect creation
  - Music integration
  - Audio event triggering

### SceneManager.js
- **Description**: Manages scene transitions and the game loop.
- **Key Features**:
  - Scene initialization and transitions
  - Game loop management
  - Error handling
  - Frame rate control
- **Tool Potential**: 
  - Custom scene creation
  - Game flow automation
  - Testing scene transitions

### PluginManager.js
- **Description**: Handles plugin loading and command registration.
- **Key Features**:
  - Plugin setup and initialization
  - Command registration and execution
  - Plugin parameter management
- **Tool Potential**: 
  - Dynamic plugin generation
  - Plugin parameter configuration
  - Custom command registration

### ImageManager.js
- **Description**: Manages image resource loading and caching.
- **Key Features**:
  - Image loading and caching
  - Resource management
  - Bitmap creation
- **Tool Potential**: 
  - Dynamic image generation
  - Resource optimization
  - Custom sprite creation

## Manager Components as Agent Tools

The manager classes in RPG Maker MZ offer excellent opportunities for creating powerful agent tools:

1. **Data Management Tools**
   - Create/modify game data files (maps, events, actors, etc.)
   - Generate new game content programmatically
   - Validate data structures

2. **Battle System Tools**
   - Create custom battle scenarios
   - Test battle balance
   - Design enemy encounters
   - Automate combat mechanics

3. **Audio and Visual Tools**
   - Generate and integrate sound effects
   - Manage music transitions
   - Create visual effects

4. **Scene and UI Tools**
   - Create custom scenes
   - Design menu systems
   - Automate UI flows

5. **Storage and Persistence Tools**
   - Handle save/load operations
   - Manage game state
   - Import/export game data

## rmmz_objects Folder

The `rmmz_objects` folder contains the game object classes that represent the various elements and entities in the game world. These classes handle game state, behavior, and interactions.

### Game_Map.js
- **Description**: Manages the game map, including scrolling, passage, and events.
- **Key Features**:
  - Map loading and initialization
  - Coordinate and position handling
  - Passage determination (can walk here?)
  - Event management
  - Scrolling and display position
  - Tile and terrain information
- **Tool Potential**: 
  - Map creation and editing
  - Automated map testing
  - Custom map generation
  - Pathfinding algorithms

### Game_Event.js
- **Description**: Represents events on the map (NPCs, triggers, etc.)
- **Key Features**:
  - Event page switching
  - Conditional checks
  - Movement and animation
  - Trigger handling (touch, action, etc.)
  - Parallel process execution
- **Tool Potential**: 
  - Event creation and management
  - NPC behavior programming
  - Cutscene automation
  - Interactive element generation

### Game_Actor.js
- **Description**: Represents a playable character in the game.
- **Key Features**:
  - Parameter and stat management
  - Equipment handling
  - Skill and level management
  - Battle action handling
  - Experience and growth
- **Tool Potential**: 
  - Character creation and balancing
  - Party composition tools
  - Character progression design
  - Stat calculation and simulation

### Game_Interpreter.js
- **Description**: The command interpreter for executing event commands.
- **Key Features**:
  - Event command execution
  - Command flow control (conditional branches, loops)
  - Message and choice handling
  - Variable and switch operations
  - Various game state alterations
- **Tool Potential**: 
  - Event script generation
  - Dialogue tree creation
  - Quest design automation
  - Game logic programming

### Game_Character.js
- **Description**: Base class for characters that appear on the map.
- **Key Features**:
  - Movement and direction
  - Sprite animation
  - Route processing
  - Collision detection
- **Tool Potential**: 
  - Character movement patterns
  - Pathfinding algorithms
  - Animation sequencing

### Game_Party.js
- **Description**: Manages the player's party, inventory, and gold.
- **Key Features**:
  - Party member management
  - Inventory handling
  - Item, weapon, and armor management
  - Gold management
  - Battle member selection
- **Tool Potential**: 
  - Inventory system design
  - Party composition tools
  - Economy balancing

### Game_Troop.js
- **Description**: Manages enemy troops in battle.
- **Key Features**:
  - Enemy party setup
  - Battle event handling
  - Turn conditions
  - Rewards calculation
- **Tool Potential**: 
  - Enemy group generation
  - Battle balance testing
  - Encounter design

### Game_System.js
- **Description**: Manages various game system settings.
- **Key Features**:
  - Save/load enablement
  - Menu access control
  - Battle and sound settings
  - Encounter rate modification
- **Tool Potential**: 
  - Game settings configuration
  - System customization
  - Feature toggling

## Game Objects as Agent Tools

The game objects in RPG Maker MZ provide an excellent foundation for building agent tools:

1. **Map Design and Generation Tools**
   - Procedural map generation
   - Tile and passage setting
   - Region and terrain design
   - Map connection and world building

2. **Event and Narrative Tools**
   - Event script generation based on high-level descriptions
   - Dialogue tree creation
   - Cutscene choreography
   - Quest logic implementation

3. **Character and Battle Tools**
   - Character stat balancing
   - Party composition optimization
   - Enemy design and balance
   - Battle AI programming

4. **Game Logic Tools**
   - Variable and switch management
   - Game state tracking
   - Conditional logic creation
   - Game flow programming

5. **Testing and Simulation Tools**
   - Automated game testing
   - Balance simulation
   - Playthrough scenario testing
   - Performance analysis

## rmmz_scenes Folder

The `rmmz_scenes` folder contains the scene classes that represent different screens and states in the game. These classes handle the UI, user input, and the flow between different game states.

### Scene_Base.js
- **Description**: The base class for all scenes in the game.
- **Key Features**:
  - Scene initialization and termination
  - Scene transitions (fade in/out)
  - Window management
  - UI layout and positioning
  - Input handling
- **Tool Potential**: 
  - Scene flow automation
  - UI layout customization
  - Transition effect creation
  - Scene lifecycle management

### Scene_Map.js
- **Description**: The scene for the main map gameplay.
- **Key Features**:
  - Map display and interaction
  - Player movement
  - Event triggering
  - Menu access
  - Encounter handling
- **Tool Potential**: 
  - Map testing automation
  - Event trigger simulation
  - Gameplay flow automation
  - Map transition testing

### Scene_Battle.js
- **Description**: The scene for battle gameplay.
- **Key Features**:
  - Battle flow management
  - Command selection
  - Action execution
  - Battle UI management
  - Result handling (victory/defeat)
- **Tool Potential**: 
  - Battle simulation
  - Combat balance testing
  - AI behavior testing
  - Battle system customization

### Scene_Menu.js
- **Description**: The main menu scene.
- **Key Features**:
  - Menu command management
  - Status display
  - Navigation to other scenes
  - Party management
- **Tool Potential**: 
  - Menu system customization
  - UI layout automation
  - Menu flow testing

### Other Key Scenes
- **Scene_Title**: Title screen display and game start
- **Scene_Item**: Item inventory management
- **Scene_Skill**: Character skill management
- **Scene_Equip**: Equipment management
- **Scene_Status**: Character status display
- **Scene_Shop**: Shopping interaction
- **Scene_Save/Load**: Game save and load functionality

## Scene Components as Agent Tools

The scene classes in RPG Maker MZ provide excellent foundations for creating tools that manage game flow and user interaction:

1. **Scene Flow Tools**
   - Scene transition management
   - Game state progression
   - UI flow automation
   - Scene sequence creation

2. **UI Layout Tools**
   - Window positioning and sizing
   - UI element arrangement
   - Menu system generation
   - Custom UI design

3. **Interaction Testing Tools**
   - User input simulation
   - Menu navigation testing
   - Battle command testing
   - Event interaction verification

4. **Game Flow Automation Tools**
   - Cutscene creation
   - Battle sequence generation
   - Menu navigation scripting
   - Game state transition management

5. **Scene Creation Tools**
   - Custom scene generation
   - Scene template creation
   - UI component library
   - Scene integration helpers

## rmmz_windows Folder

The `rmmz_windows` folder contains the window classes that make up the user interface in RPG Maker MZ. These classes handle everything from displaying text and images to processing user input and interaction.

### Window_Base.js
- **Description**: The foundational class for all windows in the game.
- **Key Features**:
  - Window creation and management
  - Text drawing and formatting
  - Image display (icons, faces, characters)
  - Window appearance customization
  - Input handling
- **Tool Potential**: 
  - UI component creation
  - Text and dialog systems
  - Custom window templates
  - Visual layout automation

### Window_Selectable.js
- **Description**: Extends Window_Base with selection and navigation capabilities.
- **Key Features**:
  - Cursor movement
  - Item selection
  - Scrolling content
  - Handler management for commands
  - Touch/mouse input processing
- **Tool Potential**: 
  - Interactive menu creation
  - Selection UI components
  - List and grid visualization
  - Input system customization

### Window_Command.js
- **Description**: A standardized command menu window.
- **Key Features**:
  - Command list management
  - Command enabling/disabling
  - Command handlers
  - Standardized layout
- **Tool Potential**: 
  - Command menu generation
  - Decision tree interfaces
  - Custom command systems

### Window_Message.js
- **Description**: The window for displaying text messages and dialogues.
- **Key Features**:
  - Text message display
  - Character-by-character text animation
  - Text codes for formatting and control
  - Choice lists integration
  - Face display for speakers
- **Tool Potential**: 
  - Dialogue system automation
  - Narrative construction
  - Text-based interaction
  - Story presentation tools

### Other Key Windows
- **Battle Windows**: Window_BattleStatus, Window_BattleLog, Window_ActorCommand
- **Menu Windows**: Window_MenuCommand, Window_MenuStatus, Window_Gold
- **Item/Skill Windows**: Window_ItemList, Window_SkillList, Window_EquipItem
- **Shop Windows**: Window_ShopBuy, Window_ShopSell, Window_ShopStatus
- **Utility Windows**: Window_Help, Window_ScrollText, Window_ChoiceList

## Window Components as Agent Tools

The window classes provide a powerful foundation for creating tools that handle UI and user interaction in an agentic framework:

1. **UI Creation Tools**
   - Window layout generation
   - Menu system creation
   - Dialog box templates
   - Form and input interfaces
   - Information display components

2. **Text Processing Tools**
   - Text formatting and styling
   - Message queue management
   - Text animation control
   - Language and localization handling
   - Text code processing

3. **Input Handling Tools**
   - Selection interface creation
   - Command menu generation
   - User input validation
   - Interactive element management
   - Touch/mouse interaction systems

4. **Data Visualization Tools**
   - Status display components
   - Inventory management interfaces
   - Parameter visualization
   - Progress tracking displays
   - Statistical reporting interfaces

5. **Information Flow Tools**
   - Help text systems
   - Tutorial interfaces
   - Notification components
   - Alert and confirmation dialogs
   - Information hierarchy management

## rmmz_sprites Folder

The `rmmz_sprites` folder contains the sprite classes that handle the visual representation of game elements. These classes are responsible for rendering characters, animations, UI elements, and other visual components.

### Sprite_Character.js
- **Description**: Represents and renders characters on the game map.
- **Key Features**:
  - Character image loading and management
  - Animation frame updates
  - Movement visualization
  - Character appearance changes
  - Visibility control
- **Tool Potential**: 
  - Character appearance customization
  - Movement pattern creation
  - Visual effect application
  - Character state visualization

### Spriteset_Base.js
- **Description**: Base class for managing collections of sprites.
- **Key Features**:
  - Layer management (lower/upper)
  - Filter and effect application
  - Animation processing
  - Screen positioning
  - Visual element organization
- **Tool Potential**: 
  - Visual layer management
  - Effect orchestration
  - Scene composition
  - Visual hierarchy control

### Sprite_Animation.js
- **Description**: Handles the display of animations in the game.
- **Key Features**:
  - Animation loading and playback
  - Timing and sequencing
  - Target tracking
  - Effect rendering
  - Animation completion detection
- **Tool Potential**: 
  - Animation creation tools
  - Visual effect sequencing
  - Combat visualization
  - Event feedback systems

### Sprite_Battler.js
- **Description**: Base class for battle participants (actors and enemies).
- **Key Features**:
  - Battler visualization
  - State and condition display
  - Battle position management
  - Motion and action visualization
  - Selection and targeting effects
- **Tool Potential**: 
  - Battle visualization tools
  - Combat state representation
  - Battle choreography
  - Combat feedback systems

### Other Key Sprites
- **UI Sprites**: Sprite_Button, Sprite_Gauge, Sprite_Name, Sprite_StateIcon
- **Map Sprites**: Sprite_Destination, Sprite_Balloon, Sprite_Picture
- **Battle Sprites**: Sprite_Actor, Sprite_Enemy, Sprite_Weapon, Sprite_Damage
- **Effect Sprites**: Sprite_Timer, Sprite_StateOverlay, Sprite_Battleback

## Sprite Components as Agent Tools

The sprite classes provide essential building blocks for creating tools that handle visual representation and animation in an agentic framework:

1. **Visual Representation Tools**
   - Character appearance management
   - Battle visualization
   - Animation generation and control
   - Visual state indication
   - Map element rendering

2. **Animation Control Tools**
   - Animation sequencing
   - Motion pattern creation
   - Visual effect timing
   - Frame-by-frame animation control
   - Transition management

3. **Visual Feedback Tools**
   - State change visualization
   - Action result indication
   - Progress representation
   - Alert and notification display
   - Interactive element highlighting

4. **Scene Composition Tools**
   - Layer management
   - Visual depth control
   - Element positioning
   - Screen space organization
   - Camera and viewport control

5. **Visual Effect Tools**
   - Filter application
   - Color and tone management
   - Weather and environmental effects
   - Special visual effects
   - Screen transitions

# Summary and Agentic Framework Implementation Plan

## Comprehensive Analysis Summary

We have completed a thorough analysis of the RPG Maker MZ codebase, examining all major components:

1. **Core Systems**: Base functionality and utilities that underpin the entire engine
2. **Managers**: Controllers that manage game state, resources, and high-level systems
3. **Objects**: Game entities that represent the game's data model and behaviors
4. **Scenes**: Screen states that organize the flow and interaction of the game
5. **Windows**: UI components that display information and handle user input
6. **Sprites**: Visual representations of game elements on screen

This analysis has revealed a well-structured object-oriented framework with clear separation of concerns, making it highly suitable for wrapping as an agentic framework. Most functionality is exposed through well-defined APIs that can be programmatically accessed and manipulated.

## Agentic Framework Implementation Plan

### 1. Tool Wrapper Layer

Create a layer of wrapper functions that expose the core functionality of RPG Maker MZ as tools for LangGraph agents:

```python
# Example tool wrappers
class RPGMakerTools:
    # Data Management Tools
    def create_map(self, width, height, tileset_id):
        # Wraps $gameMap creation functionality
        pass
    
    def create_event(self, map_id, x, y, event_data):
        # Wraps Game_Event creation
        pass
    
    # Character Tools
    def create_actor(self, name, class_id, initial_level):
        # Wraps Game_Actor creation
        pass
    
    # Battle Tools
    def create_enemy(self, enemy_id, x, y):
        # Wraps Game_Enemy creation
        pass
    
    # Scene Management Tools
    def change_scene(self, scene_type, params=None):
        # Wraps SceneManager.push/goto
        pass
```

### 2. Schema Definitions

Define Pydantic schemas that represent the data structures used by RPG Maker MZ:

```python
from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any

class EventCommand(BaseModel):
    code: int
    parameters: List[Any]
    indent: int = 0

class EventPage(BaseModel):
    conditions: Dict[str, Any]
    image: Dict[str, Any]
    movement_type: int
    list: List[EventCommand]
    # other properties...

class MapEvent(BaseModel):
    id: int
    name: str
    x: int
    y: int
    pages: List[EventPage]
```

### 3. LangGraph Integration

Implement a LangGraph state model and workflows for the agentic framework:

```python
import langgraph as lg
from langgraph.graph import StateGraph

# Define state schema
class RPGMakerState(BaseModel):
    game_data: Dict[str, Any] = Field(default_factory=dict)
    current_task: Optional[str] = None
    # other state fields...

# Create nodes for the graph
def analyze_task(state):
    """Analyze the current task and determine next steps"""
    # LLM-based analysis of what needs to be done
    return state

def create_game_element(state):
    """Create or modify a game element based on the current task"""
    # Use RPGMakerTools to implement changes
    return state

def test_implementation(state):
    """Test that the implementation meets requirements"""
    # Verification logic
    return state

# Build the graph
workflow = StateGraph(RPGMakerState)

workflow.add_node("analyze", analyze_task)
workflow.add_node("create", create_game_element)
workflow.add_node("test", test_implementation)

# Add edges
workflow.add_edge("analyze", "create")
workflow.add_edge("create", "test")
workflow.add_edge("test", "analyze")

# Compile the graph
app = workflow.compile()
```

### 4. Tool Implementation Priority

Based on our analysis, we should implement tools in the following order of priority:

1. **Data Structure Tools**: Create and manipulate maps, events, actors, items, etc.
2. **Event Scripting Tools**: Create and manipulate event commands and flow
3. **Game State Tools**: Save, load, and modify game state
4. **Visual Tools**: Modify sprites, animations, and visual elements
5. **UI Tools**: Create and customize UI elements

### 5. Testing and Validation

Implement a testing framework to validate the agentic tools:

1. **Unit Tests**: Verify each tool functions correctly
2. **Integration Tests**: Test workflows that combine multiple tools
3. **End-to-End Tests**: Create sample games using the agentic framework

### 6. Documentation

Create comprehensive documentation for the agentic framework:

1. **API Reference**: Document all available tools and their parameters
2. **Schema Reference**: Document all data schemas
3. **Tutorial**: Step-by-step guide to creating a game using the framework
4. **Examples**: Sample code for common game creation tasks

## Next Steps

1. Create a basic implementation of the RPGMakerTools class
2. Define the core schemas for game data structures
3. Implement a simple LangGraph workflow for basic game creation
4. Test the implementation with a simple game creation task
5. Iteratively expand the tool set based on testing results
