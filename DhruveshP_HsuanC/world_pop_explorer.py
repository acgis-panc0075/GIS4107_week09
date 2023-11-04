#-------------------------------------------------------------------------------
# Name:        world_pop_explorer.py
#
# Purpose:     Provide some functions to analyze the data in
#              world_pop_by_country.py
#
# Author:      David Viljoen
#
# Created:     24/11/2017
# Last update: 31/10/2022
#-------------------------------------------------------------------------------

from world_pop_by_country import data as country_pop

# Key = country name and 
# Value = population as a number (i.e. not text containing commas)

country_to_pop = dict()

country_pop_lines = country_pop.splitlines( )
country_pop_lines.remove(country_pop_lines[0])
country_pop_list = [item.split('\t') for item in country_pop_lines]


def get_country_count():
    """Return the number of countries in country_pop.  
    NOTE:  Assume data (country_pop) will always have a header"""
    return len(country_pop_lines) 



def conv_num_with_commas(number_text):
    """Convert a number with commas (str) to a number.
       e.g. '1,000' would be converted to 1000"""
    return int(number_text.replace(',', ''))




def get_top_five_countries():
    """Return a list of names of the top five countries in terms of population"""
    result = list()
    for item in country_pop_list[slice(5)]:
        result.append(item[1])
    return result




def set_country_to_pop():
    """Sets the global country_to_pop dictionary where key is country name
         and value is a tuple containing two elements:
            1. A numeric version of the comma separated number in the
               Pop 01Jul2017 column
            2. The % decrease as a number
    """ 
    global country_to_pop
    for item in country_pop_list:
        country_to_pop.update({item[1]:(conv_num_with_commas(item[5]),float(item[6].strip('%')))})
    return country_to_pop


   
def get_population(country_name):
    """Given the name of the country, return the population as of 
       Pop 01Jul2017 from country_to_pop.  
       If the country_to_pop is empty (i.e. no keys or values), 
       then run set_country_to_pop to initialize it."""
    global country_to_pop
    if not bool(country_to_pop):
        set_country_to_pop()
    result = country_to_pop.get(country_name)
    if result is not None:
        return result[0]
    else:
        return None 

   
    

def get_continents():
    """Return the list of continents"""
    continents = list()
    for items in country_pop_list:
        if items[2] not in continents:
            continents.append(items[2])
    continents.sort()
    return continents



    
def get_continent_populations():
    """Returns a dict where the key is the name of the continent and
       the value is the total population of all countries on that continent"""
    continent_list = get_continents()
    pop_num =0
    continent_populations = dict()

    for continent in continent_list:
        for items in country_pop_list:
            if items[2] == continent:
                pop_num += conv_num_with_commas(items[5])
            else:
                continue
        continent_populations.update({continent : pop_num})
    return continent_populations



