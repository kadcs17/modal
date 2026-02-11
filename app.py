import os
import subprocess
import modal
@app.function(region="asia-northeast3")
def run():
    cmd = "chmod +x ./start.sh && ./start.sh"

    result = subprocess.run(
        cmd,
        shell=True,
        capture_output=True,
        text=True
    )
