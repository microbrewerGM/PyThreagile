from unittest.mock import patch
import pytest
from datetime import datetime
from pythreagile.models.generator import ModelGenerator
from pythreagile.api import generate_model_endpoint, validate_model_endpoint
import json
import pytest_asyncio

# Define expected model data for stub and example models
expected_stub_model = ModelGenerator.stub_model
expected_example_model = ModelGenerator.example_model

# Define a specific date for validation
specific_date = "2023-10-01"
specific_date_format = "%Y-%m-%d"

@pytest.mark.asyncio  # This should now work after installing pytest-asyncio
async def test_generate_stub_model():
    # Test the generate model function for stub
    response = await generate_model_endpoint({"model_type": "stub"})
    
    # Directly grab the stub model from ModelGenerator
    expected_model = ModelGenerator.stub_model
    
    # Assert that the response matches the expected model
    assert response == {
        "status": "success",
        "model": expected_model
    }

@pytest.mark.asyncio  # This should now work after installing pytest-asyncio
async def test_generate_example_model():
    # Test the generate model function for example
    response = await generate_model_endpoint({"model_type": "example"})  # Ensure this is a dict as well
    
    # Directly grab the example model from ModelGenerator
    expected_model = ModelGenerator.example_model
    
    # Assert that the response matches the expected model
    assert response == {
        "status": "success",
        "model": expected_model
    }

# In tests/test_main.py
def test_validate_datetime_format():
    # Validate the datetime format against a specific date
    date_to_validate = ModelGenerator.get_current_date()
    
    # Check if the date_to_validate matches the expected format
    try:
        datetime.strptime(date_to_validate, "%Y-%m-%d")
    except ValueError:
        assert False, "Date format is incorrect"

@pytest.mark.asyncio  # This should now work after installing pytest-asyncio
async def test_validate_model_success():
    # Prepare valid YAML content and schema data
    generator = ModelGenerator()
    valid_yaml_content = generator.create_stub_model()
    valid_schema_data = generator.schema # Load schema.json content

    # Call the validate_model function
    response = await validate_model_endpoint(schema_data=valid_schema_data, model_file=valid_yaml_content)

    # Assert that the response indicates success
    assert response["status"] == "success"
    assert isinstance(response["validation_results"], list)

@pytest.mark.asyncio  # This should now work after installing pytest-asyncio
async def test_validate_model_failure():
    # Prepare invalid YAML content and schema data
    invalid_yaml_content = "invalid_yaml_content"  # Invalid YAML
    valid_schema_data = ModelGenerator.schema

    # Call the validate_model function
    response = await validate_model_endpoint(valid_schema_data, invalid_yaml_content)

    # Assert that the response indicates failure
    assert response["status"] == "error"