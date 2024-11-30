from unittest.mock import patch
import pytest
from datetime import datetime
from pythreagile.models.generator import ModelGenerator
from pythreagile.api import generate_model_endpoint, validate_model_endpoint
import asyncio

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
    date_to_validate = ModelGenerator.today()  # Assuming today() returns a date string
    specific_date_format = "%Y-%m-%d"  # Define the expected date format

    # Check if the date_to_validate matches the expected format
    try:
        datetime.strptime(date_to_validate, specific_date_format)
    except ValueError:
        assert False, "Date format is incorrect"
