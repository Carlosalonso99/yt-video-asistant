from dotenv import load_dotenv, find_dotenv
import gradio as gr
from langchain_community.document_loaders import YoutubeLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

load_dotenv(find_dotenv())


class VideoDatabaseManager:
    def __init__(self):
        self.db = None
        self.current_title = ""
        self.embeddings = OpenAIEmbeddings()

    def crear_dataBase_yt_video(self, video_url):
        loader = YoutubeLoader.from_youtube_url(video_url, add_video_info=True, language=["es", "en"], translation="es")
        transcripcion = loader.load()
        separador_texto = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        docs = separador_texto.split_documents(transcripcion)
        db = FAISS.from_documents(docs, self.embeddings)
        return db, transcripcion[0].metadata

    def cargar_video(self, video_url):
        try:
            if video_url == "":
                return "Introduzca la url de un video"
            db, metadata = self.crear_dataBase_yt_video(video_url)
            self.db = db
            self.current_title = metadata['title']
            return f"Video cargado: {self.current_title}"
        except Exception as e:
            print(str(e))
            return "La url no es valida"


class VideoChatInterface:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def pregunta_sobre_video(self, query, k=4):
        if self.db_manager.db is None:
            return "Primero carga un video"
        
        docs = self.db_manager.db.similarity_search(query, k=k)
        docs_contenido = " ".join([d.page_content for d in docs])
        chat = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.2)

        template = """
            You are an expert writing and reporting assistant who can answer questions about a YouTube video based on the transcript: {docs}
            Use only factual information from the transcript to answer the question.
            Your answer should be verbose and detailed. Think step by step.
        """
        prompt_sistema = SystemMessagePromptTemplate.from_template(template)
        prompt_humano = HumanMessagePromptTemplate.from_template("Answer the following question: {pregunta}")

        prompt_chat = ChatPromptTemplate.from_messages([prompt_sistema, prompt_humano])

        chain = LLMChain(llm=chat, prompt=prompt_chat)
        respuesta = chain.run(pregunta=query, docs=docs_contenido)
        return respuesta

    def chat(self, message, history):
        try:
            respuesta = self.pregunta_sobre_video(message)
            return respuesta
        except Exception:
            return "Primero carga un video"


css = """
"""

if __name__ == "__main__":
    db_manager = VideoDatabaseManager()
    chat_interface = VideoChatInterface(db_manager)

    with gr.Blocks(theme="soft", css=css) as demo:
        with gr.Tab("Asistente de Youtube"):
            with gr.Row():
                url_video = gr.Textbox(label="Url del video", placeholder="Escribe la url del video de YouTube")
                btn_cargar_info = gr.Button(value="Cargar Video")
                titulo_video = gr.Textbox(label="Video cargado", interactive=False)

            gr.ChatInterface(chat_interface.chat)

        btn_cargar_info.click(db_manager.cargar_video, inputs=url_video, outputs=titulo_video)

    demo.queue().launch()
