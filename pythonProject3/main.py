import re
print("Our magical operator")
print("Type 'quit' to exit\n")
previous=0
run=True
def performMath():
    #declare run global to gain access
    global run
    global previous
    equation=""
    if previous==0:
       equation=input("Enter equation:")
    else:
        equation=input(str(previous))

    if equation=='quit':
        print('Goodbye, human')
        run= False
    else:
        #remove all other characters from equation
        equation=re.sub('[a-zA-Z,.:()" "]','',equation)
        if previous==0:
            previous=eval(equation)
        else:
            previous=eval(str(previous)+equation)
            print(previous)
while run:
    performMath()