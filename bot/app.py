# -*- coding: utf-8 -*-

import urllib.parse
import streamlit as st

# ========== INICIALIZAÇÃO DO MODO ESCURO (deve vir primeiro) ==========
if "modo_escuro" not in st.session_state:
    st.session_state.modo_escuro = False


# Configuração do Contato WhatsApp (Formato internacional: DDI 55 + DDD 11 + Número)
NUMERO_WHATSAPP = "SEU NUMERO AQUI"
WHATSAPP_FORMATADO = "(11) 99999-9999"  # Formato legível para exibição

# 1. Configuração da página
st.set_page_config(
    page_title="NOME DA SUA LOJA | Atendimento Inteligente",
    page_icon="📱",
    layout="wide"
)

# 2. CSS Customizado para Estilização Profissional
# 2. CSS Customizado (claro ou escuro)
if st.session_state.modo_escuro:
    css = """
    <style>
    .main-header {
        font-size: 2.2rem;
        color: #60a5fa;
        font-weight: 700;
        margin-bottom: 0px;
    }
    .sub-header {
        font-size: 1rem;
        color: #9ca3af;
        margin-bottom: 10px;
    }
    .project-info {
        font-size: 0.85rem;
        color: #cbd5e1;
        margin-bottom: 15px;
        font-style: italic;
    }
    .contato-destaque {
        background-color: #1e293b;
        border: 1px solid #25D366;
        border-radius: 8px;
        padding: 10px 15px;
        margin-bottom: 20px;
        display: inline-block;
        font-weight: bold;
        color: #4ade80;
    }
    .produto-card {
        background-color: #1f2937;
        border-left: 5px solid #25D366;
        border-radius: 8px;
        padding: 15px;
        margin-bottom: 15px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.5);
        color: #f3f4f6;
    }
    .btn-whatsapp {
        display: inline-block;
        background-color: #25D366;
        color: white !important;
        text-decoration: none;
        padding: 8px 16px;
        border-radius: 5px;
        font-weight: bold;
        font-size: 0.9rem;
        margin-top: 10px;
    }
    .btn-whatsapp:hover {
        background-color: #1eb854;
        color: white !important;
    }
    body {
        background-color: #0f172a;
        color: #f3f4f6;
    }
    .stApp {
        background-color: #0f172a;
    }
    </style>
    """
else:
    css = """
    <style>
    .main-header {
        font-size: 2.2rem;
        color: #1E3A8A;
        font-weight: 700;
        margin-bottom: 0px;
    }
    .sub-header {
        font-size: 1rem;
        color: #6B7280;
        margin-bottom: 10px;
    }
    .project-info {
        font-size: 0.85rem;
        color: #4B5563;
        margin-bottom: 15px;
        font-style: italic;
    }
    .contato-destaque {
        background-color: #e8f5e9;
        border: 1px solid #25D366;
        border-radius: 8px;
        padding: 10px 15px;
        margin-bottom: 20px;
        display: inline-block;
        font-weight: bold;
        color: #1b5e20;
    }
    .produto-card {
        background-color: #ffffff;
        border-left: 5px solid #25D366;
        border-radius: 8px;
        padding: 15px;
        margin-bottom: 15px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.08);
        color: #1f2937;
    }
    .btn-whatsapp {
        display: inline-block;
        background-color: #25D366;
        color: white !important;
        text-decoration: none;
        padding: 8px 16px;
        border-radius: 5px;
        font-weight: bold;
        font-size: 0.9rem;
        margin-top: 10px;
    }
    .btn-whatsapp:hover {
        background-color: #1eb854;
        color: white !important;
    }
    body {
        background-color: #ffffff;
        color: #000000;
    }
    .stApp {
        background-color: #ffffff;
    }
    </style>
    """

st.markdown(css, unsafe_allow_html=True)

