"""
Pagina Titulos — Listagem de fin_titulo com summary cards e tabs.
"""
import streamlit as st

from ui.helpers import (
    format_brl, format_brl_short, format_date_br,
    page_header, status_badge,
)
from ui.icons import icon
from database.mock_data import TITULOS, FAVORECIDOS


@st.dialog("Novo Título Financeiro", width="large")
def _modal_novo_titulo(natureza: str) -> None:
    is_receita = natureza == "receita"
    box_class = "receita" if is_receita else "despesa"
    box_label = "Lançamento de Receita (Crédito)" if is_receita else "Lançamento de Despesa (Débito)"
    box_color = "#065f46" if is_receita else "#881337"
    box_icon = icon("trend_up" if is_receita else "trend_down", size=16, color=box_color, stroke=2.25)
    st.markdown(
        f'<div class="fluxo-info-box {box_class}">{box_icon}<span>{box_label}</span></div>',
        unsafe_allow_html=True,
    )

    with st.form(f"form_titulo_{natureza}", clear_on_submit=False):
        descricao = st.text_input("Descrição *", placeholder="Ex: Compra de fertilizantes - Lote 4521")

        c1, c2 = st.columns(2)
        with c1:
            favorecido = st.selectbox(
                "Favorecido *",
                options=[""] + [f["nome"] for f in FAVORECIDOS],
                format_func=lambda x: "Selecione..." if x == "" else x,
            )
        with c2:
            categoria = st.selectbox(
                "Categoria *",
                options=["", "Insumos Agrícolas", "Logística", "Pessoal", "Tecnologia", "Vendas", "Manutenção"],
                format_func=lambda x: "Selecione..." if x == "" else x,
            )

        c3, c4, c5 = st.columns(3)
        with c3:
            valor = st.number_input("Valor (R$) *", min_value=0.0, step=100.0, format="%.2f")
        with c4:
            vencimento = st.date_input("Vencimento *", value=None)
        with c5:
            competencia = st.date_input("Competência", value=None)

        c6, c7 = st.columns(2)
        with c6:
            conta = st.selectbox("Conta Bancária", options=["Banco do Brasil · CC 12345-6", "Sicoob · CC 78901-2"])
        with c7:
            meio = st.selectbox("Meio de Pagamento", options=["PIX", "Boleto", "TED", "Dinheiro"])

        observacao = st.text_area("Observações", placeholder="Notas internas...", height=80)

        st.markdown(
            '<div style="font-size:11px;color:var(--slate-500);margin-top:8px;">Campos com <span style="color:var(--rose-500);font-weight:700;">*</span> são obrigatórios.</div>',
            unsafe_allow_html=True,
        )

        c_cancel, c_submit = st.columns([1, 1])
        with c_cancel:
            cancel = st.form_submit_button("Cancelar", use_container_width=True)
        with c_submit:
            submit = st.form_submit_button("✓ Salvar Título", use_container_width=True, type="primary")

        if submit:
            missing = []
            if not descricao:  missing.append("Descrição")
            if not favorecido: missing.append("Favorecido")
            if not categoria:  missing.append("Categoria")
            if not valor:      missing.append("Valor")
            if not vencimento: missing.append("Vencimento")
            if missing:
                st.error(f"Preencha os campos obrigatórios: {', '.join(missing)}")
            else:
                st.success("Título salvo! (mock — em produção: insert no Supabase)")
                st.rerun()
        if cancel:
            st.rerun()


