"""
Header — Tenant badge, Organizacao, Busca global, Notificacoes, Usuario.
Layout replicando o design React de referencia.
"""
import streamlit as st

from database.mock_data import ORGANIZACOES
from ui.state import get_current_org, set_organization
from ui.icons import icon


def _format_brl(value: float) -> str:
    formatted = f"{value:,.2f}"
    return "R$ " + formatted.replace(",", "X").replace(".", ",").replace("X", ".")


def render_header() -> None:
    tenant = st.session_state.current_tenant
    user = st.session_state.current_user
    current_org = get_current_org()

    # Colunas: [Tenant] [Org] [Busca] [Notif] [User]
    c_tenant, c_org, c_search, c_notif, c_user = st.columns(
        [1.6, 2.0, 3.4, 0.4, 1.6],
        gap="small",
        vertical_alignment="center",
    )

    # ---------- Tenant ----------
    with c_tenant:
        st.markdown(
            f'<div class="fluxo-tenant-badge">'
            f'<div class="fluxo-tenant-mark">{tenant["logo"]}</div>'
            f'<div class="fluxo-tenant-text">'
            f'<div class="fluxo-tenant-label">TENANT</div>'
            f'<div class="fluxo-tenant-name">{tenant["exibicao"]}</div>'
            f'</div></div>',
            unsafe_allow_html=True,
        )

    # ---------- Organizacao ----------
    with c_org:
        org_options = {o["id"]: o["nome"] for o in ORGANIZACOES}
        selected = st.selectbox(
            "Organização",
            options=list(org_options.keys()),
            format_func=lambda x: org_options[x],
            index=list(org_options.keys()).index(current_org["id"]),
            label_visibility="collapsed",
            key="org_selector",
        )
        if selected != st.session_state.current_org_id:
            set_organization(selected)
            st.rerun()

    # ---------- Busca Global ----------
    with c_search:
        st.text_input(
            "Busca",
            placeholder="🔍  Buscar títulos, favorecidos, lançamentos...",
            key="header_search",
            label_visibility="collapsed",
        )

    # ---------- Notificacoes ----------
    with c_notif:
        bell_svg = icon("bell", size=18, color="#475569", stroke=1.75)
        st.markdown(
            f'<div class="fluxo-notif-wrap">'
            f'<button class="fluxo-notif-btn" title="Notificações">'
            f'{bell_svg}'
            f'<span class="fluxo-notif-dot"></span>'
            f'</button>'
            f'</div>',
            unsafe_allow_html=True,
        )

    # ---------- User ----------
    with c_user:
        st.markdown(
            f'<div class="fluxo-user">'
            f'<div class="fluxo-user-text">'
            f'<div class="fluxo-user-name">{user["nome"]}</div>'
            f'<div class="fluxo-user-status"><span class="fluxo-user-dot"></span>Online · {user["papel"]}</div>'
            f'</div>'
            f'<div class="fluxo-user-avatar">{user["iniciais"]}</div>'
            f'</div>',
            unsafe_allow_html=True,
        )

    st.divider()
