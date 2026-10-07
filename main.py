"""MVP: Intent Classifier for Code Refactoring."""
import json
from typing import Dict, Any

def classify_intent(query: str) -> Dict[str, Any]:
    """Classify intent based on query keywords."""
    q = query.lower()
    features = {
        "has_code": "def " in q or "class " in q or ".py" in q,
        "has_commands": "git " in q or "npm " in q,
        "recent_commands": ["git status", "git add ."] if "git" in q else [],
        "query_length": len(q),
        "file_ext": ".py" if ".py" in q else ".js"
    }
    
    if "refactor" in q or "clean" in q or "optimize" in q:
        intent = "code_refactor"
    elif "test" in q or "assert" in q:
        intent = "test_generation"
    elif "doc" in q or "comment" in q:
        intent = "documentation"
    else:
        intent = "unknown"
        
    return {"features": features, "intent": intent}

def demo() -> str:
    """Run a demo classification."""
    result = classify_intent("refactor this python code")
    print(json.dumps(result, indent=2))
    return result["intent"]