#QUESTION
1. >>> print 'ab123'.isalnum()
True
>>> print 'ab123#'.isalnum()
False

2. >>> print 'abcD'.isalpha()
True
>>> print 'abcd1'.isalpha()
False

3. >>> print '1234'.isdigit()
True
>>> print '123edsd'.isdigit()
False

4. >>> print 'abcd123#'.islower()
True
>>> print 'Abcd123#'.islower()
False

5. >>> print 'ABCD123#'.isupper()
True
>>> print 'Abcd123#'.isupper()
False

#CODE
if __name__ == '__main__':
    s = input()
    print(any([i.isalnum() for i in s]))
    print(any([i.isalpha() for i in s]))
    print(any([i.isdigit() for i in s]))
    print(any([i.islower() for i in s]))
    print(any([i.isupper() for i in s]))
    
