#!/usr/bin/env python3
"""This is the program to obtain Alta3 certification, my instructor is Mr. Chad Feese. 
This program will cover to,
1. Include a shebang
2. Documentation at the top (which is this you are reading :))
3. Comments on the code for clarity
4. script with main()"""

import requests
import os

def findPopulation():
    """Main function to retrive the data from Data USA  API"""
    # create request object for Data USA
    reqDataUSA = requests.get("https://datausa.io/api/data?drilldowns=Nation&measures=Population")
    os.system('clear')
    for x in range(len(reqDataUSA.json().get('data'))):
        print(f"{x}: {reqDataUSA.json().get('data')[x].get('Year')}")
    yearRequest = input("Please choose the number from the year list above to find out the population\n>")
    if yearRequest.isdigit() == True:
        yearRequest = int(yearRequest)
        if yearRequest >= 0 and yearRequest < 6:
            print(f"\nThe total population for the year {reqDataUSA.json().get('data')[yearRequest].get('Year') } is {reqDataUSA.json().get('data')[yearRequest].get('Population')}")
            print(f"\nThe source of this data is from {reqDataUSA.json().get('source')[0].get('annotations').get('source_name')} - {reqDataUSA.json().get('source')[0].get('annotations').get('source_description')}")
        else:
            print("The choice you have enter is not present")
    else:
        print("The choice you have enter is not present")


def main():
    toContinue = "Y"
    while toContinue == "Y":
        findPopulation()
        toContinue = input("\nDo you want to continue (Y / N)?").upper()
    if toContinue.upper() != "N":
        print("You have not chosen Y / N, hence quiting the program")
if __name__ == "__main__":
    main()
