## Project 11 - Google Currency Conversion
## 12/01/12
## UM

import urllib.request
''' For precision math, unlike float which is not exact. The Decimal mod
    is capable of handling precision, which is pivotal for currency exchanges. '''
from decimal import * 

class Currency(object):
    def __init__(self, amount, currency):
        self.amount = round(amount, 2)
        self.currency = currency
    def __str__(self):
        return "Amount: %0.2f %s" % (self.amount, self.currency)
    def convert_to(self, convert_to_currency):
        self.convert_to_currency = convert_to_currency
        web_obj = urllib.request.urlopen("http://www.google.com/ig/calculator?hl=en&q=%f%s=?%s" % (self.amount, self.currency, self.convert_to_currency))
        result_str = str(web_obj.read())
        results_str = result_str.replace('"','')
        results_str2 = results_str.split()
        ''' Quantity to convert '''
        input_amount = Decimal(results_str2[1])
        ''' Quantity converted '''
        output_amount = Decimal(results_str2[4])
        web_obj.close()
        return "%0.2f %s is %0.2f %s" % (input_amount, self.currency, output_amount, self.convert_to_currency)
    def __add__(self, other):
        ''' Check if comparing floats/int or different currencies '''
        if type(other) == type(self):
            ''' If it is different currencies, convert one to the other, then add. '''
            output = self.convert_to(other.currency)
            output = output.split()
            output_amount = Decimal(output[3])
            return Currency(output_amount+other.amount,other.currency)
        else:
            return Currency(self.amount+other,self.currency)
    def __radd__(self, other):
        if type(other) == type(self):
            output = self.convert_to(other.currency)
            output = output.split()
            output_amount = Decimal(output[3])
            return Currency(other.amount+output_amount,other.currency)
        else:
            return Currency(self.amount+other,self.currency)
    def __sub__(self, other):
        if type(other) == type(self):
            output = self.convert_to(other.currency)
            output = output.split()
            output_amount = Decimal(output[3])
            return Currency(output_amount-other.amount,other.currency)
        else:
            return Currency(self.amount-other,self.currency)  
    def __rsub__(self, other):
        if type(other) == type(self):
            output = self.convert_to(other.currency)
            output = output.split()
            output_amount = Decimal(output[3])
            return Currency(other.amount-output_amount,other.currency)
        else:
            return Currency(other-self.amount,self.currency)
    def __gt__(self, other):
        if type(other) == type(self):
            output = self.convert_to(other.currency)
            output = output.split()
            output_amount = Decimal(output[3])
            ## print (output_amount, other.amount) ''' (5.73 EUR, 2.00 EUR) thus 5.73 > 2.00 == True '''
            return (output_amount > other.amount, other.currency)
        else:
            ## print (self.amount, other) ''' (2 EUR, 5.00 EUR) thus 2.00 > 5.00 == False. '''
            return (self.amount > other, self.currency)
    def __lt__(self, other):
        if type(other) == type(self):
            output = self.convert_to(other.currency)
            output = output.split()
            output_amount = Decimal(output[3])
            ## print (output_amount, other.amount) ''' (5.73 EUR, 2.00 EUR) thus 5.73 < 2.00 == False '''
            return (output_amount < other.amount, other.currency)
        else:
            ## print (self.amount, other) ''' (2 EUR, 5.00 EUR) thus 2.00 < 5.00 == True. '''
            return (self.amount < other, self.currency)
        
def main():
    ''' Because we were told not to test ever single currency, here is a small list of
       currencies that should work: CAD, AUD, USD, JPY, EUR, DZD, DKK, EGP, INR, SAR '''
    ''' Numbering added for easier reading '''

    ''' Prints out $7.50 USD '''
    curr = Currency(7.50, 'USD')
    print("1.", curr)
    
    ''' Prints 2 EUR '''
    curr2 = Currency(2, 'EUR')
    print("2.", curr2)
    
    ''' Prints curr ($7.50 USD) to EUR '''
    new_curr = curr.convert_to('EUR')
    print ("3. Conversion Result -", new_curr)
    
    ''' Prints curr to JPY '''
    new_curr2 = curr.convert_to('JPY')
    print ("4. Conversion Result -", new_curr2)
    
    ''' First converts USD to EUR, then adds '''
    sum_curr = curr + curr2
    print ("5. Sum of different currencies -", sum_curr)
    
    ''' Adds the $7.50 + 5.00 USD for a total of $12.50 USD '''
    sum_curr2 = curr + 5.00
    print ("6. Sum of same currency -", sum_curr2)
    
    ''' Similar to add function '''
    radd_curr2 = 5.00 + curr2
    print ("7. Reverse add of different currencies -", radd_curr2)
    
    ''' Similar to add function '''
    radd_curr = 5.00 + curr
    print ("8. Reverse add of same currency -", radd_curr)
    
    ''' Converts first currency and then subtracts from 2nd currency. '''
    diff_curr = curr - curr2
    print ("9. Subtraction of different currencies -", diff_curr)
    
    ''' Same thing but with the same currency '''
    diff_curr2 = curr - 5.50
    print ("10. Subtraction of same currency -", diff_curr2)

    ''' Similar to subtract function '''
    rsub_curr = 5.00 - curr2
    print ("11. Reverse subtraction of different currencies -", rsub_curr)

    ''' Similar to subtract function '''
    rsub_curr2 = 5.00 - curr
    print ("12. Reverse subtraction of same currency -", rsub_curr2)

    ''' First convert Currency 1 to Currency 2 and then compare '''
    gt_curr = curr > curr2
    print ("13. Currency 1 greater than Currency 2? -", gt_curr)

    gt_curr2 = curr2 > 5.00
    ''' Where X is equal to the number. '''
    print ("14. Currency 2 greater than X? -", gt_curr2)

    ''' First convert Currency 1 to Currency 2 and then compare '''
    lt_curr = curr < curr2
    print ("15. Currency 1 less than Currency 2? -", lt_curr)

    lt_curr2 = curr2 < 5.00
    ''' Where X is equal to the number. '''
    print ("16. Currency 2 less than X? -", lt_curr2)
      
main()
