class LongNameDict(dict):
    """
    varName = LongNameDict() # Assigns Class to Variable
    varName['key'] = value # Assigns a key and value pair to class variable
    varname['key2'] = value2 # Assigns a key and value pair to class variable
    varName.longest_key() # Calls Function
    """
    def longest_key(self):
        longest = None
        for key in self:
            if not longest or len(key) > len(longest):
                longest = key
        return longest
