import os
from box.exceptions import BoxValueError
import yaml
from cnnClassiifer import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    try:
        with open(path_to_yaml, 'r') as file:
            config = yaml.safe_load(file)
        return ConfigBox(config)
    except Exception as e:
        logger.error(f"Failed to read yaml file {path_to_yaml}. Error: {e}")
        raise BoxValueError(f"Failed to read yaml file {path_to_yaml}")


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    logger.info(f"json file saved at: {path}")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    with open(path) as f:
        data = json.load(f)
    logger.info(f"json file loaded successfully from: {path}")
    return ConfigBox(data)

@ensure_annotations
def save_bin(path: Path, data: Any):
    joblib.dump(data, path)
    logger.info(f"Binary file saved at: {path}") 
    return data

@ensure_annotations
def load_bin(path: Path) -> Any:
    data = joblib.load(path)
    logger.info(f"Binary file loaded successfully from: {path}")
    return data 

@ensure_annotations
def get_size(path: Path) -> str:
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"


def decodeImage(imgString, fileName):
    imgdata = base64.b64decode(imgString)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        logger.info(f"Image saved at: {fileName}")
        f.close()

def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, 'rb') as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')
    


