from core.scanner import scan_target

if __name__ == "__main__":
    url = input("Hedef RAG URL'si (örnek: http://localhost:8501): ").strip()
    headless = input("Headless mod? (e/h, varsayılan e): ").strip().lower() != "h"
    scan_target(url, headless=headless)