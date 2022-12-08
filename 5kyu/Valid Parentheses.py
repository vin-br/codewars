'''Description:

Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return true if the string is valid, and false if it's invalid.
Examples

"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true

Constraints

0 <= input.length <= 100

Along with opening (() and closing ()) parenthesis, input may contain any valid ASCII characters. Furthermore, the input string may be empty and/or not contain any parentheses at all. Do not treat other forms of brackets as parentheses (e.g. [], {}, <>).
'''

# Solution
def valid_parentheses(s): 
    
    # Removing all characters between parentheses in the string
    s = "".join(c for c in s if c in "()")
    
    # Replacing sets of two parentheses by nothing at all
    while "()" in s:
        s = s.replace("()", "")
        
    # Returning True if the string is empty, else it's false
    return True if s == "" else False