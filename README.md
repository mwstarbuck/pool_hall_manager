U of H Pool Hall Table manager

 allows manager to checkout and close tables.  Tracks the time played for each table and prints out information for each session includding the cost. 

 Updates: Now includes DATA RECOVERY feature and menu choice confirmation to back out of user choice error.  More descriptive commenting

 TO RUN: 
  type -  python3 table_manager.py  


Modules:

Table manager --  handles all menu operations  -- handles all user entry

Table -- represents the actual pool tables and has all necessary attributes

Formatter -- handles all date and cost formatting for readability

Activity_log -- generates json files for billing and data recovery 
                handles loading of json file for recovery