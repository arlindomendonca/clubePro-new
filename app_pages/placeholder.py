"""
Placeholder elegante para modulos em construcao.
"""
import streamlit as st
from ui.helpers import page_header


def render(title: str, subtitle: str, icon: str = "📋") -> None:
    page_header(title, subtitle)

    st.markdown(
        f'<div class="card" style="padding:48px;text-align:center;">'
        f'<div style="max-width:420px;margin:0 auto;">'
        f'<div style="width:64px;height:64px;margin:0 auto 16px;border-radius:16px;background:linear-gradient(135deg,var(--slate-100),var(--slate-50));border:1px solid var(--slate-200);display:flex;align-items:center;justify-content:center;font-size:28px;">{icon}</div>'
        f'<h3 style="margin:0 0 4px;font-size:16px;font-weight:700;color:var(--slate-800);">Módulo em construção</h3>'
        f'<p style="margin:0 0 20px;font-size:14px;color:var(--slate-500);">Esta seção seguirá o mesmo padrão visual de listagem (DataGrid, filtros, modais e integração com Supabase).</p>'
        f'</div></div>',
        unsafe_allow_html=True,
    )

    if st.button("+  Criar primeiro registro", key=f"placeholder_btn_{title}", type="primary"):
        st.toast("Em desenvolvimento — será implementado quando conectado ao Supabase.")
