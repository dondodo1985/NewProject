# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def my_function(str1,str2):
    print(str1)
    print(str2)
my_function('string1','string2')
my_function('Hello','World')
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
#type
def difisil(name='No_name',age='Unknown'):
    print('My name is',name,'my age is',age)
difisil('Ragive',35)
difisil(age=24)
difisil(name='James')
difisil()
difisil(None,28)
difisil(age=29,name='Merde')
#print a list of name
def print_people(*people):
    for person in people:
        print('This person name is',person)
print_people('James','Ragive','Dominique')