import json
from pydantic import BaseModel, ValidationError as PydanticValidationError
from typing import List, Dict, Any

class ModelSchema(BaseModel):
    pythreagile_version: str
    title: str
    date: str
    author: dict
    management_summary_comment: str
    business_criticality: str
    business_overview: dict
    technical_overview: dict
    questions: dict
    abuse_cases: dict
    security_requirements: dict
    tags_available: list
    data_assets: dict

class ValidationError(Exception):
    """Custom exception for validation errors"""
    def __init__(self, message: str, path: str = ""):
        self.message = message
        self.path = path
        super().__init__(f"{path}: {message}" if path else message)

class ModelValidator:
    def __init__(self, schema: dict):
        self.schema = schema

    def validate(self, model_data: dict) -> List[str]:
        """Validate the model against the schema"""
        errors = []

        # Check required top-level fields from schema
        required_fields = self.schema.get('required', [])
        for field in required_fields:
            if field not in model_data:
                errors.append(f"Missing required field: {field}")

        # Validate the model data using Pydantic
        try:
            ModelSchema(**model_data)  # Validate the model data
        except PydanticValidationError as e:
            errors.append(f"Validation error: {e.errors()}")
        except Exception as e:
            errors.append(f"Error during validation: {e}")

        # Validate each field according to schema
        try:
            self._validate_object(model_data, self.schema['properties'], "")
        except ValidationError as e:
            errors.append(str(e))

        return errors

    def _validate_object(self, data: Dict[str, Any], schema_properties: Dict[str, Any], path: str):
        """Validate an object against schema properties"""
        for key, value in data.items():
            if key not in schema_properties:
                continue  # Skip validation for fields not in schema

            field_schema = schema_properties[key]
            field_path = f"{path}.{key}" if path else key
            self._validate_field(value, field_schema, field_path)

    def _validate_field(self, value: Any, schema: Dict[str, Any], path: str):
        """Validate a single field against its schema"""
        if 'type' not in schema:
            return  # Nothing to validate

        field_type = schema['type']
        nullable = False
        if isinstance(field_type, list):
            if 'null' in field_type:
                nullable = True
                field_type = [t for t in field_type if t != 'null']
                if not field_type:
                    return  # Only null is allowed
                field_type = field_type[0]
            else:
                field_type = field_type[0]

        if value is None:
            if not nullable:
                raise ValidationError(f"Field '{path}' cannot be null.", path)
            else:
                return  # Valid as null

        try:
            if field_type == 'string':
                self._validate_string(value, schema, path)
            elif field_type == 'object':
                if not isinstance(value, dict):
                    raise ValidationError(f"Expected object for '{path}', got {type(value).__name__}", path)
                required_fields = schema.get('required', [])
                for req_field in required_fields:
                    if req_field not in value:
                        raise ValidationError(f"Missing required field '{req_field}' in '{path}'", path)
                self._validate_object(value, schema.get('properties', {}), path)
            elif field_type == 'array':
                self._validate_array(value, schema, path)
            elif field_type == 'integer':
                self._validate_integer(value, schema, path)
            elif field_type == 'number':
                self._validate_number(value, schema, path)
            elif field_type == 'boolean':
                if not isinstance(value, bool):
                    raise ValidationError(f"Expected boolean for '{path}', got {type(value).__name__}", path)
        except ValidationError as ve:
            raise ve
        except Exception as e:
            raise ValidationError(f"Unexpected error during validation at '{path}': {str(e)}", path)

    def _validate_string(self, value: Any, schema: Dict[str, Any], path: str):
        """Validate string fields"""
        if not isinstance(value, str):
            raise ValidationError(f"Expected string for '{path}', got {type(value).__name__}", path)

        if 'enum' in schema:
            if value not in schema['enum']:
                allowed = ', '.join(schema['enum'])
                raise ValidationError(f"Value '{value}' for '{path}' must be one of: {allowed}", path)

    def _validate_array(self, value: Any, schema: Dict[str, Any], path: str):
        """Validate array fields"""
        if not isinstance(value, list):
            raise ValidationError(f"Expected array for '{path}', got {type(value).__name__}", path)

        if schema.get('uniqueItems', False):
            seen = set()
            for index, item in enumerate(value):
                item_key = json.dumps(item, sort_keys=True)
                if item_key in seen:
                    raise ValidationError(f"Array items at '{path}' must be unique", path)
                seen.add(item_key)

        if 'items' in schema:
            item_schema = schema['items']
            for index, item in enumerate(value):
                item_path = f"{path}[{index}]"
                self._validate_field(item, item_schema, item_path)

    def _validate_integer(self, value: Any, schema: Dict[str, Any], path: str):
        """Validate integer fields"""
        if not isinstance(value, int):
            raise ValidationError(f"Expected integer for '{path}', got {type(value).__name__}", path)

    def _validate_number(self, value: Any, schema: Dict[str, Any], path: str):
        """Validate number fields"""
        if not isinstance(value, (int, float)):
            raise ValidationError(f"Expected number for '{path}', got {type(value).__name__}", path)
