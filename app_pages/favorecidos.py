"""
Pagina Favorecidos — Listagem de comp_favorecido com busca e modal.
"""
import streamlit as st

from ui.helpers import page_header, ativo_badge, initials
from database.mock_data import FAVORECIDOS


@st.dialog("Novo Favorecido", width="large")
def _modal_novo_favorecido() -> None:
    st.caption("Cadastre um novo cliente, fornecedor ou contraparte financeira.")

    with st.form("form_favorecido", clear_on_submit=False):
        c1, c2 = st.columns(2)
        with c1:
            tipo = st.selectbox("Tipo de Pessoa *", options=["Pessoa Jurídica", "Pessoa Física"])
        with c2:
            categoria = st.selectbox("Categoria", options=["Cliente", "Fornecedor", "Funcionário", "Outro"])

        nome = st.text_input("Nome / Razão Social *", placeholder="Ex: Indústria Brasileira S.A.")

        c3, c4 = st.columns(2)
        with c3:
            doc = st.text_input("CPF / CNPJ *", placeholder="00.000.000/0000-00")
        with c4:
            email = st.text_input("E-mail", placeholder="contato@empresa.com")

        c5, c6, c7 = st.columns([1, 1, 1])
        with c5:
            cep = st.text_input("CEP", placeholder="00000-000")
        with c6:
            telefone = st.text_input("Telefone", placeholder="(00) 00000-0000")
        with c7:
            ativo = st.toggle("Ativo", value=True)

        endereco = st.text_input("Endereço", placeholder="Rua, número, complemento, bairro, cidade")
        observacao = st.text_area("Observações", placeholder="Notas internas...", height=80)

        st.markdown(
            '<div style="font-size:11px;color:var(--slate-500);margin-top:8px;">Campos com <span style="color:var(--rose-500);font-weight:700;">*</span> são obrigatórios.</div>',
            unsafe_allow_html=True,
        )

        c_cancel, c_submit = st.columns([1, 1])
        with c_cancel:
            cancel = st.form_submit_button("Cancelar", use_container_width=True)
        with c_submit:
            submit = st.form_submit_button("✓ Salvar Favorecido", use_container_width=True, type="primary")

        if submit:
            missing = []
            if not nome: missing.append("Nome / Razão Social")
            if not doc:  missing.append("CPF / CNPJ")
            if missing:
                st.error(f"Preencha os campos obrigatórios: {', '.join(missing)}")
            else:
                st.success("Favorecido salvo! (mock — em produção: insert no Supabase)")
                st.rerun()
        if cancel:
            st.rerun()


def render() -> None:
    col_title, col_action = st.columns([4, 1], vertical_alignment="bottom")
    with col_title:
        page_header("Favorecidos", "Clientes, fornecedores e demais contrapartes financeiras")
    with col_action:
        if st.button("+  Novo Favorecido", key="btn_new_favorecido", use_container_width=True, type="primary"):
            _modal_novo_favorecido()

    # ---------- Toolbar ----------
    c_search, c_filter, c_export = st.columns([5, 1, 1])
    with c_search:
        search = st.text_input(
            "Buscar",
            placeholder="🔍  Buscar por nome, CPF/CNPJ ou e-mail...",
            key="favorecidos_search",
            label_visibility="collapsed",
        )
    with c_filter:
        st.button("⚙ Filtros", use_container_width=True, key="filter_btn")
    with c_export:
        st.button("⬇ Exportar", use_container_width=True, key="export_btn")

    if search:
        s = search.lower()
        rows = [f for f in FAVORECIDOS if s in f["nome"].lower() or s in f["doc"].lower() or s in f["email"].lower()]
    else:
        rows = FAVORECIDOS

    # ---------- DataGrid ----------
    parts = [
        '<div class="datagrid"><table><thead><tr>'
        '<th>Favorecido</th><th>Documento</th><th>Categoria</th>'
        '<th>Cidade</th><th>Status</th>'
        '</tr></thead><tbody>'
    ]
    for f in rows:
        avatar_class = "pj" if f["tipo"] == "pessoa_juridica" else "pf"
        tipo_label = "PJ" if f["tipo"] == "pessoa_juridica" else "PF"
        parts.append(
            f'<tr>'
            f'<td><div class="row-flex">'
            f'<div class="avatar-initials {avatar_class}">{initials(f["nome"])}</div>'
            f'<div><div class="row-name">{f["nome"]}</div>'
            f'<div class="row-sub">{f["email"]}</div></div>'
            f'</div></td>'
            f'<td><div style="font-variant-numeric:tabular-nums;">{f["doc"]}</div>'
            f'<div style="font-size:10px;font-weight:700;color:var(--slate-400);letter-spacing:0.05em;">{tipo_label}</div></td>'
            f'<td><span class="tag">{f["categoria"]}</span></td>'
            f'<td>{f["cidade"]}</td>'
            f'<td>{ativo_badge(f["ativo"])}</td>'
            f'</tr>'
        )
    parts.append(
        f'</tbody></table>'
        f'<div class="datagrid-footer">'
        f'<span>Mostrando <strong>{len(rows)}</strong> de <strong>{len(FAVORECIDOS)}</strong> favorecidos</span>'
        f'<span style="color:var(--slate-400);">Página 1 de 1</span>'
        f'</div></div>'
    )
    st.markdown("".join(parts), unsafe_allow_html=True)
