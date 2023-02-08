import utilities
import read_csv
import charts
import pandas as pd


def run():
    '''
    if len(answer) > 0:
        country = answer[0]
        labels, values = utilities.get_population(country)
        charts.generate_bar_chart(country['Country/Territory'], labels, values)
'''

dataf = pd.read_csv('data.csv')
dataf = dataf[dataf['Continent'] == 'Europe']

countries = dataf['Country/Territory'].values
percentages = dataf['World Population Percentage'].values
charts.generate_pie_chart(countries, percentages)

dataset = read_csv.read_csv('data.csv')
country = input('Type country: ')
print(country)

answer = utilities.population_by_country(dataset, country)

if len(answer) > 0:
        country = answer[0]
        labels, values = utilities.get_population(country)
        
        
        
if __name__ == '__main__':
    run()



"""

import utilities


def get_total(orders):
    obtain = utilities.get_totals(orders)
    summary = utilities.calc_total(obtain)
    return summary


orders = [
    {
        "customer_name": "Nicolas",
        "total": 100,
        "delivered": True,
    },
    {
        "customer_name": "Zulema",
        "total": 120,
        "delivered": False,
    },
    {
        "customer_name": "Santiago",
        "total": 20,
        "delivered": False,
    }
]

total = get_total(orders)
print(total)


"""