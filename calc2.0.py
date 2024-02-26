def landing_page():
    print('''
        My Calculator
        
        1. Addition
        2. Subtraction
        3. Division
        4. Multiplication
        5. exponential 
        6.exit
        
        
        ''')
    
    user = int(input('Select operation: ').strip())
    if user == 1:
        addition()
    elif user == 2:
        subtraction()
    elif user == 3:
        division()
    elif user == 4:
        multiplication()
    elif user == 5:
        exponential()
    elif user == 6:
        exit()
    else:
        print('Invalid input...')
        
def addition():
    val1 = int(input('value1: ').strip())
    val2 = int(input('value2: ').strip())
    result = val1 + val2 
    print(f'{val1} + {val2} = {result}')
    
def subtraction():
    val1 = int(input('value1: ').strip())
    val2 = int(input('value2: ').strip())
    result = val1 - val2 
    print(f'{val1} - {val2} = {result}')
    
def division():
    val1 = int(input('value1: ').strip())
    val2 = int(input('value2: ').strip())
    result = val1 / val2 
    print(f'{val1} / {val2} = {result}')
    
def multiplication():
    val1 = int(input('value1: ').strip())
    val2 = int(input('value2: ').strip())
    result = val1 * val2 
    print(f'{val1} * {val2} = {result}')   
    
def exponential():
    val1 = int(input('value1: ').strip())
    val2 = int(input('value2: ').strip())
    result = val1 ** val2 
    print(f'{val1} ** {val2} = {result}')
    

landing_page()