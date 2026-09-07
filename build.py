"""Build a static portfolio website from validated JSON content.

The build process performs the following steps:

- Loads all JSON schemas from `./schemas`.
- Registers the schemas so that relative `$ref` values resolve correctly.
- Loads and validates the portfolio data from `portfolio.json`.
- Renders the Jinja template `index.html`.
- Writes the generated page to `dist/`.
- Copies static assets and the permissions file for CUNIX servers into the output directory.
"""

from __future__ import annotations

import json
import shutil
from pathlib import Path
from typing import Any

from jinja2 import Environment, FileSystemLoader, StrictUndefined, select_autoescape
from jsonschema import Draft202012Validator
from referencing import Registry, Resource

ROOT_DIR = Path(__file__).resolve().parent
SCHEMAS_DIR = ROOT_DIR / "schemas"
TEMPLATES_DIR = ROOT_DIR / "templates"
STATIC_DIR = ROOT_DIR / "static"
OUTPUT_DIR = ROOT_DIR / "dist"

ROOT_SCHEMA_FILE = SCHEMAS_DIR / "portfolio.schema.json"
DATA_FILE = ROOT_DIR / "portfolio.json"
PERMISSIONS_SOURCE = ROOT_DIR / "CUNIX" / "permissions.txt"


def _load_schema_registry(schema_dir: Path) -> tuple[dict[str, dict], Registry]:
    """Load JSON schemas and create a schema registry.

    :param schema_dir: Directory containing files whose names match `*.schema.json`.
    :returns: (A mapping from schema filename to parsed schema data, A registry containing all loaded schemas)
    :raises json.JSONDecodeError: If a schema file contains invalid JSON.
    :raises OSError: If a schema file cannot be read.
    """
    schemas: dict[str, dict] = {}
    registry = Registry()
    for schema_path in schema_dir.glob("*.schema.json"):
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        schema_uri = schema_path.resolve().as_uri()
        schema["$id"] = schema_uri
        schemas[schema_path.name] = schema
        registry = registry.with_resource(schema_uri, Resource.from_contents(schema))
    return schemas, registry


def validate_profile(data: dict[Any, Any]) -> None:
    """Validate JSON data against the root JSON Schema.

    :param data: Data JSON.
    :raises FileNotFoundError: If the root schema is not present in the schema directory.
    :raises jsonschema.exceptions.ValidationError: If the data does not conform to the root schema.
    :raises json.JSONDecodeError: If one of the schema files contains invalid JSON.
    :raises OSError: If a schema file cannot be read.
    """
    schemas, registry = _load_schema_registry(SCHEMAS_DIR)
    root_schema_name = ROOT_SCHEMA_FILE.name
    try:
        root_schema = schemas[root_schema_name]
    except KeyError as exc:
        raise FileNotFoundError(f"Missing root schema: {ROOT_SCHEMA_FILE}") from exc
    validator = Draft202012Validator(root_schema, registry=registry)
    validator.validate(data)


def build_site() -> None:
    """Render the portfolio website into the distribution directory.

    The function loads and validates the portfolio data, renders the `index.html` Jinja template,
    and writes the result to `dist/index.html`.
    Static assets are copied into `dist/static/`.
    CUNIX permissions are copied to `dist/static/permissions.txt`.

    :raises json.JSONDecodeError: If the portfolio data or a schema contains invalid JSON.
    :raises jsonschema.exceptions.ValidationError: If the portfolio data is invalid.
    :raises FileNotFoundError: If a required schema, template, static directory, or permissions file is missing.
    :raises jinja2.exceptions.TemplateError: If the template cannot be parsed or rendered.
    :raises OSError: If a file or directory cannot be created, removed, read, written, or copied.
    """
    profile = json.loads(DATA_FILE.read_text(encoding="utf-8"))
    validate_profile(profile)

    environment = Environment(
        loader=FileSystemLoader(TEMPLATES_DIR),
        autoescape=select_autoescape(["html", "xml"]),
        undefined=StrictUndefined,
    )

    rendered_html = environment.get_template("index.html").render(**profile)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    output_file = OUTPUT_DIR / "index.html"
    output_file.write_text(rendered_html, encoding="utf-8")

    output_static_dir = OUTPUT_DIR / "static"
    shutil.rmtree(output_static_dir, ignore_errors=True)
    shutil.copytree(STATIC_DIR, output_static_dir)

    shutil.copy2(PERMISSIONS_SOURCE, output_static_dir / PERMISSIONS_SOURCE.name)

    print(f"Built site: {output_file}")


if __name__ == "__main__":
    build_site()
