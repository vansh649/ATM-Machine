## VITYARTHI PROJECT

## Bank / ATM Management System

## 1. Project Overview

This is a simple Python-based Bank/ATM Management System that allows a user to securely access their bank account using a PIN and perform basic banking operations. The project demonstrates variables, loops, conditional statements, user input, and arithmetic operations.

## 2. Features

- PIN Authentication: The user gets a maximum of 3 attempts. After 3 incorrect attempts, the card is blocked.

- Display Account Number: The user can view the account number after successful authentication.

- Deposit Money: A deposit amount is added to the existing bank balance and the updated balance is displayed.

- Withdraw Money: The user can enter an amount to withdraw and the program performs a balance check.

- Check Bank Balance: The current bank balance can be displayed.

## 3. Technologies Used

- Python

- Variables

- input() and print()

- if-elif-else

- while loops

- Arithmetic operators

- User authentication

- Basic banking operations

## 4. Program Flow

```
START
|
v
Enter PIN
|
+-- Correct PIN --> Welcome User --> Banking Menu
|
+-- Wrong PIN --> Attempts Decrease
|
+-- Attempts Remaining --> Try Again
|
+-- 0 Attempts --> Card Blocked
```

Banking Menu:


- 1. Account Number

- 2. Deposit

- 3. Withdrawal

- 4. Check Balance

## 5. PIN Authentication

The program first asks the user to enter their PIN. The number of available attempts is initialized to 3. If the entered PIN is correct, the program displays “WELCOME USER”. If it is incorrect, the number of remaining attempts decreases. After all attempts are exhausted, the program displays “YOUR CARD HAS BEEN BLOCKED”.

## 6. Banking Operations

| Option | Operation | Description |
| --- | --- | --- |
| Option 1 | Account Number | Displays the user's account number. |
| Option 2 | Deposit | Accepts a deposit amount, adds it to the current balance, and displays the new balance. |
| Option 3 | Withdrawal | Accepts a withdrawal amount and performs the program's balance check before displaying the |
| Option 4 | Balance | Displays the current bank balance. |

## 7. How to Run

Make sure Python is installed, then open VITYARTHI PROJECT.py in VS Code, PyCharm, IDLE, or another Python-supported editor.

```
python --version
python "VITYARTHI PROJECT.py"
```

## 8. Example

```
enter your pin: 2410
WELCOME USER
enter a number between 1 to 4: 4
20000
```

## 9. Learning Objectives

- Take input from users

- Use variables

- Understand loops

- Use conditional statements

- Implement a basic authentication system

- Use arithmetic operations for transactions

- Design a menu-driven Python program

## 10. Important Note


This project is intended for educational purposes only. It should not be used as a real banking application because sensitive information such as the PIN and account details are directly stored in the Python source code. A real banking system would require secure authentication, encrypted data storage, transaction validation, database management, and proper security practices.

## 11. Project Details

| Project Name | VITYARTHI PROJECT |
| --- | --- |
| Language | Python |
| Project Type | Beginner Banking / ATM Management System |
| Purpose | Educational / Academic Project |
