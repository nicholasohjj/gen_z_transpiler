import re
import sys
import subprocess
import asyncio

def transpile_code(source_code):
    """Transpile custom keywords in the source code to standard Python."""
    # Extended slang mappings
    slang_mappings = {
        re.compile(r'\byeet(?=\()'): 'print',  # Lookahead for an opening parenthesis
        # Control flow
        re.compile(r'\bno cap\b'): 'if',  # If condition, "no cap" means "seriously" or "for real"
        re.compile(r'\bfacts\b'): 'else',  # Else condition, "facts" is used to agree or confirm
        re.compile(r'\bbet\b'): 'elif',  # Elif condition, "bet" indicates agreement or acknowledgment
        re.compile(r'\bvibe check\b'): 'for',  # For loop, "vibe check" assesses the situation or atmosphere
        re.compile(r'\bsimpin\b'): 'while',  # While loop, "simpin" suggests a more focused, sometimes obsessive loop
        re.compile(r'\bslide\b'): 'continue',  # Continue loop, "slide" implies moving on smoothly
        re.compile(r'\bdipped\b'): 'break',  # Break loop, "dipped" means to leave abruptly
        re.compile(r'\bsend it\b'): 'pass',  # Pass statement, "send it" means to go for it or proceed without hesitation
        re.compile(r'\bsus\b'): 'try',  # Try block, "sus" means suspect or suspicious, indicating caution
        re.compile(r'\bcaught lackin\b'): 'except',  # Except block, "caught lackin" means caught off guard
        re.compile(r'\bwe gucci\b'): 'finally',  # Finally block, "we gucci" means all is good or resolved
        re.compile(r'\bpressed\b'): 'assert',  # Assert statement, "pressed" means to insist or assert forcefully
        re.compile(r'\bthrow shade\b'): 'raise',  # Raise exception, "throw shade" means to criticize or express disdain

        # Boolean and comparisons
        re.compile(r'\blit\b'): 'True',  # True, "lit" remains popular for excitement or awesomeness
        re.compile(r'\bsalty\b'): 'False',  # False, "salty" means upset or bitter, indicating negativity
        re.compile(r'\bghosted\b'): 'not',  # Not, "ghosted" means ignored or excluded, suggesting negation
        re.compile(r'\band I oop\b'): 'and',  # And, "and I oop" adds dramatic pause or emphasis
        re.compile(r'\bperiodt\b'): 'or',  # Or, "periodt" signifies emphasis or finality, used for alternatives

        # Others
        re.compile(r'\bcanceled\b'): 'del',  # Delete statement, "canceled" means to reject or dismiss
        re.compile(r'\bchill with\b'): 'with',  # With statement, "chill with" implies association or collaboration
        re.compile(r'\biconic\b'): 'as',  # As statement, "iconic" signifies notable or significant alignment
        re.compile(r'\blowkey flex\b'): 'async',  # Async declaration, "lowkey flex" suggests a subtle, understated action
        re.compile(r'\bhighkey waiting\b'): 'await',  # Await statement, "highkey waiting" implies an eager or anxious wait
        re.compile(r'\bsnatched\b'): 'lambda',  # Lambda function, "snatched" means impressive or on point, signifying a concise function

                # Functions and classes
        re.compile(r'\bglow up\b'): 'def',  # Define a function, "glow up" signifies transformation or improvement
        re.compile(r'\bgang gang\b'): 'class',  # Define a class, "gang gang" expresses close association or teamwork
        re.compile(r'\bstan\b'): 'from',  # From import statement, "stan" means to support or admire
        re.compile(r'\bflex\b'): 'import',  # Import statement remains the same, as "flex" is still popular
        re.compile(r'\btea\b'): 'return',  # Return statement, "tea" means truth or gossip, suggesting returning info
        re.compile(r'\bclout\b'): 'global',  # Global declaration, "clout" symbolizes influence or power
        re.compile(r'\bjuiced\b'): 'nonlocal',  # Nonlocal declaration, "juiced" means energized or empowered
        re.compile(r'\bhits different\b'): 'yield',  # Yield statement, "hits different" means it has a unique impact

        re.compile(r'\bspill the tea\b'): 'input',  # Input function
        re.compile(r'\bflex on\b'): 'len',  # Length function
        re.compile(r'\bglitched\b'): 'error',  # Placeholder for raising generic errors
        re.compile(r'\bfinesse\b'): 'str',  # String conversion
        re.compile(r'\bstacked\b'): 'int',  # Integer conversion
        re.compile(r'\bvibes\b'): 'list',  # List constructor
        re.compile(r'\bsquad\b'): 'dict',  # Dictionary constructor
        re.compile(r'\biced out\b'): 'float',  # Float conversion
        re.compile(r'\bfire\b'): 'max',  # Max function
        re.compile(r'\bfrozen\b'): 'min',  # Min function
        re.compile(r'\bsnack\b'): 'sum',  # Sum function
        re.compile(r'\bmood\b'): 'type',  # Type checking
        re.compile(r'\bglitching\b'): 'error',  # Error raising
        re.compile(r'\bghost\b'): 'exit',  # Exit program
    }
    
    # Apply mappings
    transpiled_code = source_code
    for slang, py_equiv in slang_mappings.items():
        transpiled_code = slang.sub(py_equiv, transpiled_code)
    return transpiled_code

async def execute_async_code(local_namespace):
    for name, obj in local_namespace.items():
        if asyncio.iscoroutinefunction(obj):
            await obj()

def execute_transpiled_code(transpiled_code):
    try:
        local_namespace = {}
        exec(transpiled_code, {"__builtins__": __builtins__, "asyncio": asyncio}, local_namespace)
        asyncio.run(execute_async_code(local_namespace))
    except Exception as e:
        print(f"Error executing transpiled code: {e}")

def main(input_file_path):
    try:
        with open(input_file_path, 'r') as file:
            source_code = file.read()
        transpiled_code = transpile_code(source_code)
        print("Transpiled Code:\n", transpiled_code)
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
