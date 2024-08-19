# AILang

*Work in progress!!*

AILang is an interpreted, declarative, non-deterministic programming language designed to streamline the creation, management, and optimization of codebases. By leveraging artificial intelligence, AILang provides a user-friendly interface that distills complex programming tasks into intuitive commands.

## Getting Started

### Prerequisites

- Python 3.8 or higher

### Installation

Clone the repository:

```sh
git clone https://github.com/TurbulentRice/AILang.git
cd AILang
pip install -r requirements.txt
```

### Run the interpreter

`python main.py`

## Usage

### General Syntax

AILang commands follow this general formula:
`[action] [subject] [type] [...args] -p ["prompt"] [path]`

### Actions

Actions specify what operation to perform. Here are the available actions:

	•	create: Create a new entity (project, file, directory, config).
	•	delete: Delete an existing entity (project, file, directory, config).
	•	update: Update dependencies or settings.
	•	run: Execute a script, command, or application.
	•	test: Run tests on code.
	•	build: Build a project or code.
	•	deploy: Deploy an application or service.
	•	analyze: Analyze code, logs, or data.
	•	fix: Fix code or configuration issues.

### Subjects

Subjects define what the action is performed on. Here are the allowed subjects for each action:

	•	project: A software project (node, python, java).
	•	file: A file (html, css, json, yaml).
	•	directory: A directory.
	•	config: Configuration files or settings.
	•	dependencies: Project dependencies (npm, pip).
	•	settings: Project settings.
	•	script: A script file (shell, python, node).
	•	command: Command-line commands.
	•	app: An application.
	•	service: A service.
	•	code: Source code.
	•	logs: Log files.
	•	data: Data files.
	•	docs: Documentation.
	•	report: Reports.

### Types

Types further specify the nature of the subject. Here are the allowed types for some subjects:

	•	project: node, python, java.
	•	file: html, css, json, yaml.
	•	dependencies: npm, pip.
	•	script: shell, python, node.

### Arguments

Arguments modify the action’s behavior. Here are the common arguments:

	•	-p: A prompt that provides additional instructions for the AI.
	•	-v: Specify the version (e.g., latest).
	•	-n: Specify the name (e.g., project name).
	•	-t: Specify a tag.

### Examples

```sh
# Create a Node.js project of the latest version named “my_project” in the current directory
create project node -v latest -n my_project -p "basic api with jwt token authentication" ./

# Convert JavaScript code to TypeScript:
convert code javascript typescript -p "use best practices" ./

# Analyze code for security vulnerabilities
analyze code -p "identify security vulnerabilities" ./

# Update DotNet dependencies
update dependecies dotnet ./

# Run a Python script in the current directory
run script python -p "convert all jpeg files to 16-bit png format" ./
```
