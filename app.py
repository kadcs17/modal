import os
import subprocess
@app.function(region="koreacentral")

# Define the command to be executed
cmd = "chmod +x ./start.sh && ./start.sh"

# Execute the shell command with shell=True
subprocess.run(cmd, shell=True)
