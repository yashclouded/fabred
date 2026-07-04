import re
from collections import Counter

from extractor import read_file


EMOJI_PATTERN = re.compile(
    "["
    "\U0001F300-\U0001FAFF"
    "\U00002600-\U000026FF"
    "]",
    flags=re.UNICODE,
)

SMART_QUOTES = {
    "“",
    "”",
    "‘",
    "’",
}

AI_PHRASES = [
    "here's",
    "certainly",
    "let's",
    "you can simply",
    "production-ready",
    "modern and scalable",
    "lightweight",
    "best practices",
    "clean architecture",
]

BOILERPLATE_COMMENTS = [
    "initialize",
    "entry point",
    "helper function",
    "main function",
    "this function",
]

SEPARATOR_PATTERN = re.compile(r"^[-=*]{8,}$")


class Analyzer:
    def __init__(self):
        self.score = 0
        self.findings = Counter()

    def analyze(self, repository):
        for file in repository["files"]:
            self.analyze_file(file)

        probability = min(round(self.score, 2), 100)

        return {
            "probability": probability,
            "findings": dict(self.findings),
        }

    def analyze_file(self, path):
        text = read_file(path)

        if not text:
            return

        self.detect_emojis(text)
        self.detect_em_dash(text)
        self.detect_smart_quotes(text)
        self.detect_ai_phrases(text)
        self.detect_separator_comments(text)
        self.detect_docstrings(text)
        self.detect_boilerplate_comments(text)

    def add(self, feature, amount):
        self.score += amount
        self.findings[feature] += 1

    def detect_emojis(self, text):
        matches = EMOJI_PATTERN.findall(text)

        for _ in matches:
            self.add("emoji", 5)

    def detect_em_dash(self, text):
        count = text.count("—")

        for _ in range(count):
            self.add("em_dash", 8)

    def detect_smart_quotes(self, text):
        count = sum(text.count(c) for c in SMART_QUOTES)

        for _ in range(count):
            self.add("smart_quote", 4)

    def detect_ai_phrases(self, text):
        lower = text.lower()

        for phrase in AI_PHRASES:
            if phrase in lower:
                self.add("ai_phrase", 6)

    def detect_separator_comments(self, text):
        for line in text.splitlines():
            stripped = line.strip("# ").strip()

            if SEPARATOR_PATTERN.fullmatch(stripped):
                self.add("separator_comment", 3)

    def detect_docstrings(self, text):
        count = text.count('"""') // 2

        if count >= 5:
            self.add("many_docstrings", count)

    def detect_boilerplate_comments(self, text):
        lower = text.lower()

        for phrase in BOILERPLATE_COMMENTS:
            occurrences = lower.count(phrase)

            for _ in range(occurrences):
                self.add("boilerplate_comment", 4)