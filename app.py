import os
import subprocess
import modal
app = modal.App()

@app.function(region="koreacentral")
def run():
    cmd = "chmod +x ./start.sh && ./start.sh"


# Execute the shell command with shell=True
subprocess.run(cmd, shell=True)
