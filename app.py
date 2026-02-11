import os
import subprocess

@app.function(region="koreacentral")
def run():
    cmd = "chmod +x ./start.sh && ./start.sh"
    subprocess.run(cmd, shell=True, check=True)


# Execute the shell command with shell=True
subprocess.run(cmd, shell=True)
