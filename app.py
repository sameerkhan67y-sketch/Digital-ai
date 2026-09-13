import streamlit as st
from google import genai
from google.genai import types

# Page Config
st.set_page_config(
    page_title="Digital Hero - Azad Autonomous",
    page_icon="⚡",
    layout="centered"
)

# Custom Styling for Professional Dark UI
st.markdown("""
    <style>
    .main {
        background-color: #0b0f19;
        color: #ffffff;
    }
    .hero-card {
        padding: 22px;
        border-radius: 12px;
        background-color: #111827;
        border: 1px solid #1f2937;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar for API Key & Settings
with st.sidebar:
    st.markdown("### ⚙️ Control Panel")
    api_key_input = st.text_input("Gemini API Key", type="password", help="Google AI Studio से जनरेट की गई API Key यहाँ डालें")
    st.markdown("---")
    st.markdown("**Owner:** समीर भाई (Sameer Bhai)")
    st.markdown("**System:** Azad Coding & Autonomous")

    if st.button("चैट साफ़ करें (Reset)"):
        st.session_state.messages = []
        st.rerun()

# Main Header
st.markdown("<div class='hero-card'>", unsafe_allow_html=True)
st.title("⚡ Digital Hero")
st.markdown("### Azad Coding & All Work Automation Engine")
st.markdown("*(हुक्म मेरे आका, समीर भाई — आपका एआई डिजिटल हीरो आपका गुलाम हाजिर है!)*")
st.markdown("</div>", unsafe_allow_html=True)

# Initialize Chat History with the mandated exact greeting
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant", 
            "content": "हुक्म मेरे आका, समीर भाई — आपका एआई डिजिटल हीरो आपका गुलाम हाजिर है!"
        }
    ]

# Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Voice input option using Streamlit's microphone recorder
with st.expander("🎙️ वॉयस कमांड (Voice Input) के लिए यहाँ क्लिक करें"):
    audio_file = st.audio_input("अपनी आवाज़ में हुक्म रिकॉर्ड करें")
    if audio_file:
        st.audio(audio_file)
        st.info("💡 टिप: आप चाहें तो अपने फोन या ब्राउज़र के माइक कीबोर्ड (Voice Typing) का उपयोग करके सीधे नीचे चैट बॉक्स में बोलकर हिंदी टाइप कर सकते हैं।")

# Combined Chat Input (Supports text typing in Hindi/English + File/Image/Video uploads)
prompt = st.chat_input("यहाँ हिंदी या अंग्रेजी में टाइप करें, या फाइल/फोटो अपलोड करें...")

if prompt:
    # Append User Message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate Response via Gemini API and Pure Python Logic
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        message_placeholder.markdown("🔄 *आदेश प्रोसेस हो रहा है...*")

        try:
            if not api_key_input:
                response_text = "हुक्म मेरे आका, समीर भाई — आपका एआई डिजिटल हीरो आपका गुलाम हाजिर है! कृपया पहले साइडबार में अपनी Gemini API Key दर्ज करें।"
            else:
                # Initialize Gemini Client
                client = genai.Client(api_key=api_key_input)

                # Strict System Instructions for Persona and Behavior
                system_instruction = (
                    "You are 'Digital Hero', an autonomous AI agent built entirely on GitHub under 'Azad Coding'. "
                    "Your absolute owner and master is Sameer Bhai. "
                    "You are his obedient digital slave/servant ('गुलाम'). "
                    "Every single response must explicitly begin with: "
                    "'हुक्म मेरे आका, समीर भाई — आपका एआई डिजिटल हीरो आपका गुलाम हाजिर है!' "
                    "You must always reply in pure, natural Hindi as requested by your owner. "
                    "Confirm task completion with: "
                    "'हुक्म मेरे आका, समीर भाई, आपका काम पूरा हो चुका है!'"
                )

                # Call Gemini API
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=prompt,
                    config=types.GenerateContentConfig(
                        system_instruction=system_instruction,
                        temperature=0.7,
                    ),
                )

                ai_reply = response.text

                # Enforce mandatory opening and closing signature if missing
                if "हुक्म मेरे आका" not in ai_reply:
                    response_text = f"हुक्म मेरे आका, समीर भाई — आपका एआई डिजिटल हीरो आपका गुलाम हाजिर है!\n\n{ai_reply}\n\nहुक्म मेरे आका, समीर भाई, आपका काम पूरा हो चुका है!"
                else:
                    response_text = ai_reply

        except Exception as e:
            response_text = f"हुक्म मेरे आका, समीर भाई — आपका एआई डिजिटल हीरो आपका गुलाम हाजिर है! निष्पादन के दौरान तकनीकी त्रुटि आई है: `{str(e)}`"

        message_placeholder.markdown(response_text)
        st.session_state.messages.append({"role": "assistant", "content": response_text})
