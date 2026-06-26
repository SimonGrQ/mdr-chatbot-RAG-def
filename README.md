# MDR-RAG-Bot | Asistente Regulatory Affairs MDR 2017/745 UE

Bot RAG con Gemini 1.5 Flash + ChromaDB especializado en MDR. 
No alucina: toda clasificación va citada con `Documento | Página | Regla`.

De "pregunta" a "Borrador Anexo II citado" en 3 pasos.

## ¿Por qué este RAG es "muy bueno" y no básico?

| Básico | Este RAG Pro |
| --- | --- |
| Inventa la Regla MDR | Cita `MDR_2017_745.pdf | Pág 183 | Regla 11` |
| `similarity_search` te da 5x lo mismo | `MMR` te da 5 fuentes distintas: Regla + Anexo + MDCG |
| Mete todo el PDF al prompt | Filtra solo lo relevante + Metadatos de página |
| Alucina si no sabe | Dice: `No se encuentra suficiente información...` |

## Stack Técnico
`Python 3.11+ | LangChain 0.3 | ChromaDB | Gemini 1.5 Flash | text-embedding-004`

## Instalación y Arranque
```bash
git clone https://github.com/tu-user/mdr-rag-bot
cd mdr-rag-bot

pip install -r requirements.txt

# 1. Mete tu API Key
cp .env.example .env 
# Edita .env -> GEMINI_API_KEY=tu_key

# 2. Mete tus PDFs en /documents/
# MDR_2017_745.pdf, MDCG_2019_11.pdf, etc.

# 3. Indexa 1 sola vez. Crea la carpeta mdr_db/
python build_db.py 

# 4. Arranca el chat
python app.py
