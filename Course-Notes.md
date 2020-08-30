# Data 690 Class 1 Notes 20200828
## Ways to Run Python Code:
1. Use Interactive Python Shell (Interpreter)
- Python.org
2. Python Scripts through Command Line
3. Use Jupyter Notebooks/ cloud based computing 
- Notebooks.ai: *For this class we will be using notebooks.ai*
- This is a unic machine in the cloud which uses linux 
- Jupyter: (Julia, Python and R) 


## Some Basic Python Comands 
1. REPL: Read, Execute, Print, Loop 
2. Print comand: print ("Hello World") 
3. ls= dir: list files
4. Python space file.py will run that files code 
5. Shift Enter will execute a cell


## Git Hub
1. Use to keep code organized 
2. Good to make portfolio

# Python for Data Analysis-notes
# Chapter 1 Preliminaries 
## Kinds of Data 
   1. Tabular or spreadsheet like: String, Numeric, Date or Otherwise
   2. Multidimensional Arrays (matrices) 
   3. Multiple tables of data interrelated by key columns
   4. Evenly or unevenly spaced time series 

## Why Python for Data Analysis 
   1. Success in scientific computing due to the easy ability to integrate C, C++ and FORTRAN
   2. Suitable for not only research and prototyping but also building production systems in essence solving the "two-language problem"

## Essential Python Libraries 
   1. NumPy
   2. Pandas
   3. matplotlib
   4. IPython and Jupyter 
   5. SciPy
   6. Scikit-learn
   7. Statsmodels

# Chapter 2 Python Language Basics, IPython and Jupyter Notebooks

## The Python Interpreter
1. Interpreted language --> The python interpreter runs a program by executing one statement at a time. 
     - to run a py file execute the following command python file.py
## IPython Basics 
1. Running the IPython Shell
    - You can launch the IPython shell on the command line same as launching the regular Python interpreter 
    - object? -> Details about 'object', use 'object??' for extra details.
     - you can execute python statements by typing them and pressing return 
2. Running the Jupyter Notebook 
      - a type of interactive document for code, text (with or without markup), data visualizations, and other output. 
      - The Jupyter notebook interacts with kernels (implementations of the Jupyter interactive computing protocol in any number of programming languages)
3. Tab Completion 
      - While entering expressions in the shell, pressing the Tab key will search for any variables (objects, functions, etc.) matching the characters typed so far
4. Introspection 
      - Using a question mark (?) before or after a variable to show general info about the object (referred to as *object introspection*) 
5. The %run Command 
      - You can run any file as a Python program inside the environment of your session using the %run command.
      - In the Jupyter notebook use %load magic function, which imports a script into a code cell
 6. Executing Code from the Clipboard
      - %paste takes whatever text is in the clipboard and executes it as a single block in the shell. %cpaste gives you a special prompt for pasting code into 

## Python Language Basics 

1. Language semantics 
    - ***Indentations not braces***: A colon denotes the start of indented code block after which all of the code must be indented by the same amount.
    - ***Everything is an object***: Every number, string, data structure, function, class, module, and so on exists in the Python interpreter in its own box which is referred to as a Python object. 
    - ***Comments*** # ignored by python code
    - ***Function and object method cells*** using parentheses 
    - ***Variables and argument passing*** 
    - ***Dynamic references, Strong types*** 
    - ***Attributes and Methods**: other python objects stored inside the object/ functions associated with an object can have access to the objects internal data
    - ***Duck typing**: not caring about the type of an object as long as it has certain methods or behavior
    - ***Imports***: We can access the variables and functions defined in file.py, from another file in the same directory though import function
    - ***Binary operators and comparisons***: math operations and comparisons as normal
    - ***Mutable and immutable objects***:most objects and values can be modified some strings and tuples are not able to be modified   
 2. Scalar types 
     - Small set of built-in types for handling numerical data, strings, boolean (True or False) values, and dates and time.
    - Numeric types: Int(Arbitrary precision signed integer) and Float (Double-precision, floating-point number)
    - Strings: str can use single or double quotes
    - Bytes and Unicode
    - Booleans: true or false comparisons
    - Type casting: can cast values to the different types 
    - None: null value type
    - Dates and times: built-in date and time module 
3. Control Flow 
    - if elif and else: key words for conditional logic
    - For loops: iterating over a collection 
    - while loops: specifies a condition to be executed until it is false or until it is ended with a break 
    - pass: "no-op statement in python used as a place holder" 
    - range: yields evenly spaced integers
    - ternary expressions: combine an if-else block 
