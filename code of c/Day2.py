
def tipping(tip_percentage,total_bill,total_people , total):
    
    if tip_percentage in [10 ,12 ,15]:
        
       tip = ((total_bill * (tip_percentage/100))+tip)
       total_with_tip  = (total_bill + tip)/total_people
       return total_with_tip
    else:
         return total
        

def main():

    print("Welcome To the Tip Calculator!!")
    
    
    total_bill= float(input("What was the total Bill ?  "))
    total_people= int(input("How many people to split the bill ? "))
    tip_percentage = int(input("What percentage tip would you like to give 10 , 12 or 15 : "))

    total = total_bill / total_people 
    pay = round(tipping(tip_percentage,total_bill,total_people , total))


    print(f"Each person should pay ${pay:.2f}")
    
main()