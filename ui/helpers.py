"""
Helpers visuais reutilizaveis: formatadores, badges, page header.
HTML compactado em linha unica para evitar code-block do markdown.
"""
import streamlit as st


def format_brl(value: float) -> str:
    formatted = f"{value:,.2f}"
    return "R$ " + formatted.replace(",", "X").replace(".", ",").replace("X", ".")


def format_brl_short(value: float) -> str:
    formatted = f"{value:,.2f}"
    return formatted.replace(",", "X").replace(".", ",").replace("X", ".")


def format_date_br(iso_date: str) -> str:
    if not iso_date:
        return "—"
    try:
        y, m, d = iso_date.split("-")
        return f"{d}/{m}/{y}"
    except (ValueError, AttributeError):
        return iso_date


def page_header(title: str, subtitle: str = "") -> None:
    sub_html = f'<p class="page-subtitle">{subtitle}</p>' if subtitle else ""
    st.markdown(
        f'<div class="page-header"><h1 class="page-title">{title}</h1>{sub_html}</div>',
        unsafe_allow_html=True,
    )


def status_badge(status: str) -> str:
    labels = {
        "aberto":     "Em Aberto",
        "pago":       "Pago",
        "atrasado":   "Atrasado",
        "parcial":    "Parcial",
        "cancelado":  "Cancelado",
    }
    label = labels.get(status, status.title())
    return f'<span class="badge {status}"><span class="badge-dot"></span>{label}</span>'


def ativo_badge(ativo: bool) -> str:
    if ativo:
        return '<span class="badge ativo"><span class="badge-dot"></span>Ativo</span>'
    return '<span class="badge inativo"><span class="badge-dot"></span>Inativo</span>'


def initials(text: str, max_chars: int = 2) -> str:
    parts = [p for p in text.split() if p]
    return "".join(p[0].upper() for p in parts[:max_chars])
