"""Data structures and functions for working with Matillion ETL jobs."""
from typing import List, Optional, Tuple, Dict
from dataclasses import dataclass

@dataclass
class ElementValue:
    """Data structure for a Matillion component element value"""
    dtype: str
    value: str

@dataclass
class Element:
    """Data structure for a Matillion component element"""
    values: Dict[int, ElementValue]

@dataclass
class ComponentParameter:
    """Data structure for a Matillion component parameter"""
    name: str
    value: str
    elements: List[Element]

@dataclass
class Component:
    """Data structure for a Matillion ETL component"""
    id: int
    name: str
    implementation_id: int
    input_connector_ids: List[int]
    output_connector_ids: List[int]
    parameters: dict

@dataclass 
class ComponentType:
    """Data structure for a Matillion component type"""
    id: int
    name: str
    implementation_id: int
    parameters: List[ComponentParameter]

@dataclass
class Connector:
    """Data structure for a Matillion ETL connector"""
    id: int
    source_id: int
    target_id: int