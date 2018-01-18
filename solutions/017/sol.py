digits = len('one' 'two' 'three' 'four' 'five' 'six' 'seven' 'eight' 'nine' )

teens = len('ten' 'eleven' 'twelve' 'thirteen' 'fourteen' 'fifteen' 'sixteen' 'seventeen' 'eighteen' 'nineteen')

tens = len('twenty' 'thirty' 'forty' 'fifty' 'sixty' 'seventy' 'eighty' 'ninety')

hundred = len('hundred')
and_ = len('and')
thousand = len('thousand')

# The number of letters required for one through ninety-nine
#             1-9      10-19   each ten repeated for each digit (and 0)
sub_hundred = digits + teens + tens * 10 + digits * 8


# one through ninety-nine is repeated 10 times
# (*one*, one hundred and *one*, ..., nine hundred and *one*, ...)
result = sub_hundred*10

# Each digit is repeated 100 times in it's hundred range
# (*one* hundred, *one* hundred and one, ..., *one* hundred and ninety-nine)
result += digits*100

# in each range of hundred (9 of them, one for each digit) "hundred" is
# repeated 100 times and "and" is repeated 99 times
# (one *hundred*, one *hundred* *and* one, ..., one *hundred* *and* ninety-nine)
result += (len('hundred')*100 + len('and')*99)*9

# don't forget "one thousand"!
result += len('one' 'thousand')

print(result)
