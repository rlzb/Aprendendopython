def figure_x(salary):
    tally = 0 
    if salary == 0:
        tally +=1
        
    while salary >=1:
        salary = salary /10
        tally +=1
    
    return tally
print("The CEO has a " + str(figure_x(2300000)) + "-figure salary")