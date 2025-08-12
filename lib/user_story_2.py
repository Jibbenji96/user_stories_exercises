def grammar_checker(text):
    starts_correctly = text[0].isupper()
    ends_correctly = text[-1] in "!.?"  

    if starts_correctly and ends_correctly:
        return "String grammar is correct."
    
    elif not starts_correctly and not ends_correctly:
        return "Missing starting capital letter and ending punctuation mark."
    
    elif not starts_correctly:
        return "Missing starting capital letter."
    
    elif not ends_correctly:
        return "Missing ending punctuation mark."