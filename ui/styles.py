"""
Injeção de CSS global. Estiliza:
 - Sidebar nativa do Streamlit (paleta Deep Corporate / dark)
 - Header sticky e demais componentes
 - DataGrids, badges e cards customizados
"""
import streamlit as st


GLOBAL_CSS = """

<style>
/* ============================================================
   1. FONTS & CSS VARIABLES
   ============================================================ */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
:root {
    --navy-950: #0a1628;
    --navy-900: #0d1b30;
    --navy-800: #112240;
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
    --emerald-300: #6ee7b7;
    --emerald-400: #34d399;
    --emerald-500: #10b981;
    --emerald-600: #059669;
    --emerald-700: #047857;
    --emerald-800: #065f46;
    --rose-400: #fb7185;
    --rose-500: #f43f5e;
    --rose-700: #be123c;
    --sky-400:  #38bdf8;
    --amber-400:#fbbf24;
    --shadow-sm: 0 1px 2px 0 rgba(15, 23, 42, 0.05);
    --shadow-md: 0 4px 12px -2px rgba(15, 23, 42, 0.08);
    --shadow-lg: 0 10px 30px -8px rgba(15, 23, 42, 0.12);
}
/* ============================================================
   2. GLOBAL — fontes, scrollbar, esconde elementos nativos
   ============================================================ */
html, body, [class*="css"], .stApp {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    -webkit-font-smoothing: antialiased;
}
/* Esconde header e menu nativos — MAS preserva botão de abrir sidebar */
header[data-testid="stHeader"] {
    background: transparent;
    height: 0;
    z-index: 999;
}
/* Garante que o botão de toggle da sidebar fique visível e clicável */
header[data-testid="stHeader"] button[kind="header"],
[data-testid="stSidebarCollapsedControl"],
[data-testid="collapsedControl"] {
    display: flex !important;
    visibility: visible !important;
    z-index: 9999 !important;
    background: var(--navy-900) !important;
    color: white !important;
    border-radius: 8px !important;
}
[data-testid="stToolbar"] { display: none !important; }
[data-testid="stDecoration"] { display: none !important; }
#MainMenu { display: none !important; }
footer { display: none !important; }
.stDeployButton { display: none !important; }
.tabular-nums, .money { font-variant-numeric: tabular-nums; }
/* Scrollbar */
::-webkit-scrollbar { width: 8px; height: 8px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: rgba(148, 163, 184, 0.3); border-radius: 8px; }
::-webkit-scrollbar-thumb:hover { background: rgba(148, 163, 184, 0.5); }
.stApp { background: var(--slate-100); }
/* ============================================================
   3. SIDEBAR NATIVA — paleta dark "Deep Corporate"
   ============================================================ */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, var(--navy-950) 0%, var(--navy-900) 100%) !important;
    border-right: 1px solid rgba(30, 41, 59, 0.6) !important;
    width: 260px !important;
    min-width: 260px !important;
}
section[data-testid="stSidebar"] > div {
    padding-top: 1rem !important;
    padding-left: 0.75rem !important;
    padding-right: 0.75rem !important;
}
/* Brand block */
.fluxo-brand {
    display: flex; align-items: center; gap: 12px;
    padding: 4px 8px 16px;
}
.fluxo-brand-mark {
    width: 38px; height: 38px;
    border-radius: 12px;
    background: linear-gradient(135deg, var(--emerald-400), var(--emerald-600));
    display: flex; align-items: center; justify-content: center;
    color: white; font-weight: 700; font-size: 16px;
    box-shadow: 0 4px 14px rgba(16, 185, 129, 0.35),
                inset 0 1px 0 rgba(255, 255, 255, 0.2);
    flex-shrink: 0;
}
.fluxo-brand-mark svg { width: 18px; height: 18px; }
.fluxo-brand-text { display: flex; flex-direction: column; line-height: 1.1; }
.fluxo-brand-name {
    color: white; font-size: 16px; font-weight: 700; letter-spacing: -0.02em;
}
.fluxo-brand-name span { color: var(--emerald-400); }
.fluxo-brand-tag {
    color: var(--slate-500); font-size: 10px; font-weight: 600;
    letter-spacing: 0.15em; margin-top: 3px;
}
.fluxo-brand-divider {
    height: 1px; background: rgba(30, 41, 59, 0.6);
    margin: 0 -0.75rem 16px;
}
/* Nav group labels */
.fluxo-nav-label {
    padding: 0 12px 8px;
    font-size: 10px; font-weight: 700; color: var(--slate-500);
    letter-spacing: 0.18em;
}
/* Botoes dentro da sidebar */
section[data-testid="stSidebar"] .stButton > button {
    width: 100%;
    background: transparent !important;
    border: none !important;
    color: var(--slate-300) !important;
    padding: 10px 14px !important;
    border-radius: 8px !important;
    font-size: 13.5px !important;
    font-weight: 500 !important;
    text-align: left !important;
    justify-content: flex-start !important;
    transition: all 200ms ease-in-out !important;
    margin-bottom: 2px !important;
    box-shadow: none !important;
    min-height: 40px !important;
    height: auto !important;
    line-height: 1.3 !important;
}
section[data-testid="stSidebar"] .stButton > button:hover {
    background: rgba(255, 255, 255, 0.04) !important;
    color: white !important;
    border: none !important;
    transform: none !important;
}
section[data-testid="stSidebar"] .stButton > button:focus,
section[data-testid="stSidebar"] .stButton > button:focus-visible {
    box-shadow: none !important;
    outline: none !important;
    border: none !important;
}
section[data-testid="stSidebar"] .stButton > button:active {
    background: rgba(255, 255, 255, 0.06) !important;
    transform: none !important;
}
/* ATIVO: gradient + barra esmeralda + glow */
section[data-testid="stSidebar"] .stButton > button[kind="primary"] {
    background: linear-gradient(90deg, rgba(16, 185, 129, 0.18), rgba(16, 185, 129, 0.04)) !important;
    color: white !important;
    border-left: 3px solid var(--emerald-400) !important;
    padding-left: 11px !important;
    font-weight: 600 !important;
    box-shadow: -3px 0 12px -2px rgba(52, 211, 153, 0.4) !important;
}
section[data-testid="stSidebar"] .stButton > button[kind="primary"]:hover {
    background: linear-gradient(90deg, rgba(16, 185, 129, 0.25), rgba(16, 185, 129, 0.06)) !important;
}
/* Esconde divisor padrao dentro da sidebar */
section[data-testid="stSidebar"] hr { display: none !important; }
/* ============================================================
   4. MAIN CONTENT AREA
   ============================================================ */
[data-testid="stAppViewContainer"] > .main {
    background: var(--slate-100);
}
.main .block-container {
    padding-top: 1.5rem !important;
    padding-bottom: 3rem !important;
    max-width: 1600px !important;
}
/* ============================================================
   5. HEADER — Tenant + Org + Saldo + User
   ============================================================ */
.fluxo-header-anchor { height: 0; margin: 0; }
.fluxo-tenant-badge {
    display: flex; align-items: center; gap: 10px;
    padding: 4px 0;
}
.fluxo-tenant-mark {
    width: 34px; height: 34px;
    border-radius: 8px;
    background: linear-gradient(135deg, var(--slate-700), var(--slate-900));
    display: flex; align-items: center; justify-content: center;
    color: white; font-weight: 700; font-size: 12px;
    box-shadow: var(--shadow-sm);
    flex-shrink: 0;
}
.fluxo-tenant-text { display: flex; flex-direction: column; line-height: 1.2; min-width: 0; }
.fluxo-tenant-label {
    font-size: 9px; font-weight: 700; color: var(--slate-400);
    letter-spacing: 0.15em;
}
.fluxo-tenant-name {
    font-size: 13px; font-weight: 700; color: var(--slate-800);
    overflow: hidden; text-overflow: ellipsis; white-space: nowrap;
}
/* Saldo */
.fluxo-saldo {
    display: flex; align-items: center; gap: 10px;
    padding: 8px 14px;
    border-radius: 10px;
    background: linear-gradient(135deg, rgba(16, 185, 129, 0.1), rgba(16, 185, 129, 0.03));
    border: 1px solid rgba(16, 185, 129, 0.25);
}
.fluxo-saldo-icon {
    width: 28px; height: 28px;
    border-radius: 6px;
    background: rgba(16, 185, 129, 0.12);
    display: flex; align-items: center; justify-content: center;
    flex-shrink: 0;
}
.fluxo-saldo-icon svg { display: block; }
.fluxo-saldo-text { display: flex; flex-direction: column; line-height: 1.2; }
.fluxo-saldo-label {
    font-size: 9px; font-weight: 700;
    color: var(--emerald-700); opacity: 0.8;
    letter-spacing: 0.12em;
}
.fluxo-saldo-value {
    font-size: 14px; font-weight: 700; color: var(--emerald-800);
    font-variant-numeric: tabular-nums;
    margin-top: 2px;
}
/* User */
.fluxo-user {
    display: flex; align-items: center; gap: 10px;
    justify-content: flex-end;
}
.fluxo-user-text { display: flex; flex-direction: column; align-items: flex-end; line-height: 1.2; }
.fluxo-user-name { font-size: 13px; font-weight: 700; color: var(--slate-800); }
.fluxo-user-status {
    font-size: 10px; font-weight: 500; color: var(--slate-500);
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
/* ============================================================
   6. PAGE HEADER
   ============================================================ */
.page-header {
    margin-bottom: 24px;
}
.page-title {
    font-size: 26px; font-weight: 800; color: var(--slate-900);
    letter-spacing: -0.025em; margin: 0;
    line-height: 1.2;
}
.page-subtitle {
    font-size: 14px; color: var(--slate-500); margin-top: 4px;
}
/* ============================================================
   7. CARDS / KPI
   ============================================================ */
.card {
    background: white;
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
    background: white;
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
    font-size: 11px; font-weight: 700; color: var(--slate-500);
    letter-spacing: 0.05em; text-transform: uppercase;
}
.kpi-value {
    font-size: 24px; font-weight: 700; color: var(--slate-900);
    letter-spacing: -0.02em; line-height: 1.2;
    font-variant-numeric: tabular-nums;
    margin-bottom: 4px;
}
.kpi-change { font-size: 12px; font-weight: 500; }
.kpi-change.positive { color: var(--emerald-700); }
.kpi-change.negative { color: var(--rose-700); }
.kpi-change.neutral  { color: var(--slate-600); }
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
.summary-card.resultado .summary-label { color: var(--slate-700); }
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
   8. DATAGRID
   ============================================================ */
.datagrid {
    background: white;
    border: 1px solid var(--slate-200);
    border-radius: 12px;
    overflow: hidden;
    margin-top: 16px;
}
.datagrid table {
    width: 100%; border-collapse: collapse;
}
.datagrid thead {
    background: var(--slate-50);
    border-bottom: 1px solid var(--slate-200);
}
.datagrid th {
    padding: 12px 20px;
    text-align: left;
    font-size: 11px; font-weight: 700;
    color: var(--slate-500);
    text-transform: uppercase; letter-spacing: 0.05em;
}
.datagrid td {
    padding: 14px 20px;
    border-bottom: 1px solid var(--slate-100);
    font-size: 14px; color: var(--slate-700);
    vertical-align: middle;
}
.datagrid tbody tr:hover {
    background: var(--slate-50);
    transition: background 200ms ease-in-out;
}
.datagrid tbody tr:last-child td { border-bottom: none; }
.datagrid-footer {
    padding: 12px 20px;
    border-top: 1px solid var(--slate-200);
    background: var(--slate-50);
    display: flex; justify-content: space-between; align-items: center;
    font-size: 12px; color: var(--slate-600);
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
.row-name { font-weight: 600; color: var(--slate-800); font-size: 14px; }
.row-sub  { font-size: 12px; color: var(--slate-500); margin-top: 2px; }
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
   9. BADGES
   ============================================================ */
.badge {
    display: inline-flex; align-items: center; gap: 6px;
    padding: 3px 9px;
    border-radius: 6px;
    font-size: 12px; font-weight: 600;
    border: 1px solid;
}
.badge-dot { width: 6px; height: 6px; border-radius: 50%; flex-shrink: 0; }
.badge.aberto    { background: rgba(56, 189, 248, 0.1); color: #0369a1; border-color: rgba(56, 189, 248, 0.25); }
.badge.aberto    .badge-dot { background: var(--sky-400); }
.badge.pago      { background: rgba(16, 185, 129, 0.1); color: var(--emerald-800); border-color: rgba(16, 185, 129, 0.25); }
.badge.pago      .badge-dot { background: var(--emerald-400); }
.badge.atrasado  { background: rgba(244, 63, 94, 0.1);  color: #991b1b; border-color: rgba(244, 63, 94, 0.25); }
.badge.atrasado  .badge-dot { background: var(--rose-400); }
.badge.parcial   { background: rgba(251, 191, 36, 0.1); color: #92400e; border-color: rgba(251, 191, 36, 0.25); }
.badge.parcial   .badge-dot { background: var(--amber-400); }
.badge.cancelado { background: var(--slate-100); color: var(--slate-500); border-color: var(--slate-200); }
.badge.cancelado .badge-dot { background: var(--slate-400); }
.badge.ativo     { background: rgba(16, 185, 129, 0.1); color: var(--emerald-800); border-color: rgba(16, 185, 129, 0.25); }
.badge.ativo     .badge-dot { background: var(--emerald-500); }
.badge.inativo   { background: var(--slate-100); color: var(--slate-500); border-color: var(--slate-200); }
.badge.inativo   .badge-dot { background: var(--slate-400); }
.tag {
    display: inline-block;
    padding: 3px 9px;
    border-radius: 6px;
    background: var(--slate-100);
    color: var(--slate-700);
    font-size: 12px; font-weight: 500;
}
/* ============================================================
   10. STREAMLIT BUTTONS (área principal)
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
    color: var(--slate-700);
}
.main .stButton > button:hover {
    box-shadow: var(--shadow-md);
    transform: translateY(-1px);
    border-color: var(--slate-300);
    color: var(--slate-900);
}
.main .stButton > button[kind="primary"] {
    background: var(--slate-900) !important;
    color: white !important;
    border: 1px solid var(--slate-900) !important;
}
.main .stButton > button[kind="primary"]:hover {
    background: var(--slate-800) !important;
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
.main div[data-baseweb="input"] input:focus,
.main div[data-baseweb="textarea"] textarea:focus {
    border-color: var(--emerald-400) !important;
    box-shadow: 0 0 0 4px rgba(16, 185, 129, 0.1) !important;
}
.main div[data-testid="stWidgetLabel"] > label {
    font-size: 12px !important;
    font-weight: 600 !important;
    color: var(--slate-700) !important;
}
/* Selectbox do header — visual destacado */
.main div[data-baseweb="select"] > div {
    background: white !important;
    min-height: 42px !important;
    font-size: 13px !important;
}
/* ============================================================
   12. TABS / RADIO HORIZONTAL
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
    color: var(--slate-600) !important;
    transition: all 200ms ease-in-out !important;
    cursor: pointer;
    margin: 0 !important;
}
div[data-testid="stRadio"] label:has(input:checked) {
    background: white !important;
    color: var(--slate-900) !important;
    box-shadow: var(--shadow-sm) !important;
    font-weight: 600 !important;
}
div[data-testid="stRadio"] label > div:first-child { display: none !important; }
/* ============================================================
   13. ALERTS / INFO BOXES (modais)
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
/* ============================================================
   14. DIVIDERS — refinamento
   ============================================================ */
.main hr {
    margin: 1rem 0 1.5rem !important;
    border-color: var(--slate-200) !important;
}
</style>

"""


def inject_global_css() -> None:
    """Injeta o stylesheet global. Deve ser chamado uma vez por execução."""
    st.markdown(GLOBAL_CSS, unsafe_allow_html=True)
