import streamlit as st
import random
import time

# ============================================================
# CONFIGURAÇÃO DA PÁGINA
# ============================================================

st.set_page_config(
    page_title="Accuracy Musiik",
    page_icon="🎵",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# TELA DE ABERTURA (SPLASH SCREEN)
# Exibida na primeira abertura da sessão antes do site principal.
# ============================================================

if "site_started" not in st.session_state:
    st.session_state.site_started = False

if not st.session_state.site_started:
    st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(135deg, #3b087a 0%, #5b16a8 52%, #26004f 100%);
            color: #ffffff;
        }
        #MainMenu, footer, header { visibility: hidden; }
        [data-testid="stSidebar"] { display: none; }
        .block-container {
            max-width: 920px;
            padding-top: 7vh;
            padding-bottom: 2rem;
        }
        .splash-wrap {
            min-height: 65vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            text-align: center;
        }
        .splash-art {
            width: min(300px, 65vw);
            margin-bottom: 22px;
            filter: drop-shadow(0 12px 18px rgba(72, 61, 91, .10));
        }
        .splash-title {
            color: #ffffff;
            font-size: clamp(2.1rem, 5vw, 3.4rem);
            font-weight: 800;
            letter-spacing: -.055em;
            line-height: 1.05;
            margin: 0 0 12px;
        }
        .splash-subtitle {
            color: #e6d7ff;
            font-size: 1.05rem;
            max-width: 440px;
            line-height: 1.65;
            margin: 0 auto;
        }
        .splash-note {
            color: #c8a8ff;
            font-size: .78rem;
            letter-spacing: .18em;
            text-transform: uppercase;
            margin-top: 26px;
        }
        .stButton > button {
            width: 100%;
            border: 1px solid #d4cddd;
            border-radius: 999px;
            padding: 13px 24px;
            background: #d4c9e4;
            color: #383247;
            font-size: 1rem;
            font-weight: 700;
            box-shadow: 0 8px 20px rgba(72, 61, 91, .08);
            transition: transform .2s ease, background .2s ease;
        }
        .stButton > button:hover {
            background: #c9bbdc;
            color: #30283f;
            border-color: #c9bbdc;
            transform: translateY(-2px);
        }
    </style>

    <div class="splash-wrap">
      <svg class="splash-art" viewBox="0 0 320 260" role="img" aria-label="Ilustração minimalista de uma fita cassete musical">
        <ellipse cx="160" cy="224" rx="102" ry="13" fill="#d7d0e2"/>
        <g transform="rotate(-6 160 128)">
          <rect x="48" y="48" width="224" height="154" rx="22" fill="#c8b9dc"/>
          <rect x="58" y="58" width="204" height="134" rx="15" fill="#f3eff7" stroke="#b5a6ca" stroke-width="2"/>
          <rect x="74" y="73" width="172" height="56" rx="9" fill="#e4ddeb"/>
          <path d="M88 101h13l8-15 12 28 12-20 9 7h17l8-12 10 18 9-6h25" fill="none" stroke="#9c8bb8" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
          <circle cx="112" cy="153" r="24" fill="#c7b7d8" stroke="#9c8bb8" stroke-width="3"/>
          <circle cx="208" cy="153" r="24" fill="#c7b7d8" stroke="#9c8bb8" stroke-width="3"/>
          <circle cx="112" cy="153" r="8" fill="#f3eff7"/>
          <circle cx="208" cy="153" r="8" fill="#f3eff7"/>
          <rect x="139" y="139" width="42" height="27" rx="5" fill="#e4ddeb" stroke="#b5a6ca" stroke-width="2"/>
          <path d="M146 145v15m8-15v15m8-15v15m8-15v15" stroke="#b5a6ca" stroke-width="2" stroke-linecap="round"/>
          <circle cx="72" cy="72" r="3" fill="#b5a6ca"/>
          <circle cx="248" cy="72" r="3" fill="#b5a6ca"/>
          <circle cx="72" cy="178" r="3" fill="#b5a6ca"/>
          <circle cx="248" cy="178" r="3" fill="#b5a6ca"/>
        </g>
        <g fill="#a99ac0">
          <path d="M55 39v-14l17-4v14a6 6 0 1 1-4-5V17l-9 2v16a6 6 0 1 1-4-5z"/>
          <path d="M258 41v-12l14-3v12a5 5 0 1 1-4-4V24l-6 1v12a5 5 0 1 1-4-4z"/>
        </g>
      </svg>
      <div class="splash-title">Accuracy Musiik</div>
      <p class="splash-subtitle">Explore o som, descubra padrões e conheça o potencial da sua música.</p>
      <div class="splash-note">Music · Data · Discovery</div>
    </div>
    """, unsafe_allow_html=True)

    left, center, right = st.columns([1, 1.1, 1])
    with center:
        progress = st.progress(0, text="Preparando sua experiência musical...")
        for value in range(1, 101):
            time.sleep(0.025)
            progress.progress(value, text="Carregando o Accuracy Musiik...")
        st.session_state.site_started = True
        st.rerun()
    st.stop()

# ============================================================
# CSS
# ============================================================

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@500;600;700;800&family=Inter:wght@400;500;600;700;800&display=swap');

    /* Tipografia: personalidade underground nos títulos, leitura confortável no corpo */
    html, body, [class*="st-"] {
        font-family: 'Inter', 'Segoe UI', sans-serif !important;
    }
    h1, h2, h3, h4, .brand-mark, .splash-title {
        font-family: 'Barlow Condensed', 'Arial Narrow', sans-serif !important;
        font-weight: 700 !important;
        letter-spacing: .015em !important;
    }
    h1 { text-transform: uppercase; letter-spacing: .025em !important; }

    /* Fundo geral */
    .stApp {
        background: linear-gradient(
            135deg,
            #24004d 0%,
            #4b0b87 48%,
            #1b0038 100%
        );
        color: white;
    }

    /* Remove elementos padrão */
    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    header {
        visibility: hidden;
    }

    /* Espaçamento e hierarquia visual */
    .block-container {
        max-width: 1180px;
        padding-top: 2.8rem;
        padding-bottom: 4rem;
    }

    .brand-mark {
        display: flex;
        align-items: center;
        gap: 9px;
        margin: 0 0 2.4rem 0;
        color: #e8d7ff;
        font-size: 1.35rem;
        font-weight: 600;
        letter-spacing: -.025em;
    }
    .brand-mark strong { color: #ffffff; font-weight: 800; }

    h1 {
        text-align: center;
        color: #ffffff !important;
        font-size: clamp(2.1rem, 4vw, 3.1rem) !important;
        letter-spacing: -.04em;
        line-height: 1.15 !important;
        margin: 0 0 .9rem 0 !important;
    }

    .hero-copy {
        max-width: 680px;
        margin: 0 auto 3.2rem auto;
        color: #d8c5f2;
        text-align: center;
        font-size: 1.05rem;
        line-height: 1.8;
    }

    h2, h3 {
        color: #ffffff !important;
        letter-spacing: -.02em;
    }
    h2 { margin-top: 2.4rem !important; margin-bottom: .35rem !important; }
    h3 { margin-top: 2rem !important; margin-bottom: .35rem !important; }

    .stCaption, [data-testid="stCaptionContainer"] {
        color: #cbb8e5 !important;
        line-height: 1.65;
        margin-bottom: 1.2rem;
    }

    div[data-testid="stHorizontalBlock"] { gap: 1.25rem; }
    [data-testid="stDivider"] {
        margin: 1.5rem 0 2rem 0;
        opacity: .35;
    }
    [data-testid="stNumberInput"], [data-testid="stSelectbox"],
    [data-testid="stMultiSelect"], [data-testid="stRadio"],
    [data-testid="stFileUploader"] {
        margin-bottom: .8rem;
    }

    /* Inputs */
    .stSelectbox label,
    .stNumberInput label,
    .stMultiSelect label,
    .stRadio label,
    .stFileUploader label {
        color: #e5e1ec !important;
        font-weight: 600;
    }

    /* Botão */
    .stButton > button {
        width: 100%;
        border-radius: 12px;
        border: none;
        padding: 14px;
        background: linear-gradient(
            90deg,
            #7b3ff2,
            #a45cff
        );
        color: white;
        font-size: 17px;
        font-weight: 700;
        transition: 0.2s;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(140, 75, 255, 0.35);
    }


    /* Janela principal do site, com fundo sólido e sem animações decorativas. */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        background: linear-gradient(145deg, rgba(48, 5, 83, .98), rgba(27, 0, 49, .98));
        border: 1px solid rgba(210, 151, 255, .38) !important;
        border-radius: 24px !important;
        padding: 1.6rem 1.8rem !important;
        box-shadow: 0 12px 42px rgba(8, 0, 20, .32), inset 0 0 28px rgba(164, 76, 255, .10);
    }
    .stApp { background: radial-gradient(ellipse at top, #3d0870 0%, #1b0035 68%, #120022 100%); }

    .footer {
        text-align: center;
        margin-top: 50px;
        padding: 20px;
        color: #777184;
        font-size: 13px;
    }

</style>
""", unsafe_allow_html=True)


