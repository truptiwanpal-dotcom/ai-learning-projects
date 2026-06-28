from langchain_core.tools import tool

# Step 1 - create a function
@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a*b

result = multiply.invoke({'a': 5, 'b': 10})

print(result)  # Output: 50

print(multiply.name)  # Output: multiply
print(multiply.description)  # Output: Multiply two numbers
print(multiply.args) #{'a': {'title': 'A', 'type': 'integer'}, 'b': {'title': 'B', 'type': 'integer'}}

print(multiply.args_schema.model_json_schema()) #{'description': 'Multiply two numbers', 'properties': {'a': {'title': 'A', 'type': 'integer'}, 'b': {'title': 'B', 'type': 'integer'}}, 'required': ['a', 'b'], 'title': 'multiply', 'type': 'object'}