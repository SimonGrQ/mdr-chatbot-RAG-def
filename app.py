
import os

from dotenv import load_dotenv

import google.generativeai as genai

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

with open("prompts/system_mdr.txt","r",encoding="utf8") as f:
    SYSTEM_PROMPT = f.read()

model = genai.GenerativeModel(

    model_name="gemini-1.5-flash",

    system_instruction=SYSTEM_PROMPT,

    generation_config={
        "temperature":0.1
    }

)

chat=model.start_chat()

embedding = GoogleGenerativeAIEmbeddings(

    model="models/text-embedding-004",

    google_api_key=os.getenv("GEMINI_API_KEY")

)

db = Chroma(

    persist_directory="mdr_db",

    embedding_function=embedding

)

print("MDR Bot listo")

while True:

    question=input("\nTú: ")

    docs=db.similarity_search(

        question,

        k=5

    )

    context="\n\n".join(

        doc.page_content

        for doc in docs

    )

    prompt=f"""

Utiliza únicamente la documentación siguiente.

======================

{context}

======================

Pregunta del usuario:

{question}

Responde citando siempre el documento y la regla correspondiente.

"""

    response=chat.send_message(prompt)

    print(response.text)
