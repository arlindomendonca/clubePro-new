# 💎 ClubePRO · Finance Suite

SaaS Financeiro multi-tenant construído em **Streamlit + Supabase**, com aesthetic _Deep Corporate_ (azul-marinho + ardósia + acentos esmeralda).

> Sistema de gestão financeira para múltiplas organizações dentro de um mesmo tenant: títulos a pagar/receber, conciliação bancária, favorecidos, plano de contas e centros de custo.

---

## 🚀 Stack

- **Streamlit** ≥ 1.32 (UI + roteamento via `session_state`)
- **Supabase** (Postgres + Auth + RLS)
- **Pandas** (transformações leves para gráficos)
- CSS injetado custom para fidelidade visual

---

## 📁 Estrutura

```
saas-financeiro/
├── app.py                      # Entry point — page config, shell, roteador
├── requirements.txt
├── .gitignore
├── .streamlit/
│   ├── config.toml             # Tema base do Streamlit
│   └── secrets.toml.example    # Template — copie para secrets.toml
├── ui/                         # Camada de apresentação
│   ├── __init__.py
│   ├── styles.py               # CSS global (Deep Corporate)
│   ├── sidebar.py              # Navegação lateral sticky
│   ├── header.py               # Tenant + Org selector + Saldo + User
│   ├── state.py                # Inicialização e helpers de session_state
│   └── helpers.py              # Formatadores (BRL, data) + badges
├── app_pages/                  # Páginas individuais (uma função render() cada)
│   ├── __init__.py
│   ├── dashboard.py
│   ├── titulos.py
│   ├── favorecidos.py
│   ├── bancos.py
│   └── placeholder.py          # Para módulos em construção
└── database/                   # Camada de dados
    ├── __init__.py
    ├── connection.py           # Cliente Supabase via st.secrets
    └── mock_data.py            # Dados de exemplo (substituir por queries)
```

> ⚠️ **Por que `app_pages/` e não `pages/`?** Streamlit reserva a pasta `pages/` para multipage automático. Como queremos navegação manual via `session_state` (preservando contexto de tenant/org), isolamos as páginas em `app_pages/`.

---

## 🛠️ Setup local

```bash
# 1. Clone e entre no diretório
git clone https://github.com/seu-usuario/fluxo-finance.git
cd fluxo-finance

# 2. Crie um venv
python -m venv .venv
source .venv/bin/activate          # Linux/Mac
# .venv\Scripts\activate           # Windows

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Configure os secrets (opcional — o app roda com mock data por padrão)
cp .streamlit/secrets.toml.example .streamlit/secrets.toml
# edite .streamlit/secrets.toml com sua URL e KEY do Supabase

# 5. Rode
streamlit run app.py
```

Acesse em [http://localhost:8501](http://localhost:8501).

---

## ☁️ Deploy no Streamlit Cloud

1. **Push para o GitHub** (o `.gitignore` já protege o `secrets.toml` real).
2. Acesse [share.streamlit.io](https://share.streamlit.io) e conecte seu repositório.
3. Em **Main file path** informe `app.py`.
4. Em **App settings → Secrets**, cole:

```toml
[supabase]
url = "https://SEU-PROJETO.supabase.co"
key = "SUA-ANON-KEY"
```

5. Deploy. O Streamlit Cloud roda `pip install -r requirements.txt` automaticamente.

---

## 🔌 Conectando ao Supabase

O placeholder está pronto em `database/connection.py`. Após configurar os secrets, basta importar:

```python
from database.connection import get_supabase

sb = get_supabase()
titulos = (
    sb.table("fin_titulo")
      .select("*, favorecido:comp_favorecido(nome_razao_social)")
      .eq("tenant_id", st.session_state.current_tenant["id"])
      .eq("organizacao_id", st.session_state.current_org_id)
      .is_("deleted_at", "null")
      .order("data_vencimento")
      .execute()
      .data
)
```

### Roteiro de migração mock → produção

1. Crie `database/queries.py` com funções como `list_titulos(tenant_id, org_id)`, `list_favorecidos(...)`, etc.
2. Em cada página, troque `from database.mock_data import TITULOS` por `from database.queries import list_titulos`.
3. Mantenha a mesma _shape_ de retorno (lista de dicts) para não tocar nas páginas.
4. Habilite Row Level Security (RLS) no Supabase com policies por `tenant_id` para isolamento multi-tenant.

---

## 🎨 Aesthetic — Deep Corporate

| Token | Valor | Uso |
|---|---|---|
| `--navy-950` | `#0a1628` | Fundo da sidebar |
| `--slate-900` | `#0f172a` | Texto principal e botões primários |
| `--slate-100` | `#f1f5f9` | Fundo do conteúdo |
| `--emerald-500` | `#10b981` | Acento financeiro / receitas / status positivos |
| `--rose-500` | `#f43f5e` | Despesas / status atrasado |
| `--sky-400` | `#38bdf8` | Status "em aberto" |
| `--amber-400` | `#fbbf24` | Status "parcial" |

Tipografia: **Inter** com `font-feature-settings: 'cv11', 'ss01', 'ss03'` e `tabular-nums` em todos os valores monetários.

---

## 🗺️ Roadmap

- [ ] Implementação real das queries em `database/queries.py`
- [ ] Auth via Supabase Auth (login/signup)
- [ ] RLS policies por `tenant_id`
- [ ] Lançamentos Reais e Conciliação Bancária
- [ ] Plano de contas (categorias e centros de custo)
- [ ] Importação de OFX para conciliação
- [ ] Relatórios DRE / Fluxo de Caixa exportáveis em PDF/XLSX

---

## 📄 Licença

MIT — fique à vontade para usar como base do seu próprio projeto.
