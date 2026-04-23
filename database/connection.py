"""
Conexão com Supabase.

Este módulo encapsula a inicialização do client Supabase usando credenciais
servidas via `st.secrets`, tornando seguro o deploy em Streamlit Cloud
(as credenciais ficam fora do repositório, em Settings → Secrets).

----------------------------------------------------------------------
USO EM PRODUÇÃO:
----------------------------------------------------------------------
# Em qualquer página/módulo:
from database.connection import get_supabase

sb = get_supabase()
res = sb.table("fin_titulo").select("*").eq("tenant_id", tenant_id).execute()

----------------------------------------------------------------------
CONFIGURAÇÃO DE SECRETS:
----------------------------------------------------------------------
Local  → crie  .streamlit/secrets.toml  (NÃO commitar):

    [supabase]
    url = "https://xxxx.supabase.co"
    key = "eyJhbGciOi..."          # anon key OU service_role (cuidado!)

Cloud  → Streamlit Cloud → App Settings → Secrets → cole o mesmo TOML.
----------------------------------------------------------------------
"""
from __future__ import annotations

import streamlit as st


# ---------------------------------------------------------------------------
# Cache do client — uma única instância por sessão de app
# ---------------------------------------------------------------------------
@st.cache_resource(show_spinner=False)
def get_supabase():
    """
    Retorna um client Supabase autenticado.
    Usa cache_resource para evitar reabrir conexão a cada rerun.

    Returns:
        Client: instância de supabase.Client

    Raises:
        RuntimeError: se as credenciais não estiverem configuradas
        ImportError:  se o pacote supabase-py não estiver instalado
    """
    try:
        from supabase import create_client, Client  # noqa: F401
    except ImportError as e:
        raise ImportError(
            "Pacote 'supabase' não instalado. Adicione ao requirements.txt:\n"
            "    supabase>=2.0.0"
        ) from e

    creds = _read_credentials()
    return create_client(creds["url"], creds["key"])


def _read_credentials() -> dict:
    """
    Lê SUPABASE_URL e SUPABASE_KEY de st.secrets.

    Aceita dois formatos no secrets.toml:

        # Formato preferido (namespaced):
        [supabase]
        url = "..."
        key = "..."

        # Formato flat (fallback):
        SUPABASE_URL = "..."
        SUPABASE_KEY = "..."
    """
    if "supabase" in st.secrets:
        block = st.secrets["supabase"]
        url = block.get("url")
        key = block.get("key")
    else:
        url = st.secrets.get("SUPABASE_URL")
        key = st.secrets.get("SUPABASE_KEY")

    if not url or not key:
        raise RuntimeError(
            "Credenciais do Supabase não configuradas.\n"
            "Crie .streamlit/secrets.toml ou configure em Streamlit Cloud:\n\n"
            "    [supabase]\n"
            '    url = "https://xxx.supabase.co"\n'
            '    key = "sua-anon-key"\n'
        )

    return {"url": url, "key": key}


# ---------------------------------------------------------------------------
# Helper de healthcheck — útil para tela de configurações
# ---------------------------------------------------------------------------
def is_connected() -> bool:
    """Verifica se a conexão com o Supabase está operacional."""
    try:
        sb = get_supabase()
        # Ping leve: lista até 1 row de uma tabela do schema
        sb.table("sys_tenant").select("id").limit(1).execute()
        return True
    except Exception:
        return False


# ---------------------------------------------------------------------------
# Convenções de query (templates para implementação futura)
# ---------------------------------------------------------------------------
"""
Padrão recomendado para queries multi-tenant:

def list_titulos(tenant_id: str, organizacao_id: str | None = None):
    sb = get_supabase()
    q = (sb.table("fin_titulo")
            .select("*, favorecido:comp_favorecido(nome_razao_social)")
            .eq("tenant_id", tenant_id)
            .is_("deleted_at", "null")
            .order("data_vencimento", desc=False))
    if organizacao_id:
        q = q.eq("organizacao_id", organizacao_id)
    return q.execute().data

IMPORTANTE: como o schema usa RLS (Row Level Security) baseado em tenant_id,
considere autenticar o client com o JWT do usuário (auth.uid()) ao invés da
anon key, para que as policies sejam aplicadas automaticamente.
"""
