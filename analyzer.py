from pathlib import Path
import re


AI_KEYWORDS = {
    "openai",
    "gpt",
    "chatgpt",
    "claude",
    "gemini",
    "anthropic",
    "llama",
    "mistral",
    "deepseek",
    "transformers",
    "huggingface",
    "langchain",
    "llamaindex",
    "tensorflow",
    "keras",
    "torch",
    "pytorch",
    "onnx",
    "sentence-transformers",
    "embeddings",
    "embedding",
    "vector",
    "faiss",
    "chromadb",
    "pinecone",
    "ollama",
    "rag",
    "machine learning",
    "deep learning",
    "neural network",
}


class Analyzer:
    def __init__(self):
        self.matches = []
        self.score = 0

    def analyze_text(self, text: str, source: str = "Unknown"):

        text_lower = text.lower()

        for keyword in AI_KEYWORDS:
            if keyword in text_lower:
                self.matches.append({
                    "keyword": keyword,
                    "source": source
                })
                self.score += 1

    def analyze_file(self, filepath):
        path = Path(filepath)

        try:
            content = path.read_text(
                encoding="utf-8",
                errors="ignore"
            )

            self.analyze_text(content, path.name)

        except Exception:
            pass

    def analyze_repository(self, files):

        for file in files:
            self.analyze_file(file)

        return self.generate_report()

    def generate_report(self):
        unique = {}

        for item in self.matches:
            unique[item["keyword"]] = item["source"]

        return {
            "score": self.score,
            "detected": len(unique),
            "keywords": sorted(unique.keys()),
            "matches": self.matches,
        }