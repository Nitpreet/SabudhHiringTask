# -*- coding: utf-8 -*-
"""
Created on Tue May  5 15:48:12 2020

@author: Nitpreet
"""

'''
I first tried appending unique entries to their respective list But it was taking more than 7-8 mintues. 
Then I tried set and it worked fine.   
'''


def pentagonal(range_number):
    penta = set()
    for number in range(range_number):
        updated = ((number*(3*number-1))/2)
        penta.add(updated)
    return penta


def hexagonal(range_number):
    hexa = set()
    for number in range(range_number):
        updated = (number*(2*number-1))
        hexa.add(updated)
    return hexa

def triangle(range_number):
    triangle = set()
    for number in range(range_number):
        updated = ((number*(number+1))/2)
        triangle.add(updated)
    return triangle

def main():
    hexa = hexagonal(1000000)
    penta = pentagonal(1000000)
    tri = triangle(1000000)
    for number in tri:
        if number in hexa and number in penta and number>40755:
            print(number)
            
            
if __name__=="__main__":
    main()            