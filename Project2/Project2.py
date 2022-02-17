################## Helper Code Below -- don't delete! ##################
#Note, I fixed the helper code so it would run on my system. it was giving me an error  before 

# Helper Code 1
Path = "C:\\Users\\Spencer\\Documents\\GitHub\\CPE_101\\Project2\\" 
#Path = "C:\\Users\\spenc\\OneDrive\\Documents\\GitHub\\CPE_101\\Project2\\"
bach_data = []
with open(Path + "Bachelors.txt", "r") as file:
    for num in file:
        num = float(num.strip())
        bach_data.append(num)
file.close()


# Helper Code 2
pop_data = []
with open(Path + "Population.txt", "r") as file:
    for value in file:
        value = float(value.strip())
        pop_data.append(value)
file.close()



# Helper Code 3
avg_income = []
with open(Path + "Income.txt", "r") as file:
    for value in file:
        value = float(value.strip())
        avg_income.append(value)
file.close()



# Helper Code 4
high_school_data = []
with open(Path + "HighSchool.txt", "r") as file:
    for value in file:
        value = float(value.strip())
        high_school_data.append(value)
file.close()


# Helper Code 5
poverty_data = []
with open(Path + "Poverty.txt", "r") as file:
    for value in file:
        value = float(value.strip())
        poverty_data.append(value)
file.close()

# TASK 1

# QUESTION 1.1
def percent_bachelors(bach_data, pop_data): #loops over both lists and sums them and then devides accordingly.
    batchSum = 0
    popSum = 0
    for i in range(0,len(bach_data)):
        batchSum += (bach_data[i]/100)*pop_data[i] 
        popSum += pop_data[i]
    return (batchSum/popSum)*100
    '''
    This function takes the bachelor's and population data
    for each county and returns the percentage of people
    with a bachelors or higher across all counties
    '''
print(percent_bachelors(bach_data, pop_data))

# QUESTION 1.2


def income_above_50k(avg_income):
    over50 = 0
    count = 0
    for income in avg_income:
        count+=1
        over50 = over50 + 1 if (income > 50000) else over50
    return (over50/count)*100
    '''
    This function takes the average income of all counties
    and returns the percentage of counties with an income
    above $50,000
    '''

print (income_above_50k(avg_income))
# ---------------------------------------------------------------------------------------------------- #


# TASK 2
def high_school_below_threshold(high_school_data, threshold):
    count = 0
    for value in high_school_data:
        count = count + 1 if (value < threshold) else count
    return count
        
    '''
    Takes a list of highschool graduation rates and a threshold 
    and returns the amount of counties that are under that threshold
    '''
print(high_school_below_threshold(high_school_data, 60))
# ---------------------------------------------------------------------------------------------------- #


# TASK 3
def bachelors_above_threshold(bach_data, threshold):
    count = 0
    for value in bach_data:
        count = count + 1 if (value > threshold) else count
    return count
    '''
    Takes as inputs the bachelors data and a threshold.
    Returns the total number of counties with a percentage of bachelors strictly greater
    than the threshold percentage.
    '''
print(bachelors_above_threshold(bach_data, 60))

# ---------------------------------------------------------------------------------------------------- #


# TASK 4


def below_poverty_total(poverty_data, pop_data):
    sum = 0
    for i in range (0,len(pop_data)):
        sum += pop_data[i] * (poverty_data[i]/100)
    return sum
    ''' Takes data on population and poverty rates and calculates the total amount of people in poverty '''

print (below_poverty_total(poverty_data, pop_data))
# ---------------------------------------------------------------------------------------------------- #


# TASK 5
def percent_below_poverty(poverty_data, pop_data):
    '''Takes the computation from the below poverty data and sums the population and returns the ration between them times 100'''
    
    below = below_poverty_total(poverty_data, pop_data)
    total = 0
    for pop in pop_data:
        total += pop 

    return (below/total)*100 #15.366286413307403

print (percent_below_poverty(poverty_data, pop_data))


# ---------------------------------------------------------------------------------------------------- #


# TASK 6
def education_vs_poverty(bach_data, poverty_info):
    '''Takes the poverty data as well as the bachelors degree data and separates them into 4 catagories based on the rate of bachelor's degrees and then finds the average of each groupand returns a formatted string containing that data'''
    zero = [0,0]
    ten = [0,0]
    twenty = [0,0]
    thirty = [0,0]
    for i in range(0,len(poverty_info)):
        if bach_data[i] >= 30:
            thirty[0] += 1
            thirty[1] += poverty_info[i]
        elif bach_data[i] >= 20:
            twenty[0] += 1
            twenty[1] += poverty_info[i]
        elif bach_data[i] >= 10:
            ten[0] += 1
            ten[1] += poverty_info[i]
        elif bach_data[i] < 10:
            zero[0] += 1
            zero[1] += poverty_info[i]
            
    return (f"Average Poverty Levels:\nBachelors <10%: {zero[1]/zero[0]}\nBachelors >=10% and <20%: {ten[1]/ten[0]}\nBachelors >=20% and <30%: {twenty[1]/twenty[0]}\nBachelors >=30%: {thirty[1]/thirty[0]}")


print(education_vs_poverty(bach_data, poverty_data))

'''
Task 7:
The result given from comparing the education levels and the poverty data shows a clear inverse correlation between the two.
This is insufficient evidence to come to any conclusion about why this is the case. 
More evidence and research would be needed in order to decide weather there is a causal relationship between the two datasets.
There is a whole host of evidence that shows that it is the case that there is a causal relationship between increase and education and reduction of poverty however, 
there are many other factors at play and much more evidence than just their related rates was used to come to these conclusions.
'''