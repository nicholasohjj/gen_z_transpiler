import re
import sys
import subprocess

def transpile_code(source_code):
    """Transpile custom keywords in the source code to standard Python."""
    # Extended slang mappings
    slang_mappings = {
        r'\byeet\b': 'print',
        r'\bbig brain\b': 'def',
        r'\bno cap\b': 'assert',
        r'\bon repeat\b': 'for',
        r'\bghost\b': 'pass',
        r'\blowkey\b': 'if',
        r'\bhighkey\b': 'else',
        r'\bsquad\b': 'class',
        r'\bbusted\b': 'except',
        r'\btryna catch\b': 'try',
        r'\bflex\b': 'import',
        r'\bspill the tea\b': 'return',
        r'\bsus\b': 'raise'
    }
    
    # Apply mappings
    transpiled_code = source_code
    for slang, py_equiv in slang_mappings.items():
        transpiled_code = re.sub(slang, py_equiv, transpiled_code)
    
    return transpiled_code


def execute_transpiled_code(transpiled_code):
    """Execute the transpiled Python code."""
    try:
        exec(transpiled_code, {"__builtins__": __builtins__}, {})
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