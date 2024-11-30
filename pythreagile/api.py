# pythreagile/api.py

from fastapi import FastAPI, HTTPException
from pythreagile.models.generator import ModelGenerator
from pythreagile.models.validator import ModelValidator
from pydantic import BaseModel

app = FastAPI(
    title="PyThreagile API",
    description="An API for generating and validating threat models.",
    version="0.0.1",
    contact={
        "name": "PyThreagile",
        "email": "info@pythreagile.io",
        "url": "https://pythreagile.io",
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT",
    },
)

class GenerateModelRequest(BaseModel):
    model_type: dict

@app.post("/generate/")
async def generate_model_endpoint(request: GenerateModelRequest):
    """Generate a model (stub or example) and return the model data."""
    try:
        model_type = request.get("model_type", "").lower()  # Access the model_type from the dictionary
        generator = ModelGenerator()

        if model_type == "stub":
            model_data = generator.create_stub_model()  # Modify this method to return data instead of saving
            return {"status": "success", "model": model_data}
        elif model_type == "example":
            model_data = generator.create_example_model()  # Modify this method to return data instead of saving
            return {"status": "success", "model": model_data}
        else:
            raise HTTPException(status_code=400, detail="Invalid model type. Use 'stub' or 'example'.")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/validate/")
async def validate_model_endpoint(schema_data: dict, request: dict):
    """Validate a model file and return validation results."""
    try:
        validator = ModelValidator(schema=schema_data)
        validation_results = validator.validate(request.model_file)
        return validation_results
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
