"""
Header — Tenant badge, Organizacao (selectbox), Saldo Consolidado, Usuario.
HTML em linha unica para garantir renderizacao correta.
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
    saldo_total = sum(o["saldo"] for o in ORGANIZACOES)

    c_tenant, c_org, c_saldo, c_user = st.columns(
        [1.4, 2.2, 1.6, 1.4], gap="medium", vertical_alignment="center"
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
        org_options = {o["id"]: f"{o['nome']}  ·  {o['cidade']}" for o in ORGANIZACOES}
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

    # ---------- Saldo Consolidado ----------
    with c_saldo:
        saldo_icon = icon("wallet", size=14, color="#047857", stroke=2.25)
        st.markdown(
            f'<div class="fluxo-saldo">'
            f'<div class="fluxo-saldo-icon">{saldo_icon}</div>'
            f'<div class="fluxo-saldo-text">'
            f'<div class="fluxo-saldo-label">SALDO CONSOLIDADO</div>'
            f'<div class="fluxo-saldo-value">{_format_brl(saldo_total)}</div>'
            f'</div></div>',
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
