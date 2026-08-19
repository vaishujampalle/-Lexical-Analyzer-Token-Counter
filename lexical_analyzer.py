import re

# C language keywords
keywords = {
    "auto", "break", "case", "char", "const", "continue",
    "default", "do", "double", "else", "enum", "extern",
    "float", "for", "goto", "if", "int", "long",
    "register", "return", "short", "signed", "sizeof",
    "static", "struct", "switch", "typedef", "union",
    "unsigned", "void", "volatile", "while"
}

# Operators
operators = {
    "+", "-", "*", "/", "%", "=",
    "==", "!=", "<", ">", "<=", ">=",
    "&&", "||", "!", "++", "--",
    "+=", "-=", "*=", "/="
}

# Separators / delimiters
separators = {
    "(", ")", "{", "}", "[", "]",
    ";", ",", ":"
}

def lexical_analyzer(filename):

    with open(filename, "r") as file:
        source = file.read()

    # Pattern for tokens
    pattern = r'''
        //.*                         | # Single-line comment
        /\*[\s\S]*?\*/               | # Multi-line comment
        "(?:\\.|[^"\\])*"            | # String literal
        '(?:\\.|[^'\\])*'            | # Character literal
        \d+(?:\.\d+)?                | # Integer/Float constant
        [A-Za-z_][A-Za-z0-9_]*       | # Identifier/Keyword
        ==|!=|<=|>=|\+\+|--|&&|\|\|  | # Multi-character operators
        [+\-*/%=<>!]                 | # Single-character operators
        [()\[\]{};,:]                | # Separators
        [^\s]                          # Special symbols
    '''

    tokens = re.findall(pattern, source, re.VERBOSE)

    counts = {
        "Keywords": 0,
        "Identifiers": 0,
        "Operators": 0,
        "Constants": 0,
        "String Literals": 0,
        "Separators": 0,
        "Special Symbols": 0,
        "Comments": 0
    }

    print("TOKEN TYPE")
    print("-" * 50)

    for token in tokens:

        if token.startswith("//") or token.startswith("/*"):
            token_type = "Comment"
            counts["Comments"] += 1

        elif token.startswith('"'):
            token_type = "String Literal"
            counts["String Literals"] += 1

        elif token.startswith("'"):
            token_type = "Constant"
            counts["Constants"] += 1

        elif token in keywords:
            token_type = "Keyword"
            counts["Keywords"] += 1

        elif re.fullmatch(r'\d+(?:\.\d+)?', token):
            token_type = "Constant"
            counts["Constants"] += 1

        elif token in operators:
            token_type = "Operator"
            counts["Operators"] += 1

        elif token in separators:
            token_type = "Separator"
            counts["Separators"] += 1

        elif re.fullmatch(r'[A-Za-z_][A-Za-z0-9_]*', token):
            token_type = "Identifier"
            counts["Identifiers"] += 1

        else:
            token_type = "Special Symbol"
            counts["Special Symbols"] += 1

        print(f"{token:<20} {token_type}")

    print("\n" + "-" * 50)
    print("Token Count")

    for category, count in counts.items():
        print(f"{category:<18}: {count}")


# Main program
filename = input("Enter source file name: ")
lexical_analyzer(filename)
