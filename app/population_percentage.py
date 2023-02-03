import read_csv
import charts


def run():
    dataset = read_csv.read_csv('data.csv')
    continent = input('Type continent: ')

    dataset = list(filter(lambda i: i['Continent'] == continent, dataset))

    country = list(map(lambda i: i['Country/Territory'], dataset))
    percentage = list(map(lambda i: i['World Population Percentage'], dataset))
    charts.generate_pie_chart(country, percentage)


if __name__ == '__main__':
    run()
