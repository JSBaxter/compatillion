"""Parser for JSON formatted matillion DAGs"""
import json
import os
from .matillion import (
    ElementValue, 
    Element, 
    ComponentParameter, 
    Component, 
    ComponentType,
    Connector
)
from typing import Dict, List, Tuple
import pprint

def load_file(file_path: str) -> Dict:
    """Load a JSON file from a given path
    
    Args:
        file_path (str): Path to the JSON file
        
    Returns:
        Dict: JSON file as a dictionary
        
    Raises:
        FileNotFoundError: If the file does not exist"""
    with open(file_path, 'r') as file:
        return json.load(file)
    
def parse_json_dict(json_dict: Dict):
    """Parse a JSON dictionary for DAGs
    
    Args:
        json_dict (Dict): JSON dictionary
        
    Returns:
        Tuple[List[str], List[str]]: Tuple of DAG names and their corresponding tasks"""
    return json_dict['transformationJobs']

json_dict = load_file('trf_base_clm_ibp_red_h_airline.json')
tasks = parse_json_dict(json_dict)

components = tasks[0]['components']

components = list(components.values())

pprint.pprint(components)

def parse_element_value(element_value: Dict) -> ElementValue:
    """Parse a JSON dictionary for element values
    
    Args:
        element_value (Dict): JSON dictionary
        
    Returns:
        ElementValue: Element value data structure"""
    return ElementValue(
        slot=element_value['slot'],
        dtype=element_value['type'],
        value=element_value['value']
    )