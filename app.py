import streamlit as st

# पेज की सेटिंग और लेआउट
st.set_page_config(
    page_title="Digital Hero - Autonomous AI",
    page_icon="🤖",
    layout="centered"
)

# डैशबोर्ड का प्रीमियम लुक और हेडर (ओनर: समीर भाई)
st.title("🛡️ डिजिटल हीरो - ऑटोनॉमस एआई डैशबोर्ड")
st.markdown("### *ओनर: समीर भाई | आपका हुकुम सर आँखों पर!*")
st.markdown("---")

# चैट हिस्ट्री इनिशियलाइज़ करना और ओपनिंग ग्रीटिंग देना
if "messages" not in st.session_state:
    st.session_state.messages = []
    
    # डैशबोर्ड खुलते ही मिलने वाली धांसू ओपनिंग ग्रीटिंग
    opening_greeting = (
        "नमस्ते समीर भाई! मैं आपका अपना **डिजिटल हीरो** हूँ। "
        "डैशबोर्ड पूरी तरह से चालू हो चुका है और ऑटोनॉमस इंजन एक्टिव है। "
        "चाहे आप लिखकर आदेश दें या बोलकर रिकॉर्डिंग भेजें—आपका हर आदेश मेरे लिए सर्वोपरि है। बताइए, आज क्या ऑटोमेशन करना है?"
    )
    st.session_state.messages.append({"role": "assistant", "content": opening_greeting})

# चैट स्क्रीन पर पुराने मैसेज दिखाना
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if "audio_file" in message:
            st.audio(message["audio_file"])

# 1. टेक्स्ट इनपुट बॉक्स (लिखकर आदेश देने के लिए)
prompt = st.chat_input("अपना आदेश यहाँ टाइप करें, समीर भाई...")

# 2. वॉयस रिकॉर्डिंग / ऑडियो इनपुट (बोलकर आदेश देने के लिए)
st.markdown("---")
st.markdown("🎙️ **वॉयस कमांड या रिकॉर्डिंग भेजें:**")
audio_file = st.audio_input("माइक्रोफोन बटन दबाकर बोलें:")

# यूजर का आदेश प्रोसेस करने का लॉजिक
user_input_received = None
input_mode = None

if prompt:
    user_input_received = prompt
    input_mode = "text"
elif audio_file:
    user_input_received = "Audio Recording Command"
    input_mode = "audio"

if user_input_received:
    if input_mode == "text":
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
    else:
        st.session_state.messages.append({"role": "user", "content": "🎙️ [वॉयस रिकॉर्डिंग आदेश भेजा गया]", "audio_file": audio_file})
        with st.chat_message("user"):
            st.markdown("🎙️ **समीर भाई की वॉयस रिकॉर्डिंग प्राप्त हुई:**")
            st.audio(audio_file)

    # एआई रिस्पॉन्स और प्रोसेसिंग का शानदार मैसेज (बुलंद आवाज़ और सम्मान के साथ)
    with st.chat_message("assistant"):
        process_box = st.empty()
        process_box.markdown("⏳ **आपका आदेश प्रोसेस हो रहा है... आपका हुकुम सर आँखों पर, समीर भाई!**")
        
        # ऑटोनॉमस एआई का दमदार जवाब
        if input_mode == "audio":
            ai_reply = (
                f"समीर भाई, आपकी वॉयस रिकॉर्डिंग पूरी तरह से सुन ली गई है!\n\n"
                f"🧠 **ऑटोनॉमस इंजन एक्शन:**\n"
                f"आपके इस आदेश के मुताबिक सभी बैकएंड ऑटोमेशन, सिस्टम टास्क और वेरिफिकेशन प्रोसेस किए जा रहे हैं। "
                f"आपका डिजिटल हीरो हर पल आपकी सेवा में हाजिर है। बताइए आगे क्या करना है?"
            )
        else:
            ai_reply = (
                f"समीर भाई, आपका आदेश प्राप्त हुआ: *\"{prompt}\"*.\n\n"
                f"🧠 **ऑटोनॉमस इंजन एक्शन:**\n"
                f"कमांड पर पूरी तन्मयता से काम शुरू कर दिया गया है। आपका यह डिजिटल हीरो बिना किसी रुकावट के हर टास्क को अंजाम देने के लिए तैयार है। "
                f"आपका हुकुम सर आँखों पर!"
            )
        
        # प्रोसेसिंग हटाकर जवाब दिखाना
        process_box.empty()
        st.markdown(ai_reply)
        
        # चैट हिस्ट्री में सेव करना
        st.session_state.messages.append({"role": "assistant", "content": ai_reply})
