# Intermediate Software Development Automated Teller Project
This project will be developed over the course of several assignments.  Each assignment will build on the work done in the previous assignment(s).  Ultimately, an entire system will be created to manage bank transactions for clients who have one or more bank accounts.

## Author
Jianbin Zhang

## Assignment
Assignment 1: Classes, Encapsulation and Unit Test Planning
Assignment 2: Abstraction, Inheritance and Polymorphism
Assignment 3: Design Patterns
Assignment 4: Programming Paradigms

## Encapsulation
Through encapsulation, the BankAccount class is able to protect the property antenna external interconnection and verify the legality of the input when necessary. Protect class attributes from direct external access and modification by controlling and verifying access and modification of attributes through methods. Use double underscores (__) to make attributes private, such as __balance and __account_number. Use methods to access private attributes. Use the @property decorator to implement read-only access and use the deposit and withdraw methods to update __balance.

## Polymorphism
Polymorphism allows different subclasses of BankAccount to define their own versions of a method while maintaining a common interface. This enables us to call the same method on different objects and get behavior specific to each subclass.

## Strategy Pattern
This strategy pattern in this application encapsulates the logic of overdraft fee calculation, management fee and minimum balance independently. It allows ChequingAccount, InvestmentAccount and SavingsAccount to select the appropriate calculation method through OverdraftStrategy, ManagementStrategy and MinimumBalance dynamically.

## Observer Pattern
The Observer Pattern in this application provides a structured approach to event-driven programming, ensuring that multiple objects (observers: client) can react to changes in another object (subject: chequing_account, savings_account, investment_account) without tightly coupling them. 

## Event-Driven Programming Paradigm
When the user clickes one of the (lookup, deposit, withdraw) buttons, the corresponding functions(on_lookup_client, on_apply_transaction) will be executed. 
The is an event-driven programming paradigm.