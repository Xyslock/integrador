import streamlit as st

st.title("Calculadora")
st.write("---")
num1 = st.number_input(label="Introduce el primer número")
num2 = st.number_input(label="Introduce el segundo número")
st.write("Operación")
operation = st.radio("Selecciona una operación para realizar:",
                    ("Sumar", "Restar", "Multiplicar", "Dividir"))
ans = 0
def calculate():
    if operation == "Sumar":
        ans = num1 + num2
    elif operation == "Restar":
        ans = num1 - num2
    elif operation == "Multiplicar":
        ans = num1 * num2
    elif operation == "Dividir" and num2 != 0:
        ans = num1 / num2
    else:
        st.warning("Error de división por cero. Por favor, introduce un número distinto de cero.")
        ans = "No definido"
    st.success(f"Resultado = {ans}")
if st.button("Calcular resultado"):
    calculate()
