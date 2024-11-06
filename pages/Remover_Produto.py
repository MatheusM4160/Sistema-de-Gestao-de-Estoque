import sqlite3
import streamlit as st

def SearchProduct(name, supplier):
    with sqlite3.connect('register.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM estoque WHERE Name = ? AND Supplier = ?', (name, supplier))
        Product = cursor.fetchone()
        return Product
    
def DeleteProduct(id):
    with sqlite3.connect('register.db') as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM estoque WHERE id = ?', (id,))
        conn.commit()
        st.success('Produto deletado com sucesso!')

st.title('Remover Produto')
NameProduct = st.text_input(label='Produto', placeholder='Digite o nome do produto que deseja buscar:')
NameSupplier = st.text_input(label='Fornecedor', placeholder='Digite o nome do fornecedor:')

if st.button('Pesquisar Produto'):
    Product = SearchProduct(name=NameProduct.capitalize().strip(), supplier=NameSupplier.capitalize().strip())
    if Product:
        ProductId = Product[0]
        DeleteProduct(id=ProductId)
    else:
        st.error('Produto não encontrado')


