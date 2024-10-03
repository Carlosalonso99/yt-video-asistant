# YouTube Video Assistant

### Descripción

**YouTube Video Assistant** es una aplicación que utiliza la transcripción de videos de YouTube para responder preguntas sobre el contenido. Mediante la integración de la API de OpenAI y la carga de videos desde YouTube, la aplicación proporciona respuestas detalladas basadas en la transcripción del video seleccionado. Esta herramienta es ideal para obtener resúmenes, responder preguntas o extraer información específica de videos.

---

### Características

- **Carga de videos de YouTube**: La aplicación puede cargar videos de YouTube y procesar sus transcripciones automáticamente.
- **Asistente inteligente**: Utiliza modelos GPT-3.5 para responder preguntas sobre los videos.
- **Interfaz interactiva**: Usa Gradio para una interacción amigable y accesible.
- **Búsqueda basada en similitud**: Procesa las transcripciones con FAISS para buscar respuestas específicas en los videos.

---

### Requisitos

- Python 3.10+
- Paquetes de Python:
  - `gradio`
  - `langchain`
  - `openai`
  - `faiss-cpu`
  - `yt-dlp`
  - `dotenv`

Para instalar las dependencias necesarias, ejecuta:

```bash
pip install -r requirements.txt
