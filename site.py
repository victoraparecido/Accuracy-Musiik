
    # Gênero
    generos_favoraveis = [
        "Pop",
        "Hip-Hop",
        "Rap",
        "R&B",
        "Eletrônica",
        "Funk Brasileiro"
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

if st.button("🚀 ANALISAR MÚSICA"):

    score = gerar_resultado()

    # CLASSIFICAÇÃO
    if score >= 80:
        categoria = "🔥 Alto potencial de popularidade"
    elif score >= 60:
        categoria = "🟢 Bom potencial de popularidade"
    elif score >= 40:
        categoria = "🟡 Potencial moderado"
    else:
        categoria = "🔵 Potencial baixo"

    # RESULTADO
    st.subheader("📈 Resultado da análise")
    st.metric("Potencial de popularidade", f"{score}/100")
    st.success(categoria)

    # MÉTRICAS
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

    # DETALHES
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
st.caption(
    "Accurcy Musiik © 2026 — "
    "Projeto acadêmico de Ciência de Dados e Machine Learning"
)
