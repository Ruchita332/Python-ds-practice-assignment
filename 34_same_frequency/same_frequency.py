# Function that calcultes the frequency of each digit in a number
def freq_counter (num):
    string_num = str (num);
     
    counts = {};

    for x in string_num:
        counts [x] = counts.get (x, 0) +1;

    return counts;


def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """

    # call the freq counter function compare and return the result

    return freq_counter (num1) == freq_counter(num2);

print (same_frequency(551122, 221515))
        # True
        
print ( same_frequency(321142, 3212215))
        # False
        
print (same_frequency(1212, 2211))
        # True