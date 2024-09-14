# Task Workflow System

This project consists of a task workflow system with two main components:
- A Flask web application that provides a user interface for processing queries and displaying results.
- A command-line script that allows users to interact with the system via the terminal.

## Project Structure

- `flask_app.py`: Contains the Flask web application code.
- `main_script.py`: Contains the command-line interface code.
- `langgraph.py`: Defines the `LangGraph` class for managing tasks.
- `plan_agent.py`: Defines the `PlanAgent` class for splitting queries into sub-tasks.
- `tool_agent.py`: Defines the `ToolAgent` class for solving tasks.
- `reflection.py`: Defines the `Reflection` class for providing feedback on tasks.
- `templates/`: Contains HTML templates for the Flask app.
  - `index.html`: Main page where users enter their queries.
  - `result.html`: Page that displays the results and feedback.
  - `style.css`: It contains CSS (Cascading Style Sheets) rules that control the layout, colors, fonts, spacing, and overall design of the web pages. By linking this stylesheet to your HTML files.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
