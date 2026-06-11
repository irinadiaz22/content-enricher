def validator(text):
    text_valid = True
    if text == '':
        text_valid= False
    if len(text)<3:
        text_valid= False
    if type(text)!=str:
        text_valid= False

    if text_valid == False:
        print("Ingrese un texto váido")

    return (text_valid)
