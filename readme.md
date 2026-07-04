# GitHub AI Checker

A Python desktop application that analyzes GitHub repositories to determine whether they use AI or machine learning.

The tool clones a public repository, scans its README, dependencies, and source code, then looks for AI-related libraries, APIs, models, and implementation patterns. Based on its findings, it generates an AI confidence score along with the evidence used to reach that conclusion.

## Planned Features

- Analyze any public GitHub repository
- Detect AI frameworks and APIs
- Classify the type of AI project
- Explain why a repository was flagged
- Export analysis reports

## Tech Stack

- Python
- Git
- PySide6 (GUI)
- scikit-learn / TensorFlow 
