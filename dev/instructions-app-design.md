# Application Design

## 1. API-first Principle

- The application will use the **OpenAPI specification** to define API contracts.
- The API will include the following features:
  - **Endpoints**:
    - Generate example YAML threat model files.
      - Generate Threat Model: POST /generate
        - Request: Parameters for generating the threat model (e.g., model type).
        - Response: Links to the generated YAML files.
    - Validate YAML threat models against the schema provided in `schema.json`.
      - Validate Threat Model: POST /validate
        - Request: The YAML file to validate.
        - Response: Validation results (success/failure and error messages).
  - **Request/Response Formats**:
    - Input: JSON/YAML files containing threat model data.
    - Output: JSON responses for validation results, including error details or success messages.
  - **Expected Behavior**:
    - The API will provide a clear error structure for invalid YAML files, identifying schema mismatches.
    - Provide downloadable examples of compliant YAML threat model files.

## 2. Application Core Functionality

- **Core Features**:
  1. **Generate Threat Model Examples**:
     - Produce two example YAML files compliant with the schema.
  2. **Validate YAML Threat Models**:
     - Accept a user-uploaded YAML file.
     - Check the file against `schema.json` for compliance.
     - Return a validation report.
- **API Exposure**:
  - Each core feature will have a dedicated endpoint:
    1. `/generate-examples`: Generate and return example YAML files.
    2. `/validate`: Accept a YAML file and return the validation result.

## 3. Error Handling

### Error Handling for the API

#### 3.1. **General Strategy**

- Use consistent error responses with a clear structure.
- Define HTTP status codes for each error type.
- Include detailed error messages and optionally a code for programmatic identification.

#### 3.2. **Error Types and Responses**

| Error Type             | HTTP Status Code | Description                                    |
|------------------------|------------------|------------------------------------------------|
| **Invalid Input Data** | `400 Bad Request`| Client provides malformed or missing input.   |
| **Validation Errors**  | `422 Unprocessable Entity` | YAML does not comply with schema.json. |
| **Internal Errors**    | `500 Internal Server Error`| Unexpected issues in the server.             |

#### 3.3. **Error Response Format**

A unified error response format ensures consistency. Example structure:

```json
{
  "error": {
    "type": "ValidationError",
    "message": "The provided YAML file does not conform to the schema.",
    "details": [
      {"field": "author.name", "error": "Field is required."},
      {"field": "title", "error": "Field must be a string."}
    ]
  }
}
```

#### 3.4. **Handling Specific Error Cases**

##### Invalid Input Data (`400 Bad Request`)

- Triggers when input format is not JSON/YAML or required fields are missing.
- Implementation:

  ```python
  from fastapi import HTTPException

  @app.post("/validate")
  async def validate_yaml(file: UploadFile):
      if not file.filename.endswith(('.yaml', '.yml')):
          raise HTTPException(status_code=400, detail="Invalid file format. Only YAML is accepted.")
  ```

##### Validation Errors (`422 Unprocessable Entity`)

- Occurs when a valid YAML file fails schema validation.
- Response includes validation details:

  ```python
  from pydantic import ValidationError

  @app.post("/validate")
  async def validate_yaml(file: UploadFile):
      try:
          yaml_content = yaml.safe_load(file.file)
          validate_against_schema(yaml_content)
      except ValidationError as e:
          raise HTTPException(
              status_code=422,
              detail={"type": "ValidationError", "errors": e.errors()}
          )
  ```

##### Internal Server Errors (`500 Internal Server Error`)

- For unexpected issues (e.g., unhandled exceptions).
- Return a generic message to the client while logging full details internally:

  ```python
  import logging

  @app.exception_handler(Exception)
  async def internal_server_error_handler(request, exc):
      logging.error(f"Unhandled error: {exc}")
      return JSONResponse(
          status_code=500,
          content={"error": {"type": "ServerError", "message": "An internal server error occurred."}}
      )
  ```

#### 3.5. **Best Practices**

- **Validation Pre-checks**: Validate file extensions and formats before parsing to avoid unnecessary processing.
- **Schema Validation Details**: Provide specific error paths to help users identify issues.
- **Internal Logging**: Log stack traces and request details for internal troubleshooting.
- **Testing**: Write automated tests for all defined error scenarios.

## 4. Documentation

### Documentation Plan for the API

FastAPI provides built-in support for **OpenAPI/Swagger** and **ReDoc** for interactive and comprehensive API documentation. Here’s how to plan and implement the API documentation effectively:

---

#### 4.1. **Leverage FastAPI's Built-in Tools**

- **Swagger UI**: Automatically generates interactive API documentation at `/docs` by default.
- **ReDoc**: Generates a developer-friendly documentation interface at `/redoc`.

---

#### 4.2. **Plan Documentation Features**

- Include the following in the documentation:
  - **Endpoints**: Clearly display all API routes (`/generate-examples`, `/validate`).
  - **Request Formats**: Show input formats for each endpoint (e.g., YAML file uploads).
  - **Response Models**: Define success and error response structures with examples.
  - **Error Handling**: List all error scenarios (e.g., `400`, `422`, `500`) with descriptions.
  - **Example Inputs/Outputs**: Provide sample inputs and expected responses.

---

#### 4.3. **Define API Metadata**

Add descriptive metadata for the API:

```python
from fastapi import FastAPI

app = FastAPI(
    title="Threat Model API",
    description="API for generating and validating YAML-based threat models.",
    version="1.0.0",
    contact={
        "name": "Your Name",
        "email": "your.email@example.com",
        "url": "https://example.com",
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT",
    },
)
```

---

#### 4.4. **Use Pydantic Models for Request/Response Schemas**

Define input/output data models for documentation and validation:

```python
from pydantic import BaseModel
from typing import List, Optional

class ValidationErrorDetail(BaseModel):
    field: str
    error: str

class ValidationResponse(BaseModel):
    success: bool
    errors: Optional[List[ValidationErrorDetail]] = None

class ExampleResponse(BaseModel):
    filename: str
    content: str
```

Use these models in your endpoints for automatic inclusion in the documentation:

```python
from fastapi import UploadFile
from fastapi.responses import JSONResponse

@app.post("/validate", response_model=ValidationResponse)
async def validate_yaml(file: UploadFile):
    # Implementation here
    ...

@app.get("/generate-examples", response_model=List[ExampleResponse])
async def generate_examples():
    # Implementation here
    ...
```

---

#### 4.5. **Customize Documentation**

You can enhance the autogenerated documentation with custom descriptions and examples:

```python
from fastapi import File

@app.post(
    "/validate",
    response_model=ValidationResponse,
    summary="Validate a YAML threat model",
    description="Upload a YAML file to validate it against the schema. The response includes details of validation errors, if any.",
)
async def validate_yaml(file: UploadFile = File(..., description="YAML file to validate")):
    # Implementation here
    ...
```

---

#### 4.6. **Test the Documentation**

- Start the server and view the docs:
  - Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
  - ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

#### 4.7. **Enhance User Guidance**

- Add example inputs/outputs directly in the models or responses:

```python
class ValidationResponse(BaseModel):
    success: bool
    errors: Optional[List[ValidationErrorDetail]] = None

    class Config:
        schema_extra = {
            "example": {
                "success": False,
                "errors": [
                    {"field": "author.name", "error": "Field is required."},
                    {"field": "title", "error": "Field must be a string."}
                ]
            }
        }
    }
```

---

#### 4.8. **Host API Documentation**

- If deploying, ensure the docs are accessible in production. 
- Optionally, restrict access to documentation in sensitive environments or expose it on a separate subdomain.
