# Project Spec for Budget Tracker

### General description of the project (2 pts)
- The budget tracker project aims to help users manage their finances by tracking income, expenses, and savings to promote financial stability.
- Key features include income and expense logging, category-wise spending analysis, budget setting, and visual reports for spending patterns and budget adherence.
- Major packages used will include Pandas for data manipulation, Matplotlib/Seaborn for visualization, and possibly Flask/Django for web development, along with potential integration of financial APIs like Plaid and email services for summaries and alerts.
- The project will ideally feature a user-friendly GUI using frameworks like Tkinter for desktop or React for web applications, allowing intuitive navigation and interaction.
- It will also support a minimal Command Line Interface (CLI) for basic functionality and offer an API endpoint for remote control and integration with other applications.

--------------------------------------------------------------------------------------

### Task Vignettes (User activity "flow") (4 pts)
- Vignette 1: Logging an Expense
  - Sarah just bought groceries and wants to log this expense in her budget tracker. She opens the application and navigates to the 'Add Expense' section. Sarah inputs the date, selects the category as 'Groceries', enters the amount spent, and adds a brief description. She then clicks 'Save', and the expense is recorded in her account, updating her total expenditure and adjusting her remaining budget for the month.

  - Technical Details:
    - User Input: Date, category selection, amount, description
    - Backend: Data validation, storage in database
    - Frontend: Form for input fields, save button
  - Data Flow: User input -> Application UI -> Backend (Database)
 
- Vignette 2: Viewing Monthly Summary
  - At the end of the month, Sarah wants to review her spending. She navigates to the 'Monthly Summary' section of the budget tracker. The application displays a pie chart showing expenses by category, a bar graph for income vs. expenses, and a line chart tracking daily expenditures. Sarah can see at a glance where most of her money went and how well she stuck to her budget.

  - Technical Details:
    - User Interaction: Selection of the month, viewing graphical summaries
    - Backend: Data retrieval, aggregation of monthly data
    - Frontend: Charts and graphs display using libraries (e.g., Matplotlib/Seaborn)
    - Data Flow: Database query -> Data processing -> Visualization on UI
    
- Vignette 3: Setting a Budget
  - At the beginning of the month, Sarah decides to set a new budget. She opens the 'Set Budget' section, selects categories such as 'Groceries', 'Entertainment', 'Utilities', and assigns a budget limit to each. After setting the limits, she clicks 'Save', and the application stores these limits and starts tracking expenses against these budgets.

  - Technical Details:
    - User Input: Category selection, budget limits for each category
    - Backend: Storage of budget limits, initialization of tracking mechanism
    - Frontend: Form for input fields, save button
    - Data Flow: User input -> Application UI -> Backend (Database)
      
- Vignette 4: Receiving Budget Alerts
  - Sarah has set up budget alerts to stay informed about her spending. One day, she receives an email notification that she has spent 80% of her budget for 'Dining Out'. The email includes a summary of her recent dining expenses and suggests reviewing her spending habits. Sarah appreciates the timely alert and decides to cut back on dining out for the rest of the month.

  - Technical Details:
    - User Interaction: Setting alert thresholds, receiving email alerts
    - Backend: Monitoring expenses, triggering alerts when thresholds are met
    - Frontend: Email template, summary report generation
    - Data Flow: Expense tracking -> Threshold checking -> Email notification system
      
- Vignette 5: Importing Transactions from Bank
  - Sarah wants to quickly update her budget tracker with the latest transactions from her bank account. She navigates to the 'Import Transactions' section, selects her bank, and logs in. The application fetches her recent transactions and displays them for review. Sarah confirms and categorizes the transactions, then clicks 'Import', integrating the data into her budget tracker.

  - Technical Details:
    - User Interaction: Bank selection, login, transaction review and confirmation
    - Backend: API integration with bank, secure data retrieval
    - Frontend: Import interface, transaction review UI
    - Data Flow: Bank API -> Secure data transfer -> User review -> Database update
    - These vignettes illustrate a seamless and user-friendly experience for managing personal finances, leveraging both a GUI and backend processes to ensure smooth operation and effective financial tracking.

--------------------------------------------------------------------

### Technical "flow" (3 pts)
                        +-----------------------+
                        |  User Input Interface |
                        +-----------------------+
                                  |
                                  v
                       +----------------------+
                       | Data Validation      |
                       +----------------------+
                                  |
                                  v
                      +------------------------+
                      | Database Management    |
                      +------------------------+
                                  |
                                  v
                    +----------------------------+
                    | Data Aggregation Engine    |
                    +----------------------------+
                                  |
       +-------------+------------+-------------+---------------+
       |             |            |             |               |
       v             v            v             v               v
+-------------+ +-----------+ +--------+ +-------------+ +--------------+
| Visual      | | Budget    | | API     | | Transaction | | Notification |
| Reports     | | Alerts    | | Integration| | Review   | | Interface    |
+-------------+ +-----------+ +--------+ +-------------+ +--------------+

- Data Types in the Flow
    - User Inputs: Dictionary (with keys like date, category, amount, description)
    - Data Validation: Boolean (valid/invalid)
    - Database Management: SQL/NoSQL database entries (depending on implementation)
    - Data Aggregation: List of dictionaries (for summaries), arrays (for chart data)
    - API Integration: JSON data (from financial APIs)
    - Visual Reports: Graphical data (arrays for plotting)
    - Budget Alerts: Strings (email content)
    - Transaction Review: List of transactions (dictionaries)
- User Interaction Details
    - Input Forms: User interaction involves text input, selection from dropdowns, and button clicks.
    - Visualization Dashboard: User views graphs and charts, interacts with filters (if implemented).
    - Notification Interface: User receives email alerts, views summary notifications within the app.
    - Transaction Review: User categorizes transactions, confirms imports.
------------------------------------------------------------

