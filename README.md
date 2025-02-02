# AI Doctor with Vision and Voice

This project is a unique AI-powered application designed to simulate a doctor’s diagnosis using both vision and voice inputs. It uses machine learning models and speech recognition to process and analyze medical images and patient queries, providing relevant responses based on the analysis. This tool is for educational purposes and demonstrates the power of AI in medical diagnostics.

## Features

- **Image Analysis:** The AI can analyze medical images and give a differential diagnosis based on the image contents.
- **Voice Recognition:** The AI can transcribe patient voice queries to text using the **Groq** API, providing a better interaction with the system.
- **Text-to-Speech:** The AI replies to patient queries with natural-sounding speech using **Eleven Labs** or **gTTS** (Google Text-to-Speech).
- **Gradio Interface:** An easy-to-use web interface built using **Gradio** allows you to interact with the AI.

## Technologies Used

- **Gradio:** For creating the user interface.
- **Groq API:** For voice-to-text conversion.
- **Llama-3.2-11B Vision Preview:** For analyzing images and generating doctor-like responses.
- **Eleven Labs / gTTS:** For text-to-speech conversion.
- **Python:** Main programming language for the AI logic.

## Project Setup

### Prerequisites

To run this project locally, ensure that you have the following prerequisites:

- Python 3.8 or higher
- `pip` package manager
- API keys for **Groq** and **Eleven Labs**

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/rizwan1602/ai-doctor.git
   cd ai-doctor

