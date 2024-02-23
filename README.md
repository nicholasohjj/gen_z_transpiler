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

Below is a partial list of the slang to Python keyword mappings supported by the transpiler:

- **Control Flow:**
    - **`lowkey`** -> **`if`**
    - **`highkey`** -> **`else`**
    - **`on repeat`** -> **`for`**
    - **`chillin`** -> **`while`**
    - **`snack`** -> **`break`**
- **Functions and Classes:**
    - **`big brain`** -> **`def`**
    - **`squad`** -> **`class`**
    - **`flex`** -> **`import`**
    - **`spill the tea`** -> **`return`**
- **Boolean and Comparisons:**
    - **`woke`** -> **`True`**
    - **`basic`** -> **`False`**
    - **`not even`** -> **`not`**
- **Others:**
    - **`lit`** -> **`del`**
    - **`catching vibes`** -> **`with`**

Refer to the source code for the complete list of mappings.

## **Contributing**

Contributions to expand the slang dictionary or improve the tool are welcome. Please follow standard open-source contribution guidelines.

## **License**

This tool is provided under the MIT License. See the LICENSE file for more details.

---

This README provides a concise overview, installation and usage instructions, a brief listing of features, and contribution guidelines. Adjust the content as needed based on the project's evolution and specific requirements.