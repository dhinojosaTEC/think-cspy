x = [1, 3, -2]
y = [5, -2, -1]
m = [6, 5, 10]

#Funcion para poder calcular el centro de masas puntuales distribuidas

def centroMasa(x_list, y_list, m_list):
    y_numerator=0
    x_numerator=0
    denominator=0
    for x_num, y_num, m_num in zip(x_list, y_list, m_list):
        x_numerator += x_num*m_num
        y_numerator += y_num*m_num
        denominator += m_num
    centro_x = x_numerator/denominator
    centro_y = y_numerator/denominator
    return print("Centro de Masa del Sistema: [",centro_x,",",centro_y,"]",
                "\nMomento de sistema respecto al eje 'y':", x_numerator,
                "\nMomento de sistema respecto al eje 'x':", y_numerator)

centroMasa(x, y, m)