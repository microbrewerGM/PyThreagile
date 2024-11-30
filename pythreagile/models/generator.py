from datetime import date
import yaml
from typing import Dict, Any
from datetime import datetime

class ModelGenerator:
    def __init__(self):
        self.today = date.today().strftime("%Y-%m-%d")
        self.instance = self

    def self(self):
        return self

    @staticmethod
    def today():
        return datetime.now().strftime("%Y-%m-%d")  # Return today's date as a string in the format YYYY-MM-DD

    stub_model = {
        'pythreagile_version': '0.0.1',
        'title': 'Model Stub',
        'date': today(),
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
        "date": today(),
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
