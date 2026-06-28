# AI Learning Projects — LangChain Practice

Hands-on AI experiments using LangChain, OpenAI, and vector stores.

## Folder Structure

```
├── ChatModels/                  # Chat model integrations
│   ├── chatmodel_openai.py          - OpenAI chat model
│   ├── chatmodel_anthropic.py       - Anthropic (Claude) chat model
│   ├── chatmodel_huggingface_api.py - HuggingFace via API
│   └── chatmodel_huggingface_local.py - HuggingFace local pipeline
│
├── LLMs/                        # Base LLM usage
│   └── llm_demo.py                  - OpenAI LLM demo
│
├── EmbeddingModels/             # Text embedding examples
│   ├── embedding_openai_doc.py      - Embed documents
│   └── enbedding-openai-query.py    - Embed queries
│
├── Prompts/                     # Prompt templates and messages
│   ├── messages.py                  - System, Human, AI messages
│   ├── chat_prompt_template.py      - ChatPromptTemplate usage
│   └── prompt_ui.py                 - Streamlit UI with PromptTemplate
│
├── StructuredOutPut/            # Structured output with LLMs
│   ├── pydentic_demo.py             - Pydantic model basics
│   ├── typedict.py                  - TypedDict basics
│   ├── with_structured_output_with_pydantic.py
│   ├── with_structured_output_typed_dict.py
│   └── with_structured_output_json.py
│
├── Vector Store/                # Vector database with Chroma
│   └── langchain_chrome.py          - Add, search, update, delete docs
│
├── langchain_tool_calling/      # LangChain tools
│   ├── langchain_inbuild_tools.py           - DuckDuckGo + Shell tools
│   ├── langchain_custom_tool_calling.py     - Custom tool with @tool decorator
│   ├── langchain_custom_tool_using_BaseTool.py - Custom tool via BaseTool class
│   ├── langchain_custom_tool_tookkit.py     - Tool toolkit pattern
│   └── langchain_custom_tool_structured_outputt_pydantic.py - StructuredTool
│
├── chatbot.py                   # Simple chatbot with ChatOpenAI
├── temprature.py                # Temperature parameter demo
├── requirements.txt
└── .env                         # API keys (not committed)
```

## Setup

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/ai-learning-projects.git
cd ai-learning-projects
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure API keys
Create a `.env` file in the root folder:
```
OPENAI_API_KEY=your_openai_key_here
ANTHROPIC_API_KEY=your_anthropic_key_here
HUGGINGFACEHUB_API_TOKEN=your_huggingface_token_here
```

## Tech Stack

| Package | Purpose |
|---|---|
| `langchain` | Core framework |
| `langchain-openai` | OpenAI LLM & embeddings |
| `langchain-anthropic` | Claude (Anthropic) models |
| `langchain-huggingface` | HuggingFace models |
| `langchain-chroma` | Chroma vector store integration |
| `langchain-community` | DuckDuckGo search, Shell tool |
| `chromadb` | Vector database |
| `pydantic` | Data validation & structured output |
| `streamlit` | UI for prompt demos |
| `python-dotenv` | Load environment variables |
| `ddgs` | DuckDuckGo search backend |