# 3. Base de Dados de Telas
# -*- coding: utf-8 -*-
# CATÁLOGO LIMPO extraído das tabelas (sem Kanguru, sem endereços)
CATALOGO = {
    # ========== IPHONE HD + VIVID ==========
    "iphone x hd vivid": [
        {"tabela": "iPhone HD + VIVID", "tipo": "HD + VIVID", "atacado": "58,00", "varejo": "58,00", "marca": "Apple"}
    ],
    "iphone xs hd vivid": [
        {"tabela": "iPhone HD + VIVID", "tipo": "HD + VIVID", "atacado": "58,00", "varejo": "58,00", "marca": "Apple"}
    ],
    "iphone xs max hd vivid": [
        {"tabela": "iPhone HD + VIVID", "tipo": "HD + VIVID", "atacado": "70,00", "varejo": "70,00", "marca": "Apple"}
    ],
    "iphone xr hd vivid": [
        {"tabela": "iPhone HD + VIVID", "tipo": "HD + VIVID", "atacado": "60,00", "varejo": "60,00", "marca": "Apple"}
    ],
    "iphone 11 hd vivid": [
        {"tabela": "iPhone HD + VIVID", "tipo": "HD + VIVID", "atacado": "60,00", "varejo": "60,00", "marca": "Apple"}
    ],
    "iphone 11 pro hd vivid": [
        {"tabela": "iPhone HD + VIVID", "tipo": "HD + VIVID", "atacado": "76,00", "varejo": "76,00", "marca": "Apple"}
    ],
    "iphone 11 pro max hd vivid": [
        {"tabela": "iPhone HD + VIVID", "tipo": "HD + VIVID", "atacado": "78,00", "varejo": "78,00", "marca": "Apple"}
    ],
    "iphone 12 hd vivid": [
        {"tabela": "iPhone HD + VIVID", "tipo": "HD + VIVID", "atacado": "82,00", "varejo": "82,00", "marca": "Apple"}
    ],
    "iphone 12 pro max hd vivid": [
        {"tabela": "iPhone HD + VIVID", "tipo": "HD + VIVID", "atacado": "90,00", "varejo": "90,00", "marca": "Apple"}
    ],
    "iphone 12 mini hd vivid": [
        {"tabela": "iPhone HD + VIVID", "tipo": "HD + VIVID", "atacado": "105,00", "varejo": "105,00", "marca": "Apple"}
    ],
    "iphone 13 hd vivid": [
        {"tabela": "iPhone HD + VIVID", "tipo": "HD + VIVID", "atacado": "110,00", "varejo": "110,00", "marca": "Apple"}
    ],
    "iphone 13 pro hd vivid": [
        {"tabela": "iPhone HD + VIVID", "tipo": "HD + VIVID", "atacado": "138,00", "varejo": "138,00", "marca": "Apple"}
    ],
    "iphone 13 pro max hd vivid": [
        {"tabela": "iPhone HD + VIVID", "tipo": "HD + VIVID", "atacado": "94,00", "varejo": "94,00", "marca": "Apple"}
    ],
    "iphone 14 hd vivid": [
        {"tabela": "iPhone HD + VIVID", "tipo": "HD + VIVID", "atacado": "94,00", "varejo": "94,00", "marca": "Apple"}
    ],
    "iphone 14 pro hd vivid": [
        {"tabela": "iPhone HD + VIVID", "tipo": "HD + VIVID", "atacado": "118,00", "varejo": "118,00", "marca": "Apple"}
    ],
    "iphone 14 pro max hd vivid": [
        {"tabela": "iPhone HD + VIVID", "tipo": "HD + VIVID", "atacado": "148,00", "varejo": "148,00", "marca": "Apple"}
    ],
    # ========== IPHONE JK ==========
    "iphone x jk": [
        {"tabela": "iPhone JK", "tipo": "JK", "atacado": "78,00", "varejo": "78,00", "marca": "Apple"}
    ],
    "iphone xs jk": [
        {"tabela": "iPhone JK", "tipo": "JK", "atacado": "78,00", "varejo": "78,00", "marca": "Apple"}
    ],
    "iphone xs max jk": [
        {"tabela": "iPhone JK", "tipo": "JK", "atacado": "88,00", "varejo": "88,00", "marca": "Apple"}
    ],
    "iphone 11 jk": [
        {"tabela": "iPhone JK", "tipo": "JK", "atacado": "75,00", "varejo": "75,00", "marca": "Apple"}
    ],
    "iphone 11 pro jk": [
        {"tabela": "iPhone JK", "tipo": "JK", "atacado": "75,00", "varejo": "75,00", "marca": "Apple"}
    ],
    "iphone 11 pro max jk": [
        {"tabela": "iPhone JK", "tipo": "JK", "atacado": "90,00", "varejo": "90,00", "marca": "Apple"}
    ],
    "iphone 12 jk": [
        {"tabela": "iPhone JK", "tipo": "JK", "atacado": "95,00", "varejo": "95,00", "marca": "Apple"}
    ],
    "iphone 15 jk": [
        {"tabela": "iPhone JK", "tipo": "JK", "atacado": "125,00", "varejo": "125,00", "marca": "Apple"}
    ],
    "iphone 15 plus jk": [
        {"tabela": "iPhone JK", "tipo": "JK", "atacado": "135,00", "varejo": "135,00", "marca": "Apple"}
    ],
    "iphone 15 pro jk": [
        {"tabela": "iPhone JK", "tipo": "JK", "atacado": "140,00", "varejo": "140,00", "marca": "Apple"}
    ],
    "iphone 15 pro max jk": [
        {"tabela": "iPhone JK", "tipo": "JK", "atacado": "185,00", "varejo": "185,00", "marca": "Apple"}
    ],
    "iphone 16 jk": [
        {"tabela": "iPhone JK", "tipo": "JK", "atacado": "185,00", "varejo": "185,00", "marca": "Apple"}
    ],
    "iphone 16 pro jk": [
        {"tabela": "iPhone JK", "tipo": "JK", "atacado": "320,00", "varejo": "320,00", "marca": "Apple"}
    ],
    "iphone 16 pro max jk": [
        {"tabela": "iPhone JK", "tipo": "JK", "atacado": "375,00", "varejo": "375,00", "marca": "Apple"}
    ],
    # ========== IPHONE FHD ==========
    "iphone x fhd": [
        {"tabela": "iPhone FHD", "tipo": "FHD", "atacado": "95,00", "varejo": "95,00", "marca": "Apple"}
    ],
    "iphone xs fhd": [
        {"tabela": "iPhone FHD", "tipo": "FHD", "atacado": "95,00", "varejo": "95,00", "marca": "Apple"}
    ],
    "iphone xs max fhd": [
        {"tabela": "iPhone FHD", "tipo": "FHD", "atacado": "110,00", "varejo": "110,00", "marca": "Apple"}
    ],
    "iphone xr fhd": [
        {"tabela": "iPhone FHD", "tipo": "FHD", "atacado": "90,00", "varejo": "90,00", "marca": "Apple"}
    ],
    "iphone 11 fhd": [
        {"tabela": "iPhone FHD", "tipo": "FHD", "atacado": "90,00", "varejo": "90,00", "marca": "Apple"}
    ],
    "iphone 11 pro fhd": [
        {"tabela": "iPhone FHD", "tipo": "FHD", "atacado": "110,00", "varejo": "110,00", "marca": "Apple"}
    ],
    "iphone 11 pro max fhd": [
        {"tabela": "iPhone FHD", "tipo": "FHD", "atacado": "125,00", "varejo": "125,00", "marca": "Apple"}
    ],
    "iphone 12 fhd": [
        {"tabela": "iPhone FHD", "tipo": "FHD", "atacado": "110,00", "varejo": "110,00", "marca": "Apple"}
    ],
    "iphone 12 pro max fhd": [
        {"tabela": "iPhone FHD", "tipo": "FHD", "atacado": "175,00", "varejo": "175,00", "marca": "Apple"}
    ],
    "iphone 13 fhd": [
        {"tabela": "iPhone FHD", "tipo": "FHD", "atacado": "160,00", "varejo": "160,00", "marca": "Apple"}
    ],
    "iphone 13 pro fhd": [
        {"tabela": "iPhone FHD", "tipo": "FHD", "atacado": "130,00", "varejo": "130,00", "marca": "Apple"}
    ],
    "iphone 13 pro max fhd": [
        {"tabela": "iPhone FHD", "tipo": "FHD", "atacado": "160,00", "varejo": "160,00", "marca": "Apple"}
    ],
    "iphone 14 fhd": [
        {"tabela": "iPhone FHD", "tipo": "FHD", "atacado": "175,00", "varejo": "175,00", "marca": "Apple"}
    ],
    "iphone 14 plus fhd": [
        {"tabela": "iPhone FHD", "tipo": "FHD", "atacado": "165,00", "varejo": "165,00", "marca": "Apple"}
    ],
    "iphone 14 pro fhd": [
        {"tabela": "iPhone FHD", "tipo": "FHD", "atacado": "165,00", "varejo": "165,00", "marca": "Apple"}
    ],
    "iphone 14 pro max fhd": [
        {"tabela": "iPhone FHD", "tipo": "FHD", "atacado": "190,00", "varejo": "190,00", "marca": "Apple"}
    ],
    "iphone 16e fhd": [
        {"tabela": "iPhone FHD", "tipo": "FHD", "atacado": "420,00", "varejo": "420,00", "marca": "Apple"}
    ],
    "iphone 16 pro fhd": [
        {"tabela": "iPhone FHD", "tipo": "FHD", "atacado": "320,00", "varejo": "320,00", "marca": "Apple"}
    ],
    "iphone 16 pro max fhd": [
        {"tabela": "iPhone FHD", "tipo": "FHD", "atacado": "380,00", "varejo": "380,00", "marca": "Apple"}
    ],
    "iphone 17 fhd": [
        {"tabela": "iPhone FHD", "tipo": "FHD", "atacado": "460,00", "varejo": "460,00", "marca": "Apple"}
    ],
    "iphone 17 pro fhd": [
        {"tabela": "iPhone FHD", "tipo": "FHD", "atacado": "500,00", "varejo": "500,00", "marca": "Apple"}
    ],
    "iphone 17 pro max fhd": [
        {"tabela": "iPhone FHD", "tipo": "FHD", "atacado": "550,00", "varejo": "550,00", "marca": "Apple"}
    ],
    # ========== IPHONE OLED VIVID ==========
    "iphone x oled vivid": [
        {"tabela": "iPhone OLED VIVID", "tipo": "OLED VIVID", "atacado": "148,00", "varejo": "148,00", "marca": "Apple"}
    ],
    "iphone xs oled vivid": [
        {"tabela": "iPhone OLED VIVID", "tipo": "OLED VIVID", "atacado": "148,00", "varejo": "148,00", "marca": "Apple"}
    ],
    "iphone xs max oled vivid": [
        {"tabela": "iPhone OLED VIVID", "tipo": "OLED VIVID", "atacado": "188,00", "varejo": "188,00", "marca": "Apple"}
    ],
    "iphone 11 pro oled vivid": [
        {"tabela": "iPhone OLED VIVID", "tipo": "OLED VIVID", "atacado": "420,00", "varejo": "420,00", "marca": "Apple"}
    ],
    "iphone 11 pro max oled vivid": [
        {"tabela": "iPhone OLED VIVID", "tipo": "OLED VIVID", "atacado": "220,00", "varejo": "220,00", "marca": "Apple"}
    ],
    "iphone 12 oled vivid": [
        {"tabela": "iPhone OLED VIVID", "tipo": "OLED VIVID", "atacado": "225,00", "varejo": "225,00", "marca": "Apple"}
    ],
    "iphone 12 pro max oled vivid": [
        {"tabela": "iPhone OLED VIVID", "tipo": "OLED VIVID", "atacado": "305,00", "varejo": "305,00", "marca": "Apple"}
    ],
    "iphone 16e oled vivid": [
        {"tabela": "iPhone OLED VIVID", "tipo": "OLED VIVID", "atacado": "465,00", "varejo": "465,00", "marca": "Apple"}
    ],
    "iphone 16 pro oled vivid": [
        {"tabela": "iPhone OLED VIVID", "tipo": "OLED VIVID", "atacado": "465,00", "varejo": "465,00", "marca": "Apple"}
    ],
    "iphone 16 pro max oled vivid": [
        {"tabela": "iPhone OLED VIVID", "tipo": "OLED VIVID", "atacado": "560,00", "varejo": "560,00", "marca": "Apple"}
    ],
    "iphone 17 oled vivid": [
        {"tabela": "iPhone OLED VIVID", "tipo": "OLED VIVID", "atacado": "625,00", "varejo": "625,00", "marca": "Apple"}
    ],
    "iphone 13 oled vivid": [
        {"tabela": "iPhone OLED VIVID", "tipo": "OLED VIVID", "atacado": "350,00", "varejo": "350,00", "marca": "Apple"}
    ],
    "iphone 13 pro oled vivid": [
        {"tabela": "iPhone OLED VIVID", "tipo": "OLED VIVID", "atacado": "270,00", "varejo": "270,00", "marca": "Apple"}
    ],
    "iphone 13 pro max oled vivid": [
        {"tabela": "iPhone OLED VIVID", "tipo": "OLED VIVID", "atacado": "335,00", "varejo": "335,00", "marca": "Apple"}
    ],
    "iphone 14 oled vivid": [
        {"tabela": "iPhone OLED VIVID", "tipo": "OLED VIVID", "atacado": "340,00", "varejo": "340,00", "marca": "Apple"}
    ],
    "iphone 14 plus oled vivid": [
        {"tabela": "iPhone OLED VIVID", "tipo": "OLED VIVID", "atacado": "350,00", "varejo": "350,00", "marca": "Apple"}
    ],
    "iphone 14 pro oled vivid": [
        {"tabela": "iPhone OLED VIVID", "tipo": "OLED VIVID", "atacado": "260,00", "varejo": "260,00", "marca": "Apple"}
    ],
    "iphone 14 pro max oled vivid": [
        {"tabela": "iPhone OLED VIVID", "tipo": "OLED VIVID", "atacado": "310,00", "varejo": "310,00", "marca": "Apple"}
    ],
    "iphone 17 pro oled vivid": [
        {"tabela": "iPhone OLED VIVID", "tipo": "OLED VIVID", "atacado": "395,00", "varejo": "395,00", "marca": "Apple"}
    ],
    "iphone 17 pro max oled vivid": [
        {"tabela": "iPhone OLED VIVID", "tipo": "OLED VIVID", "atacado": "450,00", "varejo": "450,00", "marca": "Apple"}
    ],
    "iphone 15 oled vivid": [
        {"tabela": "iPhone OLED VIVID", "tipo": "OLED VIVID", "atacado": "410,00", "varejo": "410,00", "marca": "Apple"}
    ],
    "iphone 15 plus oled vivid": [
        {"tabela": "iPhone OLED VIVID", "tipo": "OLED VIVID", "atacado": "410,00", "varejo": "410,00", "marca": "Apple"}
    ],
    # ========== IPHONE GENUINA ==========
    "iphone 12 genuina": [
        {"tabela": "iPhone Genuina", "tipo": "Genuina", "atacado": "365,00", "varejo": "365,00", "marca": "Apple"}
    ],
    "iphone 12 pro max genuina": [
        {"tabela": "iPhone Genuina", "tipo": "Genuina", "atacado": "430,00", "varejo": "430,00", "marca": "Apple"}
    ],
    "iphone 13 genuina": [
        {"tabela": "iPhone Genuina", "tipo": "Genuina", "atacado": "400,00", "varejo": "400,00", "marca": "Apple"}
    ],
    "iphone 13 pro genuina": [
        {"tabela": "iPhone Genuina", "tipo": "Genuina", "atacado": "470,00", "varejo": "470,00", "marca": "Apple"}
    ],
    "iphone 13 pro max genuina": [
        {"tabela": "iPhone Genuina", "tipo": "Genuina", "atacado": "480,00", "varejo": "480,00", "marca": "Apple"}
    ],
    "iphone 14 genuina": [
        {"tabela": "iPhone Genuina", "tipo": "Genuina", "atacado": "400,00", "varejo": "400,00", "marca": "Apple"}
    ],
    "iphone 14 pro genuina": [
        {"tabela": "iPhone Genuina", "tipo": "Genuina", "atacado": "495,00", "varejo": "495,00", "marca": "Apple"}
    ],
    "iphone 14 pro max genuina": [
        {"tabela": "iPhone Genuina", "tipo": "Genuina", "atacado": "550,00", "varejo": "550,00", "marca": "Apple"}
    ],
    "iphone 15 genuina": [
        {"tabela": "iPhone Genuina", "tipo": "Genuina", "atacado": "650,00", "varejo": "650,00", "marca": "Apple"}
    ],
    "iphone 15 pro genuina": [
        {"tabela": "iPhone Genuina", "tipo": "Genuina", "atacado": "670,00", "varejo": "670,00", "marca": "Apple"}
    ],
    "iphone 15 pro max genuina": [
        {"tabela": "iPhone Genuina", "tipo": "Genuina", "atacado": "690,00", "varejo": "690,00", "marca": "Apple"}
    ],
    "iphone 16 genuina": [
        {"tabela": "iPhone Genuina", "tipo": "Genuina", "atacado": "765,00", "varejo": "765,00", "marca": "Apple"}
    ],
    "iphone 16 pro genuina": [
        {"tabela": "iPhone Genuina", "tipo": "Genuina", "atacado": "975,00", "varejo": "975,00", "marca": "Apple"}
    ],
    "iphone 16 pro max genuina": [
        {"tabela": "iPhone Genuina", "tipo": "Genuina", "atacado": "1500,00", "varejo": "1500,00", "marca": "Apple"}
    ],
    # ========== SAMSUNG NACIONAL ==========
    "samsung sm a01 nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "100,00", "varejo": "100,00", "marca": "Samsung"}
    ],
    "samsung sm a02s nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "105,00", "varejo": "105,00", "marca": "Samsung"}
    ],
    "samsung sm a03 nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "105,00", "varejo": "105,00", "marca": "Samsung"}
    ],
    "samsung sm a03s nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "105,00", "varejo": "105,00", "marca": "Samsung"}
    ],
    "samsung sm a04s nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "105,00", "varejo": "105,00", "marca": "Samsung"}
    ],
    "samsung sm a04e nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "105,00", "varejo": "105,00", "marca": "Samsung"}
    ],
    "samsung sm a05 nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "105,00", "varejo": "105,00", "marca": "Samsung"}
    ],
    "samsung sm a05s nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "105,00", "varejo": "105,00", "marca": "Samsung"}
    ],
    "samsung sm a06 4g nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "105,00", "varejo": "105,00", "marca": "Samsung"}
    ],
    "samsung sm a10 nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "100,00", "varejo": "100,00", "marca": "Samsung"}
    ],
    "samsung sm a10s nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "105,00", "varejo": "105,00", "marca": "Samsung"}
    ],
    "samsung sm a11 nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "105,00", "varejo": "105,00", "marca": "Samsung"}
    ],
    "samsung sm a12 nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "105,00", "varejo": "105,00", "marca": "Samsung"}
    ],
    "samsung sm a13 4g nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "105,00", "varejo": "105,00", "marca": "Samsung"}
    ],
    "samsung sm a14 5g nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "110,00", "varejo": "110,00", "marca": "Samsung"}
    ],
    "samsung sm a16 5g nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "320,00", "varejo": "320,00", "marca": "Samsung"}
    ],
    "samsung sm a03 core nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "100,00", "varejo": "100,00", "marca": "Samsung"}
    ],
    "samsung sm a21s nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "110,00", "varejo": "110,00", "marca": "Samsung"}
    ],
    "samsung sm a23 4g nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "110,00", "varejo": "110,00", "marca": "Samsung"}
    ],
    "samsung sm a23 5g nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "110,00", "varejo": "110,00", "marca": "Samsung"}
    ],
    "samsung sm a15 nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "295,00", "varejo": "295,00", "marca": "Samsung"}
    ],
    "samsung sm a16 4g nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "340,00", "varejo": "340,00", "marca": "Samsung"}
    ],
    "samsung sm a26 nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "400,00", "varejo": "400,00", "marca": "Samsung"}
    ],
    "samsung sm a51 nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "505,00", "varejo": "505,00", "marca": "Samsung"}
    ],
    "samsung sm a54 nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "400,00", "varejo": "400,00", "marca": "Samsung"}
    ],
    "samsung sm a56 nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "455,00", "varejo": "455,00", "marca": "Samsung"}
    ],
    "samsung sm m13 4g nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "105,00", "varejo": "105,00", "marca": "Samsung"}
    ],
    "samsung sm m14 5g nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "110,00", "varejo": "110,00", "marca": "Samsung"}
    ],
    "samsung sm m20 nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "105,00", "varejo": "105,00", "marca": "Samsung"}
    ],
    "samsung sm m52 nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "305,00", "varejo": "305,00", "marca": "Samsung"}
    ],
    "samsung sm m53 nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "365,00", "varejo": "365,00", "marca": "Samsung"}
    ],
    "samsung sm note 10 nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "635,00", "varejo": "635,00", "marca": "Samsung"}
    ],
    "samsung sm note 20 nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "505,00", "varejo": "505,00", "marca": "Samsung"}
    ],
    "samsung sm s9 nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "425,00", "varejo": "425,00", "marca": "Samsung"}
    ],
    "samsung sm s9 plus nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "625,00", "varejo": "625,00", "marca": "Samsung"}
    ],
    "samsung sm s10 nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "705,00", "varejo": "705,00", "marca": "Samsung"}
    ],
    "samsung sm s21 fe nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "655,00", "varejo": "655,00", "marca": "Samsung"}
    ],
    "samsung sm s22 ultra nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "1285,00", "varejo": "1285,00", "marca": "Samsung"}
    ],
    "samsung sm s23 nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "835,00", "varejo": "835,00", "marca": "Samsung"}
    ],
    "samsung sm s23 ultra nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "1480,00", "varejo": "1480,00", "marca": "Samsung"}
    ],
    "samsung sm s24 fe nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "575,00", "varejo": "575,00", "marca": "Samsung"}
    ],
    "samsung sm s25 nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "835,00", "varejo": "835,00", "marca": "Samsung"}
    ],
    "samsung sm s25 fe nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "630,00", "varejo": "630,00", "marca": "Samsung"}
    ],
    "samsung sm s26 ultra nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "1955,00", "varejo": "1955,00", "marca": "Samsung"}
    ],
    # ========== MOTOROLA NACIONAL ==========
    "motorola mt g05 nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "105,00", "varejo": "105,00", "marca": "Motorola"}
    ],
    "motorola mt g10 nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "100,00", "varejo": "100,00", "marca": "Motorola"}
    ],
    "motorola mt g20 nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "100,00", "varejo": "100,00", "marca": "Motorola"}
    ],
    "motorola mt g30 nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "100,00", "varejo": "100,00", "marca": "Motorola"}
    ],
    "motorola mt g15 nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "105,00", "varejo": "105,00", "marca": "Motorola"}
    ],
    "motorola mt g24 nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "105,00", "varejo": "105,00", "marca": "Motorola"}
    ],
    "motorola mt g35 nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "110,00", "varejo": "110,00", "marca": "Motorola"}
    ],
    "motorola mt g42 nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "190,00", "varejo": "190,00", "marca": "Motorola"}
    ],
    "motorola mt g52 nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "230,00", "varejo": "230,00", "marca": "Motorola"}
    ],
    "motorola mt g60 nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "110,00", "varejo": "110,00", "marca": "Motorola"}
    ],
    "motorola mt g60s nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "110,00", "varejo": "110,00", "marca": "Motorola"}
    ],
    "motorola mt g54 nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "110,00", "varejo": "110,00", "marca": "Motorola"}
    ],
    "motorola mt g22 nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "105,00", "varejo": "105,00", "marca": "Motorola"}
    ],
    "motorola mt g5g nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "170,00", "varejo": "170,00", "marca": "Motorola"}
    ],
    "motorola mt e7 nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "100,00", "varejo": "100,00", "marca": "Motorola"}
    ],
    "motorola mt e7 plus nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "100,00", "varejo": "100,00", "marca": "Motorola"}
    ],
    "motorola mt e7 power nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "100,00", "varejo": "100,00", "marca": "Motorola"}
    ],
    "motorola mt e13 nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "100,00", "varejo": "100,00", "marca": "Motorola"}
    ],
    "motorola mt e20 nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "100,00", "varejo": "100,00", "marca": "Motorola"}
    ],
    "motorola mt e22 nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "100,00", "varejo": "100,00", "marca": "Motorola"}
    ],
    "motorola mt e32 nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "100,00", "varejo": "100,00", "marca": "Motorola"}
    ],
    "motorola mt g200 nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "220,00", "varejo": "220,00", "marca": "Motorola"}
    ],
    "motorola mt g84 nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "220,00", "varejo": "220,00", "marca": "Motorola"}
    ],
    "motorola mt g75 nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "145,00", "varejo": "145,00", "marca": "Motorola"}
    ],
    # ========== XIAOMI NACIONAL ==========
    "xiaomi redmi 9a nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "110,00", "varejo": "110,00", "marca": "Xiaomi"}
    ],
    "xiaomi redmi 13c nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "110,00", "varejo": "110,00", "marca": "Xiaomi"}
    ],
    "xiaomi redmi 12 nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "110,00", "varejo": "110,00", "marca": "Xiaomi"}
    ],
    "xiaomi redmi 14c nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "115,00", "varejo": "115,00", "marca": "Xiaomi"}
    ],
    "xiaomi poco m3 nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "115,00", "varejo": "115,00", "marca": "Xiaomi"}
    ],
    "xiaomi note 8 nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "130,00", "varejo": "130,00", "marca": "Xiaomi"}
    ],
    "xiaomi note 7 nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "130,00", "varejo": "130,00", "marca": "Xiaomi"}
    ],
    "xiaomi note 10 4g nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "205,00", "varejo": "205,00", "marca": "Xiaomi"}
    ],
    "xiaomi note 10 5g nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "115,00", "varejo": "115,00", "marca": "Xiaomi"}
    ],
    "xiaomi note 9 nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "110,00", "varejo": "110,00", "marca": "Xiaomi"}
    ],
    "xiaomi redmi 10c nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "105,00", "varejo": "105,00", "marca": "Xiaomi"}
    ],
    "xiaomi note 12 5g nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "200,00", "varejo": "200,00", "marca": "Xiaomi"}
    ],
    # ========== INFINIX NACIONAL ==========
    "infinix smart 8 nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "105,00", "varejo": "105,00", "marca": "Infinix"}
    ],
    "infinix smart 8 pro nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "105,00", "varejo": "105,00", "marca": "Infinix"}
    ],
    "infinix hot 11 nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "100,00", "varejo": "100,00", "marca": "Infinix"}
    ],
    "infinix hot 11s nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "115,00", "varejo": "115,00", "marca": "Infinix"}
    ],
    "infinix hot 20i nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "100,00", "varejo": "100,00", "marca": "Infinix"}
    ],
    "infinix hot 50 pro nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "250,00", "varejo": "250,00", "marca": "Infinix"}
    ],
    "infinix smart 10 nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "105,00", "varejo": "105,00", "marca": "Infinix"}
    ],
    # ========== REALME NACIONAL ==========
    "realme note 50 nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "105,00", "varejo": "105,00", "marca": "Realme"}
    ],
    "realme note 60 nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "105,00", "varejo": "105,00", "marca": "Realme"}
    ],
    "realme 8i nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "115,00", "varejo": "115,00", "marca": "Realme"}
    ],
    "realme 9i nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "115,00", "varejo": "115,00", "marca": "Realme"}
    ],
    "realme c71 nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "115,00", "varejo": "115,00", "marca": "Realme"}
    ],
    "realme c53 nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "105,00", "varejo": "105,00", "marca": "Realme"}
    ],
    "realme c85 nacional": [
        {"tabela": "Nacional", "tipo": "Nacional", "atacado": "125,00", "varejo": "125,00", "marca": "Realme"}
    ],
    # ========== SAMSUNG VIVID ==========
    "samsung sm a15 vivid": [
        {"tabela": "Vivid", "tipo": "Vivid", "atacado": "240,00", "varejo": "240,00", "marca": "Samsung"}
    ],
    "samsung sm a32 4g vivid": [
        {"tabela": "Vivid", "tipo": "Vivid", "atacado": "180,00", "varejo": "180,00", "marca": "Samsung"}
    ],
    "samsung sm a52 vivid": [
        {"tabela": "Vivid", "tipo": "Vivid", "atacado": "215,00", "varejo": "215,00", "marca": "Samsung"}
    ],
    "samsung sm a30s vivid": [
        {"tabela": "Vivid", "tipo": "Vivid", "atacado": "175,00", "varejo": "175,00", "marca": "Samsung"}
    ],
    "samsung sm a25 vivid": [
        {"tabela": "Vivid", "tipo": "Vivid", "atacado": "240,00", "varejo": "240,00", "marca": "Samsung"}
    ],
    "samsung sm a26 vivid": [
        {"tabela": "Vivid", "tipo": "Vivid", "atacado": "260,00", "varejo": "260,00", "marca": "Samsung"}
    ],
    "samsung sm a35 vivid": [
        {"tabela": "Vivid", "tipo": "Vivid", "atacado": "205,00", "varejo": "205,00", "marca": "Samsung"}
    ],
    "samsung sm a36 vivid": [
        {"tabela": "Vivid", "tipo": "Vivid", "atacado": "205,00", "varejo": "205,00", "marca": "Samsung"}
    ],
    "samsung sm a71 vivid": [
        {"tabela": "Vivid", "tipo": "Vivid", "atacado": "190,00", "varejo": "190,00", "marca": "Samsung"}
    ],
    "samsung sm a30 vivid": [
        {"tabela": "Vivid", "tipo": "Vivid", "atacado": "175,00", "varejo": "175,00", "marca": "Samsung"}
    ],
    "samsung sm s20 fe vivid": [
        {"tabela": "Vivid", "tipo": "Vivid", "atacado": "220,00", "varejo": "220,00", "marca": "Samsung"}
    ],
    "samsung sm s21 fe vivid": [
        {"tabela": "Vivid", "tipo": "Vivid", "atacado": "230,00", "varejo": "230,00", "marca": "Samsung"}
    ],
    "samsung sm a56 vivid": [
        {"tabela": "Vivid", "tipo": "Vivid", "atacado": "215,00", "varejo": "215,00", "marca": "Samsung"}
    ],
    "samsung sm m53 vivid": [
        {"tabela": "Vivid", "tipo": "Vivid", "atacado": "200,00", "varejo": "200,00", "marca": "Samsung"}
    ],
    "samsung sm m62 vivid": [
        {"tabela": "Vivid", "tipo": "Vivid", "atacado": "200,00", "varejo": "200,00", "marca": "Samsung"}
    ],
    # ========== XIAOMI VIVID ==========
    "xiaomi note 12 4g vivid": [
        {"tabela": "Vivid", "tipo": "Vivid", "atacado": "190,00", "varejo": "190,00", "marca": "Xiaomi"}
    ],
    "xiaomi note 12s vivid": [
        {"tabela": "Vivid", "tipo": "Vivid", "atacado": "200,00", "varejo": "200,00", "marca": "Xiaomi"}
    ],
    "xiaomi poco x5 vivid": [
        {"tabela": "Vivid", "tipo": "Vivid", "atacado": "195,00", "varejo": "195,00", "marca": "Xiaomi"}
    ],

    "iphone x": [
        {"tabela": "iPhone Kanguru", "tipo": "HD + VIVID", "atacado": "58,00", "varejo": "70,00", "marca": "Apple"},
        {"tabela": "iPhone Kanguru", "tipo": "OLED VIVID", "atacado": "148,00", "varejo": "170,00", "marca": "Apple"},
        {"tabela": "iPhone Kanguru", "tipo": "Kanguru (Sem Aro)", "atacado": "135,00", "varejo": "150,00", "marca": "Apple"},
        {"tabela": "iPhone Kanguru", "tipo": "Kanguru (Com Aro)", "atacado": "155,00", "varejo": "170,00", "marca": "Apple"}
    ],
    "iphone xs": [
        {"tabela": "iPhone Kanguru", "tipo": "HD + VIVID", "atacado": "58,00", "varejo": "70,00", "marca": "Apple"},
        {"tabela": "iPhone Kanguru", "tipo": "OLED VIVID", "atacado": "148,00", "varejo": "170,00", "marca": "Apple"}
    ],
    "iphone xs max": [
        {"tabela": "iPhone Kanguru", "tipo": "HD + VIVID", "atacado": "70,00", "varejo": "85,00", "marca": "Apple"},
        {"tabela": "iPhone Kanguru", "tipo": "OLED VIVID", "atacado": "188,00", "varejo": "210,00", "marca": "Apple"}
    ],
    "iphone xr": [
        {"tabela": "iPhone Kanguru", "tipo": "HD + VIVID", "atacado": "60,00", "varejo": "75,00", "marca": "Apple"},
        {"tabela": "iPhone Kanguru", "tipo": "Kanguru (Sem Aro)", "atacado": "140,00", "varejo": "155,00", "marca": "Apple"},
        {"tabela": "iPhone Kanguru", "tipo": "Kanguru (Com Aro)", "atacado": "165,00", "varejo": "180,00", "marca": "Apple"}
    ],
    "iphone 11": [
        {"tabela": "iPhone Kanguru", "tipo": "HD + VIVID", "atacado": "60,00", "varejo": "75,00", "marca": "Apple"},
        {"tabela": "iPhone Kanguru", "tipo": "Kanguru Premium", "atacado": "160,00", "varejo": "180,00", "marca": "Apple"},
        {"tabela": "iPhone Kanguru", "tipo": "Kanguru Comum", "atacado": "125,00", "varejo": "140,00", "marca": "Apple"}
    ],
    "iphone 11 pro": [
        {"tabela": "iPhone Kanguru", "tipo": "HD + VIVID", "atacado": "76,00", "varejo": "90,00", "marca": "Apple"},
        {"tabela": "iPhone Kanguru", "tipo": "OLED VIVID", "atacado": "190,00", "varejo": "215,00", "marca": "Apple"}
    ],
    "iphone 11 pro max": [
        {"tabela": "iPhone Kanguru", "tipo": "HD + VIVID", "atacado": "78,00", "varejo": "95,00", "marca": "Apple"},
        {"tabela": "iPhone Kanguru", "tipo": "OLED VIVID", "atacado": "220,00", "varejo": "250,00", "marca": "Apple"}
    ],
    "iphone 12": [
        {"tabela": "iPhone Kanguru", "tipo": "HD + VIVID", "atacado": "82,00", "varejo": "100,00", "marca": "Apple"},
        {"tabela": "iPhone Kanguru", "tipo": "OLED VIVID", "atacado": "225,00", "varejo": "255,00", "marca": "Apple"},
        {"tabela": "iPhone Kanguru", "tipo": "Kanguru Incell", "atacado": "190,00", "varejo": "215,00", "marca": "Apple"}
    ],
    "note 11 4g": [
        {"tabela": "Varejo & Atacado", "tipo": "Oled Com Aro", "atacado": "160,00", "varejo": "180,00", "marca": "Xiaomi"},
        {"tabela": "Varejo & Atacado", "tipo": "Incell", "atacado": "75,00", "varejo": "90,00", "marca": "Xiaomi"}
    ],
    "note 11s": [
        {"tabela": "Varejo & Atacado", "tipo": "Oled Com Aro", "atacado": "160,00", "varejo": "180,00", "marca": "Xiaomi"},
        {"tabela": "Telas Nacionais", "tipo": "OLED", "atacado": "140,00", "varejo": "140,00", "marca": "Xiaomi"}
    ],
    "note 11 pro": [
        {"tabela": "Varejo & Atacado", "tipo": "Oled Sem Aro", "atacado": "165,00", "varejo": "185,00", "marca": "Xiaomi"},
        {"tabela": "Varejo & Atacado", "tipo": "Incell", "atacado": "95,00", "varejo": "115,00", "marca": "Xiaomi"}
    ],
    "moto g22": [
        {"tabela": "Varejo & Atacado", "tipo": "Incell Sem Aro", "atacado": "58,00", "varejo": "70,00", "marca": "Motorola"},
        {"tabela": "Varejo & Atacado", "tipo": "Incell Com Aro", "atacado": "73,00", "varejo": "85,00", "marca": "Motorola"}
    ],
    "sm a01": [
        {"tabela": "Telas Nacionais", "tipo": "Nacional Com Aro", "atacado": "100,00", "varejo": "115,00", "marca": "Samsung"}
    ],
    "sm a03s": [
        {"tabela": "Telas Nacionais", "tipo": "Nacional Com Aro", "atacado": "105,00", "varejo": "120,00", "marca": "Samsung"}
    ],
    "sm a15": [
        {"tabela": "Telas Nacionais", "tipo": "Vivid Com Aro", "atacado": "135,00", "varejo": "150,00", "marca": "Samsung"}
    ],
    "hot 11": [
        {"tabela": "Telas Nacionais", "tipo": "Nacional Com Aro", "atacado": "100,00", "varejo": "115,00", "marca": "Infinix"}
    ],
    "realme c53": [
        {"tabela": "Telas Nacionais", "tipo": "Nacional Com Aro", "atacado": "105,00", "varejo": "120,00", "marca": "Realme"}
    ]
}

