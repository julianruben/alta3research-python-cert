#!/usr/bin/env python3
"""This is the program to obtain Alta3 certification, my instructor is Mr. Chad Feese. 
This program will cover to,
1. Include a shebang
2. Documentation at the top (which is this you are reading :))
3. Comments on the code for clarity
4. script with main()"""

import requests

def main():
    """Main function to retrive the data from Data USA  API"""
    # create request object for Data USA
    reqNasa = requests.get("https://datausa.io/api/data?drilldowns=Nation&measures=Population")
    for x in range(len(reqNasa.json().get('data'))):
        print(f"{x}: {reqNasa.json().get('data')[x].get('Year')}")
    yearRequest = int(input("Please choose the number from the year list above to find out the population\n>"))
    print(f"The total population for the year {reqNasa.json().get('data')[yearRequest].get('Year') } is {reqNasa.json().get('data')[yearRequest].get('Population')}")
main()
