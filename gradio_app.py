import os
import gradio as gr

from brain_of_the_doctor import encode_image, analyze_image_with_query
from voice_of_the_patient import transcribe_with_groq
from voice_of_the_doctor import text_to_speech_with_elevenlabs

# ✅ Developer Name
developer_name = "Developed by: Syed Rizwan"

# ✅ Ensure Railway assigns the correct port
PORT = int(os.environ.get("PORT", 7860))  # Default to 7860 for local testing
print(f"🚀 Gradio app running on port: {PORT}")  # Debugging info

# ✅ AI Doctor System Prompt
system_prompt = """You have to act as a professional doctor, i know you are not but this is for learning purposes. 
            What's in this image? Do you find anything wrong with it medically? 
            If you make a differential, suggest some remedies for them. Donot add any numbers or special characters in 
            your response. Your response should be in one long paragraph. Also always answer as if you are answering to a real person.
            Donot say 'In the image I see' but say 'With what I see, I think you have ....'
            Dont respond as an AI model in markdown, your answer should mimic that of an actual doctor not an AI bot, 
            Keep your answer concise (max 2 sentences). No preamble, start your answer right away please."""

# ✅ Function to Process Inputs
def process_inputs(audio_filepath, image_filepath):
    speech_to_text_output = transcribe_with_groq(
        GROQ_API_KEY=os.environ.get("GROQ_API_KEY"), 
        audio_filepath=audio_filepath,
        stt_model="whisper-large-v3"
    )

    # ✅ Analyze Image if Provided
    if image_filepath:
        doctor_response = analyze_image_with_query(
            query=system_prompt + speech_to_text_output, 
            encoded_image=encode_image(image_filepath), 
            model="llama-3.2-11b-vision-preview"
        )
    else:
        doctor_response = "No image provided for me to analyze."

    # ✅ Convert Text to Speech
    output_audio_path = "final.mp3"
    text_to_speech_with_elevenlabs(input_text=doctor_response, output_filepath=output_audio_path)

    # ✅ Ensure the audio file exists
    if not os.path.exists(output_audio_path):
        output_audio_path = None  # Return None if file creation failed

    return speech_to_text_output, doctor_response, output_audio_path

# ✅ JavaScript Code for Forced Autoplay
autoplay_js = """
<script>
document.addEventListener("DOMContentLoaded", function() {
    setTimeout(() => {
        var audioElements = document.querySelectorAll("audio");
        audioElements.forEach(audio => {
            audio.play().catch(error => console.log("Autoplay blocked:", error));
        });
    }, 1000);  // Small delay ensures the element is available
});
</script>
"""

# ✅ Correct Gradio Interface with Developer Name Inside Blocks
with gr.Blocks() as iface:
    gr.Markdown(autoplay_js)  # ✅ Inject JavaScript for autoplay
    gr.Markdown(f"### 👨‍💻 {developer_name}")  # ✅ Developer credit at the bottom

    iface = gr.Interface(
        fn=process_inputs,
        inputs=[
            gr.Audio(sources=["microphone"], type="filepath"),
            gr.Image(type="filepath")
        ],
        outputs=[
            gr.Textbox(label="Speech to Text"),
            gr.Textbox(label="Doctor's Response"),
            gr.Audio(label="Generated Voice Response", autoplay=True)
        ],
        title="AI Doctor with Vision and Voice"
    )

# ✅ Launch the Gradio App
iface.launch(server_name="0.0.0.0", server_port=PORT)
