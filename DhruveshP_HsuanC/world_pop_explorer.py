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
header = country_pop_lines[0].split('\t')

for country_pop_row in country_pop_lines[1:]:
    values = country_pop_row.split('\t')
    entry = {header[i]: values[i] for i in range(len(header))}
    entry['Pop 01Jul2016'] = int(entry['Pop 01Jul2016'].replace(',', ''))
    entry['Pop 01Jul2017'] = int(entry['Pop 01Jul2017'].replace(',', ''))
    country_to_pop[entry['Country']] = entry


def get_country_count():
    """Return the number of countries in country_pop.  
    NOTE:  Assume data (country_pop) will always have a header"""
    return len(country_to_pop)

def conv_num_with_commas(number_text):
    """Convert a number with commas (str) to a number.
       e.g. '1,000' would be converted to 1000"""
    return int(number_text.replace(',', ''))

def get_top_five_countries():
    """Return a list of names of the top five countries in terms of population"""
    sorted_countries = sorted(country_to_pop.values(), key=lambda x: x['Pop 01Jul2017'], reverse=True)
    top_five = [entry['Country'] for entry in sorted_countries[:5]]
    return top_five

def set_country_to_pop():
    """Sets the global country_to_pop dictionary where key is country name
         and value is a tuple containing two elements:
            1. A numeric version of the comma separated number in the
               Pop 01Jul2017 column
            2. The % decrease as a number
    """ 
    global country_to_pop
    lines = country_pop.strip().split('\n')
    header = lines[0].split('\t')
    for line in lines[1:]:
        parts = line.split('\t')
        country_name = parts[header.index('Country')]
        population = conv_num_with_commas(parts[header.index('Pop 01Jul2017')])
        percentage_change = float(parts[header.index('Change')].strip('%'))
        country_to_pop[country_name] = (population, percentage_change)



def get_population(country_name):
    """Given the name of the country, return the population as of 01Jul2017
       from country_to_pop.  If the country_to_pop is
       empty (i.e. no keys or values), then run set_country_to_pop
       to initialize it."""
    if not country_to_pop:
     set_country_to_pop()
    return country_to_pop.get(country_name, (0, 0))

def get_continents():
    """Return the list of continents"""
    continents = set(country['Continent'] for country in country_pop)
    return list(continents)

def get_continent_populations():
    """Returns a dict where the key is the name of the continent and
       the value is the total population of all countries on that continent"""
    continent_populations = {}
    for country in country_pop:
        continent = country['Continent']
        population = conv_num_with_commas(country['Pop 01Jul2017'])
        continent_populations[continent] = continent_populations.get(continent, 0) + population
    return continent_populations 