# ============================================================
# INFORMAÇÕES DA MÚSICA
# ============================================================
with st.container(border=True):

    st.subheader("🎧 Vamos conhecer sua faixa")
    st.caption("Comece pelos dados principais: ritmo, estilo musical e plataforma.")
    st.divider()

    # ============================================================
    # PRIMEIRA LINHA
    # ============================================================

    col1, col2, col3 = st.columns(3)

    with col1:
        bpm = st.number_input(
            "BPM",
            min_value=40,
            max_value=250,
            value=120,
            step=1,
            help="Batidas por minuto da música."
        )

    with col2:
        genero = st.selectbox(
            "Gênero musical",
            [
                # ROCK
                "Rock",
                "Rock Alternativo",
                "Hard Rock",
                "Punk Rock",
                "Indie Rock",
                "Pop Rock",
                "Grunge",
                "Rock Psicodélico",

                # POP
                "Pop",
                "Synthpop",
                "Electropop",
                "Dance Pop",
                "Indie Pop",
                "K-Pop",
                "J-Pop",
                "Pop Latino",

                # HIP-HOP / RAP
                "Hip-Hop",
                "Rap",
                "Trap",
                "Drill",
                "Boom Bap",
                "Gangsta Rap",
                "Conscious Rap",
                "Lo-fi Hip-Hop",

                # ELETRÔNICA
                "Eletrônica",
                "House",
                "Deep House",
                "Tech House",
                "Techno",
                "Trance",
                "Dubstep",
                "Drum & Bass",
                "EDM",
                "Future Bass",

                # JAZZ
                "Jazz",
                "Bebop",
                "Swing",
                "Smooth Jazz",
                "Jazz Fusion",
                "Free Jazz",

                # CLÁSSICA
                "Música Clássica",
                "Barroco",
                "Romântica",
                "Ópera",
                "Sinfônica",

                # BLUES
                "Blues",
                "Delta Blues",
                "Chicago Blues",
                "Electric Blues",
                "Blues Rock",

                # COUNTRY
                "Country",
                "Country Pop",
                "Bluegrass",
                "Outlaw Country",
                "Country Rock",

                # LATIN
                "Latin",
                "Reggaeton",
                "Salsa",
                "Bachata",
                "Merengue",
                "Latin Pop",

                # MÚSICA BRASILEIRA
                "Música Brasileira",
                "MPB",
                "Sertanejo",
                "Funk Brasileiro",
                "Pagode",
                "Samba",
                "Forró",
                "Bossa Nova",
                "Axé",

                # R&B / SOUL
                "R&B",
                "Contemporary R&B",
                "Neo Soul",
                "Soul",
                "Funk Soul",
                "Motown",

                # REGGAE
                "Reggae",
                "Dancehall",
                "Dub",
                "Ska",

                # METAL
                "Metal",
                "Heavy Metal",
                "Thrash Metal",
                "Death Metal",
                "Black Metal",
                "Metalcore",

                # FOLK
                "Folk",
                "Indie Folk",
                "Folk Rock",
                "Acoustic Folk",
                "Contemporary Folk",

                # GOSPEL
                "Gospel",
                "Contemporary Gospel",
                "Gospel Rock",
                "Gospel R&B",

                # OUTROS
                "Outro"
            ]
        )

    with col3:
        streaming = st.selectbox(
            "Streaming usado",
            [
                "Spotify",
                "YouTube Music",
                "Apple Music",
                "Amazon Music",
                "Deezer",
                "SoundCloud",
                "Outro"
            ]
        )

    # ============================================================
    # DURAÇÃO
    # ============================================================

    st.subheader("⏱️ Tempo de reprodução")
    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        minutos = st.number_input(
            "Minutos",
            min_value=0,
            max_value=20,
            value=3,
            step=1
        )

    with col2:
        segundos = st.number_input(
            "Segundos",
            min_value=0,
            max_value=59,
            value=30,
            step=1
        )

    duracao_segundos = (minutos * 60) + segundos

    # ============================================================
    # INSTRUMENTOS
    # ============================================================

    st.subheader("🎸 Elementos sonoros")
    st.caption("Marque os instrumentos e sons que fazem parte da faixa.")
    st.divider()

    instrumentos = st.multiselect(
        "Instrumentos utilizados",
        [
            "Piano",
            "Violão",
            "Guitarra",
            "Baixo",
            "Bateria",
            "Violino",
            "Saxofone",
            "Trompete",
            "Sintetizador",
            "Voz",
            "Ukulele",
            "Percussão",
            "Outro"
        ]
    )

    # ============================================================
    # CARACTERÍSTICAS
    # ============================================================

    st.subheader("🎛️ Detalhes da faixa")
    st.caption("Conte um pouco mais sobre a produção e as parcerias.")
    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        acustico = st.radio(
            "A música é acústica?",
            ["Sim", "Não"],
            horizontal=True
        )

    with col2:
        feat = st.radio(
            "Possui feat/parceria?",
            ["Sim", "Não"],
            horizontal=True
        )

    # ============================================================
    # ARQUIVO DE ÁUDIO
    # ============================================================

    st.subheader("🎵 Ouça a sua faixa")
    st.caption("Se quiser, envie um áudio para ouvir aqui. A previsão atual usa os dados preenchidos no formulário.")
    st.divider()

    arquivo_musica = st.file_uploader(
        "Escolha o arquivo de áudio",
        type=[
            "mp3",
            "wav",
            "m4a",
            "flac",
            "ogg"
        ],
        help="Formatos aceitos: MP3, WAV, M4A, FLAC e OGG."
    )

    if arquivo_musica is not None:

        st.success(
            f"Arquivo carregado: {arquivo_musica.name}"
        )

        st.audio(arquivo_musica)

        st.info(
            "A análise automática do áudio será integrada "
            "ao modelo de Machine Learning em uma próxima etapa."
        )

    # ============================================================
    # FUNÇÃO DE PREVISÃO
    # ============================================================

    def gerar_resultado():

        # --------------------------------------------------------
        # ATENÇÃO:
        # Esta função é apenas uma SIMULAÇÃO.
        # Depois iremos substituir pelo modelo real do TCC.
        # --------------------------------------------------------

        score = 50

        # BPM
        if 90 <= bpm <= 140:
            score += 10

        elif 70 <= bpm <= 160:
            score += 5

        else:
            score -= 3

        # Gênero
        generos_favoraveis = [
            "Pop",
            "Hip-Hop",
            "Rap",
            "R&B",
            "Eletrônica",
            "Funk"
        ]

        if genero in generos_favoraveis:
            score += 8

        # Duração
        if 150 <= duracao_segundos <= 240:
            score += 8

        elif 120 <= duracao_segundos <= 300:
            score += 4

        else:
            score -= 2

        # Instrumentos
        if len(instrumentos) >= 3:
            score += 5

        elif len(instrumentos) == 2:
            score += 3

        # Acústico
        if acustico == "Sim":
            score += 2

        # Feat
        if feat == "Sim":
            score += 5

        # Arquivo de áudio
        if arquivo_musica is not None:
            score += 3

        # Pequena variação aleatória
        score += random.randint(-5, 5)

        # Limita entre 0 e 100
        score = max(0, min(100, score))

        return score


    # ============================================================
    # BOTÃO ANALISAR
    # ============================================================

    st.write("")

    if st.button("🚀 Analisar potencial da faixa"):

        score = gerar_resultado()

        # --------------------------------------------------------
        # CLASSIFICAÇÃO
        # --------------------------------------------------------

        if score >= 80:
            categoria = "🔥 Alto potencial de popularidade"

        elif score >= 60:
            categoria = "🟢 Bom potencial de popularidade"

        elif score >= 40:
            categoria = "🟡 Potencial moderado"

        else:
            categoria = "🔵 Potencial baixo"

        # ========================================================
        # RESULTADO
        # ========================================================

        st.subheader("📈 Resultado da análise")
        st.metric("Potencial de popularidade", f"{score}/100")
        st.success(categoria)

        # ========================================================
        # MÉTRICAS
        # ========================================================

        st.write("")

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric("BPM", bpm)

        with col2:
            st.metric("Duração", f"{minutos}:{segundos:02d}")

        with col3:
            st.metric("Instrumentos", len(instrumentos))

        with col4:
            st.metric("Gênero", genero)

        # ========================================================
        # DETALHES
        # ========================================================

        st.write("")

        st.subheader("📊 Detalhes da análise")

        st.write(f"**Gênero:** {genero}")
        st.write(f"**Streaming:** {streaming}")
        st.write(f"**BPM:** {bpm}")
        st.write(f"**Duração:** {minutos}:{segundos:02d}")
        st.write(
            f"**Instrumentos:** "
            f"{', '.join(instrumentos) if instrumentos else 'Nenhum informado'}"
        )
        st.write(f"**Acústico:** {acustico}")
        st.write(f"**Feat/parceria:** {feat}")

        if arquivo_musica:
            st.write(f"**Arquivo:** {arquivo_musica.name}")
        else:
            st.write("**Arquivo:** Nenhum arquivo enviado")


    # ============================================================
    # RODAPÉ
    # ============================================================

    st.divider()
    st.caption("Accuracy Musiik © 2026 — Projeto acadêmico de Ciência de Dados e Machine Learning")
