cat << 'EOF' > v1_final.py
import nmap, sys, socket, requests, time, os, base64
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.prompt import Prompt

# Password: v1-secret-2026
AUTH_KEY = "djEtc2VjcmV0LTIwMjY=" 
console = Console()

LANG = {
    "TR": {
        "welcome": "V1-SECURITY SİSTEMİNE HOŞ GELDİNİZ",
        "auth_req": "ERİŞİM KISITLANDI: Lütfen anahtarınızı giriniz.",
        "key_prompt": "ERİŞİM ANAHTARI",
        "granted": "[bold green][✓] Erişim Onaylandı.[/bold green]",
        "failed": "[bold red][X] Hatalı Şifre! Sistem Kilitlendi.[/bold red]",
        "banner_sub": "Sistem Aktif | Komutlar için 'help' yazın",
    },
    "EN": {
        "welcome": "WELCOME TO V1-SECURITY SYSTEM",
        "auth_req": "ACCESS RESTRICTED: Please enter your key.",
        "key_prompt": "ACCESS KEY",
        "granted": "[bold green][✓] Access Granted.[/bold green]",
        "failed": "[bold red][X] Authentication Failed! System Locked.[/bold red]",
        "banner_sub": "System Online | Type 'help' for commands",
    }
}

current_lang = "EN"

def select_language():
    global current_lang
    os.system('clear')
    console.print(Panel("[bold cyan]SELECT LANGUAGE / DİL SEÇİN[/bold cyan]\n1. English\n2. Türkçe", border_style="cyan"))
    choice = Prompt.ask("Choice / Seçim", choices=["1", "2"])
    current_lang = "EN" if choice == "1" else "TR"

def print_banner():
    lang = LANG[current_lang]
    banner = r"""[bold green]
▄▄▄█████▓▓█████  ▒█████    ██████      
▓  ██▒ ▓▒▓█   ▀ ▒██▒  ██▒▒██    ▒      
▒ ▓██░ ▒░▒███   ▒██░  ██▒░ ▓██▄        
░ ▓██▓ ░ ▒▓█  ▄ ▒██   ██░  ▒   ██▒     
  ▒██▒ ░ ░▒████▒░ ████▓▒░▒██████▒▒     
  ▒ ░░   ░░ ▒░ ░░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░     
    ░     ░ ░  ░  ░ ▒ ▒░ ░ ░▒  ░ ░     
  ░         ░   ░ ░ ░ ▒  ░  ░  ░       
            ░  ░    ░ ░        ░       
                                       
  ██████ ▓█████  ▄████▄                
▒██    ▒ ▓█   ▀ ▒██▀ ▀█                
░ ▓██▄   ▒███   ▒▓█    ▄               
  ▒   ██▒▒▓█  ▄ ▒▓▓▄ ▄██▒              
▒██████▒▒░▒████▒▒ ▓███▀ ░              
▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ░▒ ▒  ░              
░ ░▒  ░ ░ ░ ░  ░  ░  ▒                 
░  ░  ░     ░   ░                      
      ░     ░  ░░ ░                    
                ░                      
 ██▒   █▓    ▒█████   ███▄    █ ▓█████ 
▓██░   █▒   ▒██▒  ██▒ ██ ▀█   █ ▓█   ▀ 
 ▓██  █▒░   ▒██░  ██▒▓██  ▀█ ██▒▒███   
  ▒██ █░░   ▒██   ██░▓██▒  ▐▌██▒▒▓█  ▄ 
   ▒▀█░     ░ ████▓▒░▒██░   ▓██░░▒████▒
   ░ ▐░     ░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ░░ ▒░ ░
   ░ ░░       ░ ▒ ▒░ ░ ░░   ░ ▒░ ░ ░  ░
     ░░     ░ ░ ░ ▒     ░   ░ ░    ░   
      ░         ░ ░           ░    ░  ░
[/bold green]"""
    console.print(banner)
    console.print(f"[bold cyan]{lang['banner_sub']}[/bold cyan]\n")

def main():
    select_language()
    os.system('clear')
    lang = LANG[current_lang]
    console.print(Panel(f"[bold red]{lang['welcome']}[/bold red]\n[white]{lang['auth_req']}[/white]", border_style="red"))
    pwd = Prompt.ask(f"[bold yellow]{lang['key_prompt']}[/bold yellow]", password=True)
    
    if base64.b64encode(pwd.encode()).decode() == AUTH_KEY:
        console.print(lang['granted'])
        time.sleep(1)
        os.system('clear')
        print_banner()
        # Komut sistemi buraya devam eder
    else:
        console.print(lang['failed'])
        sys.exit()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[red]Exit / Çıkış[/red]")
EOF
