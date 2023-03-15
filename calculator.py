import streamlit as st

st.set_page_config(title='Calculadora BAGUPrint')

def BarraBN(Key='BN'):
    cantidadesBN = ['Líneas', '25%', '50%', '75%', '100%']
    valoresBN = [1800, 2800, 5900, 9000, 11700]
    st.subheader('Su plano es en blanco y negro')
    cantidadBN = st.select_slider('Seleccione la cantidad de Blanco y Negro estimada de su plano',
                                  options = cantidadesBN,
                                  key=Key)
    for i, j in zip(cantidadesBN, valoresBN):
        if cantidadBN == i:
            # st.write('Valor approximado: ', j)
            valor = j
    return valor

def BarraColor(Key='Color'):
    cantidadesColor = ['Líneas', '25%', '50%', '75%', '100%']
    valoresColor = [2000, 3200, 6500, 10000, 13000]
    st.subheader('Su plano es a color')
    cantidadColor = st.select_slider('Seleccione la cantidad de Color estimada de su plano',
                                    options = cantidadesColor,
                                    key=Key)
    for i, j in zip(cantidadesColor, valoresColor):
        if cantidadColor == i:
            # st.write('Valor approximado: ', j)
            valor = j
    return valor

st.title('Cotización Plano')

Formatos = ['A3 (420 x 297)', 'A2 (594 x 420)', 'A1 (841 x 594)', 'A0 (1189 x 841)', 'Personalizado']
valoresFormatos = [.297, .420, .594, 1.189]
st.header('Formato')
formato = st.selectbox(r'Seleccione el formato de su plano (mm $\times$ mm)', options = Formatos)
if formato == 'Personalizado':
    col1, col2 = st.columns(2)
    with col1:
        x = st.number_input('Ancho (en mm)', min_value=0)
    with col2:
        y = st.number_input('Alto (en mm)', min_value=0)
    if (x > 900) | (y > 900):
        customFormat = 0.001*max([x, y])
    elif (x <= 900) & (y <= 900):
        customFormat = 0.001*min([x, y])

st.header('Color')
planoColor = st.checkbox('Su plano es a color?')
if planoColor:
    valor_Ref = BarraColor()
else:
    valor_Ref = BarraBN()

st.header('Doblado')
doblado = st.checkbox('Su plano es doblado?')
if doblado:
    dVal = 250
else:
    dVal = 0

st.subheader('Copias')
n = st.number_input('Número de copias', min_value=1, label_visibility='collapsed')

for i, j in zip(Formatos[:-1], valoresFormatos):
    if formato == i:
        VALOR = int(j*valor_Ref*n + n*dVal)
        st.header('Valor: :green[$ %i] *' %VALOR)

if formato == 'Personalizado':
    VALOR = int(customFormat*valor_Ref*n + n*dVal)
    st.header('Valor: :green[$ %i] *' %VALOR)

st.write('* Valor sujeto a variaciones')
