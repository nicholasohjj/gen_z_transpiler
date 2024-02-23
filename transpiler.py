import re
import sys
import subprocess
import asyncio

def transpile_code(source_code):
    """Transpile custom keywords in the source code to standard Python."""
    # Extended slang mappings
    slang_mappings = {
        r'\byeet\b': 'print',
        # Control flow
        r'\blowkey\b': 'if',  # If condition
        r'\bhighkey\b': 'else',  # Else condition
        r'\bwhat if\b': 'elif',  # Elif condition
        r'\bon repeat\b': 'for',  # For loop
        r'\bchillin\b': 'while',  # While loop
        r'\bnext\b': 'continue',  # Continue loop
        r'\bsnack\b': 'break',  # Break loop
        r'\byolo\b': 'pass',  # Pass statement
        r'\bghost\b': 'pass',  # Alternative to pass
        r'\btryna catch\b': 'try',  # Try block
        r'\bbusted\b': 'except',  # Except block
        r'\bfinally tho\b': 'finally',  # Finally block
        r'\bno cap\b': 'assert',  # Assert statement
        r'\bbruh\b': 'raise',  # Raise exception

        # Functions and classes
        r'\bbig brain\b': 'def',  # Define a function
        r'\bsquad\b': 'class',  # Define a class
        r'\bhomies\b': 'from',  # From import statement
        r'\bflex\b': 'import',  # Import statement
        r'\bspill the tea\b': 'return',  # Return statement
        r'\bsquad goals\b': 'global',  # Global declaration
        r'\blocal vibes\b': 'nonlocal',  # Nonlocal declaration
        r'\byield from the heart\b': 'yield from',  # Yield from
        r'\bshare\b': 'yield',  # Yield statement

        # Boolean and comparisons
        r'\bwoke\b': 'True',  # True
        r'\bbasic\b': 'False',  # False
        r'\bnot even\b': 'not',  # Not
        r'\band also\b': 'and',  # And
        r'\bor like\b': 'or',  # Or
        r'\bis legit\b': 'is',  # Is
        r'\bin the crew\b': 'in',  # In

        # Others
        r'\blit\b': 'del',  # Delete statement
        r'\bcatching vibes\b': 'with',  # With statement
        r'\bas if\b': 'as',  # As statement
        r'\bdoing the most\b': 'async',  # Async declaration
        r'\bwaiting on\b': 'await',  # Await statement
        r'\bghosting\b': 'lambda',  # Lambda function
        r'\bquick maths\b': 'lambda',  # Lambda function
    }
    
    # Apply mappings
    transpiled_code = source_code
    for slang, py_equiv in slang_mappings.items():
        transpiled_code = re.sub(slang, py_equiv, transpiled_code)
    
    return transpiled_code

def execute_transpiled_code(transpiled_code):
    """Execute the transpiled Python code, handling async functions."""
    try:
        # Define a namespace for execution
        local_namespace = {}
        exec(transpiled_code, {"__builtins__": __builtins__, "asyncio": asyncio}, local_namespace)
        
        # Check for async functions and run them
        for name, obj in local_namespace.items():
            if asyncio.iscoroutinefunction(obj):
                loop = asyncio.get_event_loop()
                loop.run_until_complete(obj())
    except Exception as e:
        print(f"Error executing transpiled code: {e}")



def main(input_file_path):
    """Main function to read, transpile, and execute a Python file."""
    try:
        with open(input_file_path, 'r') as file:
            source_code = file.read()
        transpiled_code = transpile_code(source_code)
        print("Transpiled Code:\n", transpiled_code)  # Optionally print the transpiled code for verification
        execute_transpiled_code(transpiled_code)
    except FileNotFoundError:
        print(f"The file {input_file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python transpiler.py <path_to_your_python_file>")
        sys.exit(1)
    input_file_path = sys.argv[1]
    main(input_file_path)
