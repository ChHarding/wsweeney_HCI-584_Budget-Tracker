# Expense Tracker Project

<style>
    h1, h2, h3, p {
        font-family: Arial, sans-serif;
    }
    h1 {
        color: #2e6da4;
    }
    h2 {
        color: #3c763d;
    }
    h3 {
        color: #a94442;
    }
    ul {
        list-style-type: none;
        padding: 0;
    }
    li {
        padding: 5px 0;
    }
    code {
        background-color: #f7f7f9;
        padding: 2px 4px;
        border-radius: 4px;
        font-size: 14px;
    }
    .important {
        color: #d9534f;
    }
</style>

## Table of Contents
<ul>
    <li><a href="#introduction">Introduction</a></li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#setup">Setup</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#troubleshooting">Troubleshooting</a></li>
    <li><a href="#limitations">Limitations</a></li>
    <li><a href="#developer-documentation">Developer Documentation</a></li>
</ul>

## Introduction
<p>Welcome to the Expense Tracker! This project is designed to help you, esteemed user, manage and track your expenses efficiently. You can add, view, summarize, and delete expenses, and view summaries by category.</p>

## Installation
<p>Assuming you have cloned or downloaded the repository into a folder, please follow the steps below to set up and use the Expense Tracker.</p>

## Setup
1. <strong>Python Environment</strong>: Please ensure you have Python 3.6 or higher installed. You can download it from <a href="https://www.python.org/downloads/" target="_blank">python.org</a>.
2. <strong>Dependencies</strong>: Kindly install the required dependencies. Navigate to the project folder and run:
   <pre><code>pip install -r requirements.txt</code></pre>

## Usage
<p>To run the Expense Tracker, please execute the main script:</p>
<pre><code>python main.py</code></pre>

### Main Menu
<p>Upon running the script, you will see the following options:</p>
<ol>
    <li>Add an expense to a new file</li>
    <li>Summarize a file by category</li>
    <li>Add an expense to an existing file</li>
    <li>View the content of a file</li>
    <li>Delete a file</li>
    <li>Summarize all files by category</li>
    <li>Exit</li>
</ol>
<p>Please enter the corresponding number to select a task.</p>

### Adding an Expense
<ul>
    <li>Select option <code>1</code> to add an expense to a new file.</li>
    <li>Enter the date in the format <code>mm-dd-yyyy</code>.</li>
    <li>Provide the details for the expense, including name, amount, and category.</li>
    <li>Continue adding expenses or exit.</li>
</ul>

### Summarizing a File
<ul>
    <li>Select option <code>2</code> to summarize a file by category.</li>
    <li>Choose the file date from the list.</li>
    <li>View the summarized expenses by category and total amount.</li>
</ul>

### Adding an Expense to an Existing File
<ul>
    <li>Select option <code>3</code>.</li>
    <li>Choose the file date from the list.</li>
    <li>Add expenses as described in "Adding an Expense".</li>
</ul>

### Viewing File Content
<ul>
    <li>Select option <code>4</code>.</li>
    <li>Choose the file date from the list.</li>
    <li>View all expenses in the selected file.</li>
</ul>

### Deleting a File
<ul>
    <li>Select option <code>5</code>.</li>
    <li>Choose the file date from the list.</li>
    <li>Confirm deletion.</li>
</ul>

### Summarizing All Files
<ul>
    <li>Select option <code>6</code>.</li>
    <li>View a summary of all expenses by category and total amount.</li>
</ul>

## Troubleshooting
<p>Here are some common issues you might encounter:</p>
<ul>
    <li><strong>Invalid Task</strong>: If you enter an invalid task number, you will see an <span class="important">"Invalid task. Please try again!"</span> message.</li>
    <li><strong>File Not Found</strong>: Ensure the file name is correct when accessing existing files.</li>
    <li><strong>Invalid Date Format</strong>: Enter the date in <code>mm-dd-yyyy</code> format.</li>
</ul>

## Limitations
<p>Please note the following limitations:</p>
<ul>
    <li>The budget is currently fixed at $2000. This can be made dynamic if needed.</li>
    <li>The application only supports <code>.pkl</code> file format for storing expenses.</li>
</ul>

## Developer Documentation
<p>For more technical details and development guidelines, please refer to the <a href="developer_documentation.md">Developer Documentation</a>.</p>

### Example Screenshots
<img src="path_to_screenshot/main_menu.png" alt="Main Menu" />
<img src="path_to_screenshot/add_expense.png" alt="Add Expense" />
<img src="path_to_screenshot/summary.png" alt="Summary" />

### Notes
<ul>
    <li>Ensure all expense files are in the same directory as the script.</li>
    <li>Future versions may include enhancements like dynamic budgets and additional file formats.</li>
</ul>

<p>For detailed technical information and advanced usage, kindly refer to the developer documentation.</p>
