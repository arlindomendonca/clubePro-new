"""
Inicialização e gestão do st.session_state.
Centraliza chaves de estado para evitar drift entre módulos.
"""
import streamlit as st
from database.mock_data import ORGANIZACOES


def init_session_state() -> None:
    """Inicializa o estado da sessão com defaults seguros."""
    defaults = {
        "active_page": "dashboard",
        "sidebar_collapsed": False,
        "current_org_id": ORGANIZACOES[0]["id"],
        "current_tenant": {
            "id": "tenant-001",
            "nome": "Cooperativa Agroverde",
            "exibicao": "Agroverde Holdings",
            "logo": "AG",
        },
        "current_user": {
            "id": "usr-001",
            "nome": "Carlos Eduardo",
            "iniciais": "CE",
            "papel": "Admin",
            "online": True,
        },
        "show_modal": None,           # 'favorecido' | 'titulo_receita' | 'titulo_despesa' | None
        "search_query": "",
        "titulos_filter": "todos",    # 'todos' | 'receita' | 'despesa'
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def navigate_to(page_id: str) -> None:
    """Atalho para mudar de página preservando demais estados."""
    st.session_state.active_page = page_id
    st.session_state.show_modal = None  # fecha modal ao navegar


def set_organization(org_id: str) -> None:
    """Troca a organização ativa preservando tenant e usuário."""
    st.session_state.current_org_id = org_id


def get_current_org() -> dict:
    """Retorna o dict da organização ativa."""
    return next(
        (o for o in ORGANIZACOES if o["id"] == st.session_state.current_org_id),
        ORGANIZACOES[0],
    )


def toggle_sidebar() -> None:
    st.session_state.sidebar_collapsed = not st.session_state.sidebar_collapsed
