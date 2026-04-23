"""
Fluxo Finance Suite — SaaS Financeiro Multi-Tenant
Entry point principal. Configura página, injeta CSS, monta shell (sidebar + header)
e despacha para a página ativa via st.session_state.
"""
# ---------------------------------------------------------------------------
# Path bootstrap — garante que os pacotes locais (ui/, app_pages/, database/)
# sejam encontrados independentemente do CWD com que o Streamlit é invocado.
# ---------------------------------------------------------------------------
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))

import streamlit as st

from ui.styles import inject_global_css
from ui.sidebar import render_sidebar
from ui.header import render_header
from ui.state import init_session_state

from app_pages import dashboard, titulos, favorecidos, bancos, placeholder


# ---------------------------------------------------------------------------
# Page configuration — sempre primeira chamada Streamlit
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="Fluxo · Finance Suite",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": None,
        "Report a bug": None,
        "About": "Fluxo Finance Suite — SaaS Financeiro Multi-Tenant",
    },
)

# ---------------------------------------------------------------------------
# Inicialização de estado e estilos
# ---------------------------------------------------------------------------
init_session_state()
inject_global_css()


# ---------------------------------------------------------------------------
# Roteamento de páginas
# ---------------------------------------------------------------------------
PAGE_REGISTRY = {
    "dashboard":     dashboard.render,
    "titulos":       titulos.render,
    "favorecidos":   favorecidos.render,
    "bancos":        bancos.render,
    "lancamentos":   lambda: placeholder.render(
        "Lançamentos Reais", "Pagamentos e recebimentos efetivados", "💸"
    ),
    "conciliacao":   lambda: placeholder.render(
        "Conciliação Bancária", "Reconcilie extratos com lançamentos do sistema", "🔄"
    ),
    "categorias":    lambda: placeholder.render(
        "Categorias", "Plano de contas e classificações financeiras", "🏷️"
    ),
    "centros_custo": lambda: placeholder.render(
        "Centros de Custo", "Estruturas para rateio e análise gerencial", "🏢"
    ),
    "tenant":        lambda: placeholder.render(
        "Dados do Tenant", "Informações da conta master · Plano e assinatura", "🛡️"
    ),
    "organizacoes":  lambda: placeholder.render(
        "Gestão de Organizações", "Filiais, unidades e estruturas do tenant", "🏛️"
    ),
    "configuracoes": lambda: placeholder.render(
        "Configurações", "Preferências do sistema", "⚙️"
    ),
}


# ---------------------------------------------------------------------------
# Layout: sidebar nativa + main com header sticky
# ---------------------------------------------------------------------------
def main() -> None:
    # Sidebar nativa do Streamlit — robusta no Cloud
    with st.sidebar:
        render_sidebar()

    # Header + conteúdo na área principal
    render_header()

    active_page = st.session_state.active_page
    page_fn = PAGE_REGISTRY.get(active_page, PAGE_REGISTRY["dashboard"])
    page_fn()


if __name__ == "__main__":
    main()

