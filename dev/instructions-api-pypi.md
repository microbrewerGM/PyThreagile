# Instructions for building an API-first Python application that can also be published and run as a PyPI package

Here’s a structured approach to building an **API-first Python application** that can also be published and run as a PyPI package:

---

## 1. **Plan the Application Design**

- **API-first principle**: Start by designing the API contracts (e.g., using OpenAPI/Swagger). Define endpoints, request/response formats, and expected behavior.
- Decide the **core functionality** of the app and how the API will expose it.
- The application will include features for generating and validating YAML threat models, with endpoints for each core functionality.

---

## 2. **Set Up the Python Project**

- Use a directory structure like:

  ```directory_tree
  pythreagile/
  ├── pythreagile/
  │   ├── __init__.py
  │   ├── api.py          # API implementation; runs the FastAPI app
  │   ├── main.py         # Command-line interface; calls the API
  │   ├── models/
  │   │   ├── __init__.py
  │   │   ├── generator.py # Model generation logic
  │   │   └── validator.py # Validation logic
  │   └── utils.py        # Utility functions
  ├── tests/
  │   ├── test_api.py     # API tests
  │   ├── test_main.py     # CLI tests
  ├── docs/               # API documentation (optional)
  ├── setup.py            # Packaging config
  ├── pyproject.toml      # Modern dependency management
  ├── requirements.txt    # Dependencies for the app
  └── README.md           # Project description
  ```

---

## 3. **Develop the Core Logic**

- Write modular and reusable code for the app’s main functionality in `models/generator.py` and `models/validator.py`.
- The `ModelGenerator` class should handle the creation of stub and example models, while the `validator` module should manage the validation of YAML files against the defined schema.
- Keep the business logic separate from API-specific logic to maintain clarity and reusability.

---

## 4. **Develop the API Layer**

- Use **FastAPI** for building the API, which integrates seamlessly with OpenAPI and automatic documentation generation.
- Example `api.py` using FastAPI:

  ```python
  from fastapi import FastAPI
  from pythreagile.models.generator import ModelGenerator
  from pythreagile.models.validator import ModelValidator

  app = FastAPI()

  @app.post("/generate")
  def generate_model(model_type: str):
      generator = ModelGenerator()
      if model_type == "stub":
          return generator.create_stub_model("demo/stub-threagile.yaml")
      elif model_type == "example":
          return generator.create_example_model("demo/example-threagile.yaml")
      else:
          return {"error": "Invalid model type"}

  @app.post("/validate")
  def validate_model(model_file: str):
      validator = ModelValidator()
      return validator.validate(model_file)
  ```

- Use `uvicorn` for local development and testing.
- The Python package main.py shall never spawn or run an API server; this function is reserved only for the api.py file.

---

## 5. **Make the App CLI-Compatible**

- Use a CLI framework like `argparse` to make the app executable via command line.
- Example:

  ```python
  import sys
  import argparse
  from pythreagile.api import generate_model, validate_model

  def create_parser():
      parser = argparse.ArgumentParser(description='PyThreagile - Agile Threat Modeling Tool (in Python)')
      subparsers = parser.add_subparsers(dest='command', help='Available commands')

      # Generate command
      generate_parser = subparsers.add_parser('generate', help='Generate a model')
      generate_parser.add_argument('--type', type=str, choices=['stub', 'example'], required=True, help='Type of model to generate')

      # Validate command
      validate_parser = subparsers.add_parser('validate', help='Validate a model')
      validate_parser.add_argument('--model', type=str, required=True, help='Path to the model file')

      return parser

  def main():
      parser_obj = create_parser()
      args = parser_obj.parse_args()

      if args.command == 'generate':
          generate_model(args.type)
      elif args.command == 'validate':
          validate_model(args.model)
      else:
          parser_obj.print_help()
          sys.exit(1)

  if __name__ == "__main__":
      main()
  ```

---

## 6. **Package the Application**

- Create a `setup.py` or use `pyproject.toml` (recommended for modern Python):
  Example `pyproject.toml`:

  ```toml
  [build-system]
  requires = ["setuptools", "wheel"]
  build-backend = "setuptools.build_meta"

  [project]
  name = "my-python-app"
  version = "0.1.0"
  description = "An API-first Python app"
  authors = [
      { name="Your Name", email="your.email@example.com" }
  ]
  dependencies = [
      "fastapi",
      "typer",
      "uvicorn"
  ]
  classifiers = [
      "Programming Language :: Python :: 3.9",
      "License :: OSI Approved :: MIT License",
  ]
  ```

---

## 7. **Write Tests**

- Use **pytest** to test the API and core functionality:
  - Example `test_api.py`:

    ```python
    from fastapi.testclient import TestClient
    from my_python_app.api import app

    client = TestClient(app)

    def test_example_endpoint():
      response = client.get("/example?param=test")
      assert response.status_code == 200
      assert response.json() == {"result": "test_output"}
    ```

---

## 8. **Publish to PyPI**

- Register your project on [PyPI](https://pypi.org/).
- Use `twine` to upload the package:

 ```bash
 python -m build
 twine upload dist/*
 ```

---

## 9. **Run and Use the Package**

- Once installed via pip, the app should be executable via CLI or API:
  - **Run the API**:

    ```bash
    uvicorn my_python_app.api:app --reload
    ```

  - **Run the CLI**:

    ```bash
    my-python-app run --param value
    ```

---

## 10. **Documentation and Deployment**

- Use the built-in FastAPI interactive docs (Swagger UI).
- For deployment:
- Use a containerization tool like **Docker** for portability.
- Deploy using **Gunicorn** or a cloud provider like AWS, GCP, or Azure.
