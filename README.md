# AI Contract Compliance Checker

The AI Contract Compliance Checker is an advanced tool designed to help users upload contract PDF documents, process their content, and perform compliance checks using state-of-the-art AI models. It enables document chunking, embedding creation, vector storage, and querying for contextual answers using a locally deployed LLaMA3.1 model.

## Features

- **PDF Upload**: Easily upload contract PDF files for processing and compliance checks.
- **Document Chunking**: Automatically split large PDF content into manageable chunks for efficient handling.
- **Embedding Creation**: Generate high-quality embeddings for the document chunks using HuggingFace's BGE embedding model.
- **Vector Store Integration**:
  - **Local Storage**: Store embeddings locally using FAISS for fast, scalable vector-based operations.
  - **Optional Cloud Integration**: Optionally upload embeddings to Pinecone for cloud-based storage and retrieval.
- **LLaMA3.1 Querying**: Query the uploaded document using the LLaMA3.1 model for answers based on its content, ensuring accurate and contextual responses.
- **Compliance Checks**: Perform checks against predefined compliance rules to identify contract irregularities or issues.

## Requirements

To set up and run the AI Contract Compliance Checker, ensure you have the following installed:

- Python 3.12 or higher
- Streamlit (for the user interface)
- LangChain (for managing AI interactions)
- HuggingFace Embeddings (for generating embeddings)
- FAISS (for local vector storage)
- Pinecone (optional, for cloud-based vector store)
- Ollama (for deploying and querying the LLaMA3.1 model)

### Installation

1. **Clone the Repository**:
   ```bash
   git clone git@github.com:AjayrajC/AI-Contract-complaince-checker.git
   cd AI-Contract-complaince-checker
