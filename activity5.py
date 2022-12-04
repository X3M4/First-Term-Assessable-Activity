def price_calc(model): #ALL THE LOGIC WILL BE MANAGE BY A FUNCTION
    model = str(model) #INSIDE THE FUNCTION I NEED TO DECLARATE model VARIABLE AS STRING
    code = False #I WRITE A NEW BOOL VARIABLE TO ACTIVATE DISCOUNT CODE
    
    if model == "white" or model == "red" or model == "black": #CHECK THE STRING. IF MODEL IS CORRECT IT'LL CONTINUE RUNNING THE CODE OR IT'LL RUN EXCEPT BLOCK
        code_discount = input("Do you have a discount code?\n Write INENGLISHPLEASE down and get 5'%' discount\n") #NEW VARIABLE TO DISCOUNT CODE WILL BE READED BY KEYBOARD
        if  code_discount == "INENGLISHPLEASE": #IF CODE DISCOUNT IS CORRECT CONTINUE RUNNING THE CODE
            code = True #AND VARIABLE CODE IS ACTIVATED
        else: #IF CODE INS'T CORRECT...
            code = False #CODE WON'T BE ACTIVATED

    if model == "white": #CASE MODEL IS WHITE
        model_price = 250 #PRICE TO MODEL WHITE
        if code == True: #IN CASE THE CODE IS ACTIVATED...
            discount = 5 #IT'LL DECLARE INTEGER VARIABLE TO DISCOUNT CODE WITH AND ITS VALUE
            total_payment = model_price*((100-discount)/100) #CALCULATIONS OF TOTAL PAYMENT WITH DISCOUNT ACTIVATED
            print(f"{model.upper()} model price: {model_price}€") #FOR PRINTING BY SCREEN I LIKE THE MODEL IN UPPERCASE
            print(f"\033[92m INENGLISHPLEASE discount:{discount}%") #THE DISCOUNT WILL BE PRINTED IN GREEN COLOR USING ANSI SEQUENCES
            print(f"Total payment: {total_payment}€") #PRINTING TOAL PAYMENT WITH DISCOUNT ACTIVATED
        else: #IN CASE THE DISCOUNT CODE IN WRONG OR DOESN'T WORK
            total_payment = model_price #TOTAL PAYMENT IS THE MODEL PRICE
            print(f"Total payment: {total_payment}€") #PRINTING TOTAL PAYMENT WITHOUT DISCOUNT ACTIVATED

    elif model == "red": #CASE MODEL IS RED
        model_price = 280 #PRICE TO MODEL RED
        if code == True: #IN CASE THE CODE IS ACTIVATED
            discount = 5 #IT'LL DECLARE INTEGER VARIABLE TO DISCOUNT CODE WITH AND ITS VALUE
            total_payment = model_price*((100-discount)/100) #CALCULATIONS OF TOTAL PAYMENT WITH DISCOUNT ACTIVATED
            print(f"{model.upper()} model price: {model_price}€") #FOR PRINTING BY SCREEN I LIKE THE MODEL IN UPPERCASE
            print(f"\033[92m INENGLISHPLEASE discount:{discount}%") #THE DISCOUNT WILL BE PRINTED IN GREEN COLOR USING ANSI SEQUENCES
            print(f"Total payment: {total_payment}€") #PRINTING TOAL PAYMENT WITH DISCOUNT ACTIVATED
        else: #IN CASE THE DISCOUNT CODE IN WRONG OR DOESN'T WORK
            total_payment = model_price #TOTAL PAYMENT IS THE MODEL PRICE
            print(f"Total payment: {total_payment}€") #PRINTING TOTAL PAYMENT WITHOUT DISCOUNT ACTIVATED

    elif model == "black": #CASE MODEL IS BLACK
        model_price = 300 #PRICE TO MODEL BLA
        if code == True: #IN CASE THE CODE IS ACTIVATED
            discount = 5 #IT'LL DECLARE INTEGER VARIABLE TO DISCOUNT CODE WITH AND ITS VALUE
            total_payment = model_price*((100-discount)/100) #CALCULATIONS OF TOTAL PAYMENT WITH DISCOUNT ACTIVATED
            print(f"{model.upper()} model price: {model_price}€") #FOR PRINTING BY SCREEN I LIKE THE MODEL IN UPPERCASE
            print(f"\033[92m INENGLISHPLEASE discount:{discount}%") #THE DISCOUNT WILL BE PRINTED IN GREEN COLOR USING ANSI SEQUENCES
            print(f"Total payment: {total_payment}€") #PRINTING TOAL PAYMENT WITH DISCOUNT ACTIVATED
        else: #IN CASE THE DISCOUNT CODE IN WRONG OR DOESN'T WORK
            total_payment = model_price #TOTAL PAYMENT IS THE MODEL PRICE
            print(f"Total payment: {total_payment}€") #PRINTING TOTAL PAYMENT WITHOUT DISCOUNT ACTIVATED

    else:    
        print("The model you've selected is not in the database ") #PRINT A MESSAGE

    
model = input("Please, select the model you want\n") #MODEL COLOR MUST BE READED BY KEYBOARD FON RUNNING THE PROGRAM. IT'LL BE A STRING
try: #I USE TRY-EXCEPT BLOCK THE STRING WONT BE CASE SENSITIVE
    model = model.lower() #AND IT WONT BE CASE SENSITIVE BECAUSE FIRST IT'LL TRY MAKING THE STRING TO LOWERCASE.
    price_calc(model) #AND THE CALLING THE FUNCTION PASSING THE MODEL AS ARGUMENT
except: #IF THE STRING IS READED IN LOWERCASE EXCEPT BLOCK IS ACTIVATED
    price_calc(model) #AND THE CALLING THE FUNCTION PASSING THE MODEL AS ARGUMENT
