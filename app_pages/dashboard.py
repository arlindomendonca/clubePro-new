"""
Pagina Dashboard — Visao geral financeira da organizacao ativa.
HTML gerado em linhas COMPACTAS para evitar interpretacao como code-block
pelo parser de Markdown do Streamlit.
"""
import streamlit as st
import pandas as pd

from ui.helpers import format_brl, format_date_br, page_header
from ui.icons import icon
from ui.state import get_current_org
from database.mock_data import TITULOS


def render() -> None:
    org = get_current_org()
    page_header("Visão Geral", f"Acompanhamento financeiro · {org['nome']}")

    # ---------- KPI cards ----------
    kpis = [
        {"label": "Receitas (Mês)", "value": 487320.00, "change": "+12,4%",     "trend": "up",   "color": "emerald", "icon": "arrow_up_right"},
        {"label": "Despesas (Mês)", "value": 218990.50, "change": "+3,2%",      "trend": "down", "color": "rose",    "icon": "arrow_down_right"},
        {"label": "A Receber",      "value": 145200.00, "change": "8 títulos",  "trend": "flat", "color": "sky",     "icon": "dot"},
        {"label": "A Pagar",        "value":  92450.30, "change": "12 títulos", "trend": "flat", "color": "amber",   "icon": "dot"},
    ]
    icon_color_map = {"emerald": "#047857", "rose": "#be123c", "sky": "#0369a1", "amber": "#b45309"}

    parts = ['<div class="kpi-grid">']
    for k in kpis:
        change_class = "positive" if k["trend"] == "up" else "negative" if k["trend"] == "down" else "neutral"
        svg = icon(k["icon"], size=16, color=icon_color_map[k["color"]], stroke=2.25)
        parts.append(
            f'<div class="kpi-card">'
            f'<div class="kpi-header">'
            f'<span class="kpi-label">{k["label"]}</span>'
            f'<div class="kpi-icon {k["color"]}">{svg}</div>'
            f'</div>'
            f'<div class="kpi-value">{format_brl(k["value"])}</div>'
            f'<div class="kpi-change {change_class}">{k["change"]}</div>'
            f'</div>'
        )
    parts.append('</div>')
    st.markdown("".join(parts), unsafe_allow_html=True)

    # ---------- Bottom panels ----------
    col_chart, col_list = st.columns([2, 1], gap="medium")

    with col_chart:
        st.markdown(
            '<h3 style="margin:0;font-size:16px;font-weight:700;color:var(--slate-900);">Fluxo de Caixa</h3>'
            '<p style="margin:4px 0 12px;font-size:12px;color:var(--slate-500);">Últimos 30 dias · Consolidado</p>',
            unsafe_allow_html=True,
        )
        chart_data = pd.DataFrame({
            "Dia":      list(range(1, 16)),
            "Entradas": [40, 65, 45, 80, 55, 70, 60, 85, 50, 75, 90, 65, 80, 95, 70],
            "Saídas":   [16, 26, 18, 32, 22, 28, 24, 34, 20, 30, 36, 26, 32, 38, 28],
        }).set_index("Dia")
        st.bar_chart(chart_data, height=240, color=["#10b981", "#fb7185"])

    with col_list:
        st.markdown(
            '<h3 style="margin:0 0 4px;font-size:16px;font-weight:700;color:var(--slate-900);">Próximos Vencimentos</h3>'
            '<p style="margin:0 0 12px;font-size:12px;color:var(--slate-500);">Próximos 7 dias</p>',
            unsafe_allow_html=True,
        )

        proximos = [t for t in TITULOS if t["status"] in ("aberto", "atrasado")][:4]
        list_parts = ['<div style="display:flex;flex-direction:column;gap:8px;">']
        for t in proximos:
            sign = "+" if t["natureza"] == "receita" else "−"
            color = "var(--emerald-700)" if t["natureza"] == "receita" else "var(--slate-700)"
            bar_color = "var(--emerald-400)" if t["natureza"] == "receita" else "var(--rose-400)"
            valor_str = format_brl(t["valor"]).replace("R$ ", "")
            list_parts.append(
                f'<div style="display:flex;align-items:center;gap:12px;padding:10px;border-radius:8px;background:white;border:1px solid var(--slate-200);">'
                f'<div style="width:4px;height:36px;border-radius:2px;background:{bar_color};flex-shrink:0;"></div>'
                f'<div style="flex:1;min-width:0;">'
                f'<div style="font-size:13px;font-weight:600;color:var(--slate-800);white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">{t["descricao"]}</div>'
                f'<div style="font-size:11px;color:var(--slate-500);">{format_date_br(t["vencimento"])}</div>'
                f'</div>'
                f'<div style="font-size:13px;font-weight:700;color:{color};font-variant-numeric:tabular-nums;">{sign} {valor_str}</div>'
                f'</div>'
            )
        list_parts.append('</div>')
        st.markdown("".join(list_parts), unsafe_allow_html=True)
