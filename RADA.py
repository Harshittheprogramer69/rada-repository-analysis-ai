"""
RepoSense Prototype System
RADA - Repository Analysis & Debugging Assistant

This prototype demonstrates how an AI system could analyze
an entire repository and provide debugging and explanation support.

NOTE:
This code is a conceptual prototype designed for demonstration
purposes in the InnovateX competition.
"""

import os
import ast
from typing import List, Dict

class RepositoryInputHandler:
    """
    Handles repository link input from the developer.
    """

    def __init__(self, repo_link: str):
        self.repo_link = repo_link

    def fetch_repository(self):
        """
        Simulates fetching repository from GitHub.
        In a real system this would clone the repository.
        """

        print("Fetching repository from:", self.repo_link)

        repo_path = "./sample_repository"

        print("Repository stored locally at:", repo_path)

        return repo_path


class RepositoryScanner:
    """
    Scans repository folders and files.
    """

    def __init__(self, repo_path: str):
        self.repo_path = repo_path
        self.files = []

    def scan_files(self):

        print("\nScanning repository structure...\n")

        for root, dirs, files in os.walk(self.repo_path):
            for file in files:

                if file.endswith(".py"):
                    full_path = os.path.join(root, file)
                    self.files.append(full_path)

        print("Files discovered:")
        for f in self.files:
            print(" -", f)

        return self.files



class CodeStructureAnalyzer:
    """
    Analyzes Python code structure using AST parsing.
    """

    def __init__(self):
        self.functions = {}
        self.classes = {}

    def analyze_file(self, file_path):

        print("\nAnalyzing structure of:", file_path)

        with open(file_path, "r") as f:
            code = f.read()

        tree = ast.parse(code)

        for node in ast.walk(tree):

            if isinstance(node, ast.FunctionDef):
                self.functions[node.name] = file_path

            if isinstance(node, ast.ClassDef):
                self.classes[node.name] = file_path

    def summary(self):

        print("\nDiscovered Functions:")
        for func in self.functions:
            print(" -", func)

        print("\nDiscovered Classes:")
        for cls in self.classes:
            print(" -", cls)


class DependencyMapper:
    """
    Maps relationships between modules and files.
    """

    def __init__(self):
        self.dependencies = {}

    def analyze_dependencies(self, file_path):

        with open(file_path, "r") as f:
            code = f.read()

        tree = ast.parse(code)

        imports = []
  
        for node in ast.walk(tree):

            if isinstance(node, ast.Import):
                for name in node.names:
                    imports.append(name.name)

            if isinstance(node, ast.ImportFrom):
                imports.append(node.module)

        self.dependencies[file_path] = imports

    def display_graph(self):

        print("\nRepository Dependency Graph\n")

        for file, deps in self.dependencies.items():

            print(file)

            for d in deps:
                print("   ->", d)


class ContextEngine:
    """
    Builds contextual knowledge about repository structure.
    """

    def __init__(self, functions, classes, dependencies):

        self.functions = functions
        self.classes = classes
        self.dependencies = dependencies

    def build_project_map(self):

        print("\nBuilding repository context map...\n")

        project_map = {
            "functions": self.functions,
            "classes": self.classes,
            "dependencies": self.dependencies
        }

        print("Project context successfully created.")

        return project_map


class RADAEngine:
    """
    Core AI reasoning engine of RepoSense.
    """

    def __init__(self, project_context):

        self.context = project_context

    def answer_query(self, query: str):

        print("\nDeveloper Question:", query)

        # Prototype response logic

        if "error" in query.lower():
            print("\nRADA Analysis:")
            print("Potential error may originate from function interactions.")
            print("Suggested files to inspect:")

            for func in list(self.context["functions"].keys())[:3]:
                print(" -", func)

        elif "explain" in query.lower():
            print("\nRADA Explanation Mode")
            print("Analyzing repository structure...")

            print("This project contains:")
            print(len(self.context["functions"]), "functions")
            print(len(self.context["classes"]), "classes")

        else:
            print("\nRADA Response:")
            print("Query understood but prototype reasoning is limited.")



class RADAModes:
    """
    Provides multiple operating modes for RADA.
    """

    def teacher_mode(self):

        print("\nTeacher Mode Activated")
        print("Explaining code in simplified learning format.")

    def developer_mode(self):

        print("\nDeveloper Mode Activated")
        print("Providing advanced debugging insights.")



def run_reposense_prototype():

    print("\n==============================")
    print("RepoSense AI Prototype System")
    print("Powered by RADA")
    print("==============================\n")

    repo_link = "https://github.com/example/project"

    # Step 1 : Repository Input
    repo_handler = RepositoryInputHandler(repo_link)
    repo_path = repo_handler.fetch_repository()

    # Step 2 : Repository Scan
    scanner = RepositoryScanner(repo_path)
    files = scanner.scan_files()

    # Step 3 : Code Structure Analysis
    analyzer = CodeStructureAnalyzer()

    for file in files:
        analyzer.analyze_file(file)

    analyzer.summary()

    # Step 4 : Dependency Mapping
    mapper = DependencyMapper()

    for file in files:
        mapper.analyze_dependencies(file)

    mapper.display_graph()

    # Step 5 : Build Context
    context_engine = ContextEngine(
        analyzer.functions,
        analyzer.classes,
        mapper.dependencies
    )

    project_context = context_engine.build_project_map()

    # Step 6 : RADA AI Engine
    rada = RADAEngine(project_context)

    rada.answer_query("Explain this project")
    rada.answer_query("Where could an error occur?")

    # Step 7 : Modes
    modes = RADAModes()
    modes.teacher_mode()
    modes.developer_mode()


if __name__ == "__main__":
    run_reposense_prototype()