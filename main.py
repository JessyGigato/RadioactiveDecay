import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from metodos_numericos import runge_kutta_method,euler_method,values_exact_sol

st.sidebar.title("Seminario de Matemática Numérica")
st.sidebar.subheader("Metodos numéricos para resolver EDOs")
st.sidebar.subheader("Desintegración radiactiva")
method = st.sidebar.multiselect('Escoja método(s):', ('Euler', 'Runge-Kutta'))
graphic_method = st.sidebar.selectbox("Mostrar gráfico de los metodos",('Si','No'))
aprox_values = st.sidebar.selectbox("Mostrar valores aproximados",('Si','No'))

st.write("Desintegracion radiactiva")
st.write("Formula que representa el proceso de desintegración")
st.write("y'(t)=-λy(t)")
st.write("Solución exacta : y(t)=y_0 e^(-λt)")
st.write("Constante de descomposición : λ = ln2/t_(1⁄2)")
y0 = st.text_area("Introduzca el valor inicial y_0 ",value = 500)
tm = st.text_area("Introduzca el tiempo medio de descomposición t_(1⁄2) para calcular la constante de descomposición ",value = 5600)
h = st.text_area("Introduzca el tamaño de paso h",value = 0.1)
interval = st.text_area("Introduzca el intervalo en que quiere calcular las aproximaciones(separados por espacio el inicio y fin,mayores que 0)",value = '0 10')
btn_calculate = st.button("Calcular")

if btn_calculate:
    interval = interval.split()
    a = int(interval[0])
    b = int(interval[1])
    y0 = int(y0)
    tm = int(tm)
    h = float(h)
    x_euler = []
    y_euler = []
    x_rk = []
    y_rk = []
    for m in method:
        if m =='Euler':
            x_euler,y_euler = euler_method(0,y0,a,b,h,tm)
            if graphic_method == 'Si':
                plt.plot(x_euler,y_euler,color = 'r',linewidth=6,label = 'Euler')
        if m == 'Runge-Kutta':
            x_rk,y_rk = runge_kutta_method(0,y0,a,b,h,tm)
            if graphic_method == 'Si':
                plt.plot(x_rk,y_rk,color = 'y',linewidth= 4,label = 'Runge-Kutta')
    x,y = values_exact_sol(y0,a,b,h,tm)
    plt.plot(x,y,color = 'black',label = 'Solución exacta')
    plt.hold(True)
    plt.legend()
    st.pyplot()

    if aprox_values == 'Si' and len(method) > 0:
        c = len(x)
        i = 0
        table = []
        cols =['t','Real value']
        while i < c:
            row = [x[i],y[i]]
            if 'Euler' in method:
                row.append(y_euler[i])
            if 'Runge-Kutta' in method:
                row.append(y_rk[i])
            table.append(row)
            i+=1
        if 'Euler' in method:
            cols.append('Euler')
        if 'Runge-Kutta' in method:
            cols.append('Runge-Kutta')
        df = pd.DataFrame(table,columns = cols)
        st.table(df)

