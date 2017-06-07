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


# class ChartFlyweight(metaclass=ABCMeta):
#     @abstractmethod
#     def __init__(self, chart, title, x_title, y_title, id, dictionary):
#         self.chart = chart
#         self.title = title
#         self.x_title = x_title
#         self.y_title = y_title
#         self.id = id
#         self.dictionary = dictionary
#         self.chart_type = None
#
#     def set_data(self, data):
#         self.chart_type = self.chart
#         self.chart_type.title = self.title
#         self.chart_type.x_title = self.x_title
#         self.chart_type.y_title = self.y_title
#         for key in self.dictionary:
#             self.chart_type.add(key, self.dictionary[key])
#         self.chart_type.x_labels = self.id
#
#     def render(self):
#         return self.chart_type.render_in_browser
#
#
# class bar_chart(ChartFlyweight):
#     def __init__(self):
#         super().__init__()
#
#
# class pie_chart(ChartFlyweight):
#     def __init__(self):
#         super().__init__()
#
#
# class FlyweightFactory(object):
#     def __init__(self):
#         self.pool = {}
#
#     def get_flyweight(self, chart):
#         if chart not in self.pool:
#             self.pool[chart] = eval(chart + "()")
#         return self.pool[chart]

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
        return self._chart.render_in_browser()


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


class Director(object):
    def __init__(self, builder):
        self.builder = builder

    def construct(self, dictionary, id):
        self.builder.set_chart_type()
        self.builder.set_title()
        self.builder.set_labels(id)
        self.builder.set_data(dictionary)
        return self.builder.get_result()

