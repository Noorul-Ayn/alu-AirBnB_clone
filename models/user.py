#/usr/bin/python3 /home/evolver/.vscode-server/extensions/ms-python.python-2025.0.0-linux-x64/python_files/printEnvVariablesToFile.py /home/evolver/.vscode-server/extensions/ms-python.python-2025.0.0-linux-x64/python_files/deactivate/bash/envVars.txt
#!/usr/bin/python3
from models.base_model import BaseModel


class User(BaseModel):
    """User class that inherits from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
