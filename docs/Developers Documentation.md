<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Developer Documentation for Expense Tracker Project</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
            background-color: #f4f4f4;
            color: #333;
        }
        h1, h2, h3 {
            color: #2c3e50;
            border-bottom: 2px solid #3498db;
            padding-bottom: 5px;
        }
        h1 {
            font-size: 2em;
        }
        h2 {
            font-size: 1.5em;
        }
        h3 {
            font-size: 1.2em;
        }
        ul {
            list-style-type: disc;
            margin-left: 20px;
        }
        code {
            background-color: #ecf0f1;
            border: 1px solid #bdc3c7;
            border-radius: 4px;
            padding: 2px 4px;
            font-family: Consolas, Monaco, 'Andale Mono', 'Ubuntu Mono', monospace;
        }
        pre {
            background-color: #ecf0f1;
            border: 1px solid #bdc3c7;
            border-radius: 4px;
            padding: 10px;
            overflow-x: auto;
            font-family: Consolas, Monaco, 'Andale Mono', 'Ubuntu Mono', monospace;
        }
        .note {
            background-color: #dff0d8;
            border-left: 5px solid #3c763d;
            padding: 10px;
            margin: 10px 0;
            border-radius: 4px;
        }
        .warning {
            background-color: #f2dede;
            border-left: 5px solid #a94442;
            padding: 10px;
            margin: 10px 0;
            border-radius: 4px;
        }
    </style>
</head>
<body>
    <h1>Developer Documentation for Expense Tracker Project</h1>

    <h2>Table of Contents</h2>
    <ul>
        <li><a href="#overview">Overview</a></li>
        <li><a href="#project-structure">Project Structure</a></li>
        <li><a href="#installation-and-setup">Installation and Setup</a></li>
        <li><a href="#in-code-documentation">In-code Documentation</a></li>
        <li><a href="#user-interaction-and-flow">User Interaction and Flow</a></li>
        <li><a href="#known-issues">Known Issues</a></li>
        <li><a href="#future-work">Future Work</a></li>
        <li><a href="#ongoing-deploymentdevelopment">Ongoing Deployment/Development</a></li>
    </ul>

    <h2 id="overview">Overview</h2>
    <p>The Expense Tracker project is a simple application to help users manage and track their expenses. Users can add, view, summarize, and delete expenses, as well as view summaries by category. This documentation provides an in-depth guide for developers to understand the project structure, codebase, and workflow.</p>

    <h2 id="project-structure">Project Structure</h2>
    <pre><code>
ExpenseTracker/
│
├── docs/
│   ├── Review Doc.md
│   ├── spec.md
│   ├── developer_documentation.md
│
├── src/
│   ├── main.py
│   ├── expense_manager.py
│   ├── file_handler.py
│   ├── expense.py
│   ├── utils.py
│
├── requirements.txt
├── README.md
└── LICENSE
    </code></pre>
    <p>Here is a brief overview of the directory structure:</p>
    <ul>
        <li><strong>docs/</strong>: Contains user and developer documentation.</li>
        <li><strong>src/</strong>: Contains the main application code and modules.</li>
        <li><strong>tests/</strong>: Contains unit tests for the application.</li>
        <li><strong>requirements.txt</strong>: Lists the dependencies required for the project.</li>
        <li><strong>README.md</strong>: Provides an overview and instructions for users.</li>
        <li><strong>LICENSE</strong>: Contains the license information for the project.</li>
    </ul>

    <h2 id="installation-and-setup">Installation and Setup</h2>
    <ol>
        <li><strong>Clone the repository:</strong>
            <pre><code>git clone https://github.com/yourusername/ExpenseTracker.git
