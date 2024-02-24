# **Gen Z Slang Python Transpiler**

## **Overview**

This Gen Z Slang Python Transpiler allows developers to write Python code using Gen Z slang. It aims to make coding more relatable and fun for younger programmers or those who appreciate internet culture. By transpiling slang-based keywords into standard Python syntax, it bridges the gap between informal language and formal programming constructs.

## **Features**

- **Slang to Python Mapping:** Converts a variety of slang terms into their corresponding Python keywords, covering control flow, functions, classes, boolean operations, and more.
- **Execution of Transpiled Code:** Executes the transpiled Python code within the tool, enabling quick testing and iteration.
- **Error Handling:** Provides feedback on errors encountered during the transpilation or execution process.

## **Installation**

No installation is required beyond having Python 3.x installed on your system. Simply download the **`transpiler.py`** script to your local machine.

## **Usage**

To use the Python Slang Transpiler, follow these steps:

1. **Prepare Your Slang Python File:** Write your Python code using the supported slang terms. Save this file with a **`.py`** extension.
2. **Run the Transpiler:** Use the command line to navigate to the directory containing **`transpiler.py`** and your slang Python file. Execute the script with the following command:

```bash
bashCopy code
python transpiler.py <path_to_your_slang_python_file.py>

```

Replace **`<path_to_your_slang_python_file.py>`** with the actual file path of your slang Python file.

1. **Review and Execute:** The transpiler will output the transpiled standard Python code to the console and execute it. Review the output and execution results.

## **Slang Keywords Mapping**

### **Slang Mappings**

The transpiler includes mappings for various Python keywords, statements, and built-in functions to their Gen Z slang equivalents. Here are some of the slang mappings:

- **Control Flow:**
    - **`yeet`**: Replaces **`print`** but only when used as a function call.
    - **`no cap`**: Translates to **`if`**.
    - **`facts`**: Translates to **`else`**.
    - **`bet`**: Translates to **`elif`**.
    - **`vibe check`**: Translates to **`for`**.
    - **`simpin`**: Translates to **`while`**.
    - **`slide`**: Translates to **`continue`**.
    - **`dipped`**: Translates to **`break`**.
    - **`send it`**: Translates to **`pass`**.
    - **`sus`**: Translates to **`try`**.
    - **`caught lackin`**: Translates to **`except`**.
    - **`we gucci`**: Translates to **`finally`**.
    - **`pressed`**: Translates to **`assert`**.
    - **`throw shade`**: Translates to **`raise`**.
- **Boolean and Comparisons:**
    - **`lit`**: Translates to **`True`**.
    - **`salty`**: Translates to **`False`**.
    - **`ghosted`**: Translates to **`not`**.
    - **`and I oop`**: Translates to **`and`**.
    - **`periodt`**: Translates to **`or`**.
- **Other Keywords:**
    - **`canceled`**: Translates to **`del`**.
    - **`chill with`**: Translates to **`with`**.
    - **`iconic`**: Translates to **`as`**.
    - **`lowkey flex`**: Translates to **`async`**.
    - **`highkey waiting`**: Translates to **`await`**.
    - **`snatched`**: Translates to **`lambda`**.
- **Functions and Classes:**
    - **`glow up`**: Defines a function with **`def`**.
    - **`gang gang`**: Defines a class with **`class`**.
    - **`stan`**: Translates to **`from`** in import statements.
    - **`flex`**: Translates to **`import`**.
    - **`tea`**: Translates to **`return`**.
    - **`clout`**: Translates to **`global`**.
    - **`juiced`**: Translates to **`nonlocal`**.
    - **`hits different`**: Translates to **`yield`**.
- **Built-in Functions:**
    - **`spill the tea`**: Translates to **`input`**.
    - **`flex on`**: Translates to **`len`**.
    - **`glitched`**: Placeholder for errors.
    - **`finesse`**: Translates to **`str`**.
    - **`stacked`**: Translates to **`int`**.
    - **`vibes`**: Translates to **`list`**.
    - **`squad`**: Translates to **`dict`**.
    - **`iced out`**: Translates to **`float`**.
    - **`fire`**: Translates to **`max`**.
    - **`frozen`**: Translates to **`min`**.
    - **`snack`**: Translates to **`sum`**.
    - **`mood`**: Translates to **`type`**.
    - **`glitching`**: Placeholder for raising errors.
    - **`ghost`**: Translates to **`exit`**.

### **Extending the Slang Mappings**

To extend the slang mappings, add new key-value pairs to the **`slang_mappings`** dictionary, where the key is a compiled regular expression matching the slang term and the value is the standard Python equivalent.

### **Limitations**

The transpiler uses regular expressions for syntax translation, which may not perfectly handle all Python syntax nuances or complex code structures. It's intended for educational purposes.

## **Contributing**

Contributions to expand the slang dictionary or improve the tool are welcome. Please follow standard open-source contribution guidelines.


## **License**

This tool is provided under the MIT License. See the LICENSE file for more details.

---