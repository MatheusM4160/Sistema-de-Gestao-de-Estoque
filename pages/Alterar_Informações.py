import streamlit as st
import sqlite3

def SearchProduct(name, supplier):
    with sqlite3.connect('register.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM estoque WHERE Name = ? AND Supplier = ?', (name, supplier))
        Product = cursor.fetchone()
        return Product
    
def UpdateProduct(id, Name, Description, Value, Amount, Supplier, Telephone):
    with sqlite3.connect('register.db') as conn:
        cursor = conn.cursor()

        cursor.execute('''UPDATE estoque SET Name = ?, Description = ?, Value = ?,
                       Amount = ?, Supplier = ?, Telephone = ? WHERE id = ?''',
                       (Name, Description, Value, Amount, Supplier, Telephone, id))
        conn.commit()

st.title('Alterar Informações')
NameProduct = st.text_input(label='Produto', placeholder='Digite o nome do produto que deseja buscar:')
NameSupplier = st.text_input(label='Fornecedor', placeholder='Digite o nome do fornecedor:')

if st.button('Buscar Produto'):
    Product = SearchProduct(name=NameProduct.capitalize(), supplier=NameSupplier.capitalize())
    if Product:
        st.success('Produto encontrado!')

        ProductId = Product[0]
        CurrentName = st.text_input('Nome', Product[1])
        CurrentDescription = st.text_input('Descrição', Product[2])
        CurrentValue = st.text_input('Valor', value=Product[3])
        CurrentAmount = st.text_input('Quantidade', value=Product[4])
        CurrentSupplier = st.text_input('Fornecedor', Product[5])
        CurrentTelephone = st.text_input('Telefone', Product[6])

        if st.button('Atualizar Produto'):
            UpdateProduct(id=ProductId, Name=CurrentName, Description=CurrentDescription, Value=CurrentValue,
                          Amount=CurrentAmount, Supplier=CurrentSupplier, Telephone=CurrentTelephone)
            st.success('Produto atualizado com sucesso!')
    else:
        st.error('Produto não encontrado')