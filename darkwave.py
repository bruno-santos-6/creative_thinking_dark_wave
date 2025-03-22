import streamlit as st
from datetime import datetime, timedelta
import time

st.set_page_config(
    page_title="DarkWave",
    page_icon="🌊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: #FAFAFA; }
    .css-18e3th9 { padding: 2rem 5rem; }
    .plan-column { 
        background-color: #1F1F1F; 
        border-radius: 10px; 
        padding: 2rem; 
        margin: 1rem;
        transition: transform 0.2s;
    }
    .plan-column:hover { transform: scale(1.05); }
    .highlight { border: 2px solid #7C4DFF; }
    .step-box { 
        background-color: #1F1F1F;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    </style>
    """, unsafe_allow_html=True)

if 'step' not in st.session_state:
    st.session_state.step = 1

st.title("🌊 DarkWave")
st.markdown("### De 0 a 10k seguidores em 30 dias - Automatização Total")

if st.session_state.step == 1:
    with st.form("niche_form"):
        st.markdown("## Passo 1/4 - Escolha seu Nicho")
        niche = st.selectbox(
            "Selecione seu nicho principal:",
            ["Finanças Pessoais", "Fitness", "Beleza", "Tecnologia", "Games", "Empreendedorismo"],
            index=0
        )
        if st.form_submit_button("Próximo →"):
            st.session_state.step = 2

elif st.session_state.step == 2:
    with st.form("profile_form"):
        st.markdown("## Passo 2/4 - Configuração do Perfil")
        st.info("💡 Se o nome de usuário não estiver disponível, criaremos uma variação relacionada ao seu nicho")

        username = st.text_input("Escolha seu nome de usuário:")
        if st.form_submit_button("Próximo →"):
            st.session_state.step = 3

elif st.session_state.step == 3:
    with st.form("upload_form"):
        st.markdown("## Passo 3/4 - Aquecimento do Perfil")
        st.warning("⚠️ Para evitar bloqueios, precisamos de:")

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### 📸 7 Fotos do seu dia-a-dia")
            photos = st.file_uploader("Carregue fotos:",
                                      type=["png", "jpg"],
                                      key="photos",
                                      help="Fotos casuais como selfies, atividades diárias",
                                      accept_multiple_files=True)

        with col2:
            st.markdown("### 🎥 7 Vídeos curtos (5-15 segundos)")
            videos = st.file_uploader("Carregue vídeos:",
                                      type=["mp4", "mov"],
                                      key="videos",
                                      help="Vídeos casuais mostrando rotina",
                                      accept_multiple_files=True)

        submitted = st.form_submit_button("Próximo →")
        if submitted:
            if (photos and len(photos) >= 7) and (videos and len(videos) >= 7):
                st.session_state.step = 4
            else:
                st.error("⚠️ Você precisa carregar pelo menos 7 fotos e 7 vídeos!")

elif st.session_state.step == 4:
    st.markdown("## Passo 4/4 - Escolha seu Plano")

    col1, col2, col3 = st.columns(3)

    with col1:
        with st.container():
            st.markdown('<div class="plan-column">', unsafe_allow_html=True)
            st.markdown("### 🚀 Básico")
            st.markdown("#### R$ 20/mês")
            st.markdown("- 1 vídeo/dia\n- Sem agendamento\n- Suporte por email")
            if st.button("Escolher Plano Básico", key="basic"):
                st.session_state.selected_plan = "Básico"
                st.session_state.step = 5
            st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        with st.container():
            st.markdown('<div class="plan-column">', unsafe_allow_html=True)
            st.markdown("### 💎 Premium")
            st.markdown("#### R$ 30/mês")
            st.markdown("- 3 vídeos/dia\n- Sem agendamento\n- Suporte prioritário")
            if st.button("Escolher Plano Premium", key="premium"):
                st.session_state.selected_plan = "Premium"
                st.session_state.step = 5
            st.markdown('</div>', unsafe_allow_html=True)

    with col3:
        with st.container():
            st.markdown('<div class="plan-column highlight">', unsafe_allow_html=True)
            st.markdown("### 🏆 VIP")
            st.markdown("#### R$ 50/mês")
            st.markdown("- 3 vídeos/dia\n- Agendamento inteligente\n- Prioridade máxima")
            if st.button("Escolher Plano VIP", key="vip"):
                st.session_state.selected_plan = "VIP"
                st.session_state.step = 5
            st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.step == 5:
    st.markdown(f"## 🚀 Configurando seu Plano {st.session_state.selected_plan}")

    progress_bar = st.progress(0)
    status_text = st.empty()

    steps = [
        ("Criando perfil no TikTok", 0.15),
        ("Criando perfil no Kwai", 0.10),
        ("Criando perfil no YouTube Shorts", 0.12),
        ("Configurando Instagram", 0.10),
        ("Atribuindo foto de perfil", 0.08),
        ("Escrevendo descrição", 0.05),
        ("Primeira postagem de aquecimento", 0.20)
    ]

    total_weight = sum(weight for _, weight in steps)
    current_progress = 0.0

    for step, weight in steps:
        status_text.markdown(f'<div class="step-box">⏳ {step}...</div>', unsafe_allow_html=True)

        increments = 100
        step_increment = weight / total_weight / increments

        for _ in range(increments):
            current_progress += step_increment
            progress_bar.progress(min(current_progress, 1.0))
            time.sleep(0.05)

        status_text.markdown(f'<div class="step-box">✅ {step} concluído!</div>', unsafe_allow_html=True)

    progress_bar.progress(1.0)
    st.balloons()
    st.success("🎉 Configuração completa! Perfil pronto para aquecimento.")

    st.markdown("## 📅 Agenda de Publicações")
    today = datetime.now()
    for day in range(7):
        with st.expander(f"Publicações para {today + timedelta(days=day)}"):
            st.markdown(f"**Vídeo {day + 1}:**")
            st.video("https://static.streamlit.io/examples/star.mp4")
            if st.button(f"🔄 Gerar nova versão - Dia {day + 1}"):
                st.success("Nova versão gerada com sucesso!")

st.markdown("---")
st.markdown("ℹ️ Suporte: contato@darkwave.ai | [Políticas de Privacidade](https://example.com)")