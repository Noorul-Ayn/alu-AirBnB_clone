#/usr/bin/python3 /home/evolver/.vscode-server/extensions/ms-python.python-2025.0.0-linux-x64/python_files/printEnvVariablesToFile.py /home/evolver/.vscode-server/extensions/ms-python.python-2025.0.0-linux-x64/python_files/deactivate/bash/envVars.txt
#!/usr/bin/python3
from models.base_model import BaseModel


class City(BaseModel):
    """City class that inherits from BaseModel"""
    name = ""
    state_id = ""