# 4. Barra Lateral (Sidebar)
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/4712/4712027.png", width=70)
    st.title("Painel de Consulta de Peças")
    
    st.markdown("### 📱 WhatsApp Comercial")
    st.markdown(f"**[{WHATSAPP_FORMATADO}](https://wa.me/{NUMERO_WHATSAPP})**")
    st.write("---")
    
    filtro_marca = st.selectbox(
        "🎯 Filtrar por Marca:",
        ["Todas", "Apple", "Motorola", "Samsung", "Xiaomi", "Realme", "Infinix"]
    )
    st.write("---")
    
    if st.button("🗑️ Limpar Histórico do Chat"):
        st.session_state.messages = [
            {"role": "assistant", "content": f"Olá! Sou o assistente virtual do estoque. Digite o modelo de tela ou tecnologia que deseja consultar:"}
        ]
        st.rerun()
        if st.button("🌙 Modo Escuro" if not st.session_state.modo_escuro else "☀️ Modo Claro"):
            st.session_state.modo_escuro = not st.session_state.modo_escuro
            st.rerun()
        if st.button("🌙 Modo Escuro" if not st.session_state.modo_escuro else "☀️ Modo Claro"):
            st.session_state.modo_escuro = not st.session_state.modo_escuro
            st.rerun()

    

    st.write("---")
    st.markdown("**Desenvolvedor:** Fernando Vinícius")
    st.markdown("**Formação:** ADS (3º / 4º Semestre)")
    st.info("💡 **Exemplos de busca:** 'iPhone 11', 'OLED', 'Incell', 'Moto G22'")

