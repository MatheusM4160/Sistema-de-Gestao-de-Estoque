import streamlit as st
import sqlite3


def Cadastro(Name, Description, Value, Amount, Supplier, Telephone):
    with sqlite3.connect('register.db') as conn:
        cursor = conn.cursor()

        if Description == '':
            Description = 'Sem Descrição'

        if len(Telephone) == 11:
            try:
                int(Telephone)
            except:
                st.error('Número Inválido!')
            else:
                Telephone = '0' + Telephone
                Telephone = f'{Telephone[:3]} {Telephone[3:8]}-{Telephone[8:]}'

        try:
            cursor.execute("""INSERT INTO estoque (Name, Description, Value, Amount, Supplier, Telephone)
                           VALUES (?, ?, ?, ?, ?, ?)""", (Name, Description, Value, Amount, Supplier, Telephone))
            conn.commit()
            st.success('Cadastrado com Sucesso!')
        except Exception as e:
            print('Error:', e)
        
st.title('Cadastro de Produtos')
FieldName = st.text_input(label='Nome')
FieldDescription = st.text_input(label='Descrição')
FieldValue = st.text_input(label='Valor')
FieldAmount = st.text_input(label='Quantidade')
FieldSupplier = st.text_input(label='Fornecedor')
FieldTelephone = st.text_input(label='Telefone')

st.button('Cadastrar', on_click=lambda:Cadastro(Name=FieldName.capitalize().strip(), Description=FieldDescription.capitalize().strip(),
                                                Value=FieldValue.replace(',', '.').strip(), Amount=FieldAmount.strip(), Supplier=FieldSupplier.capitalize().strip(),
                                                Telephone=FieldTelephone.replace('(', '').replace(')', '').replace('-', '').replace('_', '').strip())
                                                if len(FieldTelephone) == 11 or 12
                                                else st.error('Número Inválido!'))