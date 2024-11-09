import county_demographics
import build_data
import data

# part 1
def population_total(counties:list[data.CountyDemographics])->int: # takes in a list of counties in the form of the
    # class CountyDemographics and returns the total 2014 population of all counties as an integer
    totalPop = 0
    for i in counties:
        totalPop = totalPop + i.population['2014 Population']
    return totalPop

# part 2
def filter_by_state(list1:list[data.CountyDemographics],state:str) -> list[data.CountyDemographics]: #takes in a list
    # of counties in the form of the class CountyDemographics and a state as a str and returns a new list of
    # CountyDemographics objects that have that state attribute
    stateCounties = []
    for i in list1:
        if i.state == state:
            stateCounties.append(i)
    return len(stateCounties)

# part 3
def population_by_education(list1:list[data.CountyDemographics],edu:str)->float: # takes in a list of counties in the
    # form of the class CountyDemographics and an education status as a str and returns a float value of the population
    # of people with that level of education across counties
    totalPop = 0.0
    for i in list1:
        if edu in i.education:
            percent = i.education[edu]
            subPop = float(percent / 100 * i.population['2014 Population'])
            totalPop = totalPop + subPop
    return totalPop

def population_by_ethnicity(list1:list[data.CountyDemographics],eth:str)->float: # takes in a list of counties in the
    # form of the class CountyDemographics and an ethnicity as a str and returns a float value of the population of
    # that ethnicity across counties
    totalPop = 0.0
    for i in list1:
        if eth in i.ethnicities:
            percent = i.ethnicities[eth]
            subPop = float(percent / 100 * i.population['2014 Population'])
            totalPop = totalPop + subPop
    return totalPop

def population_below_poverty_level(list1:list[data.CountyDemographics])->float: # takes in a list of counties in the
    # form of the class CountyDemographics and returns a float value of the population of people below the poverty level
    # across counties
    totalPop = 0.0
    for i in list1:
        percent = i.income['Persons Below Poverty Level']
        subPop = float(percent / 100 * i.population['2014 Population'])
        totalPop = totalPop + subPop
    return totalPop

# part 4

def percent_by_education(list1:list[data.CountyDemographics],edu:str)->float: # takes in a list of counties in the
    # form of the class CountyDemographics and an education status as a str and returns a float value of the percent of
    # the population across counties that has that education level
    allTotal = population_total(list1)
    subTotal = population_by_education(list1,edu)
    percent = subTotal/allTotal * 100
    return percent

def percent_by_ethnicity(list1:list[data.CountyDemographics],eth:str)->float: # takes in a list of counties in the
    # form of the class CountyDemographics and an ethnicity as a str and returns a float value of the percent of
    # the population of that ethncity across counties
    percent = 0.0
    allTotal = population_total(list1)
    subTotal = population_by_ethnicity(list1, eth)
    percent = subTotal / allTotal * 100
    return percent

def percent_below_poverty_level(list1:list[data.CountyDemographics])->float: # takes in a list of counties in the
    # form of the class CountyDemographics and returns a float value of the percent of the population across counties
    # that is below the poverty level
    percent = 0.0
    allTotal = population_total(list1)
    subTotal = population_below_poverty_level(list1)
    percent = subTotal / allTotal * 100
    return percent

# part 5

def education_greater_than(list1:list[data.CountyDemographics],edu:str,thresh:float)->list[data.CountyDemographics]:
    # takes in a list of counties in the form of the class CountyDemographics, an education status as a str, and a
    # threshold value as an int and returns a new list of CountyDemographics objects that have a percentage of people
    # of the certain education level above the threshold
    newList = []
    for i in list1:
        if i.education[edu] > thresh:
            newList.append(i)
    return newList


def education_less_than(list1: list[data.CountyDemographics],edu:str,thresh:float) -> list[data.CountyDemographics]:
    # takes in a list of counties in the form of the class CountyDemographics, an education status as a str, and a
    # threshold value as an int and returns a new list of CountyDemographics objects that have a percentage of people
    # of the certain education level lower than the threshold
    newList = []
    for i in list1:
        if i.education[edu] < thresh:
            newList.append(i)
    return newList

def ethnicity_greater_than(list1: list[data.CountyDemographics],eth:str,thresh:float) -> list[data.CountyDemographics]:
    # takes in a list of counties in the form of the class CountyDemographics, an ethnicity as a str, and a
    # threshold value as an int and returns a new list of CountyDemographics objects that have a percentage of people
    # of the certain ethnicity above the threshold
    newList = []
    for i in list1:
        if i.ethnicities[eth] > thresh:
            newList.append(i)
    return newList

def ethnicity_less_than(list1: list[data.CountyDemographics],eth:str,thresh:float) -> list[data.CountyDemographics]:
    # takes in a list of counties in the form of the class CountyDemographics, an ethnicity as a str, and a
    # threshold value as an int and returns a new list of CountyDemographics objects that have a percentage of people
    # of the certain ethnicity lower than the threshold
    newList = []
    for i in list1:
        if i.ethnicities[eth] < thresh:
            newList.append(i)
    return newList

def below_poverty_level_greater_than(list1: list[data.CountyDemographics],thresh:float) -> list[data.CountyDemographics]:
    # takes in a list of counties in the form of the class CountyDemographics and a threshold value as an int and
    # returns a new list of CountyDemographics objects that have a percentage of people
    # below the poverty level, above the threshold
    newList = []
    for i in list1:
        if i.income["Persons Below Poverty Level"] > thresh:
            newList.append(i)
    return newList

def below_poverty_level_less_than(list1: list[data.CountyDemographics],thresh:float) -> list[data.CountyDemographics]:
    # takes in a list of counties in the form of the class CountyDemographics and a threshold value as an int and
    # returns a new list of CountyDemographics objects that have a percentage of people
    # below the poverty level, lower than the threshold
    newList = []
    for i in list1:
        if i.income["Persons Below Poverty Level"] < thresh:
            newList.append(i)
    return newList