# 5. Cabeçalho
st.markdown('<p class="main-header">🤖 Sistema de Consulta de Peças</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Central de Atendimento Inteligente - Consulta de Peças e Atendimento Direct</p>', unsafe_allow_html=True)
st.markdown('<p class="project-info">Consulta de Peças e Atendimento Direct, criado com Python e Streamlit. Bot gratuito e de código aberto, desenvolvido por Fernando Vinícius.</p>', unsafe_allow_html=True)

# Banner de Contato em Destaque
st.markdown(f'<div class="contato-destaque">📲 Atendimento WhatsApp: <strong>{WHATSAPP_FORMATADO}</strong></div>', unsafe_allow_html=True)

# 6. Motor de Busca Flexível e Inteligente
def realizar_busca(texto_cliente, marca_filtrada):
    busca = texto_cliente.strip().lower()
    busca_sem_espaco = busca.replace(" ", "")
    resultados = []
    
    for modelo, opcoes in CATALOGO.items():
        modelo_limpo = modelo.replace(" ", "")
        
        for opcao in opcoes:
            # Aplica filtro de marca se selecionado na Sidebar
            if marca_filtrada != "Todas" and marca_filtrada.lower() not in opcao["marca"].lower():
                continue
            
            # Verifica correspondência por modelo, marca, tecnologia/tipo ou tabela
            if (busca_sem_espaco in modelo_limpo or 
                modelo_limpo in busca_sem_espaco or 
                busca in opcao["tipo"].lower() or 
                busca in opcao["tabela"].lower() or
                busca in opcao["marca"].lower()):
                
                resultados.append((modelo.upper(), opcao))
                
    if not resultados:
        return f"❌ Desculpe, não encontrei nenhuma peça correspondente no estoque atual. Entre em contato direto pelo WhatsApp **{WHATSAPP_FORMATADO}** para consultar encomendas especiais."
        
    resposta_html = f"📢 <strong>FORAM ENCONTRADAS {len(resultados)} OPÇÃO(ÕES) NO ESTOQUE:</strong><br><br>"
    
    for modelo, dados in resultados:
        texto_wa = f"Olá! Gostaria de verificar a disponibilidade da tela {modelo} ({dados['tipo']}) no valor de R$ {dados['varejo']}."
        link_wa = f"https://wa.me/{NUMERO_WHATSAPP}?text={urllib.parse.quote(texto_wa)}"
        
        card = (
            f'<div class="produto-card">'
            f'<strong>📱 {modelo}</strong> ({dados["marca"]})<br>'
            f'🔹 <strong>Qualidade:</strong> {dados["tipo"]}<br>'
            f'📦 <strong>Tabela:</strong> {dados["tabela"]}<br>'
            f'💰 <strong>Atacado:</strong> R$ {dados["atacado"]} | 💵 <strong>Varejo:</strong> R$ {dados["varejo"]}<br>'
            f'<a href="{link_wa}" target="_blank" class="btn-whatsapp">📲 Encomendar no WhatsApp ({WHATSAPP_FORMATADO})</a>'
            f'</div>'
        )
        resposta_html += card
        
    return resposta_html

# 7. Gerenciamento do Chat (Session State)

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": f"Oi! Seja bem-vindo ao sistema de consulta. Qual celular você está consertando hoje? (ou fale conosco no {WHATSAPP_FORMATADO}):"}
    ]
if "modo escuro" not in st.session_state:
    st.session_state["modo escuro"] = False

for message in st.session_state.messages:
    avatar_icon = "🤖" if message["role"] == "assistant" else "👤"
    with st.chat_message(message["role"], avatar=avatar_icon):
        if message["role"] == "assistant":
            st.markdown(message["content"], unsafe_allow_html=True)
        else:
            st.markdown(message["content"])

# 8. Entrada do Usuário
if prompt := st.chat_input("Digite o modelo de tela ou tecnologia (Ex: iPhone 11, Incell, Moto G)..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)

    with st.chat_message("assistant", avatar="🤖"):
        resposta = realizar_busca(prompt, filtro_marca)
        st.markdown(resposta, unsafe_allow_html=True)
    
    st.session_state.messages.append({"role": "assistant", "content": resposta})
