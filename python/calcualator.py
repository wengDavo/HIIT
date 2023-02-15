def add(a:float, b:float)->float:
    return a + b


def sub(a:float, b:float)->float:
    return a - b
    

def prod(a:float, b:float)->float:
    return a * b


def div(a:float, b:float)->float:
    return a / b


def mod(a:float, b:float)->float:
    return a % b


if __name__ == "__main__":
    play = True
    while play:
        value = input("Press q to quit any other character to continue:")
        if value == 'q':
            play = False
        else:
            input_1 = int(input("Enter a number:"))
            input_2 = int(input("Enter a number:"))

            functions = [add, sub, prod, div, mod]
            message = ['sum', 'subtraction', 'product', 'division', 'modulos']
            print('-'*20)
            for x in range(len(functions)):
                print(f"The {message[x]} :",functions[x](input_1,input_2))
          
