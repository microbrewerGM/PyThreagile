# pythreagile/main.py

import sys
import argparse
import yaml
import os
import asyncio
from pythreagile.api import generate_model_endpoint, validate_model_endpoint, ValidateModelRequest
from pydantic import BaseModel
import json

# Define the Pydantic model for generating a model request
class GenerateModelRequest(BaseModel):
    model_type: str  # 'stub' or 'example'

# Define the Pydantic model for validating a model request
class ValidateModelRequest(BaseModel):
    model_file: dict  # The model data as a dictionary

def create_parser():
    parser = argparse.ArgumentParser(description='PyThreagile - Agile Threat Modeling Tool (in Python)')
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Create Stub Model command
    create_stub_parser = subparsers.add_parser('create-stub-model', 
                                             help='Create a simple PyThreagile model yaml file')
    create_stub_parser.add_argument('--output-path', required=True, help='Path to save the output model.')
    
    # Create Example Model command
    create_example_parser = subparsers.add_parser('create-example-model', 
                                                help='Create an example PyThreagile model yaml file')
    create_example_parser.add_argument('--output-path', required=True, help='Path to save the output model.')
            
    # Validate command
    validate_parser = subparsers.add_parser('validate', help='Validate a model')
    validate_parser.add_argument('--model', type=str, required=True, help='Path to the model file')
    validate_parser.add_argument('--schema', type=str, required=True, help='Path to the schema file')

    return parser

async def create_stub_model(output_path):
    # Ensure the directory exists
    output_dir = os.path.dirname(output_path)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)  # Create the directory if it doesn't exist

    # Create a request object for the stub model
    request_data = GenerateModelRequest(model_type="stub")

    # Call the API function to generate the stub model
    try:
        model_data = await generate_model_endpoint(request_data)  # Pass the Pydantic model instance
        with open(output_path, 'w') as f:
            yaml.dump(model_data['model'], f, sort_keys=False, allow_unicode=True, width=float("inf"))
        print(f"Created stub model at: {output_path}")
    except Exception as e:
        print(f"Error creating stub model: {e}")

async def create_example_model(output_path):
    # Ensure the directory exists
    output_dir = os.path.dirname(output_path)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)  # Create the directory if it doesn't exist

    # Create a request object for the example model
    request_data = GenerateModelRequest(model_type="example")

    # Call the API function to generate the example model
    try:
        model_data = await generate_model_endpoint(request_data)  # Pass the Pydantic model instance
        with open(output_path, 'w') as f:
            yaml.dump(model_data['model'], f, sort_keys=False, allow_unicode=True, width=float("inf"))
        print(f"Created example model at: {output_path}")
    except Exception as e:
        print(f"Error creating example model: {e}")

async def validate_model(yaml_content, schema_data):
    """Validate the model data provided in YAML format."""
    try:
        # Load the model data from the YAML content
        model_data = yaml.safe_load(yaml_content)

        # Check if model_data is None or not a dictionary
        if model_data is None:
            raise ValueError("Model data is empty (None). Please provide valid model data.")
        if not isinstance(model_data, dict):
            raise ValueError("Model data must be a valid dictionary.")

        # Check if the model data is empty
        if not model_data:
            raise ValueError("Model data is empty. Please provide valid model data.")

        # Create a request object for validation
        request_data = ValidateModelRequest(model_file=model_data)  # Pass the loaded model data

        # Call the API function to validate the model
        validation_results = await validate_model_endpoint(schema_data, request_data)  # Pass schema_data and request_data
        if validation_results:
            print("Validation results:")
            for result in validation_results:
                print(f"- {result}")
        else:
            print("Validation successful. No errors found.")
    except Exception as e:
        print(f"Validation error: {e}")

def main():
    parser_obj = create_parser()
    args = parser_obj.parse_args()
    
    if args.command == 'validate':
        if not os.path.exists(args.model):
            print(f"Error: The model file '{args.model}' does not exist.")
            sys.exit(1)

        if not os.path.exists(args.schema):
            print(f"Error: The schema file '{args.schema}' is required for validation.")
            sys.exit(1)

        # Load schema file and create valid json object to pass to the validator
        try:
            with open(args.schema, 'r') as f:
                schema_data = json.load(f)  # Load the schema data
        except Exception as e:
            print(f"Error loading schema file: {e}")
            sys.exit(1)

        # Load model file and validate
        try:
            with open(args.model, 'r') as f:
                yaml_content = f.read()  # Read the raw YAML content
        except Exception as e:
            print(f"Error loading model file: {e}")
            sys.exit(1)

        # Call the validate_model function with the loaded YAML content and schema data
        asyncio.run(validate_model(yaml_content, schema_data))

    elif args.command == 'create-stub-model':
        asyncio.run(create_stub_model(args.output_path))  # Pass the output path

    elif args.command == 'create-example-model':
        asyncio.run(create_example_model(args.output_path))

    else:
        parser_obj.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()
