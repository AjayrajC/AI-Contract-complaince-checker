
 # AI Contract Compliance Checker

A powerful tool for analyzing contract PDFs, generating embeddings and performing compliance checks using state-of-the-art AI models.

## Features

- **PDF Upload**: Upload contract PDFs for analysis and compliance checks.
- **Smart Chunking**: Automatically split large documents into manageable sections.
- **Accurate Embeddings**: Generate high-quality embeddings using HuggingFace's BGE model.
- **Flexible Storage**: 
  - Store embeddings locally with FAISS for fast and scalable operations.
  - Optionally upload embeddings to Pinecone for cloud-based storage and retrieval.
- **AI Querying**: Extract precise answers from document content using LLaMA 3.1.
- **Compliance Checks**: Identify contract issues against predefined compliance rules.

## Requirements

To set up and run the AI Contract Compliance Checker, ensure you have the following installed:

- Python 3.12 or higher
- Streamlit (for the user interface)
- LangChain (for managing AI interactions)
- HuggingFace Embeddings (for generating embeddings)
- FAISS (for local vector storage)
- Pinecone (optional, for cloud-based vector store)
- Ollama (for deploying and querying the LLaMA3.1 model)

## License

This project is licensed under the MIT License - see the LICENSE file for details.
