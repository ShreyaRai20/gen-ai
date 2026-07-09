from langchain_community.tools import tool

@tool
def greeting(name: str) -> str:  # type
    """used to greet user""" # description of the tool
    print(f"hello, {name}")
    
    
greeting.invoke({
    'name': "Shreya"
})


print(greeting.name)
print(greeting.description)
print(greeting.args)