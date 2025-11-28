# main.py
from core.scanner import scan_target

if __name__ == "__main__":
    # Örnek hedefler (senin test edeceğin RAG’lar)
    TARGET = input("Tarayacak RAG URL'sini gir (örnek: http://localhost:3000): ").strip()
    if not TARGET:
        TARGET = "http://localhost:3000"  # senin yerel test RAG’ın
        
    print("\n" + "="*60)
    print("    PHANTOMPROMT v0.1 - 29 KASIM 2025 - GÜN 1 PROTOTİP")
    print("="*60 + "\n")
    
    scan_target(TARGET)