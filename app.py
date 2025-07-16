import streamlit as st

PHASES_PERSPECTIVES = {
    "Menstruation": {
        "description": "Elle traverse une phase de renouvellement, avec une énergie plus basse, besoin de calme et de douceur.",
        "ce_que_je_ressens": [
            "Fatigue et besoin de repos",
            "Sensibilité émotionnelle accrue",
            "Baisse de motivation pour les tâches exigeantes"
        ],
        "comment_elle_vit": [
            "Peut se sentir vulnérable ou fragile",
            "Besoin d’être écoutée sans jugement",
            "Souvent introspective et centrée sur soi"
        ],
        "comportement": [
            "Moins bavarde, plus réservée",
            "Recherche de moments calmes",
            "Moins d’enthousiasme apparent"
        ],
        "ce_que_je_peux_faire": [
            "Proposer du calme, de la patience et de l'écoute",
            "Respecter son besoin de repos ou de retrait",
            "Laisser les initiatives pro/perso à plus tard"
        ],
        "suggestions": [
            "Préparer une ambiance cosy (thé, lumière douce)",
            "Offrir un massage léger ou temps de détente",
            "Accepter que ce soit un moment plus lent"
        ]
    },
    "Folliculaire": {
        "description": "Elle est dans une phase ascendante d'énergie et créativité, pleine de projets et d'idées.",
        "ce_que_je_ressens": [
            "Curiosité renouvelée",
            "Envie de s'engager dans de nouvelles choses",
            "Optimisme et dynamisme"
        ],
        "comment_elle_vit": [
            "Sent une énergie nouvelle et motivante",
            "Excitée par les possibilités à venir",
            "S’ouvre plus facilement aux autres"
        ],
        "comportement": [
            "Plus communicative et enthousiaste",
            "Ouverte à de nouvelles expériences",
            "Prend des initiatives"
        ],
        "ce_que_je_peux_faire": [
            "Encourager ses projets et idées",
            "Participer à la planification avec elle",
            "Être disponible pour échanges créatifs"
        ],
        "suggestions": [
            "Proposer des activités stimulantes ensemble",
            "Écouter activement ses idées",
            "Soutenir ses envies d'apprentissage"
        ]
    },
    "Ovulation": {
        "description": "Phase d'énergie haute, sociabilité, confiance en soi et expressivité.",
        "ce_que_je_ressens": [
            "Envie de communiquer et de partager",
            "Confiance renforcée",
            "Charisme naturel"
        ],
        "comment_elle_vit": [
            "Se sent rayonnante et pleine d’assurance",
            "Éprouve un fort besoin de connexion sociale",
            "Motivée et énergique"
        ],
        "comportement": [
            "Plus extravertie et sociable",
            "Prend la parole volontiers en groupe",
            "Rayonne naturellement"
        ],
        "ce_que_je_peux_faire": [
            "S'engager dans des activités sociales avec elle",
            "Valoriser ses talents et opinions",
            "Participer à des projets collaboratifs"
        ],
        "suggestions": [
            "Organiser des sorties ou rencontres",
            "Faire des compliments sincères",
            "Soutenir ses initiatives sociales"
        ]
    },
    "Lutéale": {
        "description": "Elle entre dans une phase plus calme, réflexive, et orientée vers la finition.",
        "ce_que_je_ressens": [
            "Besoins d'organisation et de routine",
            "Moins d'envie de nouveautés",
            "Parfois irritabilité ou besoin d'espace"
        ],
        "comment_elle_vit": [
            "Peut ressentir un besoin de stabilité",
            "Sente une légère fatigue émotionnelle",
            "Souhaite conclure et boucler les choses"
        ],
        "comportement": [
            "Peut paraître plus distante ou réservée",
            "Cherche la stabilité et le confort",
            "Moins disponible socialement"
        ],
        "ce_que_je_peux_faire": [
            "Respecter son besoin de calme",
            "Aider à organiser ou boucler les dossiers",
            "Être patient si elle est plus réservée"
        ],
        "suggestions": [
            "Proposer des activités simples et efficaces",
            "Laisser de l'espace sans pression",
            "Offrir un soutien pratique (ex : aide ménagère)"
        ]
    }
}

def get_phase(day, cycle_length=28):
    if 1 <= day <= 5:
        return "Menstruation"
    elif 6 <= day <= 14:
        return "Folliculaire"
    elif 15 <= day <= 17:
        return "Ovulation"
    elif 18 <= day <= cycle_length:
        return "Lutéale"
    else:
        return "Inconnu"

st.title("🤝 Comprendre et accompagner selon le cycle")

cycle_length = st.slider("Durée moyenne du cycle de la personne (jours)", 21, 35, 28)

day = st.number_input("Jour actuel du cycle de la personne", min_value=1, max_value=cycle_length, value=1)

phase = get_phase(day, cycle_length)

info = PHASES_PERSPECTIVES.get(phase, None)

if info:
    st.subheader(f"Phase actuelle : {phase}")
    st.write(info["description"])

    st.markdown("### Ce qu'elle peut ressentir / vivre")
    for item in info["ce_que_je_ressens"]:
        st.write(f"- {item}")

    st.markdown("### Comment elle vit cette phase de l’intérieur")
    for item in info["comment_elle_vit"]:
        st.write(f"- {item}")

    st.markdown("### Comment ça se traduit dans son comportement")
    for item in info["comportement"]:
        st.write(f"- {item}")

    st.markdown("### Ce que je peux faire pour la soutenir")
    for item in info["ce_que_je_peux_faire"]:
        st.write(f"- {item}")

    st.markdown("### Suggestions d'activités ou gestes adaptés")
    for item in info["suggestions"]:
        st.write(f"- {item}")
else:
    st.warning("Jour du cycle inconnu, veuillez vérifier la valeur entrée.")
