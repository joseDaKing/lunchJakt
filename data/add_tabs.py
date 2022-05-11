def add_tabs(text: str) -> str:
    
    newText = ""

    for row in text.split("\n"):
        
        newText += "\t" + row + "\n"

    return newText