cd ExpenseTracker</code></pre>
        </li>
        <li><strong>Create a virtual environment:</strong>
            <pre><code>python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate</code></pre>
        </li>
        <li><strong>Install dependencies:</strong>
            <pre><code>pip install -r requirements.txt</code></pre>
        </li>
        <li><strong>Run the application:</strong>
            <pre><code>python src/main.py</code></pre>
        </li>
    </ol>

    <h2 id="in-code-documentation">In-code Documentation</h2>
    <p>Each module, class, and function in the codebase is documented with docstrings. Below is an overview of the key modules and their functionalities:</p>

    <h3>main.py</h3>
    <p>The entry point of the application. It contains the main loop and handles user input for different tasks.</p>

    <h3>expense_manager.py</h3>
    <p>Contains the <code>ExpenseManager</code> class which handles adding, viewing, and summarizing expenses.</p>

    <h3>file_handler.py</h3>
    <p>Contains functions for saving and loading expenses to and from files.</p>

    <h3>expense.py</h3>
    <p>Defines the <code>Expense</code> class representing an individual expense.</p>

    <h3>utils.py</h3>
    <p>Contains utility functions used across the application, such as formatting text.</p>

    <h2 id="user-interaction-and-flow">User Interaction and Flow</h2>
    <p>The application provides a menu-driven interface. Below is a brief recap of the user interaction flow:</p>
    <ul>
        <li><strong>Main Menu:</strong>
            <ul>
                <li>Add an expense to a new file</li>
                <li>Summarize a file by category</li>
                <li>Add an expense to an existing file</li>
                <li>View the content of a file</li>
                <li>Delete a file</li>
                <li>Summarize all files by category</li>
                <li>Exit</li>
            </ul>
        </li>
    </ul>

    <h3>Code Walkthrough</h3>
    <p>When the application starts, the user is presented with the main menu. Depending on the user’s choice, the corresponding function is called:</p>
    <ul>
        <li><strong>Adding an expense to a new file:</strong>
            <ul>
                <li><code>main.py</code>: <code>add_expense_to_new_file()</code></li>
                <li><code>expense_manager.py</code>: <code>ExpenseManager.add_expense()</code></li>
                <li><code>file_handler.py</code>: <code>save_expense_to_file()</code></li>
            </ul>
        </li>
        <li><strong>Summarizing a file by category:</strong>
            <ul>
                <li><code>main.py</code>: <code>summarize_file()</code></li>
                <li><code>expense_manager.py</code>: <code>ExpenseManager.summarize_expenses()</code></li>
            </ul>
        </li>
        <li><strong>Adding an expense to an existing file:</strong>
            <ul>
                <li><code>main.py</code>: <code>add_expense_to_existing_file()</code></li>
                <li><code>expense_manager.py</code>: <code>ExpenseManager.add_expense()</code></li>
                <li><code>file_handler.py</code>: <code>load_expense_from_file()</code>, <code>save_expense_to_file()</code></li>
            </ul>
        </li>
        <li><strong>Viewing the content of a file:</strong>
            <ul>
                <li><code>main.py</code>: <code>view_file_content()</code></li>
                <li><code>file_handler.py</code>: <code>load_expense_from_file()</code></li>
            </ul>
        </li>
        <li><strong>Deleting a file:</strong>
            <ul>
                <li><code>main.py</code>: <code>delete_file()</code></li>
                <li><code>file_handler.py</code>: <code>list_expenses()</code></li>
            </ul>
        </li>
        <li><strong>Summarizing all files by category:</strong>
            <ul>
                <li><code>main.py</code>: <code>summarize_all_files()</code></li>
                <li><code>expense_manager.py</code>: <code>ExpenseManager.summarize_all_expenses()</code></li>
            </ul>
        </li>
    </ul>

    <h2 id="known-issues">Known Issues</h2>
    <h3>Minor Issues</h3>
    <div class="note">
        <p><strong>Error handling:</strong> Input validation could be improved, particularly for numerical inputs.</p>
    </div>

    <h3>Major Issues</h3>
    <div class="warning">
        <p><strong>File operations:</strong> Concurrent access to the same file may cause issues.</p>
    </div>

    <h2 id="future-work">Future Work</h2>
    <h3>Enhancements</h3>
    <ul>
        <li>Implement a graphical user interface (GUI).</li>
        <li>Add support for exporting summaries to CSV or PDF.</li>
        <li>Integrate with external APIs for currency conversion.</li>
    </ul>

    <h3>Performance Improvements</h3>
    <ul>
        <li>Optimize file operations for large datasets.</li>
    </ul>

    <h2 id="ongoing-deploymentdevelopment">Ongoing Deployment/Development</h2>
    <p><strong>Unit Tests:</strong> Ensure all new features are covered by unit tests in the <code>tests/</code> directory.</p>
    <p><strong>Code Reviews:</strong> Regularly review code to maintain quality and consistency.</p>
    <p><strong>Documentation:</strong> Keep the documentation updated with any new changes or features.</p>
    <p><strong>Version Control:</strong> Use semantic versioning for releases to keep track of changes and updates.</p>
</body>
</html>
