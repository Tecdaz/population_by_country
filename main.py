import utils
import charts
import read_csv


def run():
    data = read_csv.read_csv('./world_population.csv')
    country = input('Ingrese el pais => ')

    result = utils.population_by_country(data, country)
    if len(result) > 0:
        country = result[0]
        keys, values = utils.get_population(country)
        charts.generate_bar_chart(keys, values)


if __name__ == '__main__':
    run()
