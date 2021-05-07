#!/usr/bin/env python3
"""This is the program to obtain Alta3 certification, my instructor is Mr. Chad Feese. 
This program will cover to,
1. Include a shebang
2. Documentation at the top (which is this you are reading :))
3. Comments on the code for clarity
4. script with main()"""

# Importing requests module to retrive objects from API.
import requests

#Importing os module to use for clearing the screen.
import os

"""Function to retrive the data from Data USA API and ask user to input year to find out thepopulation of that year"""

def findPopulation():
    # create request object for Data USA.
    reqDataUSA = requests.get("https://datausa.io/api/data?drilldowns=Nation&measures=Population")
    # Using os moudle to clear the screen.
    os.system('clear')

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

""" Main function to ask user whether or not to continue for finding the population"""
def main():
    
    # Defining the variable to check whether to continue the program or not
    toContinue = "Y"
    
    # While loop to check the population or to exit
    while toContinue == "Y":

        # calling the funtion to find the population
        findPopulation()

        # User input whether to continue or not and convert to Upper case for checking
        toContinue = input("\nDo you want to continue (Y / N)?").upper()

    # This condition is to check if the user Input other than Y or N    
    if toContinue.upper() != "N":
        
        # Display that the user chosen other than Y / N and quiting the program
        print("You have not chosen Y / N, hence quiting the program")

# Check to run if this module is the entry point to this program
if __name__ == "__main__":
    # calling main function
    main()