def render() -> None:
    col_title, col_actions = st.columns([3, 2], vertical_alignment="bottom")
    with col_title:
        page_header("Títulos Financeiros", "Contas a pagar e a receber · Gestão de obrigações")
    with col_actions:
        ca, cb = st.columns(2)
        with ca:
            if st.button("↗  Nova Receita", key="btn_new_receita", use_container_width=True, type="primary"):
                _modal_novo_titulo("receita")
        with cb:
            if st.button("↘  Nova Despesa", key="btn_new_despesa", use_container_width=True, type="primary"):
                _modal_novo_titulo("despesa")

    # ---------- Summary cards ----------
    total_rec  = sum(t["valor"] for t in TITULOS if t["natureza"] == "receita")
    total_desp = sum(t["valor"] for t in TITULOS if t["natureza"] == "despesa")
    resultado  = total_rec - total_desp
    qtd_rec    = sum(1 for t in TITULOS if t["natureza"] == "receita")
    qtd_desp   = sum(1 for t in TITULOS if t["natureza"] == "despesa")
    res_class  = "positive" if resultado >= 0 else "negative"

    icon_up   = icon("trend_up",   size=14, color="#065f46", stroke=2.25)
    icon_down = icon("trend_down", size=14, color="#881337", stroke=2.25)
    icon_zap  = icon("zap",        size=14, color="#334155", stroke=2.25)

    summary = (
        '<div class="summary-grid">'
        f'<div class="summary-card receita"><div class="summary-decoration"></div>'
        f'<div class="summary-label">{icon_up} TOTAL RECEITAS</div>'
        f'<div class="summary-value">{format_brl(total_rec)}</div>'
        f'<div class="summary-meta">{qtd_rec} títulos</div></div>'
        f'<div class="summary-card despesa"><div class="summary-decoration"></div>'
        f'<div class="summary-label">{icon_down} TOTAL DESPESAS</div>'
        f'<div class="summary-value">{format_brl(total_desp)}</div>'
        f'<div class="summary-meta">{qtd_desp} títulos</div></div>'
        f'<div class="summary-card resultado"><div class="summary-decoration"></div>'
        f'<div class="summary-label">{icon_zap} RESULTADO PROJETADO</div>'
        f'<div class="summary-value {res_class}">{format_brl(resultado)}</div>'
        f'<div class="summary-meta">Receitas − Despesas</div></div>'
        '</div>'
    )
    st.markdown(summary, unsafe_allow_html=True)

    # ---------- Filter tabs ----------
    tab_options = ["Todos", "Receitas", "Despesas"]
    tab_map = {"Todos": "todos", "Receitas": "receita", "Despesas": "despesa"}
    selected_tab = st.radio("Filtro", options=tab_options, horizontal=True,
                            label_visibility="collapsed", key="titulos_tab_selector")
    filter_value = tab_map[selected_tab]
    rows = TITULOS if filter_value == "todos" else [t for t in TITULOS if t["natureza"] == filter_value]

    # ---------- DataGrid ----------
    parts = [
        '<div class="datagrid"><table><thead><tr>'
        '<th style="width:8px;"></th>'
        '<th>Título</th><th>Favorecido</th><th>Categoria</th>'
        '<th>Vencimento</th><th style="text-align:right;">Valor</th><th>Status</th>'
        '</tr></thead><tbody>'
    ]
    for t in rows:
        is_rec = t["natureza"] == "receita"
        sign = "+" if is_rec else "−"
        color = "var(--emerald-700)" if is_rec else "var(--slate-800)"
        bar_class = "receita" if is_rec else "despesa"
        cal_icon = icon("calendar", size=13, color="#94a3b8", stroke=2)
        pago_html = (
            f'<div style="font-size:10px;color:var(--slate-500);margin-top:2px;">Pago: {format_brl(t["pago"])}</div>'
            if 0 < t["pago"] < t["valor"] else ""
        )
        parts.append(
            f'<tr>'
            f'<td><span class="nature-bar {bar_class}"></span></td>'
            f'<td><div style="font-weight:700;color:var(--slate-800);font-variant-numeric:tabular-nums;">{t["numero"]}</div>'
            f'<div style="font-size:12px;color:var(--slate-500);">{t["descricao"]}</div></td>'
            f'<td>{t["favorecido"]}</td>'
            f'<td><span class="tag">{t["categoria"]}</span></td>'
            f'<td><div style="display:inline-flex;align-items:center;gap:6px;font-variant-numeric:tabular-nums;">'
            f'{cal_icon}{format_date_br(t["vencimento"])}</div></td>'
            f'<td style="text-align:right;">'
            f'<div style="font-weight:700;color:{color};font-variant-numeric:tabular-nums;">{sign} {format_brl_short(t["valor"])}</div>'
            f'{pago_html}</td>'
            f'<td>{status_badge(t["status"])}</td>'
            f'</tr>'
        )
    parts.append(
        f'</tbody></table>'
        f'<div class="datagrid-footer">'
        f'<span>Mostrando <strong>{len(rows)}</strong> de <strong>{len(TITULOS)}</strong> títulos</span>'
        f'<span style="color:var(--slate-400);">Página 1 de 1</span>'
        f'</div></div>'
    )
    st.markdown("".join(parts), unsafe_allow_html=True)
