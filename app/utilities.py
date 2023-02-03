def get_population(country):
    population_dict = {
        '1970': country['1970 Population'],
        '1980': country['1980 Population'],
        '1990': country['1990 Population'],
        '2000': country['2000 Population'],
        '2010': country['2010 Population'],
        '2015': country['2015 Population'],
        '2020': country['2020 Population'],
        '2022': country['2022 Population']
    }

    labels = population_dict.keys()
    values = population_dict.values()
    return labels, values


def population_by_country(dataset, country):
    result = list(filter(lambda item: item['Country/Territory'] == country, dataset))
    return result


def continent(dataset, continent):
    result = list(filter(lambda item: item['Continent'] == continent, dataset))
    return result
