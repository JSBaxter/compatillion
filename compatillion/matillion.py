"""Data structures and functions for working with Matillion ETL jobs."""
from typing import List, Optional, Dict
from dataclasses import dataclass

import logging
logger = logging.getLogger(__name__)

@dataclass(frozen=True)
class ElementValue:
    """Data structure for a Matillion component element value"""
    dtype: str
    value: str

@dataclass(frozen=True)
class Element:
    """Data structure for a Matillion component element"""
    values: Dict[int, ElementValue]

@dataclass(frozen=True)
class ComponentParameter:
    """Data structure for a Matillion component parameter"""
    name: str
    visible: bool
    elements: List[Element]

@dataclass(frozen=True)
class Component:
    """Data structure for a Matillion ETL component"""
    id: int
    implementation_id: int
    input_cardinality: str
    output_cardinality: str
    input_connector_ids: List[int]
    output_connector_ids: List[int]
    parameters: Dict[int, ComponentParameter]

@dataclass(frozen=True)
class ComponentType:
    """Data structure for a Matillion component type"""
    id: int
    name: str
    implementation_id: int
    parameters: List[ComponentParameter]

@dataclass(frozen=True)
class Connector:
    """Data structure for a Matillion ETL connector"""
    id: int
    source_id: int
    target_id: int

@dataclass(frozen=True)
class Dag:
    """Data structure for a Matillion ETL DAG"""
    id: int
    components: Dict[int, Component]
    created: int
    notes: Optional[str]
    variables: Dict[str, str]
