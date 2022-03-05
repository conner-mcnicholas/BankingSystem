# BankingSystem
To run, execute: python Banking.py

Simple banking system for Springboard Python OOP mini-project

The Banking class is responsible for initializing and running the entire simulation
Some sample information is given to show a user the appropriate datatypes to be entering

This class in turn creates Customer, Account, and Loan instances.
Those require a user to enter information for name, id, and how much money should start in the account/loan.

The user can either visit an ATM, or visit a Teller.

ATM allows user to view their balance, deposit funds, withdraw funds.  Trying to remove too much funds will result in an error.
Teller allows user to pay off a loan (minimum amount or in full).  Min is calculated as total oustanding divided by months until deadline.

Both services run in a loop until the user explicitly exits

After exiting the session, a new table is printed to show that the banking system's database is updated with respect to the new customer we have added and their session transactions.
