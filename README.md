# Expense Tracker CLI

A simple, modular command-line interface (CLI) application to manage personal finances. This project allows users to track their expenses directly from the terminal, storing data persistently in a JSON file.

## Features

* **Add Expense:** Add a new expense with a description and amount.
* **Update Expense:** Update the amount of an existing expense using its ID.
* **Delete Expense:** Remove an expense from the records using its ID.
* **List Expenses:** View a formatted list of all recorded expenses.
* **Expense Summary:** View the total sum of all expenses.
* **Monthly Summary:** View the total expenses for a specific month.
* **Persistent Storage:** Data is automatically saved and retrieved from `expens.json`.

## Project Structure

* `main.py`: The entry point of the application containing the CLI argument parsing and core logic.
* `datafile_options.py`: A separate module handling database operations (reading/writing JSON files) for better modularity.
* `expens.json`: The database file where expense records are stored (automatically generated).

## Prerequisites

* Python 3.x

No external libraries are required. The project relies entirely on Python's standard library (`sys`, `json`, `os`, `datetime`).

## Usage

Run the application through your terminal or command prompt using the `python` command.

### 1. Add an Expense
    python main.py add --description "Lunch" --amount 20

### 2. List All Expenses
    python main.py list

*Output Example:*
    #        ID           Date           Description           Amount
    # 1  2024-08-06  Lunch  20

### 3. Update an Expense
    python main.py update --id 1 --amount 25

### 4. Delete an Expense
    python main.py delete --id 1

### 5. View Summary (All)
    python main.py summary

### 6. View Summary (By Month)
*(Example for August - 8th month)*
    python main.py summary --month 8

## Author
**Məhəmməd İsmayılzadə**
