class Solution:
    def is_palindrome(self, string):
        """
        Takes in a string and returns true if it is a palindrome, false otherwise.
        :param string: Input string
        :return: True if the string is a palindrome, false otherwise
        """
        string_len = len(string)

 
        if string_len <= 1:
            return True

 
        for i in range(0, int(string_len / 2)):


 
            if string[i].upper() != string[string_len - i - 1].upper():

 
                return False

 
        return True
