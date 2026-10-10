# Takes in a set of data and generates a graph from it
import matplotlib.pyplot as plt
from operator import itemgetter

class DataDisplay:
    def generate_chart_line(self, data, x_key, y_key, series_key=None):
        if not next(iter(data.values())):
            print("No data to plot!")
            return

        series = {}
        for row in next(iter(data.values())):
            series.setdefault(row.get(series_key), []).append(row)

        plt.figure(figsize=(8, 6))

        for name, rows in series.items():
            rows.sort(key=itemgetter(x_key))

            x_values = []
            y_values = []

            for row in rows:
                x_values.append(row[x_key])
                y_values.append(float(row[y_key]))

            plt.plot(x_values, y_values, marker='o', label=name)

        if series_key:
            plt.legend()

        plt.xlabel(x_key)
        plt.ylabel(y_key)
        plt.title(next(iter(data.keys())))

        plt.show()

    def generate_chart_pie(self, data, value_key, label_key, series_key, get_series):
        if not next(iter(data.values())):
            print("No data to plot!")
            return

        values = []
        labels = []

        for row in next(iter(data.values())):
            if row[series_key] == get_series:
                values.append(int(row[value_key]))
                labels.append(row[label_key])

        plt.pie(values, labels=labels, autopct='%1.0f%%')
        plt.show()

    def generate_chart_bar(self, data, x_key, y_key, series_key):
        if not next(iter(data.values())):
            print("No data to plot!")
            return

        x = []
        y = {}

        for row in next(iter(data.values())):
            if row[x_key] not in x:
                x.append(row[x_key])

            if row[series_key] in y:
                y[row[series_key]].append(int(row[y_key]))
            else:
                y[row[series_key]] = [int(row[y_key])]

        plt.grouped_bar(y, tick_labels=x)
        plt.legend()
        plt.show()