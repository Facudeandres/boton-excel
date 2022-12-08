import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets

# Carga el archivo Excel en un DataFrame de Pandas
df = pd.read_excel("nombre_del_archivo.xlsx")

# Crea una aplicación de PyQt5
app = QtWidgets.QApplication([])

# Crea una tabla
table = QtWidgets.QTableWidget()

# Establece el número de filas y columnas en la tabla
table.setRowCount(len(df))
table.setColumnCount(len(df.columns))

# Establece las etiquetas de las columnas en la tabla
table.setHorizontalHeaderLabels(df.columns)

# Agrega los datos del DataFrame a la tabla
for i in range(len(df)):
    for j in range(len(df.columns)):
        item = QtWidgets.QTableWidgetItem(str(df.iloc[i, j]))
        table.setItem(i, j, item)

# Muestra la tabla
table.show()

# Ejecuta la aplicación de PyQt5
app.exec_()
