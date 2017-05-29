"""
http://www.pygal.org/en/latest/documentation/index.html
"""
import pygal


class PyGal(object):
    def bar_char(self, id, dictionary):
        try:
            bar_chart = pygal.Bar(title='Employee Information', x_title='Employee ID\'s', y_title='Employee Data')
            for key in dictionary:
                bar_chart.add(key, dictionary[key])  # Add some values
            bar_chart.x_labels = id
            # bar_chart.render_in_browser()
            return True
        except Exception as err:
            print("The exception is: Invalid Data", err)
