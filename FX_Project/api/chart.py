from pychartjs import BaseChart, ChartType, Color                                     

class MyBarGraph(BaseChart):

    type = ChartType.Line

    class data:
        data = []
        fill = False
        tension =  0.1
        borderColor =  Color.Green
        backgroundColor = Color.Green

    class labels:
        labels = []

    class options:
        legend = None
        scales = {
            "yAxes":[
                {
                    "ticks":{
                        "callback":"<<function(value, index, values) { return value + 'hell'; }>>"
                    }
                }
            ]
        }

