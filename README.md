# compatillion
Compatillion is a third party open source python package that provides a compatibility layer between Matillion ETL and SQLGlot. This allows you to export SQL-only ETL pipelines from Matillion ETL into an AST that can be used by SQLGlot to generate a SQL script that can be run on any database.

## Installation
To install Compatillion, you can use the following command:
```bash
pip install compatillion
```

## Usage
To use Compatillion, you can import the `Compatillion` class from the package and use it to convert a Matillion ETL pipeline into an AST that can be used by SQLGlot. Here is an example of how to use Compatillion:

```python
from compatillion import generate_ast

export_dict = {
    {
    "dbEnvironment": "",
    "version": "1.72.1",
    "jobsTree": {
        "id": 12345,
        "name": "ROOT",
        "children": [
            {
                "id": 543524,
                "name": "example_node_1",
                "children": [
                    {
                        "id": 324534,
                        "name": "example_node_2",
                        "children": [],
                        "jobs": [
                            {
                                "id": 623454,
                                "name": "example_dag",
                                "description": "",
                                "type": "TRANSFORMATION",
                                "tag": "1a2b3c4d-1a2b-1a2b-1a2b-1a2b3c4d5e6f"
                            }
                        ]
                    }
                ],
                "jobs": []
            }
        ],
        "jobs": []
    },
    "orchestrationJobs": [],
    "transformationJobs": [
        {
            "id": 739344,
            "revision": 1,
            "created": 1709298573059,
            "timestamp": 1709298573059,
            "components": {
                "2917792": {
                    "id": 2917792,
                    "inputCardinality": "ZERO",
                    "outputCardinality": "MANY",
                    "implementationID": 1354890871,
                    "x": 550,
                    "y": 220,
                    "width": 32,
                    "height": 32,
                    "inputConnectorIDs": [],
                    "outputConnectorIDs": [
                        1234567
                    ],
                    "parameters": {
                        "1": {
                            "slot": 1,
                            "name": "Name",
                            "elements": {
                                "1": {
                                    "slot": 1,
                                    "values": {
                                        "1": {
                                            "slot": 1,
                                            "type": "STRING",
                                            "value": ""
                                        }
                                    }
                                }
                            },
                            "visible": true
                        },
                        "2": {
                            "slot": 2,
                            "name": "Target Table",
                            "elements": {
                                "1": {
                                    "slot": 1,
                                    "values": {
                                        "1": {
                                            "slot": 1,
                                            "type": "STRING",
                                            "value": ""
                                        }
                                    }
                                }
                            },
                            "visible": true
                        },
                        "3": {
                            "slot": 3,
                            "name": "Offset",
                            "elements": {
                                "1": {
                                    "slot": 1,
                                    "values": {
                                        "1": {
                                            "slot": 1,
                                            "type": "INTEGER",
                                            "value": ""
                                        }
                                    }
                                }
                            },
                            "visible": true
                        }
                    },
                    "exportMappings": {},
                    "expectedFailure": null,
                    "activationStatus": "ENABLED"
                },
}

```