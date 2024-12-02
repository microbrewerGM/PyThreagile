from datetime import date
import json
from typing import Dict, Any
from datetime import datetime

class ModelGenerator:
    def __init__(self):
        self.current_date = date.today().strftime("%Y-%m-%d")
        self.instance = self

    def self(self):
        return self

    @staticmethod
    def get_current_date():
        return datetime.now().strftime("%Y-%m-%d")  # Return today's date as a string in the format YYYY-MM-DD

    stub_model = {
        'pythreagile_version': '0.0.1',
        'title': 'Model Stub',
        'date': get_current_date(),
        'author': {
            'name': 'John Doe',
            'homepage': 'www.example.com'
        },
        'management_summary_comment': 'Just some <b>more</b> custom summary possible here...',
        'business_criticality': 'important',
        
        'business_overview': {
            'description': 'Some more <i>demo text</i> here and even images...',
            'images': []
        },
        
        'technical_overview': {
            'description': 'Some more <i>demo text</i> here and even images...',
            'images': []
        },
        
        'questions': {
            'Some question without an answer?': '',
            'Some question with an answer?': 'Some answer'
        },
        
        'abuse_cases': {
            'Some Abuse Case': 'Some Description'
        },
        
        'security_requirements': {
            'Some Security Requirement': 'Some Description'
        },
        
        'tags_available': ['some-tag', 'some-other-tag'],
        
        'data_assets': {
            'Some Data Asset': {
                'id': 'some-data',
                'description': 'Some Description',
                'usage': 'business',
                'tags': None,
                'origin': 'Some Origin',
                'owner': 'Some Owner',
                'quantity': 'many',
                'confidentiality': 'confidential',
                'integrity': 'critical',
                'availability': 'operational',
                'justification_cia_rating': 'Some Justification'
            }
        },
        
        "technical_assets": {
            "Some Technical Asset": {
                "id": "some-component",
                "title": "Some technical asset",
                "description": "Some Description",
                "type": "process",
                "usage": "business",
                "size": "component",
                "used_as_client_by_human": False,
                "out_of_scope": False,
                "justification_out_of_scope": None,
                "technologies": "web-service-rest",
                "tags": ["some-tag", "some-other-tag"],
                "internet": False,
                "machine": "virtual",
                "encryption": "none",
                "owner": "Some Owner",
                "confidentiality": "confidential",
                "integrity": "critical",
                "availability": "critical",
                "justification_cia_rating": "Some Justification",
                "multi_tenant": False,
                "redundant": False,
                "custom_developed_parts": True,
                "data_assets_processed": ["some-data"],
                "data_assets_stored": None,
                "data_formats_accepted": ["xml"],
                "communication_links": {
                    "Some Traffic": {
                        "target": "some-other-component",
                        "description": "Some Description",
                        "protocol": "https",
                        "authentication": "none",
                        "authorization": "none",
                        "tags": None,
                        "vpn": False,
                        "ip_filtered": False,
                        "readonly": False,
                        "usage": "business",
                        "data_assets_sent": ["some-data"],
                        "data_assets_received": None
                    }
                }
            },
            "Some Other Technical Asset": {
                "id": "some-other-component",
                "description": "Some Description",
                "type": "process",
                "usage": "business",
                "used_as_client_by_human": False,
                "out_of_scope": False,
                "justification_out_of_scope": None,
                "technologies": "web-service-rest",
                "tags": ["some-tag", "some-other-tag"],
                "internet": False,
                "machine": "virtual",
                "encryption": "none",
                "owner": "Some Owner",
                "confidentiality": "confidential",
                "integrity": "critical",
                "availability": "critical",
                "justification_cia_rating": "Some Justification",
                "multi_tenant": False,
                "redundant": False,
                "custom_developed_parts": True,
                "data_assets_processed": ["some-data"],
                "data_assets_stored": None,
                "data_formats_accepted": ["xml"],
                "communication_links": {}
            }
        },
        
        'trust_boundaries': {
            'Some Trust Boundary': {
                'id': 'some-network',
                'description': 'Some Description',
                'type': 'network-dedicated-hoster',
                'tags': None,
                'technical_assets_inside': ['some-component'],
                'trust_boundaries_nested': None
            }
        },
        
        'shared_runtimes': {
            'Some Shared Runtime': {
                'id': 'some-runtime',
                'description': 'Some Description',
                'tags': None,
                'technical_assets_running': ['some-component', 'some-other-component']
            }
        },
        
        'individual_risk_categories': {
            'Some Individual Risk Example': {
                'id': 'something-strange',
                'description': 'Some text describing the risk category...',
                'impact': 'Some text describing the impact...',
                'asvs': 'V0 - Something Strange',
                'cheat_sheet': 'https://example.com',
                'action': 'Some text describing the action...',
                'mitigation': 'Some text describing the mitigation...',
                'check': 'Check if XYZ...',
                'function': 'business-side',
                'stride': 'repudiation',
                'detection_logic': 'Some text describing the detection logic...',
                'risk_assessment': 'Some text describing the risk assessment...',
                'false_positives': 'Some text describing the most common types of false positives...',
                'model_failure_possible_reason': False,
                'cwe': 693,
                'risks_identified': {
                    'Example Individual Risk': {
                        'severity': 'critical',
                        'exploitation_likelihood': 'likely',
                        'exploitation_impact': 'medium',
                        'data_breach_probability': 'probable',
                        'data_breach_technical_assets': ['some-component'],
                        'most_relevant_data_asset': None,
                        'most_relevant_technical_asset': 'some-component',
                        'most_relevant_communication_link': None,
                        'most_relevant_trust_boundary': None,
                        'most_relevant_shared_runtime': None
                    }
                }
            }
        },
        
        'risk_tracking': {
            'unencrypted-asset@some-component': {
                'status': 'accepted',
                'justification': 'Risk accepted as tolerable',
                'ticket': 'XYZ-1234',
                'date': '2020-01-04',
                'checked_by': 'John Doe'
            }
        }
    }

    example_model = {
        "threagile_version": "0.0.1",
        "title": "Some Example Application",
        "author": {
            "name": "John Doe",
            "homepage": "www.example.com"
        },
        "date": get_current_date(),
        "business_overview": {
            "description": "Some more <i>demo text</i> here and even images..."
        },
        "technical_overview": {
            "description": "Some more <i>demo text</i> here and even images..."
        },
        "business_criticality": "important",
        "management_summary_comment": "Just some <b>more</b> custom summary possible here...",
        "security_requirements": {
            "EU-DSGVO": "Mandatory EU-Datenschutzgrundverordnung",
            "Input Validation": "Strict input validation is required to reduce the overall attack surface.",
            "Securing Administrative Access": "Administrative access must be secured with strong encryption and multi-factor authentication."
        },
        "questions": {
            "How are the admin clients managed/protected against compromise?": "",
            "How are the build pipeline components managed/protected against compromise?": "Managed by XYZ",
            "How are the development clients managed/protected against compromise?": "Managed by XYZ"
        },
        "abuse_cases": {
            "CPU-Cycle Theft": "As a hacker I want to steal CPU cycles in order to transform them into money via installed crypto currency miners.",
            "Contract Filesystem Compromise": "As a hacker I want to access the filesystem storing the contract PDFs in order to steal/modify contract data.",
            "Cross-Site Scripting Attacks": "As a hacker I want to execute Cross-Site Scripting (XSS) and similar attacks in order to takeover victim sessions and cause reputational damage.",
            "Database Compromise": "As a hacker I want to access the database backend of the ERP-System in order to steal/modify sensitive business data.",
            "Identity Theft": "As a hacker I want to steal identity data in order to reuse credentials and/or keys on other targets of the same company or outside.",
            "PII Theft": "As a hacker I want to steal PII (Personally Identifiable Information) data in order to blackmail the company and/or damage their repudiation by publishing them.",
            "Ransomware": "As a hacker I want to encrypt the storage and file systems in order to demand ransom."
        },
        "tags_available": [
            "linux", "apache", "mysql", "jboss", "keycloak", "jenkins", "git",
            "oracle", "some-erp", "vmware", "aws", "aws:ec2", "aws:s3"
        ],
        "data_assets": {
            "build-job-config": {
                "id": "build-job-config",
                "title": "Build Job Config",
                "description": "Data for customizing of the build job system.",
                "usage": "devops",
                "origin": "Company XYZ",
                "owner": "Company XYZ",
                "confidentiality": "restricted",
                "integrity": "critical",
                "availability": "operational",
                "justification_cia_rating": "Data for customizing of the build job system."
            },
            "client-application-code": {
                "id": "client-application-code",
                "title": "Client Application Code",
                "description": "Angular and other client-side code delivered by the application.",
                "usage": "devops",
                "origin": "Company ABC",
                "owner": "Company ABC",
                "integrity": "critical",
                "availability": "important",
                "justification_cia_rating": "Client-side application code."
            }
        },
        "technical_assets": {
            "apache-webserver": {
                "id": "apache-webserver",
                "title": "Apache Webserver",
                "description": "Main web server",
                "usage": "business",
                "size": "component",
                "technologies": [{
                    "name": "apache",
                    "description": "Apache HTTP Server",
                    "attributes": {
                        "web_server": True
                    }
                }],
                "owner": "Company ABC",
                "confidentiality": "restricted",
                "integrity": "critical",
                "availability": "critical",
                "justification_cia_rating": "Main web server hosting the application"
            }
        },
        "trust_boundaries": {
            "web-dmz": {
                "id": "web-dmz",
                "title": "Web DMZ",
                "description": "Web DMZ",
                "type": "network-cloud-security-group",
                "technical_assets_inside": ["apache-webserver"]
            },
            "application-network": {
                "id": "application-network",
                "title": "Application Network",
                "description": "Application Network",
                "type": "network-cloud-provider",
                "tags": ["aws"],
                "trust_boundaries_nested": ["web-dmz"]
            }
        },
        "communication_links": {
            "customer-client>customer-traffic": {
                "id": "customer-client>customer-traffic",
                "source_id": "customer-client",
                "target_id": "load-balancer",
                "title": "Customer Traffic",
                "description": "Link to the load balancer",
                "protocol": "https",
                "authentication": "session-id",
                "authorization": "end-user-identity-propagation",
                "data_assets_sent": ["customer-accounts", "customer-operational-data"],
                "data_assets_received": [
                    "customer-accounts",
                    "customer-operational-data",
                    "customer-contracts",
                    "client-application-code",
                    "marketing-material"
                ],
                "diagram_tweak_weight": 1,
                "diagram_tweak_constraint": True
            }
        },
        "shared_runtimes": {
            "Some Shared Runtime": {
                "id": "some-runtime",
                "description": "Some Description",
                "tags": None,
                "technical_assets_running": ["apache-webserver"]
            }
        }
    }

    schema = {
        "$schema": "https://json-schema.org/draft-2020-12/schema",
        "id": "file://./schema.json",
        "title": "PyThreagile",
        "description": "Agile Threat Modeling (Python version)",
        "type": "object",
        "properties": {
            "includes": {
                "description": "Include other yaml files into the model",
                "type": [
                    "array",
                    "null"
                ],
                "uniqueItems": True,
                "items": {
                    "type": "string"
                }
            },  
            "pythreagile_version": {
                "description": "Version of the PyThreagile",
                "type": "string"
            },
            "title": {
                "description": "Title of the model",
                "type": "string"
            },
            "date": {
                "description": "Date of the model",
                "type": [
                    "string",
                    "null"
                ],
                "format": "date"
            },
            "author": {
                "description": "Author of the model",
                "type": "object",
                "properties": {
                    "name": {
                        "description": "Author name",
                        "type": [
                            "string",
                            "null"
                        ]
                },
                "contact": {
                    "description": "Author contact info",
                    "type": [
                    "string",
                    "null"
                ]
                },
                "homepage": {
                "description": "Author homepage",
                "type": [
                    "string",
                            "null"
                        ]
                    }
                },
                "required": [
                    "name"
                ]
            },
            "contributors": {
                "description": "Contributors to the model",
                "type": [
                    "array",
                    "null"
                ],
                "uniqueItems": True,
                "items": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "description": "Contributor name",
                            "type": [
                                "string",
                                "null"
                            ]
                        },
                        "contact": {
                            "description": "Contributor contact info",
                            "type": [
                                "string",
                                "null"
                            ]
                        },
                        "homepage": {
                            "description": "Contributor homepage",
                            "type": [
                                "string",
                                "null"
                            ]
                        }
                    },
                    "required": [
                        "name"
                    ]
                }
            },
            "management_summary_comment": {
                "description": "Individual management summary for the report",
                "type": [
                    "string",
                        "null"
                ]
            },
            "business_criticality": {
                "description": "Business criticality of the target",
                "type": "string",
                "enum": [
                    "archive",
                    "operational",
                    "important",
                    "critical",
                    "mission-critical"
                ]
            },
            "application_description": {
                "description": "General description of the application, its purpose and functionality.",
                "type": "object",
                "properties": {
                    "description": {
                        "description": "Application description for the report",
                        "type": [
                    "string",
                            "null"
                        ]
                    },
                    "images": {
                "description": "Application images for the report",
                        "type": [
                            "array",
                            "null"
                        ],
                        "uniqueItems": True
                    }
                }
            },
            "business_overview": {
                "description": "Individual business overview for the report",
                "type": "object",
                "properties": {
                    "description": {
                "description": "Individual business overview for the report",
                "type": [
                        "string",
                        "null"
                    ]
                },
                "images": {
                "description": "Custom images for the report",
                    "type": [
                        "array",
                        "null"
                    ],
                        "uniqueItems": True
                    }
                }
            },
            "technical_overview": {
                "description": "Individual technical overview for the report",
                "type": "object",
                "properties": {
                    "description": {
                        "description": "Individual technical overview for the report",
                        "type": [
                            "string",
                            "null"
                        ]
                    },
                    "images": {
                        "description": "Custom images for the report",
                        "type": [
                            "array",
                                "null"
                        ],
                        "uniqueItems": True
                    }
                }
            },
            "questions": {
                "description": "Custom questions for the report",
                "type": [
                    "object",
                    "null"
                ],
                "uniqueItems": True
            },
            "abuse_cases": {
                "description": "Custom abuse cases for the report",
                "type": [
                "object",
                "null"
                ],
                "uniqueItems": True
            },
            "security_requirements": {
                "description": "Custom security requirements for the report",
                "type": [
                    "object",
                    "null"
                ],
                "uniqueItems": True
            },
            "tags_available": {
                "description": "Tags available",
                "type": [
                    "array",
                    "null"
                ],
                "uniqueItems": True,
                "items": {
                    "type": "string"
                }
            },
            "data_assets": {
                "description": "Data assets",
                "type": "object",
                "uniqueItems": True,
                "additionalProperties": {
                    "type": "object",
                    "properties": {
                        "id": {
                            "description": "ID",
                            "type": "string"
                        },
                        "description": {
                            "description": "Description",
                            "type": [
                                "string",
                                "null"
                            ]
                        },
                        "usage": {
                            "description": "Usage",
                            "type": "string",
                            "enum": [
                                "business",
                                "devops"
                            ]
                        },
                        "tags": {
                            "description": "Tags",
                            "type": [
                                "array",
                                "null"
                            ],
                            "uniqueItems": True,
                            "items": {
                                "type": "string"
                            }
                        },
                        "origin": {
                            "description": "Origin",
                            "type": [
                                "string",
                                "null"
                            ]
                        },
                        "owner": {
                            "description": "Owner",
                            "type": [
                                "string",
                                "null"
                            ]
                        },
                        "quantity": {
                            "description": "Quantity",
                            "type": "string",
                            "enum": [
                                "very-few",
                                "few",
                                "many",
                                "very-many"
                            ]
                        },
                        "confidentiality": {
                            "description": "Confidentiality",
                            "type": "string",
                            "enum": [
                                "public",
                                "internal",
                                "restricted",
                                "confidential",
                                "strictly-confidential"
                            ]
                        },
                        "integrity": {
                            "description": "Integrity",
                            "type": "string",
                            "enum": [
                                "archive",
                                "operational",
                                "important",
                                "critical",
                                "mission-critical"
                            ]
                        },
                        "availability": {
                            "description": "Availability",
                            "type": "string",
                            "enum": [
                                "archive",
                                "operational",
                                "important",
                                "critical",
                                "mission-critical"
                            ]
                        },
                        "justification_cia_rating": {
                            "description": "Justification of the rating",
                            "type": [
                                "string",
                                "null"
                            ]
                        }
                    },
                    "required": [
                        "id",
                        "description",
                        "usage",
                        "quantity",
                        "confidentiality",
                        "integrity",
                        "availability"
                    ]
                }
            },
            "trust_boundaries": {
                "description": "Trust boundaries",
                "type": "object",
                "uniqueItems": True,
                "additionalProperties": {
                    "type": "object",
                    "properties": {
                        "id": {
                            "description": "ID",
                            "type": "string"
                        },
                        "description": {
                            "description": "Description",
                            "type": [
                                "string",
                                "null"
                            ]
                        },
                        "type": {
                            "description": "Type",
                            "type": "string",
                            "enum": [
                                "network-on-prem",
                                "network-dedicated-hoster",
                                "network-virtual-lan",
                                "network-cloud-provider",
                                "network-cloud-security-group",
                                "network-policy-namespace-isolation",
                                "execution-environment"
                            ]
                        },
                        "tags": {
                            "description": "Tags",
                            "type": [
                                "array",
                                "null"
                            ],
                            "uniqueItems": True,
                            "items": {
                                "type": "string"
                            }
                        },
                        "technical_assets_inside": {
                            "description": "Technical assets inside",
                            "type": [
                                "array",
                                "null"
                            ],
                            "uniqueItems": True,
                            "items": {
                                "type": "string"
                            }
                        },
                        "trust_boundaries_nested": {
                            "description": "Trust boundaries nested",
                            "type": [
                                "array",
                                "null"
                            ],
                            "uniqueItems": True,
                            "items": {
                                "type": "string"
                            }
                        }
                    },
                    "required": [
                        "id",
                        "description",
                        "type",
                        "technical_assets_inside",
                        "trust_boundaries_nested"
                    ]
                }
            },
            "shared_runtimes": {
                "description": "Shared runtimes",
                "type": "object",
                "uniqueItems": True,
                "additionalProperties": {
                    "type": "object",
                    "properties": {
                        "id": {
                            "description": "ID",
                            "type": "string"
                        },
                        "description": {
                            "description": "Description",
                            "type": [
                                "string",
                                "null"
                            ]
                        },
                        "tags": {
                            "description": "Tags",
                            "type": [
                                "array",
                                "null"
                            ],
                            "uniqueItems": True,
                            "items": {
                                "type": "string"
                            }
                        },
                        "technical_assets_running": {
                            "description": "Technical assets running",
                            "type": [
                                "array",
                                "null"
                            ],
                            "uniqueItems": True,
                            "items": {
                                "type": "string"
                            }
                        },
                        "required": [
                            "id",
                            "description",
                            "technical_assets_running"
                        ]
                    }
                }
            },
            "individual_risk_categories": {
                "description": "Individual risk categories",
                "type": [
                    "object",
                    "null"
                ],
                "uniqueItems": True,
                "additionalProperties": {
                    "type": "object",
                    "properties": {
                        "status": {
                            "description": "Status",
                            "type": "string",
                            "enum": [
                                "unchecked",
                                "in-discussion",
                                "accepted",
                                "in-progress",
                                "mitigated",
                                "false-positive"
                            ]
                        },
                        "justification": {
                            "description": "Justification",
                            "type": [
                                "string",
                                "null"
                            ]
                        },
                        "ticket": {
                            "description": "Ticket",
                            "type": [
                                "string",
                                "null"
                            ]
                        },
                        "id": {
                            "description": "ID",
                            "type": "string"
                        },
                        "description": {
                            "description": "Description",
                        "type": [
                            "string",
                                "null"
                            ]
                        },
                        "impact": {
                            "description": "Impact",
                            "type": "string"
                        },
                        "asvs": {
                            "description": "ASVS",
                            "type": "string"
                        }, 
                        "cheat_sheet": {
                            "description": "Cheat sheet",
                            "type": "string"
                        },
                        "action": {
                            "description": "Action",
                            "type": "string"
                        },
                        "mitigation": {
                            "description": "Mitigation",
                            "type": "string"
                        },
                        "check": {
                            "description": "Check",
                            "type": "string"
                        },
                        "function": {
                            "description": "Function",
                            "type": "string",
                            "enum": [
                                "business-side",
                                "architecture",
                                "development",
                                "operations"
                            ]
                        },
                        "stride": {
                            "description": "STRIDE",
                            "type": "string",
                            "enum": [
                                "spoofing",
                                "tampering",
                                "repudiation",
                                "information-disclosure",
                                "denial-of-service",
                                "elevation-of-privilege"
                            ]
                        },
                        "detection_logic": {
                            "description": "Detection logic",
                            "type": "string"
                        },
                        "risk_assessment": {
                            "description": "Risk assessment",
                            "type": "string"
                        },
                        "false_positives": {
                            "description": "False positives",
                            "type": "string"
                        },
                        "model_failure_possible_reason": {
                            "description": "Model failure possible reason",
                            "type": "boolean"
                        },
                        "cwe": {
                            "description": "CWE",
                            "type": "integer"
                        },
                        "risks_identified": {
                            "description": "Risks identified",
                            "type": "object",
                            "uniqueItems": True,
                            "additionalProperties": {
                                "type": "object",
                                "properties": {
                                    "severity": {
                                        "description": "Severity",
                                        "type": "string",
                                        "enum": [
                                            "low",
                                            "medium",
                                            "elevated",
                                            "high",
                                            "critical"
                                        ]
                                    },
                                    "exploitation_likelihood": {
                                        "description": "Exploitation likelihood",
                                        "type": "string",
                                        "enum": [
                                            "unlikely",
                                            "likely",
                                            "very-likely",
                                            "frequent"
                                        ]
                                    },
                                    "exploitation_impact": {
                                        "description": "Exploitation impact",
                                        "type": "string",
                                        "enum": [
                                            "low",
                                            "medium",
                                            "high",
                                            "very-high"
                                        ]
                                    },
                                    "data_breach_probability": {
                                        "description": "Data breach probability",
                                        "type": "string",
                                        "enum": [
                                            "improbable",
                                            "possible",
                                            "probable"
                                        ]
                                    },
                                    "data_breach_technical_assets": {
                                        "description": "Data breach technical assets",
                                        "type": [
                                            "array",
                                            "null"
                                        ],
                                        "uniqueItems": True,
                                        "items": {
                                            "type": "string"
                                        }
                                    },
                                    "most_relevant_data_asset": {
                                        "description": "Most relevant data asset",
                                        "type": [
                                            "string",
                                            "null"
                                        ]
                                    },
                                    "most_relevant_technical_asset": {
                                        "description": "Most relevant technical asset",
                                        "type": [
                                            "string",
                                            "null"
                                        ]
                                    },
                                    "most_relevant_communication_link": {
                                        "description": "Most relevant communication link",
                                        "type": [
                                            "string",
                                            "null"
                                        ]
                                    },
                                    "most_relevant_trust_boundary": {
                                        "description": "Most relevant trust boundary",
                                        "type": [
                                            "string",
                                                "null"
                                        ]
                                    },
                                    "most_relevant_shared_runtime": {
                                        "description": "Most relevant shared runtime",
                                        "type": [
                                            "string",
                                            "null"
                                        ]
                                    }
                                }
                            }
                        },
                        "required": [
                            "id",
                            "description",
                            "impact",
                            "asvs",
                            "cheat_sheet",
                            "action",
                            "mitigation",
                            "check",
                            "function",
                            "stride",
                            "detection_logic",
                            "risk_assessment",
                            "false_positives",
                            "model_failure_possible_reason",
                            "cwe",
                            "risks_identified"
                        ]
                    }
                }
            },
            "risk_tracking": {
                "description": "Risk tracking",
                "type": [
                    "object",
                    "null"
                ],
                "uniqueItems": True,
                "additionalProperties": {
                    "type": "object",
                    "properties": {
                        "status": {
                            "description": "Status",
                            "type": "string",
                            "enum": [
                                "unchecked",
                                "in-discussion",
                                "accepted",
                                "in-progress",
                                "mitigated",
                                "false-positive"
                            ]
                        },
                        "justification": {
                            "description": "Justification",
                            "type": [
                                 "string",
                                "null"
                            ]
                        },
                        "ticket": {
                            "description": "Ticket",
                            "type": [
                                "string",
                                "null"
                            ]
                        },
                        "date": {
                            "description": "Date",
                            "type": [
                                "string",
                                "null"
                            ],
                            "format": "date"
                        },
                        "checked_by": {
                            "description": "Checked by",
                            "type": [
                            "string",
                                "null"
                            ]
                        },
                        "required": [
                            "status",
                            "justification",
                            "ticket",
                            "date",
                            "checked_by"
                        ]
                    }
                }
            }
        },
        "required": [
            "pythreagile_version",
            "title",
            "author",
            "business_criticality",
            "tags_available",
            "data_assets",
            "technical_assets",
            "shared_runtimes"
        ]
    }

    def _create_technical_asset(self, asset_id: str, data_assets: list, communication_links: dict) -> dict:
        return {
            'id': asset_id,
            'description': 'Some Description',
            'type': 'process',
            'usage': 'business',
            'used_as_client_by_human': False,
            'out_of_scope': False,
            'justification_out_of_scope': None,
            'size': 'component',
            'technology': 'web-service-rest',
            'tags': ['some-tag', 'some-other-tag'],
            'internet': False,
            'machine': 'virtual',
            'encryption': 'none',
            'owner': 'Some Owner',
            'confidentiality': 'confidential',
            'integrity': 'critical',
            'availability': 'critical',
            'justification_cia_rating': 'Some Justification',
            'multi_tenant': False,
            'redundant': False,
            'custom_developed_parts': True,
            'data_assets_processed': data_assets,
            'data_assets_stored': None,
            'data_formats_accepted': ['xml'],
            'communication_links': communication_links
        }

    def _create_communication_link(self, target: str, data_assets: list) -> dict:
        return {
            'target': target,
            'description': 'Some Description',
            'protocol': 'https',
            'authentication': 'none',
            'authorization': 'none',
            'tags': None,
            'vpn': False,
            'ip_filtered': False,
            'readonly': False,
            'usage': 'business',
            'data_assets_sent': data_assets,
            'data_assets_received': None
        }

    def _create_individual_risk(self) -> dict:
        return {
            'id': 'something-strange',
            'description': 'Some text describing the risk category...',
            'impact': 'Some text describing the impact...',
            'asvs': 'V0 - Something Strange',
            'cheat_sheet': 'https://example.com',
            'action': 'Some text describing the action...',
            'mitigation': 'Some text describing the mitigation...',
            'check': 'Check if XYZ...',
            'function': 'business-side',
            'stride': 'repudiation',
            'detection_logic': 'Some text describing the detection logic...',
            'risk_assessment': 'Some text describing the risk assessment...',
            'false_positives': 'Some text describing the most common types of false positives...',
            'model_failure_possible_reason': False,
            'cwe': 693,
            'risks_identified': {
                '<b>Example Individual Risk</b> at <b>Some Technical Asset</b>': {
                    'severity': 'critical',
                    'exploitation_likelihood': 'likely',
                    'exploitation_impact': 'medium',
                    'data_breach_probability': 'probable',
                    'data_breach_technical_assets': ['some-component'],
                    'most_relevant_data_asset': None,
                    'most_relevant_technical_asset': 'some-component',
                    'most_relevant_communication_link': None,
                    'most_relevant_trust_boundary': None,
                    'most_relevant_shared_runtime': None
                }
            }
        }

    def create_stub_model(self) -> None:
        """Generate a stub model with basic required structure."""
        return self.stub_model

    def create_example_model(self) -> None:
        """Creates an example Pypythreagile model based on a predefined template."""
        return self.example_model
