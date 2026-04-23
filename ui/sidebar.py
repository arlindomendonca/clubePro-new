"""
Sidebar — usa o container nativo st.sidebar do Streamlit.
Estrategia simplificada: prefixos Unicode no label do botao
(em vez de SVG sobreposto, que e fragil).
"""
import streamlit as st
from ui.state import navigate_to
from ui.icons import icon


# Caracteres Unicode geometricos limpos (renderizam consistente em qualquer plataforma)
NAV_GROUPS = [
    {
        "label": "PRINCIPAL",
        "items": [
            {"id": "dashboard", "label": "▦   Dashboard"},
        ],
    },
    {
        "label": "FINANCEIRO",
        "items": [
            {"id": "titulos",     "label": "◈   Títulos"},
            {"id": "lancamentos", "label": "⇆   Lançamentos Reais"},
            {"id": "conciliacao", "label": "⇌   Conciliação"},
        ],
    },
    {
        "label": "CADASTROS",
        "items": [
            {"id": "favorecidos",   "label": "◉   Favorecidos"},
            {"id": "categorias",    "label": "◆   Categorias"},
            {"id": "centros_custo", "label": "▣   Centros de Custo"},
            {"id": "bancos",        "label": "▤   Bancos"},
        ],
    },
    {
        "label": "CONFIGURAÇÕES",
        "items": [
            {"id": "tenant",        "label": "◐   Dados do Tenant"},
            {"id": "organizacoes",  "label": "▥   Gestão de Organizações"},
            {"id": "configuracoes", "label": "⚙   Configurações"},
        ],
    },
]


def render_sidebar() -> None:
    """Renderiza o conteudo da sidebar nativa do Streamlit."""

    # ---------- Logo / Brand ----------
    logo_svg = icon("sparkles", size=18, color="white")
    st.markdown(
        f'<div class="fluxo-brand">'
        f'<div class="fluxo-brand-mark">{logo_svg}</div>'
        f'<div class="fluxo-brand-text">'
        f'<div class="fluxo-brand-name">Fluxo<span>.</span></div>'
        f'<div class="fluxo-brand-tag">FINANCE SUITE</div>'
        f'</div></div>'
        f'<div class="fluxo-brand-divider"></div>',
        unsafe_allow_html=True,
    )

    # ---------- Nav groups ----------
    for group in NAV_GROUPS:
        st.markdown(
            f'<div class="fluxo-nav-label">{group["label"]}</div>',
            unsafe_allow_html=True,
        )

        for item in group["items"]:
            is_active = st.session_state.active_page == item["id"]
            st.button(
                item["label"],
                key=f"nav_{item['id']}",
                on_click=navigate_to,
                args=(item["id"],),
                use_container_width=True,
                type="primary" if is_active else "secondary",
            )

        st.markdown(
            '<div style="height:14px;"></div>',
            unsafe_allow_html=True,
        )
