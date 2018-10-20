# Variables


Variables are names of your choice to store values which will be used later on in your code.  
In Python there are few limitation regarding the variables names.

You **can't** use any of the words below

```python
>>> import keyword
>>> keyword.kwlist

['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 
'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 
'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 
'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```

### Recommanded rules 
source: [Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/#method-names-and-instance-variables)  

- Use the function naming rules: lowercase with words separated by underscores as necessary to improve readability.
- Use one leading underscore only for non-public methods and instance variables.
- To avoid name clashes with subclasses, use two leading underscores to invoke Python's name mangling rules.
- Variables names **must** start with a letter or an underscore **only**.
- The rest of the name may contain letters, numbers and underscores.
- Variable names are **case sensitive**.

### Using variables

```python
>>> first_name = "Dart"
>>> last_name = "Weider"
>>>
>>> print("Your name is: " + first_name +", " + last_name)
Your name is: Dart, Weider
>>>

```



[Previous page](/Chapters/01-DataTypes/0102-Operators.md) | [List of contents](/README.md#chapters) | [Next Page](/Chapters/01-DataTypes/0104-If-Else.md) | 

&copy; 2018 CodeWizardAcademy, Inc.

