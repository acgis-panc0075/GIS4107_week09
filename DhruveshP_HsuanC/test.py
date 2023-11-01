data="""Rank	Country	 Continent	Statistical region	Pop 01Jul2016	Pop 01Jul2017	Change
1	China	Asia	Eastern Asia	1,403,500,365	1,409,517,397	+0.4%
2	India	Asia	Southern Asia	1,324,171,354	1,339,180,127	+1.1%
3	United States	Americas	Northern America	322,179,605	324,459,463	+0.7%
4	Indonesia	Asia	South-Eastern Asia	261,115,456	263,991,379	+1.1%"""

country_to_pop = dict()
country_pop_lines = data.splitlines( )
header_S = country_pop_lines[0].split('\t')
header = [col.strip() for col in header_S] 
for country_pop_row in country_pop_lines[1:]:
    values = country_pop_row.split('\t')
    entry = {header[i]: values[i] for i in range(len(header))}
    entry['Pop 01Jul2016'] = int(entry['Pop 01Jul2016'].replace(',', ''))
    entry['Pop 01Jul2017'] = int(entry['Pop 01Jul2017'].replace(',', ''))
    country_to_pop[entry['Country']] = entry


def get_continent_populations():
    """Returns a dict where the key is the name of the continent and
       the value is the total population of all countries on that continent"""
    continent_populations = {}
    for country_data in country_to_pop.values():
        continent = country_data['Continent']
        population = country_data['Pop 01Jul2017']

        if continent in continent_populations:
            continent_populations[continent] += population
        else:
            continent_populations[continent] = population

    return continent_populations



