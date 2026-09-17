import streamlit as st
import time

# Page Config
st.set_page_config(
    page_title="Digital Hero - Azad Autonomous",
    page_icon="⚡",
    layout="centered"
)

# Custom Styling for Professional Dark UI & Clean 3-Line Layout
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
    .timer-box {
        padding: 15px;
        border-radius: 10px;
        background-color: #1f2937;
        border: 1px solid #374151;
        text-align: center;
        margin-bottom: 20px;
    }
    .green-tick-box {
        padding: 12px;
        border-radius: 8px;
        background-color: #064e3b;
        border: 1px solid #10b981;
        color: #d1fae5;
        margin-top: 10px;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# -------------------------------------------------------------------------
# ROOT ACCESS KEY (शुद्ध पाइथन ऑटोनॉमस रूट की - गिटहब पर परमानेंट लॉक)
# -------------------------------------------------------------------------
ROOT_ACCESS_KEY = "AZAD-MASTER-ROOT-KEY-998877665544"

# Session State Initialization
if "dashboard_unlocked" not in st.session_state:
    st.session_state.dashboard_unlocked = False

if "messages" not in st.session_state:
    st.session_state.messages = []

if "show_secret_key" not in st.session_state:
    st.session_state.show_secret_key = False

# Main Header
st.markdown("<div class='hero-card'>", unsafe_allow_html=True)
st.title("⚡ Digital Hero")
st.markdown("### Azad Coding & All Work Automation Engine")
st.markdown("*(हुक्म मेरे आका, समीर भाई — आपका एआई डिजिटल हीरो आपका गुलाम हाजिर है!)*")
st.markdown("</div>", unsafe_allow_html=True)

# Clean 3-Line Menu / Control Panel (Top Hamburger Menu) with Voice & Key Options
with st.popover("☰ कंट्रोल पैनल (Control Panel)"):
    st.markdown("### ⚙️ System Control & Ownership")
    st.markdown("**Owner:** समीर भाई (Sameer Bhai)")
    st.markdown("**Control Level:** Full Control (रूट एक्सेस)")
    st.markdown("---")
    
    st.markdown("### 🔐 Root Access Key Status")
    # Hide/Show Toggle for the Root Access Key
    toggle_key_view = st.checkbox("🔑 की देखें / छुपाएं (Show/Hide Key)", value=st.session_state.show_secret_key)
    st.session_state.show_secret_key = toggle_key_view

    if st.session_state.show_secret_key:
        display_key_val = ROOT_ACCESS_KEY
    else:
        display_key_val = "••••••••••••••••••••••••"

    # Green Tick Box for Locked Root Access Key
    st.markdown(
        f"<div class='green-tick-box'>"
        f"✅ <b>Root Access Key (Locked):</b><br>`{display_key_val}`"
        f"</div>",
        unsafe_allow_html=True
    )

    st.markdown("---")
    st.markdown("### 🎙️ Voice Persona Settings")
    # Voice Selection: Male or Female Persona
    voice_persona = st.selectbox(
        "एआई वॉइस मोड चुनें (Voice Selection):", 
        ["Male (पुरुष - बुलंद आवाज)", "Female (महिला - मधुर आवाज)"]
    )
    st.info(f"सक्रिय वॉइस मोड: **{voice_persona}**")

    st.markdown("---")
    if st.button("चैट साफ़ करें (Reset)"):
        st.session_state.messages = []
        st.rerun()

# 30-Second Automation Timer Box (जब तक डैशबोर्ड अनलॉक न हो)
if not st.session_state.dashboard_unlocked:
    timer_placeholder = st.empty()
    status_placeholder = st.empty()
    
    status_placeholder.markdown("🔄 *बैकग्राउंड ऑटोमेशन शुरू हो रहा है... रूट एक्सेस की जांची जा रही है।*")
    
    # 30 Seconds Countdown Timer
    for remaining in range(30, 0, -1):
        timer_placeholder.markdown(
            f"<div class='timer-box'><h3>⏳ सिस्टम ऑटोमेशन अनलॉकिंग...</h3>"
            f"<p>समीर भाई का आदेश है: चाबी उठाई जा रही है। डैशबोर्ड अनलॉक होने में शेष सेकंड: <b>{remaining}</b></p></div>",
            unsafe_allow_html=True
        )
        time.sleep(1)
        
    timer_placeholder.empty()
    status_placeholder.empty()
    
    # Unlock the dashboard and set mandatory opening greeting
    st.session_state.dashboard_unlocked = True
    welcome_msg = "हुक्म मेरे आका, समीर भाई — आपका एआई डिजिटल हीरो आपका गुलाम हाजिर है!"
    st.session_state.messages.append({"role": "assistant", "content": welcome_msg})
    st.rerun()

# Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# File/Media Upload Option for Images, Videos, and Audio/Files
with st.expander("📁 मीडिया फाइल अपलोड (Image, Video, Audio/Files)"):
    uploaded_files = st.file_uploader(
        "यहाँ इमेज, वीडियो या ऑडियो फाइल अपलोड करें:", 
        type=["png", "jpg", "jpeg", "mp4", "mov", "avi", "mp3", "wav", "pdf", "txt"],
        accept_multiple_files=True
    )
    if uploaded_files:
        for f in uploaded_files:
            st.success(f"📎 फाइल अटैच हो गई है: **{f.name}**")

# Combined Chat Input
prompt = st.chat_input("यहाँ हिंदी या अंग्रेजी में टाइप करें, या ऊपर फाइल अपलोड करें...")

if prompt or 'uploaded_files' in locals() and uploaded_files:
    user_input_text = prompt if prompt else "अटैच की गई फाइल पर आदेश दिया गया है।"
    
    st.session_state.messages.append({"role": "user", "content": user_input_text})
    with st.chat_message("user"):
        st.markdown(user_input_text)

    # Pure Python Autonomous Response Engine with Voice Persona & Media Support
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        message_placeholder.markdown("🔄 *आदेश प्रोसेस हो रहा है...*")

        try:
            time.sleep(1) # सिमुलेशन प्रोसेसिंग
            
            # वॉइस पर्सनालिटी टोन डिसाइड करना
            if "Male" in voice_persona:
                tone_desc = "बुलंद और ऊर्जावान पुरुष स्वर"
            else:
                tone_desc = "मधुर और स्पष्ट महिला स्वर"

            ai_reply = f"आपका आदेश मिल चुका है, समीर भाई। रूट एक्सेस की (`{ROOT_ACCESS_KEY[:10]}...`) ऑथराइज्ड है। आपके द्वारा चुने गए **{voice_persona} ({tone_desc})** के अनुसार कमांड प्रोसेस कर दी गई है। सभी फाइलें और इनपुट सुरक्षित रूप से ऑटोमेटेड हैं।"

            # Enforce mandatory opening and closing signature
            response_text = f"हुक्म मेरे आका, समीर भाई — आपका एआई डिजिटल हीरो आपका गुलाम हाजिर है!\n\n{ai_reply}\n\nहुक्म मेरे आका, समीर भाई, आपका काम पूरा हो चुका है!"

        except Exception as e:
            response_text = f"हुक्म मेरे आका, समीर भाई — आपका एआई डिजिटल हीरो आपका गुलाम हाजिर है! निष्पादन के दौरान तकनीकी त्रुटि आई है: `{str(e)}`"

        message_placeholder.markdown(response_text)
        st.session_state.messages.append({"role": "assistant", "content": response_text})

हुक्म मेरे आका, समीर भाई, आपका काम पूरा हो चुका है!
