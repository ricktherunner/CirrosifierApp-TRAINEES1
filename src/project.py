import streamlit as st

def app():
    st.markdown(
    """
    <style>
        header {
            text-align: center;
        }
        div[data-testid="column"]
        {
            text-align: center;
            justify-content: center;
        }
        [data-testid="column"] [data-testid=stImage] {
                text-align: center;
                display: flex;
                align-items: center;
                justify-content: center;
                margin-left: auto;
                margin-right: auto;
                width: 100%;
        }
        .container1 {
            border: 2px solid #3498db;
            border-radius: 8px;
            padding: 10px;
            margin-bottom: 20px;
        }
        .container2 {
            border: 2px solid #a60d4e;
            border-radius: 8px;
            padding: 10px;
            margin-bottom: 20px;
        }
        .git:hover {
            border: 1px solid white;
            border-radius: 30px;
            box-shadow: 0 0 2px rgba(255,255,255, 0.6);
        }
    </style>
    """,unsafe_allow_html=True
    )

    st.markdown("<h1 style='text-align: center;'>‎ ‎ ‎ ‎ ‎ ‎ ‎ Equipe do Cirrosifier</h1>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    blank1, c1, c2, blank2 = st.columns([2,2,2,2], gap="small")
    with c1:
        st.markdown("""
                    <div class='container2'>Davi Ribeiro<br>
                    <a href='https://github.com/davirpp'><img class='git' src='https://raw.githubusercontent.com/ricktherunner/CirrosifierApp-TRAINEES1/feature/rework/img/git2.png' style='width:42px;height:42px;' alt='GitHub'></a>
                    <br>
                    Diretor
                    """, unsafe_allow_html=True)
    with c2:
        st.markdown("""
                    <div class='container2'>Rodrigo Veríssimo<br>
                    <a href='https://github.com/rodrigo0567'><img class='git' src='https://raw.githubusercontent.com/ricktherunner/CirrosifierApp-TRAINEES1/feature/rework/img/git2.png' style='width:42px;height:42px;' alt='GitHub'></a>
                    <br>
                    Líder
                    """, unsafe_allow_html=True)
    
    c3, c4, c5, c6, c7 = st.columns([2,2,2,2,2], gap="small")
    with c3:
        st.markdown("""
                    <div class='container1'>Gabriele Targino<br>
                    <a href='https://github.com/gabitargino'><img class='git' src='https://raw.githubusercontent.com/ricktherunner/CirrosifierApp-TRAINEES1/feature/rework/img/git.png' style='width:42px;height:42px;' alt='GitHub'></a>
                    <br>
                    Membro
                    """, unsafe_allow_html=True)
    with c4:
        st.markdown("""
                    <div class='container1'>Joyce Ribeiro<br>
                    <a href='https://github.com/Joyce-Ribeiro'><img class='git' src='https://raw.githubusercontent.com/ricktherunner/CirrosifierApp-TRAINEES1/feature/rework/img/git.png' style='width:42px;height:42px;' alt='GitHub'></a>
                    <br>
                    Membro
                    """, unsafe_allow_html=True)
    with c5:
        st.markdown("""
                    <div class='container1'>Luis Henrique<br>
                    <a href='https://github.com/luyluish'><img class='git' src='https://raw.githubusercontent.com/ricktherunner/CirrosifierApp-TRAINEES1/feature/rework/img/git.png' style='width:42px;height:42px;' alt='GitHub'></a>
                    <br>
                    Membro
                    """, unsafe_allow_html=True)
    with c6:
        st.markdown("""
                    <div class='container1'>Pedro Henrique<br>
                    <a href='https://github.com/ricktherunner'><img class='git' src='https://raw.githubusercontent.com/ricktherunner/CirrosifierApp-TRAINEES1/feature/rework/img/git.png' style='width:42px;height:42px;' alt='GitHub'></a>
                    <br>
                    Membro
                    """, unsafe_allow_html=True)
    with c7:
        st.markdown("""
                    <div class='container1'>Rafael Henrique<br>
                    <a href='https://github.com/rafaelhenrique-ra'><img class='git' src='https://raw.githubusercontent.com/ricktherunner/CirrosifierApp-TRAINEES1/feature/rework/img/git.png' style='width:42px;height:42px;' alt='GitHub'></a>
                    <br>
                    Membro
                    """, unsafe_allow_html=True)

    st.markdown("---")

    st.header("Sobre a Motivação e o Desenvolvimento")
    st.markdown("""
                O projeto tem como tema a cirrose pois durante a busca por datasets o Liver Cirrhosis Stage Classification foi o que melhor se encaixou com os nossos requisitos, fazer uma análise de dados (EDA) e a aplicação de modelos de machine learning. Ainda, a cirrose é a doença colestática (em outras palavras, doença que afeta o fígado) mais comum do Brasil, então ficamos interessados em saber como os indicadores da doença se comportam.

                Para saber mais sobre como o trabalho foi desenvolvido, as tecnologias utilizadas e as conclusões feitas, publicamos um artigo no Medium explicando tudo detalhadamente. O projeto também conta com um repositório no GitHub com a EDA e as aplicações dos modelos de classificação.

                Este site faz parte de um projeto da TAIL (Technology and Artificial Intelligence League), uma liga estudantil da UFPB (Universidade Federal da Paraíba) formada, como o nome sugere, por amantes da tecnologia e da Inteligência Artificial.
                """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.header("Links Importantes")
    c8, c9, c10 = st.columns([2,2,2], gap="small")
    
    with c8:
        st.image("img/medium_logo.png")
        st.markdown("<a href='https://medium.com/@joyribeirogxavier/fff3a577da2f'>Artigo do Medium</a>", unsafe_allow_html=True)
    with c9:
        st.image("img/github_logo.png")
        st.markdown("<a href='https://github.com/rodrigo0567/Trainees1-PFR'>Repositório no GitHub</a>", unsafe_allow_html=True)
    with c10:
        st.image("img/tail_logo.png")
        st.markdown("<a href='https://tail-tech.com'>Site da TAIL</a>", unsafe_allow_html=True)