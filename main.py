import re

# (^[A-z]\w+)(\:\=)\s
def isAttributionClass(statement):
    varStatement = re.compile("(?<=(^var\s))[A-z]{0,}\w+") # identify var foo
    defaultStatement = re.compile("([A-z])(?<!\:\=)\w+") # Identify foo := bar

    if re.match(defaultStatement, statement): return True
    if re.match(varStatement, statement): return True

    return False

def isNumber(statement):
    numberRegex = re.compile("(([0-9]+)(\.|\,[0-9]+)?)|(\.?[0-9]+)\d+") # identify natural/real numbers

    if re.match(numberRegex, statement): return True

    return False

def isCommentary(statement):
    hastagComment = re.compile("(\#).*")
    doubleSlash = re.compile("(\/\/).*")
    # blockCommentary = re.compile("")
    
    if re.match(hastagComment,statement): return True
    if re.match(doubleSlash,statement): return True
    # if statement.match(blockCommentary): return True
    
    return False

def isVariableIdentifier(statement):
    variableIdentifier = re.compile("^[A-z]\w+")

    if re.match(variableIdentifier,statement): return True

    return False

def checkType(statement): 
    if isAttributionClass(statement): return "attribution"
    if isCommentary(statement): return "commentary"
    if isVariableIdentifier(statement): return "variable"
    if isNumber(statement): return "number"
    return "invalid"

statement=(input("Entre com o statement: "))
print ("Statement: ", statement)

typeVariable=checkType(statement)

print (statement, typeVariable)
