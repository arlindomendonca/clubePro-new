"""
Stylesheet global — ClubePRO Finance Suite.

Estrategia visual (Opcao A — Fundo Claro Premium):
  - Conteudo: branco puro / cinza-gelo (#F8FAFC) para legibilidade de dados densos
  - Sidebar: navy escuro (premium contrast)
  - Tipografia: tons escuros (#0F172A / #1E293B) para titulos e dados
  - Acoes positivas: esmeralda (#10B981)
  - Acoes neutras: cinza ardosia
  - Acoes destrutivas: vermelho (reservado)
  - Header: cinza-gelo com borda inferior delicada para delimitacao
"""
import streamlit as st


GLOBAL_CSS = """
<style>
/* ============================================================
   1. FONTS & CSS VARIABLES
   ============================================================ */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

:root {
    /* Sidebar — Deep navy */
    --navy-950: #0a1628;
    --navy-900: #0d1b30;
    --navy-800: #112240;

    /* Slate (cinzas ardosia — escuros para texto) */
    --slate-50:  #f8fafc;
    --slate-100: #f1f5f9;
    --slate-200: #e2e8f0;
    --slate-300: #cbd5e1;
    --slate-400: #94a3b8;
    --slate-500: #64748b;
    --slate-600: #475569;
    --slate-700: #334155;
    --slate-800: #1e293b;
    --slate-900: #0f172a;

    /* Acentos */
    --emerald-300: #6ee7b7;
    --emerald-400: #34d399;
    --emerald-500: #10b981;
    --emerald-600: #059669;
    --emerald-700: #047857;
    --emerald-800: #065f46;

    --rose-400: #fb7185;
    --rose-500: #f43f5e;
    --rose-600: #e11d48;
    --rose-700: #be123c;

    --sky-400:  #38bdf8;
    --amber-400:#fbbf24;

    /* Sombras refinadas */
    --shadow-sm: 0 1px 2px 0 rgba(15, 23, 42, 0.05);
    --shadow-md: 0 4px 12px -2px rgba(15, 23, 42, 0.08);
    --shadow-lg: 0 10px 30px -8px rgba(15, 23, 42, 0.12);

    /* Backgrounds principais */
    --bg-app:     #ffffff;
    --bg-canvas:  #f8fafc;
    --bg-card:    #ffffff;
    --bg-header:  #f8fafc;
    --bg-input:   #f1f5f9;

    /* Texto */
    --text-primary:   #0f172a;
    --text-secondary: #475569;
    --text-muted:     #64748b;
    --text-label:     #64748b;
}

/* ============================================================
   2. GLOBAL — fontes, scrollbar, esconde elementos nativos
   ============================================================ */
html, body, [class*="css"], .stApp {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    -webkit-font-smoothing: antialiased;
    color: var(--text-primary);
}

/* Header e menu nativos */
header[data-testid="stHeader"] {
    background: transparent !important;
    min-height: 0 !important;
    z-index: 999;
}
[data-testid="stToolbar"] { display: none !important; }
[data-testid="stDecoration"] { display: none !important; }
#MainMenu { display: none !important; }
footer { display: none !important; }
.stDeployButton { display: none !important; }

/* Botao de toggle quando sidebar colapsada — visivel e estilizado */
[data-testid="stSidebarCollapsedControl"],
[data-testid="collapsedControl"] {
    display: flex !important;
    visibility: visible !important;
    opacity: 1 !important;
    position: fixed !important;
    top: 14px !important;
    left: 14px !important;
    z-index: 99999 !important;
    background: var(--navy-900) !important;
    color: white !important;
    border-radius: 10px !important;
    padding: 6px !important;
    box-shadow: 0 4px 14px rgba(15, 23, 42, 0.25) !important;
    transition: all 200ms ease-in-out !important;
}
[data-testid="stSidebarCollapsedControl"]:hover,
[data-testid="collapsedControl"]:hover {
    background: var(--navy-800) !important;
    transform: translateY(-1px);
}
[data-testid="stSidebarCollapsedControl"] svg,
[data-testid="collapsedControl"] svg {
    color: white !important;
    fill: white !important;
}

/* Scrollbar */
::-webkit-scrollbar { width: 8px; height: 8px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: rgba(148, 163, 184, 0.3); border-radius: 8px; }
::-webkit-scrollbar-thumb:hover { background: rgba(148, 163, 184, 0.5); }

.stApp { background: var(--bg-canvas); }
.tabular-nums, .money { font-variant-numeric: tabular-nums; }

/* ============================================================
   3. SIDEBAR — Deep Navy com brand "ClubePRO"
   ============================================================ */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, var(--navy-950) 0%, var(--navy-900) 100%) !important;
    border-right: 1px solid rgba(30, 41, 59, 0.6) !important;
    width: 260px !important;
    min-width: 260px !important;
    transition: width 300ms ease-in-out, min-width 300ms ease-in-out !important;
}
section[data-testid="stSidebar"] > div {
    padding-top: 1rem !important;
    padding-left: 0.75rem !important;
    padding-right: 0.75rem !important;
    transition: padding 300ms ease-in-out !important;
}

/* Botao nativo de COLAPSAR — REPOSICIONADO dentro do brand container.
   Streamlit renderiza esse botao no header da sidebar; usamos position: absolute
   para encaixa-lo ao lado direito do logo ClubePRO. */
section[data-testid="stSidebar"] [data-testid="stSidebarCollapseButton"] {
    position: absolute !important;
    top: 22px !important;
    right: 12px !important;
    z-index: 10 !important;
}
section[data-testid="stSidebar"] [data-testid="stSidebarCollapseButton"] button {
    color: var(--slate-400) !important;
    background: rgba(255, 255, 255, 0.04) !important;
    border: 1px solid rgba(148, 163, 184, 0.15) !important;
    border-radius: 8px !important;
    padding: 4px !important;
    width: 28px !important;
    height: 28px !important;
    transition: all 200ms ease-in-out !important;
}
section[data-testid="stSidebar"] [data-testid="stSidebarCollapseButton"] button:hover {
    color: white !important;
    background: rgba(255, 255, 255, 0.08) !important;
    border-color: rgba(148, 163, 184, 0.35) !important;
}
section[data-testid="stSidebar"] [data-testid="stSidebarCollapseButton"] svg {
    color: currentColor !important;
    fill: currentColor !important;
    width: 16px !important;
    height: 16px !important;
}

/* Brand block — ClubePRO */
.fluxo-brand {
    display: flex; align-items: center; gap: 12px;
    padding: 4px 8px 16px;
    position: relative;
    padding-right: 48px; /* espaco para o botao de colapsar */
}
.fluxo-brand-mark {
    width: 38px; height: 38px;
    border-radius: 12px;
    background: linear-gradient(135deg, var(--emerald-400), var(--emerald-600));
    display: flex; align-items: center; justify-content: center;
    color: white; font-weight: 700;
    box-shadow: 0 4px 14px rgba(16, 185, 129, 0.35),
                inset 0 1px 0 rgba(255, 255, 255, 0.2);
    flex-shrink: 0;
}
.fluxo-brand-mark svg { width: 18px; height: 18px; }
.fluxo-brand-text { display: flex; flex-direction: column; line-height: 1.1; min-width: 0; }
.fluxo-brand-name {
    color: white; font-size: 17px; font-weight: 700; letter-spacing: -0.025em;
}
.fluxo-brand-name span { color: var(--emerald-400); font-weight: 800; }
.fluxo-brand-tag {
    color: var(--slate-500); font-size: 9.5px; font-weight: 600;
    letter-spacing: 0.18em; margin-top: 4px;
}
.fluxo-brand-divider {
    height: 1px; background: rgba(30, 41, 59, 0.6);
    margin: 0 -0.75rem 16px;
}

/* ==== SIDEBAR COLAPSADA ==== */
section[data-testid="stSidebar"][aria-expanded="false"] {
    width: 68px !important;
    min-width: 68px !important;
    transform: translateX(0) !important;
    visibility: visible !important;
    margin-left: 0 !important;
}
section[data-testid="stSidebar"][aria-expanded="false"] > div {
    padding-left: 0.5rem !important;
    padding-right: 0.5rem !important;
}
section[data-testid="stSidebar"][aria-expanded="false"] .fluxo-brand-text,
section[data-testid="stSidebar"][aria-expanded="false"] .fluxo-nav-label {
    display: none !important;
}
section[data-testid="stSidebar"][aria-expanded="false"] .fluxo-brand {
    justify-content: center;
    padding: 4px 0 16px;
}
section[data-testid="stSidebar"][aria-expanded="false"] [data-testid="stSidebarCollapseButton"] {
    position: relative !important;
    top: auto !important;
    right: auto !important;
    margin: 0 auto 8px !important;
    display: flex !important;
    justify-content: center !important;
}
section[data-testid="stSidebar"][aria-expanded="false"] .stButton > button > div[data-testid="stMarkdownContainer"],
section[data-testid="stSidebar"][aria-expanded="false"] .stButton > button p {
    display: none !important;
}
section[data-testid="stSidebar"][aria-expanded="false"] .stButton > button {
    padding: 14px 0 !important;
    justify-content: center !important;
    gap: 0 !important;
    min-width: 0 !important;
    min-height: 48px !important;
    margin-bottom: 6px !important;
}
section[data-testid="stSidebar"][aria-expanded="false"] .stButton > button > div {
    justify-content: center !important;
}
section[data-testid="stSidebar"][aria-expanded="false"] .stButton > button span[data-testid*="Icon"],
section[data-testid="stSidebar"][aria-expanded="false"] .stButton > button [data-testid="stIconMaterial"] {
    font-size: 22px !important;
    margin: 0 !important;
}
section[data-testid="stSidebar"][aria-expanded="false"] .stButton > button[kind="primary"] {
    border-left-width: 3px !important;
    padding: 14px 0 !important;
}
section[data-testid="stSidebar"][aria-expanded="false"] .fluxo-brand-divider {
    margin-bottom: 8px;
}

/* Nav group labels */
.fluxo-nav-label {
    padding: 0 12px 8px;
    font-size: 10px; font-weight: 700; color: var(--slate-500);
    letter-spacing: 0.18em;
}

/* Botoes dentro da sidebar */
section[data-testid="stSidebar"] .stButton > button {
    width: 100% !important;
    background: transparent !important;
    border: none !important;
    border-left: 3px solid transparent !important;
    color: var(--slate-300) !important;
    padding: 10px 12px !important;
    border-radius: 8px !important;
    font-size: 13.5px !important;
    font-weight: 500 !important;
    text-align: left !important;
    justify-content: flex-start !important;
    align-items: center !important;
    transition: all 200ms ease-in-out !important;
    margin-bottom: 2px !important;
    box-shadow: none !important;
    min-height: 40px !important;
    height: auto !important;
    line-height: 1.3 !important;
    gap: 12px !important;
    display: flex !important;
}
section[data-testid="stSidebar"] .stButton > button > div {
    justify-content: flex-start !important;
    width: auto !important;
    flex: 0 1 auto !important;
}
section[data-testid="stSidebar"] .stButton > button > div[data-testid="stMarkdownContainer"] {
    text-align: left !important;
    width: auto !important;
    flex: 1 1 auto !important;
}
section[data-testid="stSidebar"] .stButton > button > div[data-testid="stMarkdownContainer"] > p {
    text-align: left !important;
    margin: 0 !important;
    white-space: nowrap !important;
}
section[data-testid="stSidebar"] .stButton > button span[data-testid*="Icon"],
section[data-testid="stSidebar"] .stButton > button [data-testid="stIconMaterial"] {
    color: var(--slate-400) !important;
    font-size: 20px !important;
    flex-shrink: 0 !important;
    transition: color 200ms ease-in-out !important;
}
section[data-testid="stSidebar"] .stButton > button:hover {
    background: rgba(255, 255, 255, 0.04) !important;
    color: white !important;
    border-left-color: transparent !important;
    transform: none !important;
}
section[data-testid="stSidebar"] .stButton > button:hover span[data-testid*="Icon"],
section[data-testid="stSidebar"] .stButton > button:hover [data-testid="stIconMaterial"] {
    color: var(--slate-200) !important;
}
section[data-testid="stSidebar"] .stButton > button:focus,
section[data-testid="stSidebar"] .stButton > button:focus-visible {
    box-shadow: none !important;
    outline: none !important;
}
section[data-testid="stSidebar"] .stButton > button:active {
    background: rgba(255, 255, 255, 0.06) !important;
    transform: none !important;
}
section[data-testid="stSidebar"] .stButton > button[kind="primary"] {
    background: linear-gradient(90deg, rgba(16, 185, 129, 0.18), rgba(16, 185, 129, 0.04)) !important;
    color: white !important;
    border-left: 3px solid var(--emerald-400) !important;
    font-weight: 600 !important;
    box-shadow: -3px 0 12px -2px rgba(52, 211, 153, 0.4) !important;
}
section[data-testid="stSidebar"] .stButton > button[kind="primary"] span[data-testid*="Icon"],
section[data-testid="stSidebar"] .stButton > button[kind="primary"] [data-testid="stIconMaterial"] {
    color: var(--emerald-400) !important;
}
section[data-testid="stSidebar"] .stButton > button[kind="primary"]:hover {
    background: linear-gradient(90deg, rgba(16, 185, 129, 0.25), rgba(16, 185, 129, 0.06)) !important;
    border-left-color: var(--emerald-400) !important;
}
section[data-testid="stSidebar"] hr { display: none !important; }

/* ============================================================
   4. MAIN CONTENT AREA — fundo claro
   ============================================================ */
[data-testid="stAppViewContainer"] > .main {
    background: var(--bg-canvas);
}
.main .block-container {
    padding-top: 1.5rem !important;
    padding-bottom: 3rem !important;
    padding-left: 2rem !important;
    padding-right: 2rem !important;
    max-width: 1600px !important;
}

/* ============================================================
   5. HEADER — Tenant + Org + Busca + Notif + User
   ============================================================ */
/* Container do bloco do header — fundo cinza-gelo + borda inferior */
[data-testid="stHorizontalBlock"]:has(.fluxo-tenant-badge),
[data-testid="stHorizontalBlock"]:has(.fluxo-user) {
    align-items: center !important;
    min-height: 68px !important;
    background: var(--bg-header);
    border-bottom: 1px solid var(--slate-200);
    border-radius: 0;
    padding: 12px 20px !important;
    margin-bottom: 24px !important;
    margin-left: -2rem !important;
    margin-right: -2rem !important;
    margin-top: -1.5rem !important;
}

.fluxo-tenant-badge,
.fluxo-user,
.fluxo-notif-wrap {
    display: flex;
    align-items: center;
    min-height: 44px;
}

.fluxo-tenant-badge { gap: 10px; }
.fluxo-tenant-mark {
    width: 36px; height: 36px;
    border-radius: 8px;
    background: linear-gradient(135deg, var(--slate-700), var(--slate-900));
    display: flex; align-items: center; justify-content: center;
    color: white; font-weight: 700; font-size: 12px;
    box-shadow: var(--shadow-sm);
    flex-shrink: 0;
}
.fluxo-tenant-text { display: flex; flex-direction: column; line-height: 1.2; min-width: 0; }
.fluxo-tenant-label {
    font-size: 9px; font-weight: 700; color: var(--text-label);
    letter-spacing: 0.15em;
}
.fluxo-tenant-name {
    font-size: 13px; font-weight: 700; color: var(--text-primary);
    overflow: hidden; text-overflow: ellipsis; white-space: nowrap;
}

/* Selectbox do header — visual destacado */
.main [data-testid="stSelectbox"] {
    min-height: 44px;
    display: flex;
    align-items: center;
}
.main [data-testid="stSelectbox"] > div { width: 100%; }
.main div[data-baseweb="select"] > div {
    background: white !important;
    min-height: 44px !important;
    font-size: 13px !important;
    border-color: var(--slate-200) !important;
}

/* Input de busca — fundo um pouco mais escuro que o header */
.main [data-testid="stTextInput"] {
    min-height: 44px;
    display: flex;
    align-items: center;
}
.main [data-testid="stTextInput"] > div { width: 100%; }
.main [data-testid="stTextInput"] input {
    height: 44px !important;
    background: var(--bg-input) !important;
    border-color: transparent !important;
    color: var(--text-primary) !important;
}
.main [data-testid="stTextInput"] input:focus {
    background: white !important;
    border-color: var(--emerald-400) !important;
}

/* Notificacoes */
.fluxo-notif-wrap {
    display: flex;
    justify-content: center;
    align-items: center;
}
.fluxo-notif-btn {
    position: relative;
    width: 38px; height: 38px;
    border-radius: 10px;
    background: white;
    border: 1px solid var(--slate-200);
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 200ms ease-in-out;
    color: var(--text-secondary);
}
.fluxo-notif-btn:hover {
    background: var(--slate-50);
    border-color: var(--slate-300);
    color: var(--text-primary);
}
.fluxo-notif-dot {
    position: absolute;
    top: 7px; right: 7px;
    width: 8px; height: 8px;
    border-radius: 50%;
    background: var(--rose-500);
    border: 2px solid white;
    box-shadow: 0 0 0 1px rgba(244, 63, 94, 0.3);
}

/* User */
.fluxo-user {
    gap: 10px;
    justify-content: flex-end;
}
.fluxo-user-text { display: flex; flex-direction: column; align-items: flex-end; line-height: 1.2; }
.fluxo-user-name {
    font-size: 13px; font-weight: 700; color: var(--text-primary);
}
.fluxo-user-status {
    font-size: 10.5px; font-weight: 500; color: var(--text-muted);
    display: flex; align-items: center; gap: 5px; margin-top: 3px;
}
.fluxo-user-dot {
    width: 6px; height: 6px; border-radius: 50%;
    background: var(--emerald-500);
    box-shadow: 0 0 6px rgba(16, 185, 129, 0.7);
    display: inline-block;
}
.fluxo-user-avatar {
    width: 36px; height: 36px;
    border-radius: 50%;
    background: linear-gradient(135deg, var(--slate-700), var(--slate-900));
    display: flex; align-items: center; justify-content: center;
    color: white; font-weight: 600; font-size: 12px;
    box-shadow: 0 0 0 2px white, var(--shadow-md);
    flex-shrink: 0;
}

/* Esconde divider apos o header */
.main hr {
    display: none !important;
}

/* ============================================================
   6. PAGE HEADER (titulo das paginas)
   ============================================================ */
.page-header { margin-bottom: 24px; }
.page-title {
    font-size: 26px; font-weight: 800;
    color: var(--text-primary);
    letter-spacing: -0.025em; margin: 0;
    line-height: 1.2;
}
.page-subtitle {
    font-size: 14px; color: var(--text-secondary); margin-top: 4px;
}

/* ============================================================
   7. CARDS / KPI
   ============================================================ */
.card {
    background: var(--bg-card);
    border: 1px solid var(--slate-200);
    border-radius: 12px;
    padding: 20px;
    transition: all 250ms ease-in-out;
}
.card:hover {
    border-color: var(--slate-300);
    box-shadow: var(--shadow-md);
}

.kpi-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 16px;
    margin-bottom: 24px;
}
.kpi-card {
    background: var(--bg-card);
    border: 1px solid var(--slate-200);
    border-radius: 12px;
    padding: 20px;
    transition: all 250ms ease-in-out;
}
.kpi-card:hover { border-color: var(--slate-300); box-shadow: var(--shadow-md); }
.kpi-header {
    display: flex; justify-content: space-between; align-items: flex-start;
    margin-bottom: 12px;
}
.kpi-label {
    font-size: 11px; font-weight: 700; color: var(--text-label);
    letter-spacing: 0.05em; text-transform: uppercase;
}
.kpi-value {
    font-size: 24px; font-weight: 700; color: var(--text-primary);
    letter-spacing: -0.02em; line-height: 1.2;
    font-variant-numeric: tabular-nums;
    margin-bottom: 4px;
}
.kpi-change { font-size: 12px; font-weight: 500; }
.kpi-change.positive { color: var(--emerald-700); }
.kpi-change.negative { color: var(--rose-700); }
.kpi-change.neutral  { color: var(--text-secondary); }
.kpi-icon {
    width: 32px; height: 32px;
    border-radius: 8px;
    display: flex; align-items: center; justify-content: center;
    flex-shrink: 0;
}
.kpi-icon svg { display: block; }
.kpi-icon.emerald { background: rgba(16, 185, 129, 0.1); color: var(--emerald-700); }
.kpi-icon.rose    { background: rgba(244, 63, 94, 0.1);  color: var(--rose-700); }
.kpi-icon.sky     { background: rgba(56, 189, 248, 0.1); color: #0369a1; }
.kpi-icon.amber   { background: rgba(251, 191, 36, 0.1); color: #b45309; }

/* Summary cards (Receitas/Despesas) */
.summary-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 16px;
    margin-bottom: 24px;
}
.summary-card {
    border-radius: 12px;
    padding: 20px;
    border: 1px solid;
    position: relative;
    overflow: hidden;
}
.summary-decoration {
    position: absolute;
    top: -20px; right: -20px;
    width: 96px; height: 96px;
    border-radius: 50%;
    filter: blur(28px);
    opacity: 0.5;
    pointer-events: none;
}
.summary-card.receita {
    background: linear-gradient(135deg, #ecfdf5, rgba(236, 253, 245, 0.4));
    border-color: rgba(16, 185, 129, 0.25);
}
.summary-card.receita .summary-decoration { background: var(--emerald-400); }
.summary-card.despesa {
    background: linear-gradient(135deg, #fff1f2, rgba(255, 241, 242, 0.4));
    border-color: rgba(244, 63, 94, 0.25);
}
.summary-card.despesa .summary-decoration { background: var(--rose-400); }
.summary-card.resultado {
    background: linear-gradient(135deg, var(--slate-50), white);
    border-color: var(--slate-200);
}
.summary-card.resultado .summary-decoration { background: var(--slate-400); }
.summary-label {
    display: flex; align-items: center; gap: 8px;
    font-size: 11px; font-weight: 700; text-transform: uppercase;
    letter-spacing: 0.05em; margin-bottom: 8px;
    position: relative;
}
.summary-card.receita .summary-label { color: var(--emerald-800); }
.summary-card.despesa .summary-label { color: #881337; }
.summary-card.resultado .summary-label { color: var(--text-secondary); }
.summary-value {
    font-size: 24px; font-weight: 700; line-height: 1.2;
    letter-spacing: -0.02em; font-variant-numeric: tabular-nums;
    position: relative;
}
.summary-card.receita .summary-value { color: #064e3b; }
.summary-card.despesa .summary-value { color: #881337; }
.summary-card.resultado .summary-value.positive { color: var(--emerald-800); }
.summary-card.resultado .summary-value.negative { color: var(--rose-700); }
.summary-meta { font-size: 12px; opacity: 0.75; margin-top: 4px; position: relative; }

/* ============================================================
   8. DATAGRID — refinado para dados densos
   ============================================================ */
.datagrid {
    background: var(--bg-card);
    border: 1px solid var(--slate-200);
    border-radius: 12px;
    overflow: hidden;
    margin-top: 16px;
    box-shadow: var(--shadow-sm);
}
.datagrid table {
    width: 100%; border-collapse: collapse;
}
.datagrid thead {
    background: var(--slate-50);
    border-bottom: 1px solid var(--slate-200);
}
.datagrid th {
    padding: 14px 20px;
    text-align: left;
    font-size: 11px; font-weight: 700;
    color: var(--text-label);
    text-transform: uppercase; letter-spacing: 0.06em;
}
.datagrid td {
    padding: 16px 20px;
    border-bottom: 1px solid var(--slate-100);
    font-size: 14px; color: var(--text-secondary);
    vertical-align: middle;
}
.datagrid tbody tr {
    transition: background 200ms ease-in-out;
}
.datagrid tbody tr:hover {
    background: var(--slate-50);
}
.datagrid tbody tr:last-child td { border-bottom: none; }

.datagrid-footer {
    padding: 12px 20px;
    border-top: 1px solid var(--slate-200);
    background: var(--slate-50);
    display: flex; justify-content: space-between; align-items: center;
    font-size: 12px; color: var(--text-secondary);
}
.datagrid-footer strong {
    color: var(--text-primary);
    font-weight: 700;
}

.avatar-initials {
    width: 36px; height: 36px;
    border-radius: 8px;
    display: inline-flex; align-items: center; justify-content: center;
    font-size: 12px; font-weight: 600;
    flex-shrink: 0;
}
.avatar-initials.pj { background: #e0f2fe; color: #0369a1; }
.avatar-initials.pf { background: #ede9fe; color: #6d28d9; }

.row-flex { display: flex; align-items: center; gap: 12px; }
.row-name {
    font-weight: 600;
    color: var(--text-primary);
    font-size: 14px;
}
.row-sub  {
    font-size: 12px;
    color: var(--text-muted);
    margin-top: 2px;
}

.nature-bar {
    display: inline-block;
    width: 4px; height: 36px;
    border-radius: 2px;
    vertical-align: middle;
}
.nature-bar.receita {
    background: var(--emerald-400);
    box-shadow: 0 0 6px rgba(52, 211, 153, 0.4);
}
.nature-bar.despesa {
    background: var(--rose-400);
    box-shadow: 0 0 6px rgba(251, 113, 133, 0.4);
}

/* ============================================================
   9. BADGES (Status) — fundo suave + borda
   ============================================================ */
.badge {
    display: inline-flex; align-items: center; gap: 6px;
    padding: 4px 10px;
    border-radius: 6px;
    font-size: 12px; font-weight: 600;
    border: 1px solid;
    line-height: 1.2;
}
.badge-dot { width: 6px; height: 6px; border-radius: 50%; flex-shrink: 0; }

.badge.aberto    { background: rgba(56, 189, 248, 0.1); color: #0369a1; border-color: rgba(56, 189, 248, 0.3); }
.badge.aberto    .badge-dot { background: var(--sky-400); }
.badge.pago      { background: rgba(16, 185, 129, 0.1); color: var(--emerald-800); border-color: rgba(16, 185, 129, 0.3); }
.badge.pago      .badge-dot { background: var(--emerald-400); }
.badge.atrasado  { background: rgba(244, 63, 94, 0.1);  color: #991b1b; border-color: rgba(244, 63, 94, 0.3); }
.badge.atrasado  .badge-dot { background: var(--rose-400); }
.badge.parcial   { background: rgba(251, 191, 36, 0.1); color: #92400e; border-color: rgba(251, 191, 36, 0.3); }
.badge.parcial   .badge-dot { background: var(--amber-400); }
.badge.cancelado { background: var(--slate-100); color: var(--text-muted); border-color: var(--slate-200); }
.badge.cancelado .badge-dot { background: var(--slate-400); }
.badge.ativo     { background: rgba(16, 185, 129, 0.1); color: var(--emerald-800); border-color: rgba(16, 185, 129, 0.3); }
.badge.ativo     .badge-dot { background: var(--emerald-500); }
.badge.inativo   { background: var(--slate-100); color: var(--text-muted); border-color: var(--slate-200); }
.badge.inativo   .badge-dot { background: var(--slate-400); }

.tag {
    display: inline-block;
    padding: 3px 9px;
    border-radius: 6px;
    background: var(--slate-100);
    color: var(--text-secondary);
    font-size: 12px; font-weight: 500;
}

/* ============================================================
   10. STREAMLIT BUTTONS (area principal)
   Filosofia: PRIMARY = positivo (esmeralda); SECONDARY = neutro (slate);
   Vermelho fica RESERVADO para acoes destrutivas (no mapeado aqui).
   ============================================================ */
.main .stButton > button {
    border-radius: 8px;
    font-weight: 600;
    font-size: 14px;
    transition: all 200ms ease-in-out;
    border: 1px solid var(--slate-200);
    box-shadow: var(--shadow-sm);
    padding: 8px 16px;
    background: white;
    color: var(--text-secondary);
}
.main .stButton > button:hover {
    box-shadow: var(--shadow-md);
    transform: translateY(-1px);
    border-color: var(--slate-300);
    color: var(--text-primary);
}

/* PRIMARY — Acao positiva (Salvar, Nova Receita, Criar) → Esmeralda */
.main .stButton > button[kind="primary"] {
    background: var(--emerald-600) !important;
    color: white !important;
    border: 1px solid var(--emerald-600) !important;
}
.main .stButton > button[kind="primary"]:hover {
    background: var(--emerald-700) !important;
    border-color: var(--emerald-700) !important;
    box-shadow: 0 8px 20px -6px rgba(5, 150, 105, 0.35) !important;
}

/* SECONDARY — Acao neutra (Nova Despesa, Cancelar, Filtros) → Slate */
.main .stButton > button[kind="secondary"] {
    background: var(--slate-800) !important;
    color: white !important;
    border: 1px solid var(--slate-800) !important;
}
.main .stButton > button[kind="secondary"]:hover {
    background: var(--slate-900) !important;
    border-color: var(--slate-900) !important;
    box-shadow: 0 8px 20px -6px rgba(15, 23, 42, 0.3) !important;
}

/* ============================================================
   11. INPUTS
   ============================================================ */
div[data-baseweb="input"] input,
div[data-baseweb="textarea"] textarea,
div[data-baseweb="select"] > div {
    border-radius: 8px !important;
    border-color: var(--slate-200) !important;
    transition: all 200ms ease-in-out !important;
}
.main div[data-baseweb="input"]:focus-within input,
.main div[data-baseweb="textarea"]:focus-within textarea {
    border-color: var(--emerald-400) !important;
    box-shadow: 0 0 0 4px rgba(16, 185, 129, 0.1) !important;
}
.main div[data-testid="stWidgetLabel"] > label {
    font-size: 12px !important;
    font-weight: 600 !important;
    color: var(--text-secondary) !important;
}

/* ============================================================
   12. RADIO HORIZONTAL (tabs custom)
   ============================================================ */
div[data-testid="stRadio"] > div[role="radiogroup"] {
    background: var(--slate-100);
    padding: 4px;
    border-radius: 8px;
    gap: 4px;
    width: fit-content;
}
div[data-testid="stRadio"] label {
    background: transparent !important;
    border-radius: 6px !important;
    padding: 6px 16px !important;
    font-size: 14px !important;
    font-weight: 500 !important;
    color: var(--text-secondary) !important;
    transition: all 200ms ease-in-out !important;
    cursor: pointer;
    margin: 0 !important;
}
div[data-testid="stRadio"] label:has(input:checked) {
    background: white !important;
    color: var(--text-primary) !important;
    box-shadow: var(--shadow-sm) !important;
    font-weight: 600 !important;
}
div[data-testid="stRadio"] label > div:first-child { display: none !important; }

/* ============================================================
   13. ALERTS / INFO BOXES
   ============================================================ */
.fluxo-info-box {
    padding: 10px 14px;
    border-radius: 10px;
    display: flex; align-items: center; gap: 10px;
    font-size: 14px; font-weight: 600;
    margin: 12px 0;
}
.fluxo-info-box svg { flex-shrink: 0; }
.fluxo-info-box.receita {
    background: rgba(16, 185, 129, 0.08);
    color: var(--emerald-800);
    border: 1px solid rgba(16, 185, 129, 0.25);
}
.fluxo-info-box.despesa {
    background: rgba(244, 63, 94, 0.08);
    color: #881337;
    border: 1px solid rgba(244, 63, 94, 0.25);
}
</style>
"""


def inject_global_css() -> None:
    st.markdown(GLOBAL_CSS, unsafe_allow_html=True)
