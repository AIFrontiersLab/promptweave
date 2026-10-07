# Promptweave

Proactively suggest relevant next steps in CLI interactions to reduce the 'blank page' problem.

# Code Intent MVP

A simple classifier for code-related intents.

## Usage
python -c "from main import demo; demo()"

## Tests
pytest -q

## Architecture

![Architecture](docs/architecture.png)

<details>
<summary>Mermaid source</summary>

```mermaid
flowchart LR
    A[User Query] --> B[Keyword Extraction]
    B --> C[Intent Classification]
    C --> D[Suggestion Generation]
    D --> E[Response]
```

</details>
