# // By .startsWith() method

string = 'Hello Weolrd';

starts = string.startswith('He',0);
if starts:
    print("The string starts with He")
else:
    print("Does'nt starts with He");

# // By lastIndexOf()

starts2 = string.index('e');

if starts2 == 0:
    print("The string starts with He");
else:
    print(starts2);

