import random
import time
import sys
import os

# Clear screen for hacker vibe
os.system('cls' if os.name == 'nt' else 'clear')

# ANSI color code for green text
GREEN = '\033[92m'
RESET = '\033[0m'

# Hacker-style random data generators
def random_ip():
    return f"{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}"

def random_hex():
    return ''.join(random.choices('0123456789ABCDEF', k=8))

def random_binary():
    return ''.join(random.choice('01') for _ in range(random.randint(8, 32)))

def random_matrix():
    return ''.join(random.choices('01アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン', k=random.randint(10, 50)))

def random_log():
    actions = ["CONNECT", "ACCESS GRANTED", "BREACH DETECTED", "FIREWALL BYPASSED", "DATA EXTRACTED", "TRACE INITIATED"]
    users = ["root", "admin", "guest", "hacker_1337", "shadow", "neo"]
    return f"[{time.strftime('%H:%M:%S')}] {random.choice(users)}@{random_ip()}: {random.choice(actions)}"

def random_code():
    keywords = ["def", "import", "class", "while", "for", "if", "else", "try", "except", "return", "break", "continue"]
    return f"{random.choice(keywords)} {random_hex().lower()}():"

# Main hacker-style printing loop
print(f"{GREEN}INITIALIZING NEURAL INTERFACE...{RESET}")
time.sleep(1.5)
print(f"{GREEN}BYPASSING SECURITY PROTOCOLS...{RESET}")
time.sleep(1)

try:
    while True:
        # Choose random line type
        line_type = random.choice([
            random_ip,
            random_hex,
            random_binary,
            random_matrix,
            random_log,
            random_code,
            lambda: f"SYSTEM SCAN: {random.randint(1, 100)}% COMPLETE",
            lambda: f"ENCRYPTION KEY: 0x{random_hex()}",
            lambda: f"UPLOADING VIRUS... [{random_binary()}]",
            lambda: f"DECRYPTING FILES... {random.randint(1024, 999999)} BYTES"
        ])
        
        line = line_type()
        
        # Random delay for realism
        delay = random.uniform(0.05, 0.3)
        time.sleep(delay)
        
        # Print in green
        print(f"{GREEN}{line}{RESET}")
        
        # Occasionally clear a line or add glitch effect
        if random.random() < 0.05:
            sys.stdout.write("\033[F")  # Move cursor up
            sys.stdout.write("\033[K")  # Clear line
            print(f"{GREEN}>>> GLITCH DETECTED <<<{RESET}")

except KeyboardInterrupt:
    print(f"\n{GREEN}SYSTEM SHUTTING DOWN...{RESET}")
    time.sleep(1)
    print(f"{GREEN}CONNECTION TERMINATED.{RESET}")