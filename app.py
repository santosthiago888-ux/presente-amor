
import streamlit as st
import plotly.graph_objects as go
import numpy as np
import time


# =========================================================
# CONFIGURAÇÕES DA PÁGINA
# =========================================================

st.set_page_config(
    page_title="Para você ❤️",
    page_icon="❤️",
    layout="wide"
)


# =========================================================
# PERSONALIZAÇÃO
# =========================================================

NOME = "Meu amor"


MENSAGEM_FINAL = """
Eu poderia simplesmente ter escrito:

**"Eu te amo."**

Mas achei que seria mais especial transformar
esse sentimento em algumas linhas de código.

Cada ponto, cada linha e cada equação
foram feitos pensando em você.

Porque no final...

# VOCÊ + EU = ❤️
"""


# =========================================================
# ESTILO DA PÁGINA
# =========================================================

st.markdown(
    """
    <style>

    .stApp {
        background:
            radial-gradient(
                circle at 20% 20%,
                #ffe4ec 0%,
                transparent 30%
            ),
            radial-gradient(
                circle at 80% 80%,
                #ffd6e5 0%,
                transparent 30%
            ),
            linear-gradient(
                135deg,
                #fff5f8,
                #ffe9f0
            );
    }

    .block-container {
        max-width: 1100px;
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    /* TÍTULOS */

    .titulo {
        text-align: center;
        font-size: 52px;
        font-weight: 800;
        color: #8e244d;
        margin-bottom: 10px;
    }

    .subtitulo {
        text-align: center;
        font-size: 21px;
        color: #6b3045;
        margin-bottom: 30px;
    }

    /* TEXTO GERAL */

    .stMarkdown {
        color: #5a2538;
    }

    /* CARTÃO DA MENSAGEM */

    .mensagem-final {
        background: rgba(255, 255, 255, 0.82);
        padding: 35px;
        border-radius: 30px;
        text-align: center;
        box-shadow: 0px 10px 40px rgba(194, 24, 91, 0.15);
        margin-top: 25px;
        margin-bottom: 25px;
    }

    /* RODAPÉ */

    .rodape {
        text-align: center;
        color: #8e536b;
        margin-top: 40px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# FUNÇÃO PARA CRIAR O GRÁFICO DAS LETRAS
# =========================================================

def criar_grafico_letras(elementos):

    fig = go.Figure()

    for elemento in elementos:

        fig.add_trace(
            go.Scatter(
                x=elemento["x"],
                y=elemento["y"],
                mode="lines",
                line=dict(
                    width=10
                ),
                showlegend=False
            )
        )

    fig.update_layout(

        height=500,

        xaxis=dict(
            visible=False,
            range=[-1, 23]
        ),

        yaxis=dict(
            visible=False,
            range=[-1, 6]
        ),

        showlegend=False,

        plot_bgcolor="rgba(255,255,255,0)",

        paper_bgcolor="rgba(255,255,255,0)",

        margin=dict(
            l=10,
            r=10,
            t=10,
            b=10
        )
    )

    return fig


# =========================================================
# FUNÇÃO PARA CRIAR O CORAÇÃO
# =========================================================

def criar_grafico_coracao():

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=CORACAO["x"],
            y=CORACAO["y"],
            mode="lines",
            line=dict(
                width=10
            ),
            showlegend=False
        )
    )

    fig.update_layout(

        height=550,

        xaxis=dict(
            visible=False,
            range=[-6, 6]
        ),

        yaxis=dict(
            visible=False,
            range=[-6, 6],
            scaleanchor="x",
            scaleratio=1
        ),

        showlegend=False,

        plot_bgcolor="rgba(255,255,255,0)",

        paper_bgcolor="rgba(255,255,255,0)",

        margin=dict(
            l=20,
            r=20,
            t=20,
            b=20
        )
    )

    return fig


# =========================================================
# LETRAS
# =========================================================

I = {
    "x": [0, 0],
    "y": [0, 5]
}


L = {
    "x": [2, 2, 4],
    "y": [5, 0, 0]
}


# O

t = np.linspace(
    0,
    2 * np.pi,
    300
)

O = {
    "x": 6 + 1.5 * np.cos(t),
    "y": 2.5 + 2.5 * np.sin(t)
}


# V

V = {
    "x": [9, 10.5, 12],
    "y": [5, 0, 5]
}


# E

E_vertical = {
    "x": [14, 14],
    "y": [0, 5]
}


E_top = {
    "x": [14, 16],
    "y": [5, 5]
}


E_middle = {
    "x": [14, 15.5],
    "y": [2.5, 2.5]
}


E_bottom = {
    "x": [14, 16],
    "y": [0, 0]
}


# U

U_left = {
    "x": [18, 18],
    "y": [5, 2]
}


t_u = np.linspace(
    np.pi,
    2 * np.pi,
    200
)


U_curve = {
    "x": 19.5 + 1.5 * np.cos(t_u),
    "y": 2.5 + 2.5 * np.sin(t_u)
}


U_right = {
    "x": [21, 21],
    "y": [2, 5]
}


# =========================================================
# EQUAÇÃO DO CORAÇÃO
# =========================================================

t_coracao = np.linspace(
    0,
    2 * np.pi,
    1000
)


x_coracao = (
    16 * np.sin(t_coracao) ** 3
)


y_coracao = (
    13 * np.cos(t_coracao)
    - 5 * np.cos(2 * t_coracao)
    - 2 * np.cos(3 * t_coracao)
    - np.cos(4 * t_coracao)
)


CORACAO = {
    "x": x_coracao / 3.5,
    "y": y_coracao / 3.5
}


# =========================================================
# CONTROLE DA TELA INICIAL
# =========================================================

if "inicio" not in st.session_state:

    st.session_state.inicio = False


# =========================================================
# TELA INICIAL
# =========================================================

if not st.session_state.inicio:

    st.markdown(
        "# ❤️"
    )

    st.markdown(
        f"# Oi, {NOME}!"
    )

    st.markdown(
        "### Eu fiz uma pequena coisa para você..."
    )

    st.write("")
    st.write("")

    st.markdown(
        """
        ### Não é nada muito complicado...

        São algumas linhas de Python,  
        matemática e um pouquinho de amor. ❤️

        Mas quero que você veja até o final.
        """
    )

    st.write("")
    st.write("")

    if st.button(
        "✨ Começar",
        use_container_width=True
    ):

        st.session_state.inicio = True

        st.rerun()


# =========================================================
# DECLARAÇÃO
# =========================================================

else:

    st.markdown(
        "# I LOVE U ❤️"
    )

    st.markdown(
        "### Construindo uma declaração..."
    )


    # -----------------------------------------------------
    # I
    # -----------------------------------------------------

    grafico = st.empty()

    grafico.plotly_chart(
        criar_grafico_letras(
            [I]
        ),
        use_container_width=True,
        key="grafico_i"
    )

    time.sleep(0.8)


    # -----------------------------------------------------
    # IL
    # -----------------------------------------------------

    grafico.plotly_chart(
        criar_grafico_letras(
            [I, L]
        ),
        use_container_width=True,
        key="grafico_il"
    )

    time.sleep(0.8)


    # -----------------------------------------------------
    # ILO
    # -----------------------------------------------------

    grafico.plotly_chart(
        criar_grafico_letras(
            [I, L, O]
        ),
        use_container_width=True,
        key="grafico_ilo"
    )

    time.sleep(0.8)


    # -----------------------------------------------------
    # ILOV
    # -----------------------------------------------------

    grafico.plotly_chart(
        criar_grafico_letras(
            [I, L, O, V]
        ),
        use_container_width=True,
        key="grafico_ilov"
    )

    time.sleep(0.8)


    # -----------------------------------------------------
    # ILOVE
    # -----------------------------------------------------

    grafico.plotly_chart(
        criar_grafico_letras(
            [
                I,
                L,
                O,
                V,
                E_vertical,
                E_top,
                E_middle,
                E_bottom
            ]
        ),
        use_container_width=True,
        key="grafico_ilove"
    )

    time.sleep(0.8)


    # -----------------------------------------------------
    # I LOVE U
    # -----------------------------------------------------

    grafico.plotly_chart(
        criar_grafico_letras(
            [
                I,
                L,
                O,
                V,
                E_vertical,
                E_top,
                E_middle,
                E_bottom,
                U_left,
                U_curve,
                U_right
            ]
        ),
        use_container_width=True,
        key="grafico_iloveu"
    )

    time.sleep(1.5)


    # =====================================================
    # TRANSIÇÃO PARA O CORAÇÃO
    # =====================================================

    st.markdown(
        "### Mas existe uma coisa que representa isso ainda melhor..."
    )

    time.sleep(1)


    # =====================================================
    # CORAÇÃO
    # =====================================================

    st.plotly_chart(
        criar_grafico_coracao(),
        use_container_width=True,
        key="grafico_coracao"
    )

    time.sleep(1)


    # =====================================================
    # MENSAGEM FINAL
    # =====================================================

    st.markdown(
        "## ❤️"
    )

    st.markdown(
        MENSAGEM_FINAL
    )

    st.markdown(
        "## ❤️ Eu te amo ❤️"
    )


    # =====================================================
    # EFEITO FINAL
    # =====================================================

    st.balloons()

    st.markdown(
        "Feito com Python 🐍 + matemática 📐 + amor ❤️"
    )
