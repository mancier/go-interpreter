import re

def isAttribution(statement):
    varStatement = re.compile("((^var\s)|(^const\s))[A-z]{0,}\w+") # identify var foo  
    defaultStatement = re.compile("([A-z]{0,})(\:\=)\w+") # Identify foo := bar

    if re.match(defaultStatement, statement): return True
    if re.match(varStatement, statement): return True

    return False

def isNumber(statement):
    numberRegex = re.compile("((([0-9]+)(\.|\,[0-9]+)?)|(\.?[0-9]+))\d") # identify natural/real numbers

    if re.match(numberRegex, statement): return True

    return False

def isCommentary(statement):
    doubleSlash = re.compile("(\/\/).*")
    blockCommentary = re.compile("\/\*(\*(?!\/)|[^*])*\*\/")
    
    if re.match(doubleSlash,statement): return True
    if re.match(blockCommentary, statement): return True
    
    return False

def isVariable(statement):
    variableIdentifier = re.compile("([a-zA-Z])")

    if re.match(variableIdentifier,statement): return True

    return False

def checkType(statement): 
    if isAttribution(statement): return "attribution"
    if isVariable(statement): return "variable"
    if isNumber(statement): return "number"
    if isCommentary(statement): return "commentary"
    return "invalid"

while True:
    statement=(input("Entre com o statement: "))

    if statement == "exit": break
    
    typeVariable=checkType(statement)
    print (statement," -> ", typeVariable)
