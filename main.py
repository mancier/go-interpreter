import re

# (^[A-z]\w+)(\:\=)\s
def isAttribuitionClass(statement):
    re.compile("")
    return True

def isNumber(statement):
    numberRegex = re.compile("[0-9]")

    if re.match(numberRegex, statement): return True

    return True

################################# Regex #################################
# \/\/  => (\/\/).*
# #     => (\#).*
# /**/  => 
def isCommentary(statement):
    hastagComment = re.compile("(\#).*")
    doubleSlash = re.compile("(\/\/).*")
    # blockCommentary = re.compile("")
    
    if re.match(hastagComment,statement): return True
    if re.match(doubleSlash,statement): return True
    # if statement.match(blockCommentary): return True
    
    return False

def isVariableIdentifier(statement):
    return True


statement=(input("Entre com o statement: "))
print ("Statement: ", statement)


