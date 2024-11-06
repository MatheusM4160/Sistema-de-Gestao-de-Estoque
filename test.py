import streamlit as st

# Título da aplicação
st.title("Simulação de Dialog no Streamlit")

# Botão para abrir o "Dialog"
if st.button("Abrir Janela de Aviso"):
    with st.expander("Aviso Importante!", expanded=True):
        st.write("Esta é uma janela de aviso, similar a um dialog.")
        st.write("Aqui você pode exibir informações importantes ou solicitar uma confirmação.")
        
        # Botões de confirmação ou cancelamento
        if st.button("Confirmar"):
            st.success("Ação confirmada!")
            st.rerun()
        if st.button("Cancelar"):
            st.info("Ação cancelada.")
            st.rerun()