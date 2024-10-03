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
```

### Instalación

1. **Clonar el repositorio**:

```bash
   git clone https://github.com/Carlosalonso99/yt-video-assistant.gitZZ
  ```

2. **Instalar dependencias**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Configurar el archivo .env**:

   ```bash
   OPENAI_API_KEY=tu_api_key_de_openai
   ```

4. **Ejecutar la aplicación**:

   ```bash
   python AppAsistenteVideos.py
   ```

### Uso

1. **Cargar un video**: Ingresa la URL de un video de YouTube en el campo de entrada y presiona "Cargar Video".
   
2. **Hacer preguntas**: Una vez que el video esté cargado, puedes hacer preguntas sobre el contenido del video. El asistente utilizará la transcripción del video para proporcionar respuestas detalladas.

3. **Interfaz de Chat**: La aplicación incluye una interfaz de chat interactiva donde puedes conversar con el asistente.

### Funcionalidades Técnicas

- **Carga de videos con`YoutubeLoader`**: El sistema utiliza `YoutubeLoader` de `langchain_community` para obtener la transcripción del video y metadatos adicionales, admitiendo varios idiomas (español e inglés).

- **Procesamiento de texto con `langchain`**: 
   - La transcripción del video se procesa con `RecursiveCharacterTextSplitter` para dividir el contenido en fragmentos manejables de texto, con un tamaño de 1000 caracteres y un solapamiento de 100.
   - Los fragmentos se almacenan y procesan para su posterior búsqueda.

- **Búsqueda basada en similitud con FAISS**: 
   - El sistema utiliza FAISS (`Facebook AI Similarity Search`) para indexar los fragmentos de transcripción y realizar búsquedas rápidas y precisas basadas en similitud de contenido cuando se hacen preguntas sobre el video.

- **Modelos GPT-3.5**:
   - Se utiliza el modelo `gpt-3.5-turbo` de OpenAI a través de `ChatOpenAI` para generar respuestas basadas en las transcripciones.
   - Las respuestas son generadas a partir de un **LLMChain** utilizando plantillas de mensajes del sistema y del usuario, proporcionadas por `ChatPromptTemplate`, con instrucciones detalladas para responder preguntas de manera estructurada y coherente.

- **Interfaz interactiva con Gradio**:
   - La aplicación utiliza `Gradio` para crear una interfaz amigable y accesible para los usuarios.
   - Los usuarios pueden ingresar la URL de un video de YouTube, cargar su transcripción y luego hacer preguntas relacionadas con el contenido del video a través de un chatbot interactivo.










