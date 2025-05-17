To run Expiriement ensure you have uv installed.

Then Run these commands:

uv init mcp-server-demo

cd .\mcp-server-demo\

uv add "mcp[cli]"

pip install "mcp[cli]"

Ensure you have claude desktop installed, transfer the main.py code into the newly created folder inside main.py

then run : 

uv run mcp install main.py

Restart Claude by stopping it from Task Manager, after opening again, should see new tools available.
This is important as Claude needs to completely restart to recognise newly added tools.

Also can see claude config to see if tools successfully added. Go to File->Settings->Developer->Edit Config

Should see mcp server added with correct path

Ask Claude to create notes about something and see notes.txt created and notes added.
