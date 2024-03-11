# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 19:32:22 2024

@author: Vikrant sinha
"""
# DATETIME LIBRARY:-It helps to get the current date and time
import datetime as dt
#calender library used to access the calender and the years
import calendar as cd

class transactions:
    
    
# A CONSTRUCTOR HAVING THE DICTONARY OF YOUR EXPENSES NAMED : KHARCHA AND HAVE THE TOTAL SUM OF YOUR MONEY
    def __init__(self,total_money):
        self.total_money=total_money
        self.kharcha={}
        
        
# FOR GETTING SAVINGS
    def savings(self,saving):
        self.saved_money=saving
        
        
# SPENDING GETING FUNCTION
    def spendings(self,exp_nam,exp_pri):
        self.spend_money=self.total_money-self.saved_money
        
        if self.spend_money>0:
            key=exp_nam
            cost=exp_pri
            self.kharcha[key]=cost
        else:
            print("The wallet of yours has been emptied/or your savings is more than your main money")
            
            
            
# SPENDING DISPLAY
    def show_spendings(self):
        print(self.kharcha)
        
        
# ACCOUNT SECTION FUNCTION
    def show_acount(self):
        self.money_spended=sum(self.kharcha.values())
        self.left=self.spend_money-self.money_spended
        spend_diary={'total money':self.total_money,'savings':self.saved_money,'Money spended':self.money_spended,'money left':self.left}
        print(spend_diary)
        
        
# DAILY LIMIT SECTION FUNCTION :-)
    def daily_limit(self):
#here we had used the calender as well as datetime module
        now=dt.datetime.now()
        month=now.month
        year=now.year
        total_days=cd.monthrange(year,month)[1]
        date=now.day
        to_count=total_days - date
        
        money_to_spend=self.left/to_count
        
        print("The mmoney you can spent on daily basis is:-",money_to_spend)
        

# CALLING OUR MAIN CLASS USING AN OBJECT NAMED AKSHAY 
akshay=transactions(10000)

# ENTER THE AMOUNT OF MONEY YOU WANT TO SAVE IN THE CLOSED BRACKET 
akshay.savings(1000)

#ENTER YOUR SPENDINGS THAT YOU HAVE DONE IN FORMAT ('SPENDING NAME',SPENDING COST's)
akshay.spendings('rent', 2000)
akshay.spendings('food', 1000)
akshay.spendings('gift', 500)
akshay.spendings('Chicken',125)
print("------:The money have spended:-------")
#FROM NEXT LINE YOU WILL GET THE OUTPUT ABOUT YOUR SPENDINGS
akshay.show_spendings()
print("------:The acount:----")
#FROM NEXT LINE YOU WILL GET THE SHOWN OF YOUR ACCOUNT
akshay.show_acount()
print("------:Daily Limit:------")
#FROM THIS LINE YOU WILL GET THE KNOW ABOUT HOW MUCH YOU CAN EXPEND IN A DAY
akshay.daily_limit()

        
            
            
            
    
