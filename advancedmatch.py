def match(pattern, word):
    # If we reach at the end of both strings, we are done
    if len(pattern) == 0 and len(word) == 0: return True
 
    # If the pattern string contains '?', or current characters
    # of both strings match
    if (len(pattern) > 1 and pattern[0] == '?') or (len(pattern) != 0
        and pattern[0] == word[0] and len(word) !=0):
        return match(pattern[1:],word[1:]);

    # Make sure that the characters after '*' are present
    # in word string. This function assumes that the pattern
    # string will not contain two consecutive '*'
    if len(word) == 0 and pattern[0] == '*' and  len(pattern) > 1: return False
    # If there is *, then there are two possibilities
    # a) We consider current character of word string
    # b) We ignore current character of word string.
    if pattern[0] == '*' and len(pattern) !=0:
        return match(pattern[1:],word) or match(pattern,word[1:])
    return False