from __future__ import annotations

import json
import shutil
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, StrictUndefined, select_autoescape
from jsonschema import Draft202012Validator
from referencing import Registry, Resource


ROOT_DIR = Path(__file__).resolve().parent
SCHEMAS_DIR = ROOT_DIR / "schemas"

DATA_FILE = ROOT_DIR / "portfolio.json"
TEMPLATES_DIR = ROOT_DIR / "templates"
STATIC_DIR = ROOT_DIR / "static"
OUTPUT_DIR = ROOT_DIR / "dist"

ROOT_SCHEMA_FILE = SCHEMAS_DIR / "portfolio.schema.json"
PERMISSIONS_SOURCE = ROOT_DIR / "CUNIX" / "permissions.txt"


def _load_schema_registry(
        schema_dir: Path,
) -> tuple[dict[str, dict], Registry]:
    schemas: dict[str, dict] = {}
    registry = Registry()

    for schema_path in schema_dir.glob("*.schema.json"):
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        schema_uri = schema_path.resolve().as_uri()

        # Give each schema a stable URI so relative $ref values resolve correctly.
        schema["$id"] = schema_uri
        schemas[schema_path.name] = schema

        registry = registry.with_resource(
            schema_uri,
            Resource.from_contents(schema),
        )

    return schemas, registry


def validate_profile(profile: dict) -> None:
    schemas, registry = _load_schema_registry(SCHEMAS_DIR)
    root_schema_name = ROOT_SCHEMA_FILE.name

    try:
        root_schema = schemas[root_schema_name]
    except KeyError as exc:
        raise FileNotFoundError(
            f"Missing root schema: {ROOT_SCHEMA_FILE}"
        ) from exc

    validator = Draft202012Validator(
        root_schema,
        registry=registry,
    )
    validator.validate(profile)


def load_profile() -> dict:
    """Load and validate website content from the JSON file."""
    profile = json.loads(DATA_FILE.read_text(encoding="utf-8"))
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

    rendered_html = environment.get_template("index.html").render(**profile)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    output_file = OUTPUT_DIR / "index.html"
    output_file.write_text(rendered_html, encoding="utf-8")

    output_static_dir = OUTPUT_DIR / "static"
    shutil.rmtree(output_static_dir, ignore_errors=True)
    shutil.copytree(STATIC_DIR, output_static_dir)

    shutil.copy2(
        PERMISSIONS_SOURCE,
        output_static_dir / PERMISSIONS_SOURCE.name,
        )

    print(f"Built site: {output_file}")


if __name__ == "__main__":
    build_site()
