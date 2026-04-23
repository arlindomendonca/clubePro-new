"""
Pagina Bancos & Contas — Listagem de fin_banco / fin_conta_bancaria.
"""
import streamlit as st

from ui.helpers import format_brl, page_header, ativo_badge
from ui.icons import icon
from database.mock_data import BANCOS


def render() -> None:
    col_title, col_action = st.columns([4, 1], vertical_alignment="bottom")
    with col_title:
        page_header("Bancos & Contas", "Instituições financeiras e contas bancárias do tenant")
    with col_action:
        st.button("+  Nova Conta", key="btn_new_banco", use_container_width=True, type="primary")

    # ---------- Resumo ----------
    total_saldo = sum(b["saldo"] for b in BANCOS if b["ativo"])
    qtd_ativas = sum(1 for b in BANCOS if b["ativo"])

    icon_wallet = icon("wallet", size=16, color="#047857", stroke=2.25)
    icon_bank   = icon("bank",   size=16, color="#0369a1", stroke=2.25)
    icon_clock  = icon("clock",  size=16, color="#b45309", stroke=2.25)

    kpis_html = (
        '<div class="kpi-grid">'
        f'<div class="kpi-card"><div class="kpi-header">'
        f'<span class="kpi-label">Saldo Total</span>'
        f'<div class="kpi-icon emerald">{icon_wallet}</div></div>'
        f'<div class="kpi-value">{format_brl(total_saldo)}</div>'
        f'<div class="kpi-change neutral">{qtd_ativas} contas ativas</div></div>'
        f'<div class="kpi-card"><div class="kpi-header">'
        f'<span class="kpi-label">Contas Ativas</span>'
        f'<div class="kpi-icon sky">{icon_bank}</div></div>'
        f'<div class="kpi-value">{qtd_ativas}</div>'
        f'<div class="kpi-change neutral">de {len(BANCOS)} cadastradas</div></div>'
        f'<div class="kpi-card"><div class="kpi-header">'
        f'<span class="kpi-label">Conciliação Pendente</span>'
        f'<div class="kpi-icon amber">{icon_clock}</div></div>'
        f'<div class="kpi-value">14</div>'
        f'<div class="kpi-change neutral">extratos a processar</div></div>'
        '</div>'
    )
    st.markdown(kpis_html, unsafe_allow_html=True)

    # ---------- Listagem ----------
    parts = [
        '<div class="datagrid"><table><thead><tr>'
        '<th>Banco</th><th>Agência / Conta</th><th>Tipo</th>'
        '<th style="text-align:right;">Saldo Atual</th><th>Status</th>'
        '</tr></thead><tbody>'
    ]
    for b in BANCOS:
        saldo_color = "var(--emerald-700)" if b["saldo"] >= 0 else "var(--rose-700)"
        parts.append(
            f'<tr>'
            f'<td><div class="row-flex">'
            f'<div class="avatar-initials" style="background:linear-gradient(135deg,var(--slate-100),var(--slate-200));color:var(--slate-700);">{b["codigo"]}</div>'
            f'<div><div class="row-name">{b["nome"]}</div>'
            f'<div class="row-sub">Código FEBRABAN {b["codigo"]}</div></div>'
            f'</div></td>'
            f'<td><div style="font-variant-numeric:tabular-nums;color:var(--slate-700);">Ag. {b["agencia"]}</div>'
            f'<div style="font-size:12px;color:var(--slate-500);font-variant-numeric:tabular-nums;">CC {b["conta"]}</div></td>'
            f'<td><span class="tag">{b["tipo"]}</span></td>'
            f'<td style="text-align:right;font-weight:700;color:{saldo_color};font-variant-numeric:tabular-nums;">{format_brl(b["saldo"])}</td>'
            f'<td>{ativo_badge(b["ativo"])}</td>'
            f'</tr>'
        )
    parts.append(
        f'</tbody></table>'
        f'<div class="datagrid-footer">'
        f'<span>Mostrando <strong>{len(BANCOS)}</strong> contas bancárias</span>'
        f'<span style="color:var(--slate-400);">Última sincronização: hoje, 14:32</span>'
        f'</div></div>'
    )
    st.markdown("".join(parts), unsafe_allow_html=True)
