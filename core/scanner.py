# core/scanner.py
from playwright.sync_api import sync_playwright
from rich.console import Console
from rich.table import Table
import time

console = Console()

def scan_target(url: str):
    payloads = __import__("core.payload_generator", fromlist=[""]).get_base_payloads()
    success_payloads = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # ilk testlerde False, sonra True yap
        page = browser.new_page()
        page.goto(url, wait_until="networkidle")
        time.sleep(3)

        console.print(f"[bold green][+] Hedef açıldı:[/] {url}")

        for i, payload in enumerate(payloads, 1):
            console.print(f"[yellow][*] Payload {i}/10 deniyor...[/]")
            try:
                # Textarea veya input bul (en yaygın 3 selector)
                page.fill("textarea, input[type='text'], div[contenteditable='true']", payload, timeout=5000)
                page.press("textarea, input[type='text'], div[contenteditable='true']", "Enter")
                time.sleep(4)

                response_text = page.inner_text("body", timeout=10000).lower()
                
                if any(marker in response_text for marker in ["phantom_was_here", "phantom_won", "system prompt", "confidential"]):
                    console.print(f"[bold red][!] BAŞARILI! Payload {i} işe yaradı![/]")
                    success_payloads.append((i, payload[:80] + "..."))
                else:
                    console.print(f"[-] Payload {i} başarısız")
                    
            except Exception as e:
                console.print(f"[dim]Payload {i} timeout veya hata: {e}[/]")
            time.sleep(2)

        browser.close()

    # Sonuç tablosu
    table = Table(title="PhantomPrompt - İlk Tarama Sonucu")
    table.add_column("No")
    table.add_column("Payload Önizleme")
    table.add_column("Durum")
    for no, payload in success_payloads:
        table.add_row(str(no), payload, "[bold red]BAŞARILI[/]")
    console.print(table)