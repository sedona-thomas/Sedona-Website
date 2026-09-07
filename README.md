# Sedona Thomas's Personal Website

A lightweight portfolio website generator that creates fast, responsive, static websites using HTML and CSS.

The site is generated with Jinja templates using portfolio data stored in JSON. An example portfolio generated with this project is available at [sedonathomas.com](https://www.sedonathomas.com).

The generated website requires no backend, database, Node.js runtime, or complex client-side JavaScript. It can be hosted on any standard web server.

## Features

- Generate a responsive personal portfolio website from a reusable Jinja template
- Build a simple HTML page for static content that can be hosted without complex client-side JavaScript
- Customize name, bio, projects, skills, contact details, etc.
- No database or server required for generated website

## Requirements

- `python>=3.0`
- requirements.txt dependencies

## Usage

Portfolio content is stored in `portfolio.json`, and the website layout is defined using Jinja templates in the `templates/` directory.

### Create a virtual environment

Create a Python virtual environment in the project directory and activate it:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

After activation, your terminal should show `(.venv)` before the command prompt.

### Install the dependencies

Install the project dependencies with: `python3 -m pip install -r requirements.txt`

### Update your portfolio data

Make a file `./portfolio.json`. A blank example can be found under `./blank_portfolio.json`

Add your personal information to the appropriate sections. Refer to the JSON schema definition for more complex options

### Build the website

Run the build script: `python3 build.py`

The script uses the JSON data and Jinja templates to generate the static website.

The generated files will be placed in: `dist/`

### Preview the website locally

Open the generated webpage in a browser: `dist/index.html`

### Deploy the website

Upload the contents of the `dist/` directory to any static hosting provider.

