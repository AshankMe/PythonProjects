print('Currency Converter')
print('------------------')
print('Note: This converter only uses currency abbreviations such as USD, INR. If you do not know the abbreviation for your currency, use this: https://www.ifcmarkets.com/en/about-forex/currencies-and-abbreviations')
#Imports
from forex_python.converter import CurrencyRates 
#Asking the user the 2 currencys
c = CurrencyRates()
fc = input('What is the currency that your amount is in?')
tc = input('What currency is it being transfered to?')
#Listing the conversion rate
cr = c.convert(fc,tc,1)
print('The conversion rate for', fc, 'and',tc, 'is', cr)
    


useramount = int(input('Enter the amount that you want to convert.'))

print(fc,'To',tc,useramount)
result = c.convert(fc,tc,useramount)
print('Your result is', result)