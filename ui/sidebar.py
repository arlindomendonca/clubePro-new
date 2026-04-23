"""
Sidebar — usa o container nativo st.sidebar + parametro icon= do st.button,
que renderiza icones Material Symbols nativamente pelo Streamlit.

Vantagens dessa abordagem:
- Alinhamento perfeito (mesmo espacamento entre icone e texto em todos itens)
- Funciona com sidebar colapsada (Streamlit mostra so o icone)
- SVG nativo (sem risco de quebra por CSS injection)
"""
import streamlit as st
from ui.state import navigate_to
from ui.icons import icon as svg_icon


# Icones Material Symbols: https://fonts.google.com/icons
# Sintaxe do Streamlit: ":material/icon_name:"
NAV_GROUPS = [
    {
        "label": "PRINCIPAL",
        "items": [
            {"id": "dashboard", "label": "Dashboard", "icon": ":material/dashboard:"},
        ],
    },
    {
        "label": "FINANCEIRO",
        "items": [
            {"id": "titulos",     "label": "Títulos",            "icon": ":material/account_balance_wallet:"},
            {"id": "lancamentos", "label": "Lançamentos Reais",  "icon": ":material/swap_horiz:"},
            {"id": "conciliacao", "label": "Conciliação",        "icon": ":material/compare_arrows:"},
        ],
    },
    {
        "label": "CADASTROS",
        "items": [
            {"id": "favorecidos",   "label": "Favorecidos",        "icon": ":material/group:"},
            {"id": "categorias",    "label": "Categorias",         "icon": ":material/sell:"},
            {"id": "centros_custo", "label": "Centros de Custo",   "icon": ":material/business:"},
            {"id": "bancos",        "label": "Bancos",             "icon": ":material/account_balance:"},
        ],
    },
    {
        "label": "CONFIGURAÇÕES",
        "items": [
            {"id": "tenant",        "label": "Dados do Tenant",        "icon": ":material/verified_user:"},
            {"id": "organizacoes",  "label": "Gestão de Organizações", "icon": ":material/corporate_fare:"},
            {"id": "configuracoes", "label": "Configurações",          "icon": ":material/settings:"},
        ],
    },
]


def render_sidebar() -> None:
    """Renderiza o conteudo da sidebar nativa do Streamlit."""

    # ---------- Logo / Brand ----------
    logo_svg = svg_icon("sparkles", size=18, color="white")
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
                icon=item["icon"],
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
