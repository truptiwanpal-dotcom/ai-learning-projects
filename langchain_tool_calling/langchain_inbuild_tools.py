from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.tools import ShellTool

search_tool = DuckDuckGoSearchRun()

results = search_tool.invoke('top news in india today')

#print(results)

shell_tool = ShellTool()

results = shell_tool.invoke('whoami')

print(results)

print(search_tool.name)  # Output: multiply
print(search_tool.description)  # Output: Multiply two numbers
print(search_tool.args)  # Output: {'query': {'type': 'string', 'description': 'The query to search for'}}