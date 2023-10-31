from world_pop_by_country import data as country_pop

# Key = country name and 
# Value = population as a number (i.e. not text containing commas)
#

country_to_pop = dict()

country_pop_lines = country_pop.splitlines( )
header = country_pop_lines[0].split('\t')

for country_pop_row in country_pop_lines[1]:
    values = country_pop_row.split(',')
    entry = {header[i]: values[i] for i in range(len(header))}
    country_to_pop[entry['Name']] = entry
    
print(header)