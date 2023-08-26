"""
Write a Python program to find the location of Python module sources.
"""
import inspect
def find_module_source_location(module_name):
    try:
        module = __import__(module_name)
        module_file = inspect.getfile(module)
        return module_file
    except ImportError:
        return f"Module '{module_name}' not found."

if __name__ == "__main__":
    module_name = input("Enter the name of the module: ")
    source_location = find_module_source_location(module_name)
    print(f"The source file for module '{module_name}' is located at:\n{source_location}")

