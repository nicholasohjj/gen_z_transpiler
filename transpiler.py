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
        r'\bno cap\b': 'if',  # If condition, "no cap" means "seriously" or "for real"
        r'\bfacts\b': 'else',  # Else condition, "facts" is used to agree or confirm
        r'\bbet\b': 'elif',  # Elif condition, "bet" indicates agreement or acknowledgment
        r'\bvibe check\b': 'for',  # For loop, "vibe check" assesses the situation or atmosphere
        r'\bsimpin\b': 'while',  # While loop, "simpin" suggests a more focused, sometimes obsessive loop
        r'\bslide\b': 'continue',  # Continue loop, "slide" implies moving on smoothly
        r'\bdipped\b': 'break',  # Break loop, "dipped" means to leave abruptly
        r'\bsend it\b': 'pass',  # Pass statement, "send it" means to go for it or proceed without hesitation
        r'\bsend it\b': 'pass',  # Pass statement, "send it" means to go for it or proceed without hesitation
        r'\bsus\b': 'try',  # Try block, "sus" means suspect or suspicious, indicating caution
        r'\bcaught lackin\b': 'except',  # Except block, "caught lackin" means caught off guard
        r'\bwe gucci\b': 'finally',  # Finally block, "we gucci" means all is good or resolved
        r'\bpressed\b': 'assert',  # Assert statement, "pressed" means to insist or assert forcefully
        r'\bthrow shade\b': 'raise',  # Raise exception, "throw shade" means to criticize or express disdain

        # Boolean and comparisons
        r'\blit\b': 'True',  # True, "lit" remains popular for excitement or awesomeness
        r'\bsalty\b': 'False',  # False, "salty" means upset or bitter, indicating negativity
        r'\bghosted\b': 'not',  # Not, "ghosted" means ignored or excluded, suggesting negation
        r'\band I oop\b': 'and',  # And, "and I oop" adds dramatic pause or emphasis
        r'\bperiodt\b': 'or',  # Or, "periodt" signifies emphasis or finality, used for alternatives

        # Others
        r'\bcanceled\b': 'del',  # Delete statement, "canceled" means to reject or dismiss
        r'\bchill with\b': 'with',  # With statement, "chill with" implies association or collaboration
        r'\biconic\b': 'as',  # As statement, "iconic" signifies notable or significant alignment
        r'\blowkey flex\b': 'async',  # Async declaration, "lowkey flex" suggests a subtle, understated action
        r'\bhighkey waiting\b': 'await',  # Await statement, "highkey waiting" implies an eager or anxious wait
        r'\bsnatched\b': 'lambda',  # Lambda function, "snatched" means impressive or on point, signifying a concise function

                # Functions and classes
        r'\bglow up\b': 'def',  # Define a function, "glow up" signifies transformation or improvement
        r'\bgang gang\b': 'class',  # Define a class, "gang gang" expresses close association or teamwork
        r'\bstan\b': 'from',  # From import statement, "stan" means to support or admire
        r'\bflex\b': 'import',  # Import statement remains the same, as "flex" is still popular
        r'\btea\b': 'return',  # Return statement, "tea" means truth or gossip, suggesting returning info
        r'\bclout\b': 'global',  # Global declaration, "clout" symbolizes influence or power
        r'\bjuiced\b': 'nonlocal',  # Nonlocal declaration, "juiced" means energized or empowered
        r'\bhits different\b': 'yield',  # Yield statement, "hits different" means it has a unique impact

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
