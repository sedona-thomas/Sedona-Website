from __future__ import annotations

import json
import shutil
from jinja2 import Environment, FileSystemLoader, StrictUndefined, select_autoescape
from jsonschema import Draft202012Validator
from pathlib import Path
from referencing import Registry, Resource

ROOT_DIR = Path(__file__).parent
DATA_FILE = ROOT_DIR / "portfolio.json"
TEMPLATES_DIR = ROOT_DIR / "templates"
STATIC_DIR = ROOT_DIR / "static"
OUTPUT_DIR = ROOT_DIR / "dist"
SCHEMA_FILE = ROOT_DIR / "schemas" / "portfolio.schema.json"

SCHEMA_DIR = Path(__file__).resolve().parent / "schemas"
ROOT_SCHEMA_NAME = "portfolio.schema.json"


def _load_schema_registry(schema_dir: Path) -> tuple[dict, Registry]:
    schemas: dict[str, dict] = {}

    # Load all schema files and assign each one its local file URI.
    for schema_path in schema_dir.glob("*.schema.json"):
        schema = json.loads(schema_path.read_text(encoding="utf-8"))

        # Use the real local path as the schema's identifier.
        schema["$id"] = schema_path.resolve().as_uri()
        schemas[schema_path.name] = schema

    registry = Registry()

    # Register every schema using the same URI stored in its $id.
    for schema_path in schema_dir.glob("*.schema.json"):
        schema_uri = schema_path.resolve().as_uri()
        registry = registry.with_resource(schema_uri, Resource.from_contents(schemas[schema_path.name]))

    return schemas, registry


def validate_profile(profile: dict) -> None:
    schemas, registry = _load_schema_registry(SCHEMA_DIR)
    try:
        root_schema = schemas[ROOT_SCHEMA_NAME]
    except KeyError as exc:
        raise FileNotFoundError(f"Missing root schema: {SCHEMA_DIR / ROOT_SCHEMA_NAME}") from exc

    validator = Draft202012Validator(schema=root_schema, registry=registry)
    validator.validate(profile)


def load_profile() -> dict:
    """Load and return website content from the JSON file."""
    with DATA_FILE.open("r", encoding="utf-8") as file:
        profile = json.load(file)
        validate_profile(profile)
        return profile


def build_site() -> None:
    """Render the site into the dist directory."""
    profile = load_profile()

    environment = Environment(
        loader=FileSystemLoader(TEMPLATES_DIR),
        autoescape=select_autoescape(["html", "xml"]),
        undefined=StrictUndefined,
    )

    template = environment.get_template("index.html")
    rendered_html = template.render(**profile)

    OUTPUT_DIR.mkdir(exist_ok=True)

    output_file = OUTPUT_DIR / "index.html"
    output_file.write_text(rendered_html, encoding="utf-8")

    output_static_dir = OUTPUT_DIR / "static"
    if output_static_dir.exists():
        shutil.rmtree(output_static_dir)

    shutil.copytree(STATIC_DIR, output_static_dir)

    print(f"Built site: {output_file}")


if __name__ == "__main__":
    build_site()
