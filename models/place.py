#/usr/bin/python3 /home/evolver/.vscode-server/extensions/ms-python.python-2025.0.0-linux-x64/python_files/printEnvVariablesToFile.py /home/evolver/.vscode-server/extensions/ms-python.python-2025.0.0-linux-x64/python_files/deactivate/bash/envVars.txt
#!/usr/bin/python3
from models.base_model import BaseModel


class Place(BaseModel):
    """Place class that inherits from BaseModel"""
    user_id = ""
    city_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
