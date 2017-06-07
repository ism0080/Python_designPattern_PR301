"""
http://www.pygal.org/en/latest/documentation/index.html
"""
import pygal
from abc import abstractmethod, ABCMeta


# class PyGal(object):
#     def bar_char(self, id, dictionary):
#         try:
#             bar_chart = pygal.Bar(title='Employee Information', x_title='Employee ID\'s', y_title='Employee Data')
#             for key in dictionary:
#                 bar_chart.add(key, dictionary[key])  # Add some values
#             bar_chart.x_labels = id
#             # bar_chart.render_in_browser()
#             return True
#         except Exception as err:
#             print("The exception is: Invalid Data", err)

class AbstractBuilder(metaclass=ABCMeta):
    def __init__(self):
        self._chart = None

    @abstractmethod
    def set_title(self):
        pass

    @abstractmethod
    def set_chart_type(self):
        pass

    @abstractmethod
    def set_data(self, dict):
        pass

    @abstractmethod
    def set_labels(self, id):
        pass

    def get_result(self):
        self._chart.render_in_browser()


class BarChartBuilder(AbstractBuilder):
    def __init__(self):
        super().__init__()

    def set_title(self):
        self._chart.title = "bar chart"
        self._chart.x_title = "x title"
        self._chart.y_title = "y title"

    def set_chart_type(self):
        self._chart = pygal.Bar()

    def set_data(self, dict):
        for key in dict:
            self._chart.add(key, dict[key])

    def set_labels(self, id):
        self._chart.x_labels = id


class PieChartBuilder(AbstractBuilder):
    def __init__(self):
        super().__init__()

    def set_title(self):
        self._chart.title = "pie chart"

    def set_chart_type(self):
        self._chart = pygal.Pie()

    def set_data(self, dict):
        for key in dict:
            self._chart.add(key, dict[key])

    def set_labels(self, id):
        pass


class RadarChartBuilder(AbstractBuilder):
    def __init__(self):
        super().__init__()

    def set_title(self):
        self._chart.title = "Radar chart"
        self._chart.x_title = "x title"
        self._chart.y_title = "y title"

    def set_chart_type(self):
        self._chart = pygal.Radar()

    def set_data(self, dict):
        for key in dict:
            self._chart.add(key, dict[key])

    def set_labels(self, id):
        self._chart.x_labels = id


class BoxChartBuilder(AbstractBuilder):
    def __init__(self):
        super().__init__()

    def set_title(self):
        self._chart.title = "Box chart"
        self._chart.x_title = "x title"
        self._chart.y_title = "y title"

    def set_chart_type(self):
        self._chart = pygal.Box()

    def set_data(self, dict):
        for key in dict:
            self._chart.add(key, dict[key])

    def set_labels(self, id):
        pass


class PyGal(object):
    def __init__(self, builder):
        self.builder = builder

    def construct(self, dictionary, id):
        self.builder.set_chart_type()
        self.builder.set_title()
        self.builder.set_labels(id)
        self.builder.set_data(dictionary)
        self.builder.get_result()

