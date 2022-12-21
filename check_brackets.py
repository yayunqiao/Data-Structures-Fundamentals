#{}python3
    
def find_mismatch(text):
    """
    This function find the mismatches bracket in the input and return its location
    
    param text: The input string eg. {}, {}[], foo(bar)
    param stack: the stack to put in the begining of the bracket eg {, [, (
    param mapping: mapping of the bracket
    
    returns: the location of the mismatche bracket
    """
    stack = [(0, 0)]
    mapping = {0:None, '(':')', '[':']', '{':'}'}
    
    if(len(text) == 1): return 1 # if there is only one bracket than it is definitly not a match
    
    for i, c in enumerate(text):
        
        if i == 0 and c in mapping.values(): return 1 #exclude senarios like ")[]"
        if i == len(text)-1 and c in mapping: return len(text) #exclude senarios like "{}["
        
        if c in mapping:
            stack.append((i, c))
        elif c in mapping.values():
            if mapping[stack.pop()[1]] != c: # exclude senarios like "{}{}]"
                return i+1

    if len(stack) >= 2: #exclude senarios like "{}(()"
        return stack.pop()[0]+1
 
        
    
    
def main():
    """main _summary_
    param test: input
    param mismatch: the location of the mismatch bracket
    
    return: if the mismatch is None, return "Success", the input string brackets matched
    if the mismatch is not None, not matchm and returb the location of the mismatch bracket
    """
    text = input()
    mismatch = find_mismatch(text)

    if not mismatch:
        print("Success")
    else:
        print(mismatch)



if __name__ == "__main__":
    main()

 