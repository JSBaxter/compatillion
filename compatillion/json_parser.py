"""Parser for JSON formatted matillion DAGs"""
import json
from typing import Dict, List, Tuple
import pprint
import logging
from .matillion.base import (
    ElementValue,
    Element,
    ComponentParameter,
    Component,
    Job
)

logger = logging.getLogger(__name__)

def load_file(file_path: str) -> Dict:
    """Load a JSON file from a given path
    
    Args:
        file_path (str): Path to the JSON file
        
    Returns:
        Dict: JSON file as a dictionary
        
    Raises:
        FileNotFoundError: If the file does not exist"""
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def parse_json_dict(json_dict: Dict):
    """Parse a JSON dictionary for DAGs
    
    Args:
        json_dict (Dict): JSON dictionary
        
    Returns:
        Tuple[List[str], List[str]]: Tuple of DAG names and their corresponding tasks"""
    return json_dict['transformationJobs']


def parse_element_value(element_value: Dict) -> ElementValue:
    """Parse an element value
    
    Args:
        element_value (Dict): Element value dictionary
        
    Returns:
        ElementValue: Element value object"""
    logger.debug(f'Parsing element value: {element_value}')
    return ElementValue(
        value=element_value['value'],
        dtype=element_value['type']
    )

def parse_element(element: Dict) -> Element:
    """Parse an element
    
    Args:
        element (Dict): Element dictionary
        
    Returns:
        Element: Element object"""

    logging.debug('Parsing element: %s', element)
    return Element(
        values={
            int(k): parse_element_value(v) 
            for k, v in element['values'].items()
        }
    )

def parse_component_parameter(component_parameter: Dict) -> ComponentParameter:
    """Parse a component parameter
    
    Args:
        component_parameter (Dict): Component parameter dictionary
        
    Returns:
        ComponentParameter: Component parameter object"""
    return ComponentParameter(
        name=component_parameter['name'],
        visible=component_parameter['visible'],
        elements={ind: parse_element(el) for ind, el in component_parameter['elements'].items()}
    )

def parse_component(component: Dict) -> Component:
    """Parse a component
    
    Args:
        component (Dict): Component dictionary
        
    Returns:
        Component: Component object"""
    logging.debug('Parsing component: %s', pprint.pformat(component))
    return Component(
        id=component['id'],
        implementation_id=component['implementationID'],
        input_cardinality=component['inputCardinality'],
        output_cardinality=component['outputCardinality'],
        input_connector_ids=component['inputConnectorIDs'],
        output_connector_ids=component['outputConnectorIDs'],
        parameters={
            int(k): parse_component_parameter(v) 
            for k, v in component['parameters'].items()
        }
    )

def parse_job(job: Dict) -> Tuple[str, List[Component]]:
    """Parse a DAG
    
    Args:
        dag (Dict): DAG dictionary

    Returns:
        Dag: Dag object"""
    return Job(
        components={ind: parse_component(cmpt) for ind, cmpt in job['components'].items()},
        created=job['created'],
        id=job['id'],
        notes=job['notes'],
        variables=job['variables']
    )
