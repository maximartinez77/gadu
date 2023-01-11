import plotly
import numpy as np
from sympy import *
import plotly.graph_objs as go

x, e = symbols('x, e')

def plot(function, *, derivatives=1, xlower_limit=-10, xupper_limit=10, ylower_limit=0, yupper_limit=0, points=1000):
    """Función para graficar derivadas de orden superior dada una función f(x).
    
    Keyword arguments:
    ------------------
    function -- Cadena de texto que contiene f(x)
    derivatives -- Cantidad de derivadas a graficar (default 1)
    xlower_limit -- Límite inferior del eje X (default -10)    
    xupper_limit -- Límite superior del eje X (default 10)
    ylower_limit -- Límite inferior del eje Y (default 0)
    yupper_limit -- Límite superior del eje y (default 0)
    points -- Cantidad de puntos a generar en el eje X (default 1000)
    """
    function = function.subs(e, E)
    
    x_values = np.linspace(xlower_limit, xupper_limit, points)

    
    if ylower_limit == 0 and yupper_limit == 0:
        yaxis_dict = dict(autorange = True)
    else:
        yaxis_dict = dict(range = [ylower_limit, yupper_limit])

    
    layout_dict = dict(
        layout = go.Layout(
            title="Funcion y derivadas de orden superior",
            yaxis=yaxis_dict
        ))

    
   
    data = dict(data = list())
    function_dict = {}
    for n in range(derivatives + 1):
        f = lambdify(x, str(function), 'numpy')
        fx = np.full(points, f(x_values)) if isinstance(f(x_values), (int, float)) else f(x_values) 

        trace = go.Scatter(
            x=x_values,
            y=fx,
            name=f'''f{"'"*n}(x)'''
            )
        function_dict[f'''f{"'"*n}(x)'''] = latex(function).replace('\operatorname', '')

        data['data'].append(trace)
       
        function = function.diff(x)

   
    return function_dict, plotly.offline.plot({**data, **layout_dict}, output_type='div', include_plotlyjs=True, show_link=False)
