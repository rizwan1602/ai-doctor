
# AI Doctor with Vision and Voice

The **AI Doctor with Vision and Voice** project is a cutting-edge application designed to simulate a doctor's diagnostic process using both **image analysis** and **voice recognition**. It combines machine learning models, speech recognition, and natural language processing to process medical images and patient queries, providing insightful, AI-powered responses. This tool is designed for educational purposes and demonstrates the potential of AI in medical diagnostics.

## Features

- **Image Analysis:** The AI can analyze medical images and provide a differential diagnosis based on the visual content.
- **Voice Recognition:** Transcribes patient voice queries to text using the **Groq** API for a seamless interaction with the system.
- **Text-to-Speech:** Converts AI-generated responses into natural-sounding speech using **Eleven Labs** or **gTTS** (Google Text-to-Speech).
- **Gradio Interface:** An intuitive, user-friendly web interface built using **Gradio** that allows easy interaction with the AI system.

## Technologies Used

- **Gradio:** For creating the interactive user interface.
- **Groq API:** For converting voice input into text (Speech-to-Text).
- **Llama-3.2-11B Vision Preview:** For analyzing medical images and generating doctor-like responses.
- **Eleven Labs / gTTS:** For converting text-based responses into speech (Text-to-Speech).
- **Python:** The main programming language for implementing the logic of the AI system.

## Project Setup

### Prerequisites

Before you begin, ensure you have the following:

- Python 3.8 or higher
- `pip` package manager installed
- **Groq API Key** and **Eleven Labs API Key**

### Installation Steps

Follow these instructions to set up the project locally:

1. **Clone the Repository:**
   Clone the repository to your local machine using Git:
   ```bash
   git clone https://github.com/rizwan1602/ai-doctor.git
   cd ai-doctor
   ```

2. **Set Up a Virtual Environment (optional but recommended):**
   To keep your dependencies isolated, it's a good practice to use a virtual environment:
   ```bash
   python3 -m venv venv
   ```

3. **Activate the Virtual Environment:**
   - On **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```
   - On **Windows**:
     ```bash
     .env\Scriptsctivate
     ```

4. **Install Required Dependencies:**
   Install the required dependencies using `pip`:
   ```bash
   pip install -r requirements.txt
   ```

5. **Set Up API Keys:**
   Create a `.env` file in the root directory of the project, and add your API keys for **Groq** and **Eleven Labs**:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ELEVENLABS_API_KEY=your_elevenlabs_api_key_here
   ```

6. **Run the Application:**
   To launch the application, run the following:
   ```bash
   python gradio_app.py
   ```

7. **Access the Interface:**
   Open your web browser and navigate to [http://127.0.0.1:7860](http://127.0.0.1:7860) to interact with the AI Doctor interface.

### How It Works

1. **Voice Input:** The patient speaks into the microphone, and the **Groq** API transcribes the speech into text.
2. **Image Analysis:** If an image is provided, the AI analyzes it and generates a diagnostic response using the **Llama-3.2-11B Vision Preview** model.
3. **Response Generation:** Based on the voice input and image analysis, the AI generates a diagnosis and suggests remedies (if necessary).
4. **Text-to-Speech Output:** The AI response is converted to natural-sounding speech using **Eleven Labs** or **gTTS**, and played back to the patient.

### Code Overview

The core functionality resides in the `process_inputs` function. Here’s a breakdown of the steps:

- **Audio to Text:** The audio file from the patient is processed, and the speech is converted to text using the **Groq API**.
- **Image Processing:** If an image is provided, it's encoded and sent to the **Llama-3.2-11B Vision Preview** model to extract medical insights.
- **Response Generation:** The doctor-like response is formulated using the **system_prompt**.
- **Text-to-Speech Conversion:** The AI's response is converted into speech using **Eleven Labs** or **gTTS**.

