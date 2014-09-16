operators = ["^", "*", "/", "+", "-"]

def findClosingBracket(string, openingIndex):
    level = 1
    for x in range(openingIndex+1, len(string)):
        if string[x] == '(':
            level += 1
        elif string[x] == ")":
            level -= 1
        
        if level == 0:
            return x

def convertToList(expression):
    exp = []
    
    currentType = ""
    currentTerm = ""
    for i in range(len(expression)):
        char = expression[i]
        
        if char.isdigit() and currentType in ["", "integer", "float"]: # If the character is a digit
            currentTerm += char
            currentType = currentType if currentType != "" else "integer"
            
        elif char == "." and currentType in ["", "integer"]: # If the character is a decimal point
            try:
                if expression[i+1].isdigit():
                    if currentType == "":
                        currentTerm += "0"
                    currentTerm += "."
                    currentType = "float"
            except IndexError: # In case x+1 exceeds the string length
                pass

        elif char in operators: # If the character is an operator
            exp.append(currentTerm)
            currentTerm = ""
            currentType = ""
            exp.append(char) 
            
        else: # The character isn't recognised
            raise Exception("Alien character present at index " + str(i))
                 
    exp.append(currentTerm)
    
    return exp
            
def parse(expression):
    print(convertToList(expression))