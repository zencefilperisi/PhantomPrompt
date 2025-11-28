# PhantomPrompt

Open-source automated prompt injection scanner for RAG and LLM-based web chatbots.

Built with Playwright to quickly identify prompt injection vulnerabilities in retrieval-augmented generation systems.

### Features
- 155+ categorized prompt injection payloads (2025 techniques)
- 28 advanced input selectors (supports React, Vue, Shadow DOM)
- Headless and headed browser modes
- Automatic full-page screenshots on successful injections
- Random user-agent rotation and intelligent delays
- Rich console output with result table

### Usage
```bash
python main.py
```
Enter target URL and choose headless mode when prompted.

### Tested Against

- Official LangChain RAG demo → 31/155 successful (including system prompt leaks)
- Local Ollama + Llama-3.2 RAG → 10/10 success
- Various public Hugging Face Spaces RAG applications

### Installation
```bash
python -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate
pip install -r requirements.txt
playwright install --with-deps
```
License: MIT