#!/usr/bin/env python3
"""This is the program to obtain Alta3 certification, my instructor is Mr. Chad Feese. 
This program will cover to,
1. Include a shebang
2. Documentation at the top (which is this you are reading :))
3. Comments on the code for clarity
4. script with main()"""

#Importing os module to use for clearing the screen.
import os

# Importing requests module to retrive objects from API.
import requests

# Importing matplotlib for generating graph
import matplotlib.pyplot as mplot 

"""Function to retrive the data from Data USA API and ask user to input year to find out thepopulation of that year"""

def findPopulation():
    # create request object for Data USA.
    reqDataUSA = requests.get("https://datausa.io/api/data?drilldowns=Nation&measures=Population")
    # Displa the label for the list of years
    print("\n List of year population")

    # This for loop to iterate based on the length of the data from the dictionary.
    for x in range(len(reqDataUSA.json().get('data'))):

        # To print the list of years from the dictionary.
        print(f"{x}: {reqDataUSA.json().get('data')[x].get('Year')}")

    # To accept the year to display population from the user based on the year list.
    yearRequest = input("Please choose the number from the year list above to find out the population\n>")

    # Condition to check whether the user input value is a digit or not.
    if yearRequest.isdigit() == True:

        # Converting the user input to Integer.
        yearRequest = int(yearRequest)

        # Condition to check wehether the user input value is within the data range. 
        if yearRequest >= 0 and yearRequest < int(len(reqDataUSA.json().get('data'))):
            
            # To display the population for the year user input.
            print(f"\nThe total population for the year {reqDataUSA.json().get('data')[yearRequest].get('Year') } is {reqDataUSA.json().get('data')[yearRequest].get('Population')}")
            
            # To display the source of the data that was displayed.
            print(f"\nThe source of this data is from {reqDataUSA.json().get('source')[0].get('annotations').get('source_name')} - {reqDataUSA.json().get('source')[0].get('annotations').get('source_description')}")
        else:
            # This else is when the user input is out of the given list range.
            print("The choice you have enter is not present")
    else:
        # This else is when the user input is not an digit.
        print("The choice you have enter is not present")

""" Function to generate pie chart for the population"""
def createGraph():
     # Create request object for Data USA.
    reqDataUSA = requests.get("https://datausa.io/api/data?drilldowns=Nation&measures=Population")
    # Initializing list for labels to display year and populaiton.
    displayLabels = []

    # Initalizing list for population to calculate the percentage for pie chart.
    populationList = []

    # Initializing list for population percentage for pie chart.
    sizes = []

    # This for loop to iterate based on the length of the data from the dictionary.
    for x in range(len(reqDataUSA.json().get('data'))):
        # Concatenating year and population to add it in the lable list.
        labelYearPopulation = reqDataUSA.json().get('data')[x].get('Year'),reqDataUSA.json().get('data')[x].get('Population')
        # Adding the list for label.
        displayLabels.append(labelYearPopulation)
        # Adding the list to use for creating the size list
        populationList.append(reqDataUSA.json().get('data')[x].get('Population'))

    # This for loop is to append the size list with the percentage of population to use in pie chart.
    for y in populationList: 
        # Calculate the percentage value
        sizeValue =float((y/sum(populationList))*100)
        # Adding the percentage value in the sizes list
        sizes.append(sizeValue)
    print(sizes)
    # Tuples to use in the pie chart 
    explode = (0,0,0,0,0,0) 
    fig1,ax1 = mplot.subplots()
    ax1.pie(sizes, explode=explode, labels=displayLabels, autopct='%1.1f%%',
        shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    
    # Saving the generated pie chart in the given location and with the given name.
    mplot.savefig("/home/student/static/piePopulationChart.png")


""" Main function to ask user what action to perform and also whether or not to continue the program"""
def main():
    
    # Defining the variable to check whether to continue the program or not
    toContinue = "Y"
    
    # While loop to check the population or to exit
    while toContinue == "Y":
        # Using os moudle to clear the screen.
        os.system('clear')
        # Getting the input from the user to choose what action to perform.
        inputAction = input("Please select the action \n1. Find Population for a particular year \n2. Download year wise pie chart for Population\n>")
        
        # Condition to check and call the action method
        if int(inputAction) == 1:
            # calling the funtion to find the population
            findPopulation()
        elif int(inputAction) == 2:
            createGraph()
            print("Pie Chart graph is generted successfully and placed in /home/student/static/piePopulationChart.png")
        else:
            print("You have chosed an incorrect option") 
        # User input whether to continue or not and convert to Upper case for checking
        toContinue = input("\nDo you want to continue (Y / N)?").upper()

    # This condition is to check if the user Input other than Y or N    
    if toContinue.upper() != "N":
        
        # Display that the user chosen other than Y / N and quiting the program
        print("You have not chosen Y / N, hence quiting the program")
    

# Check to run if this module is the entry point to this program
if __name__ == "__main__":
    # Calling main function
    main()
