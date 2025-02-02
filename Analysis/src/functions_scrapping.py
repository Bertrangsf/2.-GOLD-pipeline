import calendar 

def convertir_valor(valor):
    """
    Enter the value as a str and convert it into float.
    """
    valor = valor.replace(".","")
    valor = valor.replace(",",".")
    return float(valor)

def month(date):
    """
    Enter the date from which you want to extract the month.
    This function takes the third and fourth digits frome the entered data and transforded in month.
    """
    for x in date:
        months = int(date[3:5])
        return calendar.month_name[(months)] 

def day(date):
    """
    Enter the date from which you want to extract the day.
    This function takes the first two digits frome the entered data.
    """
    for x in date:
        return int(date[:2])

def year(date):
    """
    Enter the date from which you want to extract the year.
    This function takes the last four digits frome the entered data. 
    """
    for x in date:
        return int(date[-4:]) 

