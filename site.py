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
            background:
                radial-gradient(ellipse at 50% 28%, rgba(145, 76, 220, .32), transparent 43%),
                linear-gradient(135deg, #2b0756 0%, #54118d 52%, #1d0339 100%);
            color: #ffffff;
        }
        #MainMenu, footer, header { visibility: hidden; }
        [data-testid="stSidebar"] { display: none; }
        .block-container {
            max-width: 960px;
            padding-top: 4vh;
            padding-bottom: 1.5rem;
        }
        .splash-wrap {
            min-height: 60vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            text-align: center;
            animation: splash-in .8s ease-out both;
        }
        .splash-art {
            width: min(330px, 68vw);
            margin-bottom: 8px;
            filter: drop-shadow(0 18px 24px rgba(12, 0, 30, .30));
            animation: cassette-float 4s ease-in-out infinite;
        }
        .splash-eyebrow {
            display: inline-block;
            color: #d8baff;
            font-size: .72rem;
            font-weight: 750;
            letter-spacing: .24em;
            text-transform: uppercase;
            margin: 0 0 12px;
        }
        .splash-title {
            color: #ffffff;
            font-size: clamp(2.25rem, 5vw, 3.55rem);
            font-weight: 850;
            letter-spacing: -.06em;
            line-height: 1.02;
            margin: 0 0 14px;
            text-shadow: 0 5px 30px rgba(14, 0, 35, .25);
        }
        .splash-title span { color: #d7b4ff; }
        .splash-subtitle {
            color: #eee3ff;
            font-size: clamp(.98rem, 2vw, 1.08rem);
            max-width: 490px;
            line-height: 1.7;
            margin: 0 auto;
        }
        .splash-points {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 9px;
            margin-top: 22px;
        }
        .splash-points span {
            color: #f3eaff;
            border: 1px solid rgba(224, 195, 255, .27);
            background: rgba(255, 255, 255, .07);
            border-radius: 999px;
            padding: 7px 12px;
            font-size: .76rem;
            letter-spacing: .02em;
        }
        .splash-note {
            color: #c9a3f7;
            font-size: .68rem;
            font-weight: 700;
            letter-spacing: .22em;
            text-transform: uppercase;
            margin-top: 24px;
        }
        [data-testid="stProgressBar"] { margin-top: 5px; }
        [data-testid="stProgressBar"] > div > div {
            background: linear-gradient(90deg, #cba1ff, #f1dfff);
        }
        .stButton > button {
            width: 100%; border: 1px solid #d4cddd; border-radius: 999px;
            padding: 13px 24px; background: #d4c9e4; color: #383247;
            font-size: 1rem; font-weight: 700;
            box-shadow: 0 8px 20px rgba(72, 61, 91, .08);
            transition: transform .2s ease, background .2s ease;
        }
        .stButton > button:hover {
            background: #c9bbdc; color: #30283f; border-color: #c9bbdc;
            transform: translateY(-2px);
        }
        @keyframes splash-in {
            from { opacity: 0; transform: translateY(14px); }
            to { opacity: 1; transform: translateY(0); }
        }
        @keyframes cassette-float {
            0%, 100% { transform: translateY(0) rotate(-1deg); }
            50% { transform: translateY(-7px) rotate(1deg); }
        }
        @media (prefers-reduced-motion: reduce) {
            .splash-wrap, .splash-art { animation: none; }
        }
        @media (max-width: 600px) {
            .block-container { padding-top: 2vh; }
            .splash-wrap { min-height: 57vh; }
            .splash-art { width: min(290px, 78vw); }
            .splash-points { gap: 6px; margin-top: 17px; }
        }
    </style>

    <div class="splash-wrap">
      <svg class="splash-art" viewBox="0 0 360 280" role="img" aria-label="Fita cassete retrô detalhada com rolos, fita magnética e detalhes musicais">
        <defs>
          <linearGradient id="cassetteBody" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#8b35d1"/><stop offset=".55" stop-color="#6920ad"/><stop offset="1" stop-color="#451078"/></linearGradient>
          <linearGradient id="cassetteLabel" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#5c2789"/><stop offset="1" stop-color="#32104f"/></linearGradient>
          <linearGradient id="reel" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#f7eaff"/><stop offset="1" stop-color="#b69bd4"/></linearGradient>
        </defs>
        <ellipse cx="180" cy="244" rx="112" ry="14" fill="#130323" opacity=".35"/>
        <g transform="rotate(-5 180 137)">
          <rect x="48" y="51" width="264" height="166" rx="20" fill="#2b0647" opacity=".9"/>
          <rect x="43" y="43" width="264" height="166" rx="20" fill="url(#cassetteBody)" stroke="#c18af0" stroke-width="2"/>
          <rect x="53" y="53" width="244" height="146" rx="14" fill="none" stroke="#a35cdd" stroke-width="1.5"/>
          <circle cx="66" cy="66" r="4" fill="#8b6aa9"/><circle cx="284" cy="66" r="4" fill="#8b6aa9"/>
          <circle cx="66" cy="186" r="4" fill="#8b6aa9"/><circle cx="284" cy="186" r="4" fill="#8b6aa9"/>
          <rect x="73" y="64" width="204" height="52" rx="7" fill="url(#cassetteLabel)"/>
          <path d="M84 102h18l8-15 11 23 12-17 9 7h17l8-12 11 18 10-7h18l8-13 11 16h18" fill="none" stroke="#d9b5ff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
          <text x="175" y="78" fill="#f5eaff" font-size="7" text-anchor="middle" letter-spacing="2.5">SIDE A • STEREO</text>
          <circle cx="111" cy="151" r="30" fill="#7d5b9d" opacity=".22"/>
          <circle cx="111" cy="147" r="27" fill="url(#reel)" stroke="#8765a8" stroke-width="2.5"/>
          <circle cx="111" cy="147" r="19" fill="none" stroke="#9b7bb8" stroke-width="2" stroke-dasharray="3 3"/>
          <circle cx="111" cy="147" r="8" fill="#6a428a" stroke="#f4eaff" stroke-width="2"/>
          <path d="M111 128v11m0 16v11m-19-19h11m16 0h11" stroke="#9b7bb8" stroke-width="3" stroke-linecap="round"/>
          <circle cx="239" cy="147" r="27" fill="url(#reel)" stroke="#8765a8" stroke-width="2.5"/>
          <circle cx="239" cy="147" r="19" fill="none" stroke="#9b7bb8" stroke-width="2" stroke-dasharray="3 3"/>
          <circle cx="239" cy="147" r="8" fill="#6a428a" stroke="#f4eaff" stroke-width="2"/>
          <path d="M239 128v11m0 16v11m-19-19h11m16 0h11" stroke="#9b7bb8" stroke-width="3" stroke-linecap="round"/>
          <path d="M138 142q18-12 36 0t36 0v17q-18 12-36 0t-36 0z" fill="#4a246b" stroke="#8c69aa" stroke-width="1.5"/>
          <path d="M142 147q14-8 28 0t28 0" fill="none" stroke="#d5b3f6" stroke-width="2"/>
          <rect x="82" y="177" width="196" height="12" rx="4" fill="#b59bcf" opacity=".75"/>
          <rect x="151" y="177" width="58" height="12" rx="3" fill="#f6edff" stroke="#a98bc6" stroke-width="1"/>
          <path d="M159 180v6m7-6v6m7-6v6m7-6v6m7-6v6m7-6v6" stroke="#a98bc6" stroke-width="1.5"/>
          <path d="M91 124h16m-8-8v16M244 124h16m-8-8v16" stroke="#9e7cbd" stroke-width="1.5" opacity=".8"/>
        </g>
        <g fill="#e4caff" stroke="#e4caff" stroke-linejoin="round">
          <path d="M53 40V20l19-5v19a7 7 0 1 1-4-6V21l-10 3v17a7 7 0 1 1-5-1z" stroke="none"/>
          <path d="M298 56V40l15-4v16a6 6 0 1 1-4-5V42l-7 2v14a6 6 0 1 1-4-2z" stroke="none"/>
        </g>
        <circle cx="315" cy="105" r="3" fill="#c89aff"/><circle cx="38" cy="125" r="2.5" fill="#c89aff"/><path d="M315 126v12m-6-6h12" stroke="#c89aff" stroke-width="2" stroke-linecap="round"/>
      </svg>
      <div class="splash-eyebrow">Music · Data · Discovery</div>
      <div class="splash-title">Accuracy <span>Musiik</span></div>
      <p class="splash-subtitle">Explore o som por trás dos números. Descubra padrões musicais e conheça o potencial da sua faixa.</p>
      <div class="splash-points">
        <span>♫ Análise musical</span>
        <span>◈ Dados e padrões</span>
        <span>↗ Potencial da faixa</span>
      </div>
      <div class="splash-note">Uma nova forma de ouvir os dados</div>
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

    /* Fundo original em tons de roxo, sem vídeo */
    .stApp {
        background:
            radial-gradient(ellipse at 18% 18%, rgba(124, 35, 190, .30), transparent 38%),
            radial-gradient(ellipse at 82% 72%, rgba(91, 24, 150, .24), transparent 42%),
            linear-gradient(135deg, #100519 0%, #1b082b 48%, #09030f 100%) !important;
        background-attachment: fixed !important;
        color: white;
        overflow-x: hidden;
    }

    [data-testid="stAppViewContainer"] {
        background: transparent !important;
    }
    [data-testid="stHeader"] { background: transparent !important; }

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
# LOGO
# ============================================================

st.markdown('<div class="brand-mark">🎵 <span>Accuracy</span><strong>Musiik</strong></div>', unsafe_allow_html=True)

# ============================================================
# HERO
# ============================================================

st.title("Sua música. Novas possibilidades.")
st.markdown('<p class="hero-copy">Conheça os fatores da sua faixa e explore uma estimativa do seu potencial de popularidade.</p>', unsafe_allow_html=True)

# ============================================================
# INFORMAÇÕES DA MÚSICA
# ============================================================

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
