from mcp.server.fastmcp import FastMCP
import os

mcp = FastMCP("Demo")

NOTES_FILE = os.path.join(os.path.dirname(__file__),  "notes.txt") # sets path 

def ensure_file():
    if not os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "w") as f:
            f.write("")

# Register your tool
@mcp.tool()
def add_note(message: str) -> str:
    """
    Add a note to the notes file.
    
    Args:
        message (str): The note to add
        
    Returns:
        str: Confirmation message
    """
    ensure_file()
    with open(NOTES_FILE, "a") as f:
        f.write(message + "\n")
    return f"Note added!"

@mcp.tool()
def read_notes() -> str:
    """
    Read all notes from the notes file.
    
    Returns:
        str: All notes
    """
    ensure_file()
    with open(NOTES_FILE, "r") as f:
        notes = f.read()
    return notes

@mcp.resource("notes://latest")
def get_latest_note() -> str:
    """
    Get the latest note from the notes file.
    
    Returns:
        str: The latest note
    """
    ensure_file()
    with open(NOTES_FILE, "r") as f:
        notes = f.readlines()
    return notes[-1].strip() if notes else "No notes found."

@mcp.prompt()
def note_summary_prompt() -> str:
    """
    Prompt for a summary of the notes.
    
    Returns:
        str: Summary of the notes
    """
    ensure_file()
    with open(NOTES_FILE, "r") as f:
        notes = f.read().strip()
    if not notes:
        return "No notes found."
    return f"Here are your notes:\n{notes}"