# RepoSense AI
### Powered by RADA – Repository Analysis & Debugging Assistant

### IDEA
RepoSense is an AI-powered system designed to analyze and understand complete software repositories instead of isolated code snippets.

The platform uses RADA (Repository Analysis & Debugging Assistant) to scan project structures, analyze dependencies, and provide contextual debugging assistance.

The goal of this project is to help developers and students better understand complex codebases and reduce debugging time.

### PROBLEM
Modern AI coding assistants typically analyze small code snippets pasted by users.

However, real software systems consist of multiple interconnected files and modules. Bugs often originate from interactions between these files, making them difficult to detect when analyzing code in isolation.

This limitation makes debugging large repositories slow and inefficient.


### SOLUTION
RepoSense introduces a repository-level AI assistant.

Instead of analyzing single files, the system scans entire repositories, maps file relationships, and builds contextual knowledge about the project.

RADA then uses this context to provide debugging insights, explanations, and developer assistance.


### KEY FEATURES
• Repository Structure Analysis
• Cross-File Dependency Mapping
• Context-Aware Debugging
• Teacher Mode for Students
• Developer Mode for Advanced Debugging
• Repository Summary Generation


### WORK FLOW
1. User provides GitHub repository link
2. Repository is scanned and analyzed
3. Code structure is extracted using AST parsing
4. Dependencies between modules are mapped
5. Context engine builds a project knowledge graph
6. RADA AI analyzes queries and provides insights


### PROTOTYPE IMPLEMENTATION
This repository includes a conceptual prototype implementation of the RepoSense system.

The prototype demonstrates:

• repository scanning
• code structure analysis
• dependency mapping
• AI reasoning simulation


### FUTURE IMPROVEMENTS
• Integration with IDEs like VS Code
• Automated bug detection
• Repository visualization tools
• CI/CD pipeline analysis


### AUTHOR
Harshit Khanna AND Nishant
BCA Student
